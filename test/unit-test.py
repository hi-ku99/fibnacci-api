import unittest
import requests
import time
import json
 
class Testnumprint(unittest.TestCase):
    
    urls = ["https://fibonacciapi.azurewebsites.net/fib?n=3",
           "https://fibonacciapi.azurewebsites.net/fb"
            ]

    actual = [json.dumps({'results': 2}),
              json.dumps({"message":"Not found.","status":404})
            ]
    
    def test_numprint(self,expect, actual):
        for i, url in enumerate(urls):
            response = requests.request('GET', urls[i])
            expect = response.json()
            self.assertEqual(expect, actual)
            time.sleep(3)

    if __name__ == "__main__":
        unittest.main()