print("=== AJAY's CALCULATOR - Day 4 ===")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
print("1-Add, 2-Sub, 3-Mul, 4-Div")
choice = input("Choice: ")
if choice == '1':
    print(num1+num2)
elif choice == '2':
    print(num1-num2)
elif choice == '3':
    print(num1*num2)
elif choice == '4':
    print(num1/num2)
