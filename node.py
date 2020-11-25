import socket
import request

class Node:
    def __init__(self, node_id, ip, port):
        self.node_id = node_id
        self.ip = ip
        self.port = port
        self.prev = node_id
        self.next = node_id

    def hello(self, ip_dest, port_dest):
        s = request.connection(ip_dest, port_dest)
        message = {
            "cmd" : "hello",
            "args" : {
                "IP" : ip_dest,
                "port" : port_dest,
                "idNode" : self.node_id
            }
        }
        request.send_message(s, message)
        s.close()

    def hello_ok(self, id_requested, ip_resp, port_resp,
                    node_id, ):
        pass

    def hello_ko(self):
        pass

    def get(self, ip_source, key_data):
        pass

    def answer(self):
        pass

    def put(self):
        pass

    def ack(self):
        pass
