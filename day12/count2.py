line = input("输入一句英文：")
cnt = {}
for w in line.split():
    cnt[w] = cnt.get(w, 0) + 1
print(cnt)
print(max(cnt, key=cnt.get))