nums=[]
for i in range(3):
    x=float(input("输入一个数:"))
    nums.append(x)

total=0
for n in nums:
    total+=n

print(nums)
print(f"和:{total:.1f}")
print(f"平均:{total/len(nums):.1f}")
