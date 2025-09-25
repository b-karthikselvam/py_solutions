import os
number_of_students = int(input("How Many Students You Want To Enter "))
for x in range(number_of_students):
    name = input("Enter the name ")
    with open("students.txt","a") as s:
        s.write(name + "\n")
 

with open("students.txt","r") as s:
    names = s.read()
    print(f"""updated lists
{names+"\n"}""")
# number_of_students = int(input("How Many Students You Want To Enter "))
# i=1
# while(i<=number_of_students):
#     name = input("Enter the name ")
#     with open("students.txt","a") as s:
#         s.write(name + "\n")
#     i = i+1
 

# with open("students.txt","r") as s:
#     names = s.read()
#     print(f"""updated lists
# {names+"\n"}""")
