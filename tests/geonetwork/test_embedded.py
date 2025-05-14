import allure

from playwright.sync_api import Page, BrowserContext, expect

from helper.configuration_manager import ConfigurationManager
from tests.common import screenshot_page, login
import pytest

@pytest.mark.skipif(condition=ConfigurationManager.write_tests_disabled(), reason="Write tests are disabled")
class TestEmbedded:
    metadata_imported = False

    @allure.epic("Geonetwork")
    @allure.feature("Metadata import")
    @allure.description("This test attempts import a metatadata.")
    def test_import_metadata(self, page: Page):
        login(page)
        page.goto("/geonetwork")
        page.wait_for_timeout(5000)
        page.get_by_role("button", name=" Contribute").click()
        page.get_by_role("menuitem", name=" Import new records", exact=True).get_by_role("link").click()
        page.get_by_label("Upload a file from URL").check()
        page.get_by_placeholder("http://").fill("https://www.geo2france.fr/geonetwork/srv/api/records/35d867a1-9420-449c-b0c4-442e7662eca6/formatters/xml")
        page.get_by_text("Overwrite metadata with same UUID").click()
        page.get_by_text("Publish").click()
        page.get_by_role("button", name="+   Import").click()
        page.get_by_role("link", name="").click(timeout=60000)
        screenshot_page(page, "import-metadata")
        TestEmbedded.metadata_imported = True


    @allure.epic("Geonetwork-ui")
    @allure.feature("Web-component map embedding")
    @allure.description("This test attempts to render a map in an embedded web-component.")
    def test_map_embedded(self, page: Page):
        if not TestEmbedded.metadata_imported:
            pytest.skip("Metadata import test didn't run successfully")

        page.goto("http://localhost:3000/datahub-map.html")
        page.wait_for_timeout(3000)
        expect(page.get_by_role("heading", name="should display html map")).to_be_visible()
        expect(page.locator("canvas")).to_be_visible()
        expect(page.get_by_label("Map Layer Legend").locator("div")).to_be_visible()
        screenshot_page(page, "WMS")
        expect(page.get_by_role("heading", name="TOUR_Rando_Etape_point")).to_be_visible()
        page.get_by_role("button", name="Randonnées en pays Noyonnais").click()
        page.get_by_role("button", name="Randonnées en pays Noyonnais - Points d'étapes - couche WFS du portail de Gé").click()
        page.wait_for_timeout(1000)
        screenshot_page(page, "WFS")

    @allure.epic("Geonetwork-ui")
    @allure.feature("Web-component table embedding")
    @allure.description("This test attempts to render a table in an embedded web-component.")
    def test_table_embedded(self, page: Page):
        if not TestEmbedded.metadata_imported:
            pytest.skip("Metadata import test didn't run successfully")

        page.goto("http://localhost:3000/datahub-table.html")
        page.wait_for_timeout(3000)
        expect(page.get_by_role("heading", name="should display html table")).to_be_visible()
        expect(page.get_by_text("Objects in this dataset. 1 - 10 of 110")).to_be_visible()
        expect(page.locator("[id=\"table-item-TOUR_Rando_Etape_point\\.1\"]").get_by_role("cell", name="Circuit des Evêques")).to_be_visible()
        screenshot_page(page, "Table")
