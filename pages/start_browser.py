from seleniumbase import BaseCase
class StartBrowser(BaseCase):

    url = "https://www.amazon.com"

    def launch_browser(self):
        self.open(self.url)
        self.maximize_window()

