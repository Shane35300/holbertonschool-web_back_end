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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        # Définir le payload que get_json devrait retourner
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        # Définir la valeur que _public_repos_url devrait retourner
        mock_public_repos_url = "https://api.github.com/orgs/testorg/repos"

        # Utiliser patch comme gestionnaire de contexte pour mockerp...
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_url:
            mock_public_url.return_value = mock_public_repos_url

            # Créer une instance réelle de GithubOrgClient
            client = GithubOrgClient("testorg")

            # Appeler la méthode public_repos
            repos = client.public_repos()

            # Vérifier que la liste des repos retournée est celle attendue
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(repos, expected_repos)

            # Vérifier que _public_repos_url a été appelé une fois
            mock_public_url.assert_called_once()

            # Vérifier que get_json a été appelé une fois avec l'URL attendue
            mock_get_json.assert_called_once_with(mock_public_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": {}}, "my_license", False),
        ({}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        # Créer une instance de GithubOrgClient (l'instance n'est pas utilisée)
        client = GithubOrgClient("testorg")

        # Appeler la méthode has_license avec les paramètres fournis
        result = client.has_license(repo, license_key)

        # Vérifier que le résultat est celui attendu
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
