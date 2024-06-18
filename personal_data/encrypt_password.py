#!/usr/bin/env python3
"""
function that use the bcrypt package to perform the hashing (with hashpw).
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt."""
    # Génération d'un sel pour le hachage
    salt = bcrypt.gensalt()
    # Hachage du mot de passe avec le sel
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if a password matches its hashed version."""
    # Vérifie si le mot de passe fourni correspond au mot de passe haché
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
