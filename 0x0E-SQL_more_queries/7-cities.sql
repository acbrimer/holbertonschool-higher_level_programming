-- Creates database hbtn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
   id int NOT NULL AUTO_INCREMENT PRIMARY KEY
    , state_id int NOT NULL
        FOREIGN KEY REFERENCES hbtn_0d_usa.states(id)
    , name varchar(256) NOT NULL
);
