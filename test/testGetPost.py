import requests, json, unittest, os.path
from glob import glob

# test data directory
pattern = os.path.join('derivatives/', '*.json')

def getRequest(postResponse, url):
    # url for GET
    dirID = postResponse.json()["_id"]
    getURL = url + "/" + dirID
    # getURL = url + "/" + "haha"
    # GET
    getResponse = requests.get(getURL)
    return getResponse.json()

###### MAIN ######
header = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

class TestCase(unittest.TestCase):

    def testDataValid(self):
        # 1. initialize param. change to others for later use
        url = "http://localhost:80/scenarios"
        
        for fileName in glob(pattern):
            with open(fileName) as fp:
                inputData = json.load(fp) 
                # 2. POST request
                postResponse = requests.post(url, data = json.dumps(inputData), headers = header)

                # 3. GET request
                queriedData = getRequest(postResponse, url)
                
                # 4. validate input data and queried data
                for key in inputData:
                    # check missing key
                    self.assertTrue(key in queriedData)
                    # check key-value pair match
                    self.assertTrue( inputData[key] == queriedData[key] )

    def testForFailReport(self):
         # 1. initialize param. change to others for later use
        url = "http://localhost:80/scenarios"
        
        for fileName in glob(pattern):
            with open(fileName) as fp:
                inputData = json.load(fp) 
                # POST request
                postResponse = requests.post(url, data = json.dumps(inputData), headers = header)
                # this should be false. intent to fail the test
                self.assertTrue( postResponse.status_code == 200 )


if __name__ == '__main__':
    unittest.main()
