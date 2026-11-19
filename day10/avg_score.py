scores = [78,92,85,60,99]


scores.sort()
print("排序后:",scores)


scores.pop(0)
scores.pop()
print("去掉最高最低:",scores)

print(f"平均分:{sum(scores)/len(scores):.1f}")