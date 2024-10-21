-- Task: Create an index on the first letter of the name
CREATE INDEX idx_name_first_score
ON names (LEFT(name, 1), score);