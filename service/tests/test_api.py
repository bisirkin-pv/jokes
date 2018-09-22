import urllib3
import unittest


class TestApi(unittest.TestCase):
    def setUp(self):
        self.http = urllib3.PoolManager()

    def test_on_availability(self):
        request = self.http.request('GET', 'http://localhost:8787')
        print(request.status)
        self.assertEqual(request.status, 200)

    def tearDown(self):
        self.http.clear()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
