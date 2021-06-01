"""
EXTRA CREDIT OPTIONS
1. start from zero and count to 1m and time it while running through collatz
2. count up from 1m to 10 million timing each cycle # one function
3. count up to 100 million # one function
4. how high can you count if you leave the machine running each successive n
5. out put each numeral started, the cycle count and time elapsed plus current time to a csv

6. plot these data in matplotlib
submit for extra credit.
"""


def printCollatz(n):
	# We simply follow steps
	# while we do not reach 1
	while n != 1:
		print(n, end=' ')

		# If n is odd
		if n & 1:
			n = 3 * n + 1

		# If even
		else:
			n = n // 2

	# Print 1 at the end
	print(n)


# Driver code
printCollatz(6)

# This code is contributed

