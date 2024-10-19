-- Task: Create users table with these attributes:
-- id: integer, auto-increment, primary key, never null
-- email: string, never null, unique
-- name: string

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY (id)
);
