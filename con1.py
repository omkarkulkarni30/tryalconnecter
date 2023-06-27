G_key = None
while G_key is None:
    try:
        G_key = int(input("Enter the value for G_key: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")

print('G_key =', G_key)
