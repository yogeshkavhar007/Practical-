def perc(marks,n):
	if any(mark<40 for mark in marks):
		print("Fail")
	else:
		total_marks=sum(marks)
		per=(total_marks/n)
		print(f"Aggregate Percentage:{ per: .2f}")
		grade(per)
def grade(per):

	if (per >75):
		print("Grade: Distinction")
	elif(75>per>60):
		print("Grade: First Division")
	elif(60>per>50):
		print("Grade: Second Division")
	else :
		print("Grade: Third Division")
n=int(input())
marks=list(map(int,input().split()))
perc(marks,n)

    
