import http.client
import json

headers = {'User-Agent': 'http-client'}

descontar = 0
while True:
    conection = http.client.HTTPSConnection("api.fda.gov")
    conection.request("GET",
                      "/drug/label.json?limit=100&skip=" + str(descontar) + "&search=substance_name:%22ASPIRIN%22",
                      None, headers)

    r1 = conection.getresponse()
    print(r1.status, r1.reason)
    label_raw = r1.read().decode("utf-8")
    conection.close()

    fichero = open('label.json', 'w')
    fichero.write(label_raw)
    fichero.close()

    label = json.loads(label_raw)
    for i in range(len(label['results'])):
        medicamento_info = label['results'][i]
        print('ID: ', medicamento_info['id'])
        if (medicamento_info['openfda']):
            print('Fabricante: ', medicamento_info['openfda']['manufacturer_name'][0])
    if (len(label["results"]) < 100):
        print("No hay más medicamentos")
        break
    descontar = descontar + 100