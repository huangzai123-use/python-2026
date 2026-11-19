a = [3,1,4]
print("原始:",a)

a.append(9)
print("append后:",a)

a.insert(1,7)
print("insert后:",a)

a.remove(1)
print("remove后:",a)

x =a.pop(0)
print("pop 弹出:",x,"剩下:",a)

a.sort()
print("sort后:",a)

a.reverse()
print("reverse后:",a)
