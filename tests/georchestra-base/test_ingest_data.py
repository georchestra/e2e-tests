import allure

from tests.common import screenshot_page, login
from playwright.sync_api import Page, expect

@allure.feature("geOrchestra")
@allure.story("Datafeeder")
@allure.description("This test attempts to load GeoNetwork.")
@allure.title("Test the GeoNetwork webapp")
def test_import_shp_datafeeder(page: Page):
    login(page)
    page.goto("/import/")
    page.locator("input[type=file]").set_input_files("../../fixtures/antenne.zip")
    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Upload").click()
    page.get_by_role("button", name="-", exact=True).click()
    page.get_by_role("button", name="WGS84").click()
    page.get_by_role("button", name="WGS84").click()
    page.get_by_role("button", name="Lambert").click()
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
    expect(page.get_by_role("button", name="Metadata record")).to_be_visible(timeout=15000)
    expect(page.get_by_role("button", name="Map viewer")).to_be_visible()
    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="Metadata record").click()
    page1 = page1_info.value
    expect(page1.get_by_text("Awesome").first).to_be_visible()
    expect(page1.get_by_text("Antennes - WMS")).to_be_visible()
    screenshot_page(page1, "metadata")
    page1.close()
    with page.expect_popup() as page2_info:
        page.get_by_role("button", name="Map viewer").click()
    page2 = page2_info.value
    expect(page2.locator("canvas")).to_be_visible()
    screenshot_page(page2, "mapviewer")
    page2.close()
    with page.expect_popup() as page3_info:
        page.get_by_role("button", name="OGC API").click()
    page3 = page3_info.value
    page3_url = page3_info.value.url
    expect(page3.locator("pre")).to_be_visible()
    screenshot_page(page3, "ogcapi")
    page3.close()

    response = page.goto(page3_url)
    assert response.headers["content-type"] == "application/geo+json"
    assert 0 < len(response.headers["access-control-allow-origin"]) < 2
    assert response.json()['numberMatched'] == 14
    assert response.json()['numberReturned'] == 10
