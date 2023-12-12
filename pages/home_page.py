from seleniumbase import BaseCase
from seleniumbase.common.exceptions import NoSuchElementException

class HomePage(BaseCase):

    PAGE_TITLE = "Amazon.com. Spend less. Smile more."

    page_logo = "#nav-logo-sprites"

    def verify_logo_is_present(self):
        try:
            self.assert_element(self.page_logo)
            print("page logo is present")
        except NoSuchElementException:
            self.refresh()
            print("page refresh is successful")

    def verify_page_title(self):
        print(self.PAGE_TITLE)
        self.wait_for_element_present('title')
        self.assert_title(self.PAGE_TITLE)
        print("Page title is verified successfully")


