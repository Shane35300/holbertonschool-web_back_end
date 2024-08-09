-- créer une fonction qui retourne le résultat de la division de a par b
DELIMITER //
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(x INT, y INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
	DECLARE variable FLOAT;
	IF y = 0 THEN
		SET variable = 0;
	ELSE
		SET variable = x / y;
	END IF;
	RETURN variable;
END //
DELIMITER ;
