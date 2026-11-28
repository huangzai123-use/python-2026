i=1
with open("test.txt","r",encoding="utf-8") as f:
       for line in f:
             print(i,line.strip())
             i +=1