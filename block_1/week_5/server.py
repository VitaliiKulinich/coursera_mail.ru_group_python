import asyncio

database = {}


class Client_Server_Protocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport: asyncio.Transport):
        self.transport = transport

    def data_received(self, data: bytes):
        req = data.decode()[:-1].split(' ')
        method = req[0]
        query = req[1:]
        if method == 'get':
            result = self.get(query)
        elif method == 'put':
            result = self.put(query)
        else:
            result = 'error\nwrong command\n\n'
        self.transport.write(result.encode())

    @staticmethod
    def get(query):
        if len(query) != 1:
            return 'error\nwrong command\n\n'
        result = []
        query = query[0]

        if '*' in query[0]:
            for key in database:
                for j in database[key]:
                    result.append(f'{key} {float(j[0])} {j[1]}')

        else:
            try:
                for i in database[query]:
                    result.append(f'{query} {float(i[0])} {i[1]}')
            except KeyError:
                return "ok\n\n"
        result_end = "\n".join(result)

        if not result:
            return f"ok{result_end}\n\n"
        else:
            return f"ok\n{result_end}\n\n"

    @staticmethod
    def put(query):
        if len(query) != 3:
            return "error\nwrong command\n\n"
        try:
            float(query[1])
            int(query[2])
        except ValueError:
            return "error\nwrong command\n\n"

        if query[0] not in database:
            database[query[0]] = []
            database[query[0]].append((query[1], query[2]))

        elif query[0] in database:
            counter, flag = 0, True
            for i in database[query[0]]:
                if query[1] == i[0] and query[2] == i[1]:
                    return "ok\n\n"

                if i[1] == query[2]:
                    database[query[0]][counter] = (query[1], query[2])
                    flag = False
                counter += 1
            if flag:
                database[query[0]].append((query[1], query[2]))

        return "ok\n\n"


def run_server(host='127.0.0.1', port=8888):
    loop = asyncio.get_event_loop()

    coro = loop.create_server(Client_Server_Protocol, host, int(port))
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_close())
    loop.close()


if __name__ == '__main__':
    run_server()
