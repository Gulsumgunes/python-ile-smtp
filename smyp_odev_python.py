import base64
import socket
import ssl

# SMTP sunucusuna bağlanma
smtp_server = "smtp.gmail.com"
smtp_port = 587
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((smtp_server, smtp_port))
response = sock.recv(1024).decode()
print(response)

subject = "System Prog. Third Week"
message = "Merhaba.Bu bir test mailidir."

# EHLO gönderme
sock.send(b"EHLO localhost\r\n")
response = sock.recv(1024)
print(response.decode())

# STARTTLS komutunu gönderme
sock.send(b"STARTTLS\r\n")
response = sock.recv(1024).decode()
print(response)

# TLS bağlantısı kurma
sock = ssl.wrap_socket(sock)

# AUTH LOGIN ile kimlik doğrulama
sock.write(b"AUTH LOGIN\r\n")
response = sock.read(1024)
print(response.decode())


username_base64 = base64.b64encode(b'ummugulsumgunes27@gmail.com').decode() + "\r\n"
sock.write(username_base64.encode())
response = sock.read(1024)
print(response.decode())


password_base64 = base64.b64encode(b'bcag xgrp yecf mhsb').decode() + "\r\n"
sock.write(password_base64.encode())
response = sock.read(1024)
print(response.decode())


sock.write(b"MAIL FROM: <ummugulsumgunes27@gmail.com>\r\n")
response = sock.read(1024)
print(response.decode())


sock.write(b"RCPT TO: <ummugulsumgunes21@gmail.com>\r\n")
response = sock.read(1024)
print(response.decode())


sock.write(b"DATA\r\n")
response = sock.read(1024)
print(response.decode())

sock.write(bytes(f"Subject: {subject}\r\n", 'utf-8'))
sock.write(bytes("\r\n", 'utf-8'))
sock.write(bytes(message + "\r\n", 'utf-8'))
sock.write(bytes(".\r\n", 'utf-8'))

response = sock.read(1024).decode()
print(response)

# QUIT komutu ile SMTP sunucusuyla bağlantıyı kapatma
sock.write(b"QUIT\r\n")
response = sock.read(1024).decode()
print(response)

# Socket bağlantısını kapat
sock.close()
