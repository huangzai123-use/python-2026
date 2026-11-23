student={"name":"张三","age":20,"score":85}
print(student["name"])
print(student["score"])

student["score"]=92
student["city"]="北京"
print(student)

for k in student:
    print(k,student[k])