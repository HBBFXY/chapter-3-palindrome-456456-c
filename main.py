# palindrome.py

num = input().strip()

if not num.isdigit() or len(num) != 5:
    print("错误")
else:
    if num == num[::-1]:
        print("是回文数")
    else:
        print("不是回文数")

