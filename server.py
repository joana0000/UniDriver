import socket

HOST = '0.0.0.0'  # aceita conexão de qualquer IP
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Servidor iniciado...")
print("Aguardando conexão...")

conn, addr = server.accept()
print(f"Conectado com {addr}")

while True:
    data = conn.recv(1024)

    if not data:
        break

    mensagem = data.decode()
    print(f"[CLIENTE]: {mensagem}")

    resposta = f"[SERVIDOR]: Mensagem recebida com sucesso -> {mensagem}"
    conn.send(resposta.encode())

conn.close()
server.close()
