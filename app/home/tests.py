import time
from django.test import LiveServerTestCase
from selenium import webdriver

class NewTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    
    def test_name(self):
        self.browser.get(self.live_server_url)

        time.sleep(5)

        self.assertIn("Alunos", self.browser.title)
