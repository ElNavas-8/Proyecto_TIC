import psutil
import docker
from docker.errors import DockerException
from tabulate import tabulate

def get_system_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    net = psutil.net_io_counters()
    disk = psutil.disk_io_counters()

    return {
        "CPU %": cpu_percent,
        "Mem Usage": f"{mem.used / (1024**2):.2f} MiB",
        "Mem Total": f"{mem.total / (1024**2):.2f} MiB",
        "Mem %": mem.percent,
        "Net I/O": f"{net.bytes_sent / (1024**2):.2f} MiB sent / {net.bytes_recv / (1024**2):.2f} MiB recv",
        "Disk I/O": f"{disk.read_bytes / (1024**2):.2f} MiB read / {disk.write_bytes / (1024**2):.2f} MiB write",
    }

def get_docker_metrics():
    try:
        client = docker.from_env()
        containers = client.containers.list()
        if not containers:
            print("\nNo running Docker containers.\n")
            return []

        stats = []
        for container in containers:
            stat = container.stats(stream=False)
            mem_usage = stat["memory_stats"]["usage"] / (1024 ** 2)
            mem_limit = stat["memory_stats"].get("limit", 0) / (1024 ** 2)
            net_rx = stat.get("networks", {}).get("eth0", {}).get("rx_bytes", 0) / (1024 ** 2)
            net_tx = stat.get("networks", {}).get("eth0", {}).get("tx_bytes", 0) / (1024 ** 2)

            stats.append({
                "Container": container.name,
                "CPU %": round(stat["cpu_stats"]["cpu_usage"]["total_usage"] / 1e9, 2),
                "Mem Usage (MiB)": f"{mem_usage:.2f}",
                "Mem Limit (MiB)": f"{mem_limit:.2f}",
                "Mem %": f"{(mem_usage / mem_limit * 100):.2f}" if mem_limit > 0 else "N/A",
                "Net I/O": f"{net_rx:.2f} MiB / {net_tx:.2f} MiB"
            })
        return stats

    except DockerException as e:
        print(f"\n⚠️ Docker no está disponible o no hay acceso: {e}\n")
        return []

def main():
    print("=== SYSTEM METRICS ===")
    sys_stats = get_system_metrics()
    for k, v in sys_stats.items():
        print(f"{k}: {v}")

    print("\n=== DOCKER CONTAINERS ===")
    container_stats = get_docker_metrics()
    if container_stats:
        print(tabulate(container_stats, headers="keys", tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()
