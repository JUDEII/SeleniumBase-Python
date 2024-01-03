from seleniumbase import BaseCase


class SideMenu(BaseCase):

    dropdown_menu = "//span[@class='hm-icon-label']"
    arts_and_craft_option = "//div[normalize-space()='Arts & Crafts']"
    beading_and_jewelry_option = "//a[contains(text(), 'Beading & Jewelry Making')]"
    arts_and_craft_and_sewing_option = "//span[contains(text(),'Arts, Crafts & Sewing')]"
    beading_and_jewelry_making_option = "//span[contains(text(),'Beading & Jewelry Making')]"
    engraving_machines_and_tools_option = "//span[contains(text(),'Jewelry Making Engraving Machines & Tools')]"
    sort_by_dropdown = "a-autoid-0-announce"
    sort_by_high_to_low_option = "s-result-sort-select_2"

    def click_dropdownMenuOption(self):
        self.click(self.dropdown_menu, by="id")
        print("Side menu clicked successfully")
        self.wait(3)

    def click_artsAndCraftOption(self):
        self.wait_for_element_present(self.arts_and_craft_option, by="xpath")
        self.click_xpath(self.arts_and_craft_option)
        print("Arts & Craft clicked successfully")

    def click_beadingAndJewelryOption(self):
        self.wait_for_element_present(self.beading_and_jewelry_option, by="xpath")
        self.click_visible_elements(self.beading_and_jewelry_option, by="xpath")
        print("Beading & Jewelry clicked successfully")

    def click_artsAndCraftAndSewingOption(self):
        self.wait_for_element_present(self.arts_and_craft_and_sewing_option, by="xpath")
        self.click_visible_elements(self.arts_and_craft_and_sewing_option, by="xpath")
        print("Arts, Craft & Sewing clicked successfully")

    def click_beadingAndJewelryMakingOption(self):
        self.wait_for_element_present(self.beading_and_jewelry_making_option, by="xpath")
        self.click_visible_elements(self.beading_and_jewelry_making_option, by="xpath")
        print("Beading & Jewelry Making clicked successfully")

    def click_engravingMachinesAndToolsOption(self):
        self.wait_for_element_present(self.engraving_machines_and_tools_option, by="xpath")
        self.click_visible_elements(self.engraving_machines_and_tools_option, by="xpath")
        print("Engraving machines and tools clicked successfully")

    def click_sortByDropdown(self):
        self.wait_for_element_present(self.sort_by_dropdown, by="id")
        self.click(self.sort_by_dropdown, by="id")
        print("sort by dropdown clicked")

    def select_sortByHighToLowOption(self):
        self.wait_for_element_present(self.sort_by_high_to_low_option, by="id")
        self.click(self.sort_by_high_to_low_option, by="id")
        print("high to low option clicked")