import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Find indices where value matche
sac=np.where(array1 == search_value)[0]
print(sac)
# Count occurrences in array1
count=np.count_nonzero(array1 == count_value)
print(count)
# Broadcasting addition
Barray=array1 + broadcast_value
print(Barray)
# Sort the first array
sort=np.sort(array1)
print(sort)
