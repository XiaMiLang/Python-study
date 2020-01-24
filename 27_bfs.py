graph = {
    "A": ["B", "C", "D", "E"],
    "B": ["A", "C", "F", "I"],
    "C": ["A", "B", "D", "F"],
    "D": ["A", "C", "E", "G"],
    "E": ["A", "D", "G", "J"],
    "F": ["B", "C", "H", "I"],
    "G": ["D", "E", "H", "J"],
    "H": ["F", "G", "I", "J"],
    "I": ["B", "F", "H", "J"],
    "J": ["E", "G", "H", "I"],
}

start = str(input("請輸入從哪個節點開始: ")).upper()
parent = {start: None}


def BFS(graph, s):
    queue = []
    line = []
    queue.append(s)
    line.append(s)
    seen = set()
    seen.add(s)

    while (len(queue)) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                line.append(w)
                seen.add(w)
                parent[w] = vertex
    print("從", start, "開始的 BFS 節點順序為: ", line)


BFS(graph, start)

print("請稍後", end="")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for a in x:
    for b in x:
        if b == a:
            continue
        for c in x:
            if c == a or c == b:
                continue
            for d in x:
                if d == a or d == b or d == c:
                    continue
                for e in x:
                    if e == a or e == b or e == c or e == d:
                        continue
                    for f in x:
                        if f == a or f == b or f == c or f == d or f == e:
                            continue
                        for g in x:
                            if g == a or g == b or g == c or g == d or g == e or g == f:
                                continue
                            for h in x:
                                if h == a or h == b or h == c or h == d or h == e or h == f or h == g:
                                    continue
                                for i in x:
                                    if i == a or i == b or i == c or i == d or i == e or i == f or i == g or i == h:
                                        continue
                                    for j in x:
                                        if j == a or j == b or j == c or j == d or j == e or j == f or j == g or j == h or j == i:
                                            continue
                                        if (a + c + d == 19) and (a + d + e == 18) and (b + c + f == 11) and (
                                                d + e + g == 16) and (f + h + i == 17) and (g + h + j == 22):
                                            print("節點A:" + str(a), " B:" + str(b), " C:" + str(c), " D:" + str(d),
                                                  " E:" + str(e), " F:" + str(f), " G:" + str(g), " H:" + str(h),
                                                  " I:" + str(i), " J:" + str(j))

    print(".", a)

dest = input('請輸入終點路線: ').upper()
target = dest
print('從', start, '到', target, '的最短路徑為: ', end = "")

way = []
while dest is not None:
    way.append(dest)
    dest = parent[dest]
for x in way:
    print(way.pop(), "-> ", end="")
print(target)

# for key in parent:
#     print(key, parent[key])
