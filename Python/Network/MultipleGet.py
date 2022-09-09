import requests
import time

testPi="172.17.4.58" # Raspberry Pi IP
loop = 30

for x in range(loop):
    request = requests.get("http://" + testPi + "/api/devices/discover") # Call discover API

    if request.status_code != 200:
        print("Requst error")
    else:
        jsonText = request.json()
        testBoxPresent = jsonText['Testbox']['isPresent']
        uArtPresent = jsonText['Uart']['isPresent']
        
        print(f"Test {x} TestBox present: {jsonText['Testbox']['status']} {jsonText['Testbox']['isPresent']} Uart present: {jsonText['Uart']['status']} {jsonText['Uart']['isPresent']}")
        if not testBoxPresent:
            print("TestBox error")
        if not uArtPresent:
            print("Uart error")    

    #time.sleep(1) # sleep for one second
