# Docker MySQL Node.js React.js App

![App](https://github.com/ElNavas-8/Proyecto_TIC/blob/main/scripts/Screenshot%202025-05-25%201236020.png)

El repositorio cuenta con una aplicación frontend React.js donde los usuarios pueden introducir sus datos y enviarlos. Los datos enviados se transmiten de forma segura a un servidor backend Node.js, que los procesa y se almacena en una base de datos MySQL. Utilizando Docker Compose, este compila toda la aplicación, incluyendo el frontend, el backend y la base de datos, se puede orquestar y gestionar sin esfuerzo como contenedores aislados.

## Configuración

Para configurar el proyecto, siga los siguientes pasos:

### Prerrequisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

- Docker: [Descargar e instalar Docker](https://docs.docker.com/get-docker/)

- Node:  [Descargar e instalar Node.js](https://nodejs.org/) 

- MySQL: [Descargar e instalar MySQL](https://dev.mysql.com/downloads/installer/)

### Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/ElNavas-8/Proyecto_TIC
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd scripts
   ```

3. Descarga el archivo `script.sql` y colócalo en el directorio del proyecto.

4. Ejecuta el siguiente comando para construir e iniciar los contenedores Docker:

   ```bash
   docker-compose up --build
   ```

5. Inicie sesión en MySQL utilizando el 


5. Inicie sesión en MySQL utilizando el puerto, el nombre de usuario y la contraseña especificados:

   - Host: `localhost`
   - Puerto: `3307`
   - Nombre de usuario: `root`
   - Contraseña: `pass123`

   Puede utilizar un cliente MySQL como [MySQL Workbench](https://www.mysql.com/products/workbench/) o [phpMyAdmin](https://www.phpmyadmin.net/) para iniciar sesión en el servidor MySQL.

6. Inicialice la base de datos MySQL ejecutando el archivo `script.sql`.

7. Acceda a la aplicación abriendo la siguiente URL en su navegador web:

   ```
   http://localhost:3001
   ```

   Esto te llevará a la interfaz de la aplicación ReactJS donde podrás interactuar con el proyecto.
