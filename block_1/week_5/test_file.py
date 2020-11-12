metric = {}


def put(query):
    global metric
    if len(query) != 3:
        return "error\nwrong command\n\n"
    try:
        float(query[1])
        int(query[2])
    except ValueError:
        return "error\nwrong command\n\n"

    if query[0] not in metric:
        metric[query[0]] = []
        metric[query[0]].append((query[1], query[2]))
        print("Helloo")
    elif query[0] in metric:
        for i in metric[query[0]]:
            if query[1] == i[0] and query[2] == i[1]:
                return "ok\n\n"
        counter = 0
        flag = True
        for i in metric[query[0]]:
            if i[1] == query[2]:
                metric[query[0]][counter] = (query[1], query[2])
                flag = False
            counter += 1
        if flag:
            metric[query[0]].append((query[1], query[2]))


put(['1', 2.3, 4])
put(['1', 2.2, 3])
put(['1', 2.4, 3])

print(metric)