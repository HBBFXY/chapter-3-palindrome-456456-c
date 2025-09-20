num = input().strip()

if not num.isdigit() or len(num) != 5:
    print("错误提示")
elif num == num[::-1]:
    print("是回文数")
else:
    print("不是回文数")

