import os
import unittest
import tempfile
from main import app

class MyTestCase(unittest.TestCase):

    def test_iataCode(self):
        self.app = app.test_client()
        r = self.app.get('/airportName?iataCode=CDG')
        print(r.data)
        assert b'Charles de Gaulle International Airport' in r.data

    def test_lambdaCall(self):
        self.app = app.test_client()
        r = self.app.get('/lambdaExample')
        print(r.data)
        assert b'Hello World!' in r.data