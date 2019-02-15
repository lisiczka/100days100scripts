# "In order to understand recursion you first need to understand recursion."
# A script dealing with the "Collatz" sequence.
# If the given umber is even, return (number // 2), if it's odd, return (3 * number + 1). 
# Keep the value of the 'number' for the recursion.
# I've never used recursion before so writing and understanding 
# this piece of code took me a while.


def collatz(number):
	if number % 2 == 0:
		result = number // 2
		print(result)
		return result

	elif number % 2 == 1:
		result = 3 * number + 1
		print(result)
		return result


n = input("Give me the number:")

while n != 1:
	n = collatz(int(n))
