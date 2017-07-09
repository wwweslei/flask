from unittest import TestCase, main
from app import app


class testApp(TestCase):
    def setUp(self):
        test_app = app.test_client()
        self.response = test_app.get("/")
        self.response_str = self.response.data.decode('utf-8')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

if __name__ == '__main__':
    main()
