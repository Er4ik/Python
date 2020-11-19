def google_search():
    n = int(input())
    l = []
    for i in range(n):
        s = input()
        l.append(s)
    k = int(input())
    query = []
    for j in range(k):
        q = input()
        query.append(q)
    for a in range(n):
        count = 0
        for b in range(k):
            if query[b].lower() in l[a].lower():
                count += 1
                if count == k:
                    print(l[a])
google_search()
