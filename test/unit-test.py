import unittest
import requests
import json
 
class Testnumprint(unittest.TestCase):

    # 正常バージョン
    def test1(self):
        url = "https://fibonacciapi.azurewebsites.net/fib?n=3"
        expect = requests.request('GET', url).json()["results"]
        actual = 2
        self.assertEqual(expect, actual)

    # fibのスペルミス
    def test2(self):
        url = "https://fibonacciapi.azurewebsites.net/fi"
        expect = requests.request('GET', url).json()["message"]
        actual = "Not found."
        self.assertEqual(expect, actual)

    # クエリnに文字列が与えられた場合
    def test3(self):
        url = "https://fibonacciapi.azurewebsites.net/fib?n=a"
        expect = requests.request('GET', url).json()["message"]
        actual = "Value error."
        self.assertEqual(expect, actual)
    
    # クエリnに負の値が与えられた場合
    def test4(self):
        url = "https://fibonacciapi.azurewebsites.net/fib?n=-1"
        expect = requests.request('GET', url).json()["message"]
        actual = "Value error."
        self.assertEqual(expect, actual)

    # クエリnに小数が与えられた場合
    def test5(self):
        url = "https://fibonacciapi.azurewebsites.net/fib?n=1.1"
        expect = requests.request('GET', url).json()["message"]
        actual = "Value error."
        self.assertEqual(expect, actual)

    # クエリ引数が異なる場合
    def test6(self):
        url = "https://fibonacciapi.azurewebsites.net/fib?NNNN=3"
        expect = requests.request('GET', url).json()["message"]
        actual = "Value error."
        self.assertEqual(expect, actual)



if __name__ == "__main__":
    unittest.main()