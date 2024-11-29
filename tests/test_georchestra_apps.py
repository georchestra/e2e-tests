import os
import allure

from playwright.sync_api import Page, expect

from common import screenshot_page

BASE_URL="https://georchestra-127-0-0-1.nip.io"
LOCAL_ACCOUNT_USERNAME=os.getenv("LOCAL_ACCOUNT_USERNAME")
LOCAL_ACCOUNT_PASSWORD=os.getenv("LOCAL_ACCOUNT_PASSWORD")

def login(page: Page, cas: bool = False):
    page.goto(f"{BASE_URL}/datahub/")
    page.get_by_role("link", name="login").click()
    username_input = page.get_by_placeholder("Username")
    if cas:
        username_input = page.locator("#username")
    username_input.fill(LOCAL_ACCOUNT_USERNAME)
    username_input.press("Tab")
    password_input = page.get_by_placeholder("Password")
    if cas:
        password_input = page.locator("#password")
    password_input.fill(LOCAL_ACCOUNT_PASSWORD)
    password_input.press("Enter")

@allure.epic("Web interface")
@allure.feature("geOrchestra")
@allure.story("GeoNetwork")
@allure.description("This test attempts to load GeoNetwork.")
@allure.title("Test the GeoNetwork webapp")
def test_geo_network_webapp(page: Page):
    page.goto(f"{BASE_URL}/geonetwork/srv/eng/catalog.search")
    # page.wait_for_timeout(20000)
    screenshot_page(page,"geonetwork")
    expect(page.get_by_role("combobox", name="Search")).to_be_visible()

@allure.epic("Web interface")
@allure.feature("geOrchestra")
@allure.story("Console")
@allure.description("This test attempts to load the 'create account' page from the Console.")
@allure.title("Test the 'create account' interface from the Console")
def test_console_create_account(page: Page):
    page.goto(f"{BASE_URL}/console/account/new")
    screenshot_page(page,"console-createAccount")
    expect(page.get_by_role("heading", name="New account. Create your")).to_be_visible()

@allure.epic("Web interface")
@allure.feature("geOrchestra")
@allure.story("Console")
@allure.description("This test attempts to load the 'password recovery' page from the Console.")
@allure.title("Test the 'password recovery' interface from the Console")
def test_console_password_recovery(page: Page):
    page.goto(f"{BASE_URL}/console/account/passwordRecovery")
    screenshot_page(page,"console-passwordRecovery")
    expect(page.get_by_role("heading", name="Ask for a new password. You'")).to_be_visible()

@allure.epic("Web interface")
@allure.feature("geOrchestra")
@allure.story("DataFeeder")
@allure.description("This test attempts to load the 'datafeeder'/'import' wizard page, from the DataFeeder geOrchestra webapp. As it requires to be logged into geOrchestra, an initial login is performed.")
@allure.title("Test the DataFeeder webapp")
def test_data_feeder_webapp(page: Page):
    login(page)
    page.goto(f"{BASE_URL}/import/")
    screenshot_page(page,"datafeeder")
    expect(page.locator("ngx-dropzone")).to_be_visible()

@allure.epic("Web interface")
@allure.feature("geOrchestra")
@allure.story("GeoServer")
@allure.description("This test attempts to load the GeoServer main page.")
@allure.title("Test the GeoServer webapp")
def test_geo_server_webapp(page: Page):
    page.goto(f"{BASE_URL}/geoserver/web/")
    screenshot_page(page,"geoserver")
    expect(page.get_by_role("heading", name="Welcome")).to_be_visible()

@allure.epic("Web interface")
@allure.feature("geOrchestra")
@allure.story("MapStore")
@allure.description("This test attempts to load the MapStore landing page.")
@allure.title("Test the MapStore webapp")
def test_map_store_webapp(page: Page):
    page.goto(f"{BASE_URL}/mapstore/")
    screenshot_page(page,"mapstore")
    expect(page.locator("canvas")).to_be_visible()

@allure.epic("Web interface")
@allure.feature("geOrchestra")
@allure.story("GeoServer")
@allure.description("This test attempts to open Geoserver's Layer Preview of the public 'arrondissement' layer.")
@allure.title("Test a GeoServer preview of the 'arrondissement' layer")
def test_geo_server_refer_sols_layer_preview(page: Page):
    page.goto(f"{BASE_URL}/geoserver/")
    page.get_by_role("link", name="Layer Preview Layer Preview").click()
    page.get_by_placeholder("Search").click()
    page.get_by_placeholder("Search").fill("arrondissement")
    page.get_by_placeholder("Search").press("Enter")
    screenshot_page(page,"gs-layers-preview")
    page.wait_for_timeout(1000)
    # page1 = page.wait_for_popup(lambda: page.get_by_role("link", name="OpenLayers").first().click())
    # assert page1.locator("canvas").is_visible()
    # page1.screenshot(path="gs-layer-preview")

@allure.epic("Web interface")
@allure.feature("geOrchestra")
@allure.story("MapStore")
@allure.description("This test attempts to load the 'arrondissement' layer into the Mapstore viewer.")
@allure.title("Test to load the 'arrondissement' layer into the Mapstore viewer")
def test_mapstore_add_refer_sols_layer(page: Page):
    page.goto(f"{BASE_URL}/mapstore/")
    page.locator("#drawer-menu-button").click()
    page.get_by_role("button", name="").click()
    page.locator(".Select-arrow").click()
    page.get_by_label("Service de données de la").click()
    page.get_by_placeholder("text to search...").click()
    page.get_by_placeholder("text to search...").fill("arrondissement")
    page.get_by_placeholder("text to search...").press("Enter")
    page.locator("#mapstore-metadata-explorer .catalog-results").get_by_role("button").click()
    screenshot_page(page, "mapstore")
    expect(page.locator("#mapstore-layers").get_by_text("test")).to_be_visible()
