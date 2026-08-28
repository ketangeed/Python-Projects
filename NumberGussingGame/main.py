import random

num = random.randint(1, 10)
count = 0

while num > 0:
    number = int(input("Enter the Number : "))
    if number == num :
        count += 1
        print(f"Congrats you got it right in {count} Times...")
        break
    elif number > num :
        print("Too High...")
    elif number < num :
        print("Too Low...")
    else:
        pass