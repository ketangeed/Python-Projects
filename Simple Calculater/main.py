try :

    a = int(input("Enter the First Number : "))

    b = int(input("Enter the Second Number : "))

    print("Enter what kind of Operation you want to perform:\nPress + for Addition\nPress - for Substraction\nPress * for Multiplication\nPress / for Division")

    o = input("Enter the Operation : ")

    
    match o:
        case "+":
            print(f"The Addition is = {a+b}")
        case "-":
            print(f"The Substraction is = {a-b}")
        case "*":
            print(f"The Multiplication is = {a*b}")
        case "/":
            print(f"The Division is = {a/b}")
        case _:
            print("...CHOSE THE GIVEN OPERATION...")

except ZeroDivisionError:
    print("Can't Divide by zero..")

except ValueError:
    print("Only Integers are allowed...")

except Exception as e:
    print("...Print Valid a and b value...")
