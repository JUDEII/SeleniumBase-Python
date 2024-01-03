from pages.engraving_page import EngravingPage
from pages.home_page import HomePage
from pages.side_menu import SideMenu
from pages.start_browser import StartBrowser
class PurchaseEngravingTest(StartBrowser,HomePage,SideMenu,EngravingPage):

    def setUp(self):
        super().setUp()
        StartBrowser.setUp(self)
        HomePage.setUp(self)
        SideMenu.setUp(self)
        EngravingPage.setUp(self)

        print("PurchaseEngravingTest *STARTS*")
        self.launch_browser()
        self.verify_page_title()
        self.verify_logo_is_present()

    def tearDown(self):
        print("PurchaseEngravingTest *ENDS*")
        super().tearDown()

    def test_purchaseEngraving(self):
        self.click_dropdownMenuOption()
        self.click_artsAndCraftOption()
        self.click_beadingAndJewelryOption()
        self.click_artsAndCraftAndSewingOption()
        self.click_beadingAndJewelryMakingOption()
        self.click_engravingMachinesAndToolsOption()
        self.click_sortByDropdown()
        self.select_sortByHighToLowOption()
        self.click_resultThirdOption()
        self.validate_ratingIsAboveFour()
        self.validate_priceValue()
