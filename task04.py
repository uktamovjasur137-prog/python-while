while True:
    a = int(input("son: "))
    b = int(input("son: "))
    amal = input("amal (+, -, *, /): ")

    if amal == "+":
        print(a + b)

    elif amal == "-":
        print(a - b)

    elif amal == "*":
        print(a * b)

    elif amal == "/":
        if b != 0:
            print(a / b)
        else:
            print("0 ga bolish mumkin emas")

    else:
        print("Notogri amal!")

    javob = input("Davom etasizmi? (ha/yoq): ")

    if javob == "yoq":
        print("Dastur tugadi")
        break