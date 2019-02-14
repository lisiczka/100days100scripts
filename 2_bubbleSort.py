# Bubble sort. Probably the easiest one, still a challenge.
# The algorithm is based on comparing the two neighboring values and swapping them if they're in the wrong order
# More at https://www.geeksforgeeks.org/bubble-sort/


data = [5, 2, 8, 1, 9, 22, 3]
print('Unsorted:', data)
n = len(data)
iterations = 0

for i in range(n):
	for j in range(0, n-1):
		if data[j] > data[j+1]:
			data[j], data[j+1] = data[j+1], data[j]		# Swapping the elements
			iterations = iterations + 1
	else:
		j = j + 1

print('Sorted:', data)
print('iterations:', iterations)
