s=input("请输入一句话:")
cnt={}
for ch in s:
    cnt[ch]=cnt.get(ch,0)+1
print(cnt)
