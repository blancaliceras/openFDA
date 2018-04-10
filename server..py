import http.server
import socketserver
import http.client
import json


PORT = 4018

#127.0.0.1:4055=ip genérica para probar


def dame_lista():
    lista = []
    headers = {'User-Agent': 'http-client'}

    conection = http.client.HTTPSConnection("api.fda.gov")
    conection.request("GET", "/drug/label.json?limit=10", None, headers)

    r1 = conection.getresponse()
    print(r1.status, r1.reason)
    label_raw = r1.read().decode("utf-8")
    conection.close()

    label = json.loads(label_raw)
    for i in range(len(label['results'])):
        medicamento_info = label['results'][i]
        if (medicamento_info['openfda']):
            print('Fabricante: ', medicamento_info['openfda']['generic_name'][0])
            lista.append(medicamento_info['openfda']['generic_name'][0])

    return lista

class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):


    def do_GET(self):

        self.send_response(200)


        self.send_header('Content-type', 'text/html')
        self.end_headers()
        content="<html><body>"
        lista=dame_lista ()
        for e in lista:
            content += e+"<br>"
        content+="</body></html>"

        self.wfile.write(bytes(content, "utf8"))
        return



Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print("")
print("Servidor parado")