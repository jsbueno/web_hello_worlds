import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8003))
sock.listen(0)
con, address = sock.accept()

print (con, address)
data = con.recv(10000)

print(data.decode("utf-8"))


con.send("""HTTP/1.1 200 Ok
Content-Type: text/html; charset=utf-8

<h1>Alô mundo</h1>
""".encode("utf-8"))


con.send("""<p>Estamos aqui escrevendo</p>""".encode("utf-8"))


con.send("""<p>uma página em tempo <span style="color:red">real</span></p>""".encode("utf-8"))

con.close()
