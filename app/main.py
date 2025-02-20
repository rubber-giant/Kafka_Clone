import socket

def main():
    
    try:
        server = socket.create_server(("localhost", 9092), reuse_port=True)
        conn, addr = server.accept()    # wait for client
        print("connected")
        
    except Exception as e:
        print("An error occured:", e)

if __name__ == "__main__":
    main()