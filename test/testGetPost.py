import json
import logging
import os
from glob import glob

import pytest
import requests

# test data directory
boldPattern = os.path.join("test/bold/validData", "*.json")
T1wPattern = os.path.join("test/T1w/validData", "*.json")
ratingPattern = os.path.join("test/rating/validData", "*.json")

# missing field data directory
boldMissingPattern = os.path.join("test/bold/missingField", "*.json")
T1wMissingPattern = os.path.join("test/T1w/missingField", "*.json")

pytestmark = pytest.mark.integration


# url for GET
def getURL(post_resp, url):
    dirID = post_resp.json()["_id"]
    resURL = url + "/" + dirID
    return resURL


def getRequest(post_resp, url):
    # GET
    get_resp = requests.get(getURL(post_resp, url))
    return get_resp.json()


# MAIN ######
header = {"content-type": "application/json", "Accept-Charset": "UTF-8"}
authenticated_header = header.copy()
authenticated_header["Authorization"] = os.environ.get("API_TOKEN", "<secret_token>")
numOfTestData = 84

api_base_url = os.environ.get("MRIQC_API_BASE_URL", "http://localhost")
urlBold = f"{api_base_url}/api/v1/bold"
urlT1w = f"{api_base_url}/api/v1/T1w"
urlRating = f"{api_base_url}/api/v1/rating"
urlRatingCounts = f"{api_base_url}/api/v1/rating_counts?{{}}"
codeForInvalid = 422


def test_00_GETAllData():
    log = logging.getLogger("mriqcwebapi")

    input_count = 0
    for fileName in glob(T1wPattern):
        with open(fileName) as fp:
            inputData = json.load(fp)

            input_count += 1  # POST request
        postResponse = requests.post(
            urlT1w, data=json.dumps(inputData), headers=authenticated_header
        )
        postResponse.raise_for_status()

    # GET request
    get_resp = requests.get(urlT1w).json()
    log.debug("total: %d (input_count=%d)", get_resp["_meta"]["total"], input_count)
    assert input_count == get_resp["_meta"]["total"]


# Testing Bold ############
def test_01_ConnectionStatus():
    log = logging.getLogger("mriqcwebapi")

    for file_name in glob(boldPattern):
        with open(file_name) as fp:
            input_data = json.load(fp)

        # POST request
        post_resp = requests.post(
            urlBold, data=json.dumps(input_data), headers=authenticated_header
        )
        post_resp.raise_for_status()

        # GET request
        get_resp = requests.get(getURL(post_resp, urlBold))
        if get_resp.raise_for_status() is not None:
            log.debug("Response: %s", get_resp.json())
            assert get_resp.raise_for_status() is None


def test_02_MissingFieldInput():
    for file_name in glob(boldMissingPattern):
        with open(file_name) as fp:
            input_data = json.load(fp)
            # POST request
            post_resp = requests.post(
                urlBold, data=json.dumps(input_data), headers=authenticated_header
            )
            assert post_resp.status_code == codeForInvalid


# Testing T1w ############
def test_03_ConnectionStatus():
    log = logging.getLogger("mriqcwebapi")

    for file_name in glob(T1wPattern):
        with open(file_name) as fp:
            input_data = json.load(fp)
        # POST request
        post_resp = requests.post(
            urlT1w, data=json.dumps(input_data), headers=authenticated_header
        )

        log.debug("Response: %s", post_resp.json())
        if post_resp.raise_for_status() is not None:
            assert post_resp.raise_for_status() is None

        # GET request
        get_resp = requests.get(getURL(post_resp, urlT1w))
        if get_resp.raise_for_status() is not None:
            log.debug("Response: %s", get_resp.json())
            assert get_resp.raise_for_status() is None


def test_04_MissingFieldInput():
    for file_name in glob(T1wMissingPattern):
        with open(file_name) as fp:
            input_data = json.load(fp)
            # POST request
            post_resp = requests.post(
                urlT1w, data=json.dumps(input_data), headers=authenticated_header
            )
            assert post_resp.status_code == codeForInvalid


# Cross Testing: send data to wrong end point ############
def test_05_boldDataToT1wEndPoint():
    for file_name in glob(boldPattern):
        with open(file_name) as fp:
            input_data = json.load(fp)
            # POST request
            post_resp = requests.post(
                urlT1w, data=json.dumps(input_data), headers=authenticated_header
            )
            assert post_resp.status_code == codeForInvalid


def test_06_T1wDataToBoldEndPoint():
    for file_name in glob(T1wPattern):
        with open(file_name) as fp:
            input_data = json.load(fp)
            # POST request
            post_resp = requests.post(
                urlBold, data=json.dumps(input_data), headers=authenticated_header
            )
            assert post_resp.status_code == codeForInvalid


def test_07_T1wDataValid():
    for file_name in glob(T1wPattern):
        with open(file_name) as fp:
            input_data = json.load(fp)
            # 2. POST request
            post_resp = requests.post(
                urlT1w, data=json.dumps(input_data), headers=authenticated_header
            )

            # 3. GET request
            queried_data = getRequest(post_resp, urlT1w)
            # 4. validate input data and queried data
            for key in input_data:
                # check missing key
                assert key in queried_data
                # check key-value pair match
                assert input_data[key] == queried_data[key]


def test_08_boldDataValid():
    for file_name in glob(boldPattern):
        with open(file_name) as fp:
            input_data = json.load(fp)

        # 2. POST request
        post_resp = requests.post(
            urlBold, data=json.dumps(input_data), headers=authenticated_header
        )
        post_resp.raise_for_status()

        # 3. GET request
        queried_data = getRequest(post_resp, urlBold)
        # 4. validate input data and queried data
        for key in input_data:
            # check missing key
            assert key in queried_data
            # check key-value pair match
            assert input_data[key] == queried_data[key]


def test_09_failedAuth():
    with open(glob(boldPattern)[0]) as fp:
        inputData = json.load(fp)
        postResponse = requests.post(urlBold, data=json.dumps(inputData), headers=header)
        assert postResponse.status_code == 401


def test_10_ratingDataValid():
    for file_name in glob(ratingPattern):
        with open(file_name) as fp:
            input_data = json.load(fp)

            # 2. POST request
            post_resp = requests.post(
                urlRating, data=json.dumps(input_data), headers=authenticated_header
            )
            post_resp.raise_for_status()

    # retrive counts of ratings we just submitted
    get_resp = requests.get(
        urlRatingCounts.format('aggregate={"$value":"57cd35190da3c813a3c3dadccd8a4ad7"}'),
        headers=authenticated_header,
    )
    data = get_resp.json()
    for elem in data["_items"]:
        if elem["_id"] == "good":
            assert elem["count"] == 3
        if elem["_id"] == "bad":
            assert elem["count"] == 1
