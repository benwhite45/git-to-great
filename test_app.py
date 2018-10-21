import app
import unittest

class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        testApp = app.create_app()
        self.client = testApp.test_client()
 
    # executed after each test
    def tearDown(self):
        pass

    # test that /git returns 'From git...'
    def test_git(self):
        response = self.client.get('/git')
        self.assertIn( 'From git...', response.data)

    # test that /great returns '...to great'
    def test_great(self):
        response = self.client.get('/great')
        self.assertEqual(response.status_code, 200)
        self.assertIn('...to great', response.data)

if __name__ == "__main__":
    unittest.main()
