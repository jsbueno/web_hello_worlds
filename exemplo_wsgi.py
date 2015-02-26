from wsgiref import simple_server

def app(env, resp):
    #import pdb; pdb.set_trace()
    resp("200 OK", [("Content-type", "text/html; charset=utf-8")])
    return ["<h1>Alô mundo!</h1>".encode("utf-8")]


server=simple_server.make_server("", 8000, app)
server.serve_forever()