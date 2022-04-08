from turtle import home
import pytest


#@pytest.mark.parametrize("user,password", [("standard_user", "secret_sauce"), ("locked_out_user", "secret_sauce")])
#def test_login_sauce(loginPage, user, password):
#    loginPage.do_login(user, password)
#    assert loginPage.was_login_successful(), "login failed"

#def test_search_bar(homepage):
#    toSearch = "shirts"
#    homepage.search(toSearch)
#    assert toSearch in homepage.get_products_titles()

def test_product_cart(homepage):
    homepage.add_first_item_to_cart()
    assert int(homepage.get_cart_products_quantity()) is 1