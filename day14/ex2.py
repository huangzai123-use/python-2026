try:
    with open("不存在.txt","r",encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("文件不存在")