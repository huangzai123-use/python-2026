with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")

with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(repr(content))
print(len(content))