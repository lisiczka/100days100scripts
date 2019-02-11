# Fibonacci sequence script I was asked to write during the job interview but I couldn't think of it that particular moment.
# Learn the hard stuff as well as the basics so you'll not be ashamed by such trivial task anytime.
# The general equation is f(n) = f(n-1) + f(n-2)

# table initialization with first two elements
tab = [0, 1]

n = 1
while n <= 10:
	i = tab[n] + tab[n-1]
	tab.append(i)
	n = n + 1
print(tab)
