-- Creates table with default id
CREATE TABLE IF NOT EXISTS unique_id (
    id int NOT NULL UNIQUE DEFAULT 1
    , name varchar(256)
    );
