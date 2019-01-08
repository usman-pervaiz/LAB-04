print("Muhammad Usman Pervaiz - 18B-006-CS - SEC-A")
print("LAB NO: 04")

a1 = int(input("\n\nEnter the first term:"))
d = int(input("Enter the common differrence:"))
n1 = int(input("Enter the nth term:"))
an1 = a1+(n1-1)*d
print("\n",an1)
ask_user = input("\nDo you want to continue further:")
if ask_user == "yes" or "YES":
    n2 = int(input("Enter the next term:"))
    an2 = a1+(n2-1)*d
    print("\n",an2)
else:
    pass
         
