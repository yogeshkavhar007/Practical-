# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

# write your code here...
print("Original Dictionary:",student)

n_key=int(input())
name=str(input())
student[n_key]=name
print("After Insertion:",student )

m_key=int(input())
name_1=str(input())
student[m_key]=name_1
print("After Update:",student )

n_key1=int(input())
if n_key1 in student :
	del student[n_key1]
print("After Deletion:",student )

print("Traversing Dictionary:")
for i ,value in student.items() :
	print(f"{i} : {value}")
