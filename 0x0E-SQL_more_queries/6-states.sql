-- Creates database hbtn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
   id int NOT NULL AUTO_INCREMENT PRIMARY KEY
   , name varchar(256) NOT NULL
);
