import socket
import time


class ClientError(Exception):
    pass


class ClientSocketError(ClientError):
    pass


class ClientProtocolError(ClientError):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.__host = host
        self.__port = port
        self.__timeout = timeout
        try:
            self.sock = socket.create_connection((self.__host, self.__port))
        except socket.error as error:
            raise ClientSocketError("error connection", error)

    def read_answer(self):
        try:

            data = b""
            while not data.endswith(b'\n\n'):

                try:
                    data += self.sock.recv(1024)
                except socket.error as error:
                    raise ClientSocketError("error data", error)

            decoded_data = data.decode()
            status, clear_data = decoded_data.split("\n", 1)

            # if status != "ok":
            #     raise ClientProtocolError(clear_data.strip())

            clear_data = clear_data.strip()
            return clear_data

        except ValueError as error:
            raise ClientError("value error", error)

    def put(self, key, value, time_stamp=None):
        time_stamp = time_stamp or int(time.time())
        try:
            self.sock.sendall(f"put {key} {value} {time_stamp}\n".encode())
        except socket.error as error:
            raise ClientSocketError("error data", error)
        a = self.read_answer()
        return a

    def get(self, key):

        try:
            self.sock.sendall(f"get {key}\n".encode())
        except socket.error as error:
            raise ClientSocketError("error data", error)
        answer = self.read_answer()
        data = {}
        if answer == "":
            return data

        for row in answer.split("\n"):
            key, value, timestamp = row.split()
            if key not in data:
                data[key] = []
            data[key].append((int(timestamp), float(value)))
            data[key].sort(key=lambda a: a[0])
        return data

    def close(self):
        try:
            self.sock.close()
        except socket.error as error:
            raise ClientSocketError("error close connection", error)


client = Client('127.0.0.1', 8888, timeout=15)
print(client.get('*'))
client.close()