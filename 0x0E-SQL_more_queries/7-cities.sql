-- Creates database hbtn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
   id int NOT NULL AUTO_INCREMENT PRIMARY KEY
    , state_id int NOT NULL
    , name varchar(256) NOT NULL
    , CONSTRAINT FOREIGN KEY fk_cities__states
        (state_id) REFERENCES hbtn_0d_usa.states(id)
);
