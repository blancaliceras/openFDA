import http.client
import json

headers = {'User-Agent': 'http-client'}

conection = http.client.HTTPSConnection("api.fda.gov")
conection.request("GET", "/drug/label.json", None, headers)
r1 = conection.getresponse()
print(r1.status, r1.reason)
label_raw = r1.read().decode("utf-8")
conection.close()


label = json.loads(label_raw)
medicamento_info=label['results'][0]

print ('ID: ',medicamento_info['id'])
print ('Proposito: ',medicamento_info['purpose'][0])

print ('Fabricante: ',medicamento_info['openfda']['manufacturer_name'][0])