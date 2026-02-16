num_table = int(input("Enter a number for the table: "))
num_iteration = int(input("Enter a number for the table iteration: "))

for i in range(1, num_iteration + 1):
    print(f"{num_table} * {i} = {num_table * i}")


