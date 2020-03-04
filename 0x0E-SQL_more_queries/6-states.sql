-- script that creates the table id_not_null on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(id INT PRIMARY KEY UNIQUE AUTO_INCREMENT, name VARCHAR(256));
