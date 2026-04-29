list=[]
while True :
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")
	choice=int(input("Enter choice: "))
	if choice==1 :
		n=int(input("Integer: "))
		list.append(n)
		print("List after adding:",list)
	elif choice==2:
		if not list :
			print("List is empty")
		else :
			m=int(input("Integer: "))
			if m in list :
				list.remove(m)
				print("List after removing:",list)
			else :
				print("Element not found")
	elif choice==3:
		if not list :
			print("List is empty")
		else:
			print(list)
	elif choice==4:
		break
	else :
		print("Invalid choice")





			
