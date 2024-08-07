DELIMITER //

-- Supprime la procédure si elle existe déjà
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser //

-- Crée la procédure
CREATE PROCEDURE ComputeAverageScoreForUser(IN input_user_id INT)
BEGIN
    -- Déclare une variable locale pour stocker la moyenne
    DECLARE avg_score FLOAT;

    -- Calcule la moyenne des scores pour l'utilisateur donné
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = input_user_id;

    -- Met à jour la table users avec la moyenne calculée
    UPDATE users
    SET average_score = avg_score
    WHERE id = input_user_id;
END //

DELIMITER ;
