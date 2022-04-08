import pytest


@pytest.mark.parametrize("user,password", [("standard_user", "secret_sauce"), ("locked_out_user", "secret_sauce")])
def test_login_sauce(loginPage, user, password):
    loginPage.do_login(user, password)
    assert loginPage.was_login_successful(), "login failed"

