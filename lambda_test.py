import unittest
from lambda_sample import lambda_handler
import json


class LambdaTest(unittest.TestCase):

    def testcase1(csl):
        temp = lambda_handler(event = 'sad', context= 'test')
        csl.assertEqual(200, temp.get('statusCode'))
        csl.assertEqual('"Hello from Lambda!"', temp.get('body'))

if __name__ == '__main__':
    unittest.main()