 Here is the formal content in Markdown format without any emojis or external links:

#### 3. Run some python programs on Pi like:

a) Print a name 'n' times, where name and n are read from standard input,

- Take input for name and n from standard input
- Store the input values in variables 'name' and 'n' respectively
- Use a for loop to print the name n number of times
- For example:

Enter name: John
Enter n: 5
John
John
John
John
John

- The program can be written as:

name = input("Enter name: ")
n = int(input("Enter n: "))

for i in range(n):
    print(name)

- This is a basic program to demonstrate taking multiple inputs and using them in a for loop.