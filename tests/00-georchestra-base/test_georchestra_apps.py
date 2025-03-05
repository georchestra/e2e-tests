import allure

from playwright.sync_api import Page, expect

from tests.common import screenshot_page, login


@allure.epic("Geonetwork")
@allure.feature("Web interface")
@allure.description("This test attempts to load GeoNetwork.")
@allure.title("Test the GeoNetwork webapp")
def test_geonetwork_webapp(page: Page):
    page.goto("/geonetwork/srv/eng/catalog.search")
    screenshot_page(page,"geonetwork")
    expect(page.get_by_role("combobox", name="Search")).to_be_visible(timeout=20000)

@allure.epic("Console")
@allure.feature("Web interface")
@allure.description("This test attempts to load the 'create account' page from the Console.")
@allure.title("Test the 'create account' interface from the Console")
def test_console_create_account(page: Page):
    page.goto("/console/account/new")
    screenshot_page(page,"console-createAccount")
    expect(page.get_by_role("heading", name="New account. Create your")).to_be_visible()

@allure.epic("Console")
@allure.feature("Web interface")
@allure.description("This test attempts to load the 'password recovery' page from the Console.")
@allure.title("Test the 'password recovery' interface from the Console")
def test_console_password_recovery(page: Page):
    page.goto("/console/account/passwordRecovery")
    screenshot_page(page,"console-passwordRecovery")
    expect(page.get_by_role("heading", name="Ask for a new password. You'")).to_be_visible()

@allure.epic("Datafeeder")
@allure.feature("Web interface")
@allure.description("This test attempts to load the 'datafeeder'/'import' wizard page, from the DataFeeder geOrchestra webapp. As it requires to be logged into geOrchestra, an initial login is performed.")
@allure.title("Test the DataFeeder webapp")
def test_datafeeder_webapp(page: Page):
    login(page)
    page.goto("/import/")
    screenshot_page(page,"datafeeder")
    expect(page.locator("ngx-dropzone")).to_be_visible()

@allure.epic("Geoserver")
@allure.feature("Web interface")
@allure.description("This test attempts to load the GeoServer main page.")
@allure.title("Test the GeoServer webapp")
def test_geoserver_webapp(page: Page):
    page.goto("/geoserver/web/")
    screenshot_page(page,"geoserver")
    expect(page.get_by_role("heading", name="Welcome")).to_be_visible()

@allure.epic("Mapstore")
@allure.feature("Web interface")
@allure.description("This test attempts to load the MapStore landing page.")
@allure.title("Test the MapStore webapp")
def test_map_store_webapp(page: Page):
    page.goto("/mapstore/")
    screenshot_page(page,"mapstore")
    expect(page.locator("canvas")).to_be_visible(timeout=20000)
