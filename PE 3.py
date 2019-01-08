print("Muhammad Usman Pervaiz - 18B-006-CS - SEC-A")
print("LAB NO: 04")

# a program to check whether the entered string is palindrome or not
ask_user = input("\n\nEnter the word:")
ask_user1 = ask_user.casefold()
if ask_user1 == ask_user1[::-1]:
    print("\nIt is a Palindrome string")
else:
    print("\nIt is not a Palindrome string")
