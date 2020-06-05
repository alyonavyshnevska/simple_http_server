from http.server import HTTPServer, BaseHTTPRequestHandler

# holds our server
class Serv(BaseHTTPRequestHandler):
    # extending existing method for handling get requests
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'

        try: 
            # skip forward slash
            f = open(self.path[1:]).read()
            self.send_response(200)

        except:
            f = "File not found"
            self.send_response(404)
        self.end_headers()
        # write file to screen
        self.wfile.write(bytes(f, 'utf-8'))

# http deamon runs in the background
httpd = HTTPServer(('localhost', 8000), Serv)
httpd.serve_forever()



