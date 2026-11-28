try:
    with open("test.txt", "r", encoding="utf-8") as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print("test.txt 不存在，请检查路径")