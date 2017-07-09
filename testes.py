from unittest import TestCase, main
from models import Password
from app import app, db
from views import home


class testApp(TestCase):
    def setUp(self):
        test_app = app.test_client()
        self.response_home = test_app.get("/")
        self.response_update = test_app.get("/update/10")
        self.response_select = test_app.get("/select/10")
        self.response_str = self.response_home.data.decode('utf-8')
        self.banco = Password

    def test_status_code_home(self):
        self.assertEqual(200, self.response_home.status_code)

    def test_status_code_update(self):
        self.assertEqual(200, self.response_update.status_code)

    def test_status_code_select(self):
        self.assertEqual(404, self.response_select.status_code)

    def test_bootstrap_css(self):
        self.assertIn('bootstrap.min.css', self.response_str)
        
    def test_content(self):
        self.assertIn('<title>  Home  </title>', str(self.response_str))
        self.assertIn('<legend>Cadastrar Site:</legend>',
                      str(self.response_str))

    def test_model_1_insert(self):
        test = self.banco('site_test', "user", "email", 'senha')
        db.session.add(test)
        self.assertEqual(db.session.commit(), None)

    def test_model_2_delete(self):
        test = self.banco.query.filter_by(site='site_test').first()
        db.session.delete(test)
        self.assertEqual(db.session.commit(), None)

if __name__ == '__main__':
    main()
