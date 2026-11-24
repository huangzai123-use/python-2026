cnt={}
for ch in"hello":
    cnt[ch]=cnt.get(ch,0)+1
    print("这轮:",ch,"字典变成:",cnt)
print("最后:",cnt)