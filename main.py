# main.py

num = input().strip()

# 非纯数字或不是5位数
if not num.isdigit() or len(num) != 5:
    print("输入错误: 请输入5位数字")
elif num == num[::-1]:
    print("是回文数")
else:
    print("不是回文数")
