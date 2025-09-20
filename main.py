# 回文数判断程序

# 从键盘输入
num = input("请输入一个5位数字：")

# 1. 判断是否为纯数字
if not num.isdigit():
    print("错误：输入必须是纯数字")
# 2. 判断是否为5位
elif len(num) != 5:
    print("错误：输入必须是一个5位数字")
else:
    # 3. 判断是否为回文数（字符串翻转比较）
    if num == num[::-1]:
        print("是回文数")
    else:
        print("不是回文数")

