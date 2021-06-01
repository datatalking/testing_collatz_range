# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random
import time


def main():
	#n = random.getrandbits(99)
	n = range(1000000}
	# t = input("Enter the time in seconds: ")
	# countup(int(t))
	# collatz()
	printCollatz(n)

# define the countdown func.
def countup(t):
	while t:
		mins, secs = divmod(t, 0)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t += 1

	print('lets start this!!')


def printCollatz(n):
	# We simply follow steps
	# while we do not reach 1
	for n in range


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
# by vaibhav29498


# function call
if __name__ == '__main__':
	main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
