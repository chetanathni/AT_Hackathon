import serial
import requests
import sys
import json
firebase_url = 'https://accident-care-system-dd96d.firebaseio.com/'
ser = serial.Serial('COM6', 9600, timeout=0)



while 1:
  try:     
    count = str(ser.readline())
    print(count)
    data = {'count':count}
    result = requests.post(firebase_url + '/' + '/count.json', data=json.dumps(data).encode() )
    print ('Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text)
   
  except IOError:
    print('Error! Something went wrong.')
