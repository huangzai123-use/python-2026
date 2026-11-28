lines =0
chars=0
with open ("test.txt","r",encoding="utf-8") as f:
      for line in f:
            lines +=1
            chars +=len(line.strip())

with open("report.txt","w",encoding="utf-8") as f:
     f.write(f"行数:{lines}\n")
     f.write(f"字数:{chars}\n")

with open("report.txt","r",encoding="utf-8") as f:
     print(f.read())