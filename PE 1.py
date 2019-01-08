print("Muhammad Usman Pervaiz - 18B-006-CS - SEC-A")
print("LAB NO: 04")

import cmath
a = int(input("\n\nEnter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
if (a==0):
    print("\n\nThe equation cannot be solved as there is a zero in denominator")
else:
    x1 = (-b+(cmath.sqrt(b**2)-(4*a*c)))/(2*a)
    x2 = (-b-(cmath.sqrt(b**2)-(4*a*c)))/(2*a)
    print("\nThe value of x is ",x1,x2)
