#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        # Définir la charge utile attendue
        expected_repos_url = "https://api.github.com/orgs/testorg/repos"

        # Remplacer la propriété org de la classe GithubOrgClient par un mock
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock
                          ) as mock_org:
            mock_org.return_value = {
                "repos_url": expected_repos_url
            }

            # Créer une instance réelle de GithubOrgClient
            client = GithubOrgClient("testorg")

            # Accéder à la propriété _public_repos_url
            actual_repos_url = client._public_repos_url

            # Vérifier que la valeur retournée correspond à celle attendue
            self.assertEqual(actual_repos_url, expected_repos_url)


if __name__ == '__main__':
    unittest.main()
