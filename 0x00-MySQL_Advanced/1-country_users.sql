-- Create 'users' table with these attributes
-- Table structure:
-- id: integer, auto-increment, primary key
-- email: string, unique, never null
-- name: string
-- country: ENUM ('US', 'CO', 'TN'), default 'US', never null

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
