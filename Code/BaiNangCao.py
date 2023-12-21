# Python3 implementation of the above approach
import random

# Function to print the required numbers
def find():
    res = []
    ab = []
    for n in range (1, 99):
        # Suppose b = n and we want a % b = 0
        # and also (a / b) < n so a = b * (n - 1)
        b = n
        a = b * (n - 1)
        # Special case if n = 1
        # we get a = 0 so (a * b) < n
        if a * b > n and a // b < n:
            ab.insert(0, a)
            ab.insert(1, b)
            res.append(ab)
    print (res)

# Driver Code
if __name__ == "__main__":
    find()