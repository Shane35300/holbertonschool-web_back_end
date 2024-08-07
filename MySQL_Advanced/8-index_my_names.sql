-- Crée un index sur la première lettre de la colonne `name`
CREATE INDEX idx_name_first ON names (name(1));
