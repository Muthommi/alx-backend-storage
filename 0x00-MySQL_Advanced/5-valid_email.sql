DELIMITER $$

CREATE TRIGGER reset_valid_email_before_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	-- Check if the email has changed
	IF NEW.email <> OLD.email THEN
		-- Reset valid_email to 0 if it has been changed
		SET NEW.valid_email = 0;
	END IF;
END$$

DELIMITER ;
