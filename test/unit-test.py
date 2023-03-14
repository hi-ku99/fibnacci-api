import unittest
import requests
import json
 
class Testnumprint(unittest.TestCase):
    
    def test1(self):
        url = "https://fibonacciapi.azurewebsites.net/fib?n=3"
        expect = requests.request('GET', url).json()
        actual = json.dumps({'results': 2})
        self.assertEqual(expect, actual)

    def test2(self):
        url = "https://fibonacciapi.azurewebsites.net/fi"
        expect = requests.request('GET', url).json()
        actual = json.dumps({"message":"Not found.","status":404})
        self.assertEqual(expect, actual)

if __name__ == "__main__":
    unittest.main()