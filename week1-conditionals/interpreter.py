expression = input("Enter Expression :")
x, y, z = expression.split()
x = float(x)
z = float(z)
if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "*":
    print(f"{x * z:.1f}")
else:
    print(f"{x / z:.1f}")

