import allure
import pytest
import requests
from requests.exceptions import HTTPError

@allure.epic("Data API")
@allure.feature("Headers")
@allure.description("Test if data-api response headers contains only one Access-Control-Allow-Origin header.")
@allure.title("Test the data-api headers")
def test_data_api_no_double_access_control_allow_origin(base_url):
    url = base_url + "/data/ogcapi/"
    headers = {"Origin": "http://localhost:1234/"}

    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()

    access_control_allow_origin_header = response.headers.get("Access-Control-Allow-Origin")
    # If two headers are present (e.g * and *) response.headers.get("Access-Control-Allow-Origin") returns "*, *"
    assert access_control_allow_origin_header == "*", "There should be only one header with Access-Control-Allow-Origin"

@allure.epic("Geoserver")
@allure.feature("Headers")
@allure.description("This test attempts to load GeoNetwork.")
@allure.title("Test the Geoserver headers")
def test_geoserver_wms_no_double_access_control_allow_origin(base_url: str):
    url = base_url + "/geoserver/wms"
    headers = {"Origin": "http://localhost:1234/"}

    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()

    access_control_allow_origin_header = response.headers.get("Access-Control-Allow-Origin")
    # If two headers are present (e.g * and *) response.headers.get("Access-Control-Allow-Origin") returns "*, *"
    assert access_control_allow_origin_header == "https://georchestra-127-0-0-1.nip.io", \
        "There should be only one header with Access-Control-Allow-Origin"