w=input("请输入一个词")
r=w[::-1]
print(f"反转: {r}")
if w==r:
	print("回文")
else:
	print("不是回文")