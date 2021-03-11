import sys, unittest, filecmp
from unittest.mock import patch, mock_open

import flatten

class Testflatten(unittest.TestCase):
    def test_single_nested(self):
        data = {
            "a": 1, 
            "b": True,
            "c": {
                "d": 3,
                "e": "test"
                }
            }
        true_output = {
            "a": 1,
            "b": True,
            "c.d": 3,
            "c.e": "test"
            }
        d = flatten.flatten(data, '', '.')
        self.assertEqual(d, true_output)

    def test_multilevel(self):
        data = {
            "a": {
                "d": 3,
                "e": {
                    "d": 3,
                    "e": "test"
                    }
                }, 
            "b": True,
            "c": {
                "d": {
                    "d": 3,
                    "e": "test"
                    },
                "e": "test"
                }
            }
        true_output = {
            "a.d": 3,
            "a.e.d": 3,
            "a.e.e": "test",
            "b": True,
            "c.d.d": 3,
            "c.d.e": "test",
            "c.e": "test"
        }
        d = flatten.flatten(data, '', '.')
        self.assertEqual(d, true_output)

    def test_multiple_nested(self):
        data = {
            "a": 1, 
            "b": True,
            "c": {
                "d": {
                    "d": {
                        "d": {
                            "d": 3,
                            "e": {
                                "d": 3,
                                "e": "test"
                                }
                            },
                        "e": "test"
                        },
                    "e": "test"
                    },
                "e": "test"
                }
            }
        true_output = {
            "a": 1,
            "b": True, 
            "c.d.d.d.d": 3, 
            "c.d.d.d.e.d": 3, 
            "c.d.d.d.e.e" : "test", 
            "c.d.d.e" : "test", 
            "c.d.e" : "test", 
            "c.e": "test"
            }
        d = flatten.flatten(data, '', '.')
        self.assertEqual(d, true_output)

if __name__ == '__main__':
    unittest.main()