-- prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS `bion_db`;

CREATE USER IF NOT EXISTS 'bion_dev'@'localhost' IDENTIFIED BY 'bion_dev_pwd';
GRANT ALL PRIVILEGES ON `bion_db`.* TO 'bion_dev'@'localhost';
FLUSH PRIVILEGES;
