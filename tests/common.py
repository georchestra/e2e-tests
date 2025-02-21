import allure
from playwright.sync_api import Page

from helper.configuration_manager import ConfigurationManager



def screenshot_page(page, name):
    png_bytes = page.screenshot()
    allure.attach(
        png_bytes,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )

def login(page: Page, cas: bool = False, username: str = ConfigurationManager.local_admin()['username'], password: str = ConfigurationManager.local_admin()['password']):
    page.goto("/datahub/")
    page.get_by_role("link", name="login").click()
    username_input = page.get_by_placeholder("Username")
    if cas:
        username_input = page.locator("#username")
    username_input.fill(username)
    username_input.press("Tab")
    password_input = page.get_by_placeholder("Password")
    if cas:
        password_input = page.locator("#password")
    password_input.fill(password)
    password_input.press("Enter")