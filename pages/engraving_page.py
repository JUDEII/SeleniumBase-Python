from seleniumbase import BaseCase

class EngravingPage(BaseCase):

    RATING_TEXT = None
    PRICE_VAL = None
    REVIEW_SCORE = 4.0
    PRICE = 4000

    result_third_option = "(//span[starts-with(@class, 'a-size-base-plus a-color-base a-text-normal')])[3]"
    rating = "(//*[contains(@class, 'a-declarative')]//*[contains(@class, 'a-color-base')])[1]"
    price = "(//div[@id='corePriceDisplay_desktop_feature_div']//span[@class='a-price-whole'])"

    def click_resultThirdOption(self):
        self.wait_for_element_present(self.result_third_option, by="xpath")
        self.click_xpath(self.result_third_option)
        print("3rd item clicked successfully")

    def get_rating(self):
        self.wait_for_element_present(self.rating, by="xpath")
        self.RATING_TEXT = self.get_text(self.rating, by="xpath")
        print(self.RATING_TEXT)
        return self.RATING_TEXT

    def validate_ratingIsAboveFour(self):
        rating_text = self.get_rating()
        self.assert_text("5.0", self.rating, by="xpath")
        print("assert rating passed")

        # convert rating_text to number
        rating_float = float(rating_text)
        self.assert_true(rating_float > self.REVIEW_SCORE, msg="Rating is should be above 4.0")
        print("Rating validated successfully")
        self.wait(3)

    def get_price(self):
        self.wait_for_element_present(self.price, by="xpath")
        self.PRICE_VAL = self.get_text(self.price, by="xpath")
        print(self.PRICE_VAL)
        return self.PRICE_VAL

    def validate_priceValue(self):
        self.wait_for_element_visible(self.price, by="xpath")
        returned_price = self.get_price()
        price = float(returned_price.replace('$', '').replace(',', ''))
        self.assert_true(price <= self.PRICE, msg="Price should be less than or equal 4000")
        print("Item price validated successfully")




