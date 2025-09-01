import random

rolls = int(input("How many times you want to roll the dice: "))

results = []

for _ in range(rolls):
    roll = random.randint(1, 6)
    results.append(roll)

print("\nResults:")
for side in range(1, 7):
    count = results.count(side)
    percentage = (count / rolls) * 100
    print(f"{side}: {count} times ({percentage:.2f}%)")  # fixed indentation
