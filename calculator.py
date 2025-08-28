# A CLI-based calculator

print("Welcome to our Calculator :)")

num_one = int(input("Enter first number: "))
num_two = int(input("Enter second number: "))

print("Please select the operator:")
print(""" 
1. + 
2. - 
3. / 
4. x
""")

op = input("Enter choice (1/2/3/4): ")

def main():
    if op == "1":
        result = num_one + num_two
        print(f"{num_one} + {num_two} = {result}")
    elif op == "2":
        result = num_one - num_two
        print(f"{num_one} - {num_two} = {result}")
    elif op == "3":
        result = num_one / num_two
        
    elif op == "4":
        result = num_one * num_two
        print(f"{num_one} x {num_two} = {result}")
    else:
        print("Invalid operator choice!")

main()
