DELIMITER //

-- Création de la procédure stockée AddBonus
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;

    -- Vérifiez si le projet existe déjà
    SELECT id INTO project_id FROM projects WHERE name = project_name;

    -- Si le projet n'existe pas, créez-le
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Ajouter la correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END //

DELIMITER ;
