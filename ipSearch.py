import socket 

hostname = socket.gethostname()
IpAddr = socket.gethostbyname(hostname)
print(hostname)
print(IpAddr)
