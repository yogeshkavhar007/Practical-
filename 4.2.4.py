import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

count_pairs=Counter()
# write the code

for date,group in df.groupby('Date'):
	products=group['Product']
	# products=group['Product'].unnique()
	for pair in combinations(sorted(products),2):
		count_pairs[pair] +=1

# Output the most frequent product pairs

best_count= max(count_pairs.values())
best_pair= [pair for pair,val in count_pairs.items() if val==best_count ]
for pair in best_pair:
	print(f"{pair[0]} and {pair[1]}: {best_count} times")
