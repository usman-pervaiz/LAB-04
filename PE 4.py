print("Muhammad Usman Pervaiz - 18B-006-CS - SEC-A")
print("LAB NO: 04")

print("\n\n\t\t\tMarkSheet\n")

name = input("Please Enter Your Name         :")
fname= input("Please Enter Your Father's Name:")
rno  = input("Please Enter Your Roll Number  :")
subject_name=[]
subject_marks=[]
tot_marks=0
for x in range(1,6):
    a=input("\nPlease Enter the Name of Subject"+str(x)+" :")
    b=int(input("Please Enter the Marks of Subject"+str(x)+":"))
    subject_name.append(a)
    subject_marks.append(b)

for y in range(5):
    tot_marks += subject_marks[y]

percentage = (tot_marks/500)*100
if (percentage>=50) and (percentage<60):
    grade = 'D'
elif (percentage>=60) and (percentage<70):
    grade = 'C'
elif (percentage>=70) and (percentage<80):
    grade = 'B'
elif (percentage>=80) and (percentage<90):
    grade = 'A'
elif (percentage>=90) and (percentage<100):
    grade = 'A+'
else:
    grade =  'Fail'

print("\n\nName         :",name)
print("Father's Name:",fname)
print("Roll Number  :",rno)

a = [[0 for col in range(5)] for row in range(2)]

for row in range(2):
    for col in range(5):
        if row==0:
            hmm=subject_name[col]
            a[row][col] = hmm
        if row==1:
            hmm=subject_marks[col]
            a[row][col] = hmm

dash = '_'*30
for row in range(2):
    print("\n")
    for col in range(5):
        if row==0:
            print('{:^10s}'.format(a[row][col]),end="")
        if row==1:
            print('{:^10d}'.format(a[row][col]),end="")
            
            
print("\n",'{:>10s}'.format("\nTotal Marks :"),str(tot_marks))
print('{:>10s}'.format("Percentage  :"),str(percentage))
print('{:>10s}'.format("Grade       :"),str(grade))
