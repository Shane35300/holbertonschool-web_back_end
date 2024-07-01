#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"]),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        # Créer un objet Mock pour la réponse de requests.get
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Appeler get_json avec l'URL de test
        result = get_json(test_url)

        # Vérifier que requests.get a été appelé avec la bonne URL
        mock_get.assert_called_once_with(test_url)

        # Vérifier que la sortie de get_json est égale au payload de test
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):

    def test_memoize(self):
        # Définir la classe de test
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Utiliser patch pour simuler a_method
        with patch.object(TestClass, 'a_method', return_value=42
                          ) as mock_a_method:
            # Créer une instance de TestClass
            obj = TestClass()

            # Appeler a_property deux fois
            result1 = obj.a_property
            result2 = obj.a_property

            # Vérifier que a_method a été appelé une seule fois
            mock_a_method.assert_called_once()

            # Vérifier que les résultats sont corrects
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
