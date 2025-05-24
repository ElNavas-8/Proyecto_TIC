const express = require("express");
const mysql = require("mysql2");
const cors = require("cors");
const bodyParser = require("body-parser");

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Use a MySQL connection pool (recommended)
const pool = mysql.createPool({
  host: "localhost",
  port: "3306",
  user: "user",
  password: "pass123",
  database: "appdb",
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0,
});

// GET: Fetch all users
app.get("/user", (req, res) => {
  pool.query("SELECT * FROM apptb", (err, results) => {
    if (err) {
      console.error("Error fetching users:", err);
      return res.status(500).send("Database error");
    }
    res.json(results);
  });
});

// POST: Insert a user
app.post("/user", (req, res) => {
  const name = req.body.data;
  if (!name) {
    return res.status(400).send("Missing 'data' in request body");
  }

  pool.query("INSERT INTO apptb (name) VALUES (?)", [name], (err, results) => {
    if (err) {
      console.error("Error inserting user:", err);
      return res.status(500).send("Database error");
    }
    res.json(results);
  });
});

// POST: Create database (only works if already connected to MySQL server)
app.post("/dbinit", (req, res) => {
  const connection = mysql.createConnection({
    host: "localhost",
    port: "3306",
    user: "user",
    password: "pass123",
  });

  connection.query("CREATE DATABASE IF NOT EXISTS appdb", (err) => {
    connection.end();
    if (err) {
      console.error("Error creating database:", err);
      return res.status(500).send("Error creating database");
    }
    res.send("Database created successfully");
  });
});

// POST: Create table
app.post("/tbinit", (req, res) => {
  pool.query(
    `CREATE TABLE IF NOT EXISTS apptb (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255)
    )`,
    (err) => {
      if (err) {
        console.error("Error creating table:", err);
        return res.status(500).send("Error creating table");
      }
      res.send("Table created successfully");
    }
  );
});

// Start the server
app.listen(3000, () => {
  console.log("Server running on port 3000");
});
