 Here is the formal content in Markdown format without any emojis or external links:

## 14.WAP to print sum of even and odd numbers from 1 to N numbers.

1. Take input N from the user. N refers to the limit upto which the numbers are to be summed.
2. Initialize two variables sum_even and sum_odd to 0. These will store the sum of even and odd numbers respectively.
3. Iterate from 1 to N using a loop.
4. Inside the loop, check if the number is even or odd.
5. If even, add the number to sum_even. If odd, add the number to sum_odd.
6. After the loop ends, print the sum of even and odd numbers.

The code will look like:

N = int(input("Enter the limit: "))
sum_even = 0
sum_odd = 0
for i in range(1, N+1):
    if i%2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)

The output will display the sum of even and odd numbers from 1 to the input N.