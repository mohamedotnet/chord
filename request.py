import socket
import sys
import json



def connection(ip_address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((ip_address, port))
    except socket.error:
        try:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((ip_address, port))
        except socket.error:
            s.close()
            print("Connection Failed.")
            return
    return s

def send_message(sock, message):
    payload = json.dumps(message)
    sock.send(payload)

def get(sock, ip_address, port, key):
    msg = {
        "cmd" : "get",
        "args" : {
            "host": {
                "IP" : ip_address,
                "port" : port,
                "idNode" : -1
            },
            "key" : key
        }
    }
    send_message(sock, msg)
    sock.close()

def put(sock, ip_address, port, key, value):
    msg = {
        "cmd" : "put",
        "args" : {
            "host": {
                "IP" : ip_address,
                "port" : port,
                "idNode" : -1
            },
            "key" : key,
            "value" : value
        }
    }
    send_message(sock, msg)
    sock.close()

if __name__ == '__main__':
    pass