import requests
import json
import unittest
import os.path
import logging
import sys
from glob import glob

# test data directory
boldPattern = os.path.join('test/bold/validData', '*.json')
T1wPattern = os.path.join('test/T1w/validData', '*.json')

# missing field data directory
boldMissingPattern = os.path.join('test/bold/missingField', '*.json')
T1wMissingPattern = os.path.join('test/T1w/missingField', '*.json')


# url for GET
def getURL(post_resp, url):
    dirID = post_resp.json()["_id"]
    resURL = url + "/" + dirID
    return resURL


def getRequest(post_resp, url):
    # GET
    get_resp = requests.get(getURL(post_resp, url))
    return get_resp.json()


###### MAIN ######
header = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
authenticated_header = header.copy()
authenticated_header['Authorization'] = os.environ.get('API_TOKEN', '<secret_token>')
numOfTestData = 84
urlBold = "http://0.0.0.0:80/api/v1/bold"
urlT1w = "http://0.0.0.0:80/api/v1/T1w"
codeForInvalid = 422


class TestCase(unittest.TestCase):
    def test_00_GETAllData(self):
        log = logging.getLogger("mriqcwebapi")

        input_count = 0
        for fileName in glob(T1wPattern):
            with open(fileName) as fp:
                inputData = json.load(fp)

                input_count += 1  # POST request
            postResponse = requests.post(urlT1w, data=json.dumps(inputData),
                                         headers=authenticated_header)
            self.assertTrue(postResponse.raise_for_status() is None)

        # GET request
        # print requests.get(urlT1w)
        get_resp = requests.get(urlT1w).json()
        log.debug("total: %d (input_count=%d)", get_resp['_meta']['total'],
                  input_count)
        self.assertTrue(input_count == get_resp['_meta']['total'])


    ########## Testing Bold ############
    def test_01_ConnectionStatus(self):
        log = logging.getLogger("mriqcwebapi")

        for file_name in glob(boldPattern):
            with open(file_name) as fp:
                input_data = json.load(fp)

            # POST request
            post_resp = requests.post(
                urlBold, data=json.dumps(input_data), headers=authenticated_header)

            if post_resp.raise_for_status() is not None:
                log.debug('Response: %s', post_resp.json())
                self.assertTrue(post_resp.raise_for_status() is None)

            # GET request
            get_resp = requests.get(getURL(post_resp, urlBold))
            if get_resp.raise_for_status() is not None:
                log.debug('Response: %s', get_resp.json())
                self.assertTrue(get_resp.raise_for_status() is None)


    def test_02_MissingFieldInput(self):
        log = logging.getLogger("mriqcwebapi")

        for file_name in glob(boldMissingPattern):
            with open(file_name) as fp:
                input_data = json.load(fp)
                # POST request
                post_resp = requests.post(
                    urlBold, data=json.dumps(input_data),
                    headers=authenticated_header)
                # print post_resp.status_code
                self.assertTrue(post_resp.status_code == codeForInvalid)


    ########## Testing T1w ############
    def test_03_ConnectionStatus(self):
        log = logging.getLogger("mriqcwebapi")

        for file_name in glob(T1wPattern):
            with open(file_name) as fp:
                input_data = json.load(fp)
            # print input_data
            # POST request
            post_resp = requests.post(
                urlT1w, data=json.dumps(input_data), headers=authenticated_header)

            log.debug('Response: %s', post_resp.json())
            if post_resp.raise_for_status() is not None:
                self.assertTrue(post_resp.raise_for_status() is None)

            # GET request
            get_resp = requests.get(getURL(post_resp, urlT1w))
            if get_resp.raise_for_status() is not None:
                log.debug('Response: %s', get_resp.json())
                self.assertTrue(get_resp.raise_for_status() is None)


    def test_04_MissingFieldInput(self):
        log = logging.getLogger("mriqcwebapi")

        for file_name in glob(T1wMissingPattern):
            with open(file_name) as fp:
                input_data = json.load(fp)
                # POST request
                post_resp = requests.post(
                    urlT1w, data=json.dumps(input_data),
                    headers=authenticated_header)
                # print post_resp.status_code
                self.assertTrue(post_resp.status_code == codeForInvalid)


    ########## Cross Testing: send data to wrong end point ############
    def test_05_boldDataToT1wEndPoint(self):
        log = logging.getLogger("mriqcwebapi")

        for file_name in glob(boldPattern):
            with open(file_name) as fp:
                input_data = json.load(fp)
                # POST request
                post_resp = requests.post(
                    urlT1w, data=json.dumps(input_data),
                    headers=authenticated_header)
                self.assertTrue(post_resp.status_code == codeForInvalid)


    def test_06_T1wDataToBoldEndPoint(self):
        log = logging.getLogger("mriqcwebapi")

        for file_name in glob(T1wPattern):
            with open(file_name) as fp:
                input_data = json.load(fp)
                # POST request
                post_resp = requests.post(
                    urlBold, data=json.dumps(input_data),
                    headers=authenticated_header)
                self.assertTrue(post_resp.status_code == codeForInvalid)


    def test_07_T1wDataValid(self):
        for file_name in glob(T1wPattern):
            with open(file_name) as fp:
                input_data = json.load(fp)
                # 2. POST request
                post_resp = requests.post(
                    urlT1w, data=json.dumps(input_data),
                    headers=authenticated_header)

                # 3. GET request
                queried_data = getRequest(post_resp, urlT1w)
                # 4. validate input data and queried data
                for key in input_data:
                    # check missing key
                    self.assertTrue(key in queried_data)
                    # check key-value pair match
                    self.assertTrue(input_data[key] == queried_data[key])


    def test_08_boldDataValid(self):
        for file_name in glob(boldPattern):
            with open(file_name) as fp:
                input_data = json.load(fp)

            # 2. POST request
            post_resp = requests.post(
                urlBold, data=json.dumps(input_data),
                headers=authenticated_header)
            self.assertTrue(post_resp.raise_for_status() is None)

            # 3. GET request
            queried_data = getRequest(post_resp, urlBold)
            # 4. validate input data and queried data
            for key in input_data:
                # check missing key
                self.assertTrue(key in queried_data)
                # check key-value pair match
                self.assertTrue(input_data[key] == queried_data[key])


    def test_09_failedAuth(self):
        with open(glob(boldPattern)[0]) as fp:
            inputData = json.load(fp)
            postResponse = requests.post(urlBold, data=json.dumps(inputData),
                                         headers=header)
            self.assertTrue(postResponse.status_code == 401)  # ****************


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("mriqcwebapi").setLevel(logging.DEBUG)

    unittest.main()
