#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        # Créer une instance de GithubOrgClient pour l'organisation donnée
        client = GithubOrgClient(org_name)

        # Définir le retour simulé de get_json
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.return_value = {
            "name": org_name,
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
        }

        # Accéder à la propriété org (qui est memoized)
        org_property = client.org

        # Vérifier que get_json a été appelé une fois avec l'URL attendue
        mock_get_json.assert_called_once_with(expected_url)

        # Accéder à la propriété une deuxième fois
        result = client.org

        # Vérifier que get_json n'a pas été appelé à nouveau
        mock_get_json.assert_called_once_with(expected_url)

        # Vérifier que les résultats sont corrects
        self.assertEqual(result["name"], org_name)
        self.assertEqual(result["repos_url"],
                         f"https://api.github.com/orgs/{org_name}/repos")


if __name__ == '__main__':
    unittest.main()
