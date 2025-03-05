import allure

from playwright.sync_api import Page, expect

from tests.common import screenshot_page, login
import pytest


@allure.epic("Geonetwork")
@allure.feature("Wro4j")
@allure.description("This test attempts to load every GeoNetwork wro4j.")
@allure.title("Load GeoNetwork wro4j cache")
@pytest.mark.flaky(reruns=5)
def test_geo_network_webapp(page: Page):
    login(page)
    #Search page
    page.goto("/geonetwork/srv/eng/catalog.search")
    expect(page.get_by_role("combobox", name="Search")).to_be_visible(timeout=20000)
    screenshot_page(page,"geonetwork search")
    #Editor page
    page.goto("/geonetwork/srv/eng/catalog.edit#/board?from=1&to=30")
    expect(page.get_by_role("link", name="+ Add new record")).to_be_visible(timeout=20000)
    screenshot_page(page,"geonetwork editor")
    #admin page
    page.goto("/geonetwork/srv/eng/admin.console#/home")
    expect(page.locator("body")).to_contain_text(expected="Harvesting", timeout=20000)
    screenshot_page(page,"geonetwork admin")


