-- Crée un index et permet de combiner les deux critères dans un seul index
CREATE INDEX idx_name_first_score ON names (name(1), score);
