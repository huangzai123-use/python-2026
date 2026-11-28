try:
     n=int(input("请输入一个整数:"))
     print(10/n)
except ValueError:
      print("你输入的不是整数")
except ZerovisionError:
     print("不能除以0")