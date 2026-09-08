# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
XXX Write your pseudocode here XXX 0, 1, 3, 7, 13, 17, 23, 27 
#loop structure
enter N: 
i=0 
j=1 
sum=0 
count=0 
while count <= N #count will always be less than or equal to N, so the loop will run until count is equal to N. This can be dangerous if N is not set to a number greater than 0. It can keep the code running forever.
    sum = sum + i #0+0= 0 
    next= i+j #1+0=1 
    j = next #next=1
    count = count +1  #0+1=1 
end while #while loop will end when count is equal to N. This can be dangerous if N is not set to a number greater than 0. It can keep the code running forever.
print sum #in the end, the sum of the first N numbers in the fibonacci sequence will be printed. This can be dangerous if N is not set to a number greater than 0. It can keep the code running forever.

"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6

a = 0 # set a to the first fibonacci number #a=0
b = 1 # set b to the second fibonacci number #b=6
count = 0
total = 0

while count < N:
    total = total + b #0+1=1

    next_value = a + b #0+1=1
    a = b #0=1
    b = next_value #1=1

    count = count + 1 #0 =0+1

print(total) #1

#N=3 ##N is equal to 3, so the while loop will run 3 times. This can be dangerous if N is not set to a number greater than 0. It can keep the code running forever.

#a = 0  ##set a to the first fibonacci number so we can start the sequence 
#b=1 # #set b to the second fibonacci number so we can countinue with the sequence
#count =0 ##count is set to 0 to start the while loop
#total = 0 ##total is set to 0 to continue the while loop
#while count < N: ##while loop will run until count is less than N. This can be dangerous if N is not set to a number greater than 0. It can keep the code running forever.
    #total = total + b ##total is set to the sum of total and b. This is where the error is. It should be total = total + a. The first number in the fibonacci sequence is 0, not 1.
    #next_value= a+b ##next_value is set to the sum of a and b. This is the next number in the fibonacci sequence.
    #a=b a='0' ## a = 0 because b is equal to 1. This is where the error is. It should be a = next_value. The first number in the fibonacci sequence is 0, not 1.
    #b= next_value b='1', next_value= 13 ##there is no error here because b is equal to next_value. This is the next number in the fibonacci sequence.
    #count = count+1  ##the count value here helps to keep track of how many times the while loop has run. This is important because it will help to determine when to stop the while loop. 
#print(total) total = 20  ##the total value here is the sum of the first N numbers in the fibonacci sequence. 


# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.
import numpy as np  #to import the numpy library, which is a powerful library for numerical computing in Python. It provides support for arrays, matrices, and many mathematical functions. first you need to install numpy using pip install numpy in the terminal. Then you can import it in your code using the import statement.
fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] 
std_dev = np.std(fibonacci_sequence) #standard deviation of the first 10 numbers in the fibonacci sequence is calculated using the numpy library. The np.std() function calculates the standard deviation of the input array. The input array is the first 10 numbers in the fibonacci sequence, which is stored in the variable fibonacci_sequence. The result is stored in the variable std_dev.
print("The standard deviation of the first 10 numbers in the fibonacci sequence is: ", std)

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

def sum_fib(N): #new loop structure that will take an integer N as input and return the sum of the first N numbers in the fibonacci sequence. 
    """# The function inputs an integer called "N" and finds the sum of the first N numbers in the fibonacci sequence. It returns the sum.
    :param N: number of fibonacci numbers to sum
    :type N: integer
    :return: sum of the first N fibonacci numbers
    :rtype: integer
    """
    a, b = 0, 1
    total = 0
    for _ in range(N):
        total += a
        a, b = b, a + b
    return total #returns the sum of the first N numbers in the fibonacci sequence. Not prints the inside function!

# Calculate sums for different values of N #Avoid fib_sum(5), fib_sum(10), etc. because it will print the inside function and not return the sum of the first N numbers in the fibonacci sequence.
N_values = [5, 10, 15, 20, 25, 30]
sums = [sum_fib(N) for N in N_values]
print("Sums of the first N Fibonacci numbers:", sums)

# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.
#Type Error: The variable 'index' is used before it is defined. It should be initialized before the while loop.
#

def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = "0"
    b = "1"
#how a and b are defined as strings instead of integers. This will cause a TypeError when trying to add them together. They should be defined as integers.
    while a <= limit:
        next_value = a + b
        a = b
        b = next_value
        index += 1

    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_even_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 == 0:  # This line checks if the Fibonacci number is even
            total = b
        a, b = b, a + b
    return total
#compare total with limit to see if it is less than or equal to limit. If it is, add it to total. If not, do not add it to total. This will ensure that only even Fibonacci numbers less than or equal to limit are added to total.
#stated goal is to return the sum of all even Fibonacci numbers less than or equal to the input "limit". The current implementation only returns the last even Fibonacci number less than or equal to limit, not the sum of all even Fibonacci numbers. To fix this, we need to change the line "total = b" to "total += b".

# Add your test cases here
test_cases = [10, 20, 30, 40, 50]
for limit in test_cases:
    result = sum_even_fib(limit)
    print(f"The sum of even Fibonacci numbers up to {limit} is: {result}")
#is the total updated correctly? The total is updated correctly, but it is not being returned correctly. The function should return the total, not the last even Fibonacci number. To fix this, we need to change the line "return total" to "return total".
# %%
