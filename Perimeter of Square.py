# Python Program - Calculate Perimeter of Square

print("Enter 'x' for exit.");
side = input("Enter side length of square: ");
if side == 'x':
    exit();
else:
    slength = int(side);
    perimeter = 4*slength;
    print("\nPerimeter of Square =", perimeter);
