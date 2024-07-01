#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import fixtures


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


@parameterized_class([
    {
        "org_payload": fixtures.TEST_PAYLOAD[0][0],
        "repos_payload": fixtures.TEST_PAYLOAD[0][1],
        "expected_repos": [
            "episodes.dart",
            "cpp-netlib",
            "dagger",
            "ios-webkit-debug-proxy",
            "google.github.io",
            "kratu",
            "build-debian-cloud",
            "traceur-compiler",
            "firmata.py"
        ],
        "apache2_repos": [
            "dagger",
            "kratu",
            "traceur-compiler",
            "firmata.py"
        ]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the class for integration tests."""
        cls.get_patcher = patch('requests.get',
                                side_effect=cls.mocked_requests_get)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the class after tests."""
        cls.get_patcher.stop()

    @classmethod
    def mocked_requests_get(cls, url, *args, **kwargs):
        """Mock function for requests.get"""
        if url == "https://api.github.com/orgs/google":
            mock_resp = Mock()
            mock_resp.json.return_value = cls.org_payload
            return mock_resp
        elif url == "https://api.github.com/orgs/google/repos":
            mock_resp = Mock()
            mock_resp.json.return_value = cls.repos_payload
            return mock_resp

    def test_public_repos(self):
        """Test public_repos method."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license filter."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
