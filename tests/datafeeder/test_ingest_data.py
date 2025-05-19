import allure

from helper.configuration_manager import ConfigurationManager
from tests.common import screenshot_page, login
from playwright.sync_api import Page, expect

import pytest

@allure.epic("Datafeeder")
@allure.feature("Ingestion")
@allure.description("This test attempts to load a SHP file through datafeeder and check links.")
@pytest.mark.skipif(condition=ConfigurationManager.write_tests_disabled(), reason="Write tests are disabled")
def test_import_shp_datafeeder(page: Page):
    login(page)
    page.goto("/import/")
    screenshot_page(page, "datafeeder")
    page.locator("input#undefined").first.set_input_files("./resources/files/antenne.zip")
    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Upload").click()
    # page.get_by_role("button", name="-", exact=True).click()
    # page.get_by_role("button", name="WGS84").click()
    # page.get_by_role("button", name="Lambert").click()
    page.get_by_role("button", name="OK, my data are correct").click()
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("Antennes")
    page.locator("textarea[name=\"textArea\"]").click()
    page.locator("textarea[name=\"textArea\"]").fill("Awesome")
    page.get_by_role("button", name="next").click()
    page.get_by_role("textbox").fill("a")
    page.locator("#tags div").nth(1).click()
    page.get_by_role("button", name="Addresses").click()
    page.get_by_role("button", name="next").click()
    page.get_by_role("button", name="next").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("This is the process")
    page.get_by_role("button", name="next").click()
    page.get_by_role("button", name="Submit").click()
    screenshot_page(page, "after-submit-click")
    # wait for the data to be ingested
    for i in range(5):
        page.wait_for_timeout(10000)
        if page.get_by_role("button", name="Metadata record").is_visible(timeout=5000):
            break
        page.reload()
    expect(page.get_by_role("button", name="Metadata record")).to_be_visible()
    screenshot_page(page, "after-submit-click-wait")
    screenshot_page(page, "after-ingestion")
    expect(page.get_by_role("button", name="Map viewer")).to_be_visible()
    with page.expect_popup() as geonetwork_info:
        page.get_by_role("button", name="Metadata record").click()
    geonetwork = geonetwork_info.value
    screenshot_page(geonetwork, "metadata")
    expect(geonetwork.get_by_text("Awesome").first).to_be_visible(timeout=60000)
    expect(geonetwork.locator("#main-content")).to_contain_text("psc:antennes")
    geonetwork.close()
    with page.expect_popup() as geoserver_info:
        page.get_by_role("button", name="Map viewer").click()
    geoserver = geoserver_info.value
    screenshot_page(geoserver, "mapviewer")
    expect(geoserver.locator("canvas")).to_be_visible()
    geoserver.close()
    with page.expect_popup() as ogcapi_info:
        page.get_by_role("button", name="OGC API").click()
    ogcapi = ogcapi_info.value
    ogcapi_url = ogcapi_info.value.url
    screenshot_page(ogcapi, "ogcapi")
    expect(ogcapi.locator("body")).to_be_visible()
    ogcapi.close()

    page.set_extra_http_headers({"origin": "http://localhost:1234/"})
    response = page.goto(ogcapi_url)
    assert response.headers["content-type"] == "application/geo+json"
    assert 0 < len(response.headers["access-control-allow-origin"]) < 2
    assert response.json()['numberMatched'] == 56
    assert response.json()['numberReturned'] == 10
