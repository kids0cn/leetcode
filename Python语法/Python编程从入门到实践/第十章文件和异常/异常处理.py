print("give me to numbers,and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    firstNum = input("\nFirst number:")
    if firstNum == 'q':
        break
    secondNum = input("\nSecond number:")
    # 在程序中尝试try，处理完异常，程序继续
    try:
        answer = int(firstNum)/int(secondNum)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)