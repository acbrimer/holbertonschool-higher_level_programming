-- Sets hbtn_0c_0 colation to UTF8
ALTER DATABASE hbtn_0c_0
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table
    MODIFY COLUMN name varchar(256)
        CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
