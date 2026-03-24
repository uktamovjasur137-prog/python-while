bal = 0

while True:
    belgi = input(":")

    if belgi == "+":
        bal += 10

    elif belgi == "stop":
        print(f"Umumiy bal: {bal}")
        break
    else:
        print("Faqat + va stop yozing")

