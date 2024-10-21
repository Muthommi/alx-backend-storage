-- Task: Create the SafeDiv function
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
DETERMINISTIC
BEGIN
	-- If b is zero, return 0, otherwise return a / b
	If b = 0 THEN
		RETURN 0;
	ELSE
		RETURN a / b;
	END IF;
END //

DELIMITER ;
