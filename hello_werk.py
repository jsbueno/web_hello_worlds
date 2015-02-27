from werkzeug.wrappers import Request, Response

def application(environ, start_response):
    request = Request(environ)
    text = "<h1>Alô  {}!</h1>".format(request.args.get("name", "Mundo"))
    response = Response(text, mimetype="text/html; charset=utf-8")
    return response(environ, start_response)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 8000, application)
