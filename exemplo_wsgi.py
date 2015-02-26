from wsgiref import simple_server

def app(env, resp):
    resp("200 OK", [("Content-type", "text/html")])
    return ['<h1>Alô mundo!</h1>']


server=simple_server.make_server("", 8000, app)
server.serve_forever()