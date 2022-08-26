cushos = input("custom host? y/n")
if (cushos == y):
    host = input("enter custom host:")
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
else:
    serversocket.bind((socket.gethostname(), 80))
    
serversocket.listen(5)