import requests, json, unittest, os.path, logging, sys
from glob import glob

# test data directory
boldPattern = os.path.join('test/bold/validData', '*.json')
T1wPattern  = os.path.join('test/T1w/validData', '*.json')

# missing field data directory
boldMissingPattern = os.path.join('test/bold/missingField', '*.json')
T1wMissingPattern  = os.path.join('test/T1w/missingField', '*.json')


# url for GET
def getURL(postResponse, url):
    dirID = postResponse.json()["_id"]
    resURL = url + "/" + dirID
    return resURL  

def getRequest(postResponse, url):
    # GET
    getResponse = requests.get(getURL(postResponse, url))
    return getResponse.json()

###### MAIN ######
header = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
authenticated_header = header.copy()
header['Authorization'] = '<secret_token>'
numOfTestData = 84
urlBold = "http://localhost:80/bold"
urlT1w  = "http://localhost:80/T1w"
codeForInvalid = 422

class TestCase(unittest.TestCase):
    def test_00_GETAllData(self):
        log= logging.getLogger( "SomeTest.testSomething" )

        inputCount = 0
        for fileName in glob(T1wPattern):
            with open(fileName) as fp:
                inputCount += 1
                inputData = json.load(fp) 
                # POST request
                postResponse = requests.post(urlT1w, data = json.dumps(inputData), headers = authenticated_header)
                self.assertTrue( postResponse.raise_for_status() == None )

        # GET request
        # print requests.get(urlT1w)
        getResponse = requests.get(urlT1w).json()
        log.debug( "total: %r", getResponse['_meta']['total'] )
        self.assertTrue( inputCount == getResponse['_meta']['total'] )

    ########## Testing Bold ############
    def test_01_ConnectionStatus(self):
        log= logging.getLogger( "SomeTest.testSomething" )
   
        for fileName in glob(boldPattern):
            with open(fileName) as fp:
                inputData = json.load(fp) 
                # print inputData
                # POST request
                postResponse = requests.post(urlBold, data = json.dumps(inputData), headers = authenticated_header)
                self.assertTrue( postResponse.raise_for_status() == None )
                # GET request
                getResponse = requests.get( getURL(postResponse, urlBold) )
                self.assertTrue( getResponse.raise_for_status() == None )

    def test_02_MissingFieldInput(self):
        log= logging.getLogger( "SomeTest.testSomething" )
   
        for fileName in glob(boldMissingPattern):
            with open(fileName) as fp:
                inputData = json.load(fp) 
                # POST request
                postResponse = requests.post(urlBold, data = json.dumps(inputData), headers = authenticated_header)
                # print postResponse.status_code
                self.assertTrue( postResponse.status_code == codeForInvalid )

    ########## Testing T1w ############
    def test_03_ConnectionStatus(self):
        log= logging.getLogger( "SomeTest.testSomething" )
   
        for fileName in glob(T1wPattern):
            with open(fileName) as fp:
                inputData = json.load(fp) 
                # print inputData
                # POST request
                postResponse = requests.post(urlT1w, data = json.dumps(inputData), headers = authenticated_header)
                self.assertTrue( postResponse.raise_for_status() == None )
                # GET request
                getResponse = requests.get( getURL(postResponse, urlT1w) )
                self.assertTrue( getResponse.raise_for_status() == None )

    def test_04_MissingFieldInput(self):
        log= logging.getLogger( "SomeTest.testSomething" )
   
        for fileName in glob(T1wMissingPattern):
            with open(fileName) as fp:
                inputData = json.load(fp) 
                # POST request
                postResponse = requests.post(urlT1w, data = json.dumps(inputData), headers = authenticated_header)
                # print postResponse.status_code
                self.assertTrue( postResponse.status_code == codeForInvalid )

    ########## Cross Testing: send data to wrong end point ############
    def test_05_boldDataToT1wEndPoint(self):
        log= logging.getLogger( "SomeTest.testSomething" )
   
        for fileName in glob(boldPattern):
            with open(fileName) as fp:
                inputData = json.load(fp) 
                # POST request
                postResponse = requests.post(urlT1w, data = json.dumps(inputData), headers = authenticated_header)
                self.assertTrue( postResponse.status_code == codeForInvalid )

    def test_06_T1wDataToBoldEndPoint(self):
        log= logging.getLogger( "SomeTest.testSomething" )
   
        for fileName in glob(T1wPattern):
            with open(fileName) as fp:
                inputData = json.load(fp) 
                # POST request
                postResponse = requests.post(urlBold, data = json.dumps(inputData), headers = authenticated_header)
                self.assertTrue( postResponse.status_code == codeForInvalid )

    def test_07_T1wDataValid(self):

        for fileName in glob(T1wPattern):
            with open(fileName) as fp:
                inputData = json.load(fp) 
                # 2. POST request
                postResponse = requests.post(urlT1w, data = json.dumps(inputData), headers = authenticated_header)

                # 3. GET request
                queriedData = getRequest(postResponse, urlT1w)
                # 4. validate input data and queried data
                for key in inputData:
                    # check missing key
                    self.assertTrue(key in queriedData)
                    # check key-value pair match
                    self.assertTrue( inputData[key] == queriedData[key] )


    def test_08_boldDataValid(self):

        for fileName in glob(boldPattern):
            with open(fileName) as fp:
                inputData = json.load(fp) 
                # 2. POST request
                postResponse = requests.post(urlBold, data = json.dumps(inputData), headers = authenticated_header)
                self.assertTrue( postResponse.raise_for_status() == None )

                # 3. GET request
                queriedData = getRequest(postResponse, urlBold)
                # 4. validate input data and queried data
                for key in inputData:
                    # check missing key
                    self.assertTrue(key in queriedData)
                    # check key-value pair match
                    self.assertTrue( inputData[key] == queriedData[key] )
					
    def test_09_failedAuth(self):
        with open(glob(boldPattern)[0]) as fp:
            inputData = json.load(fp) 
            postResponse = requests.post(urlBold, data = json.dumps(inputData), headers = header)
            self.assertTrue( postResponse.status_code == 401 )


# ****************


if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "SomeTest.testSomething" ).setLevel( logging.DEBUG )

    unittest.main()
