#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

To run a python program on a Raspberry Pi, you will need to have python installed on your Pi. Python is usually pre-installed on the Raspberry Pi OS. If it is not installed, you can install it by running the following command in the terminal:

```
sudo apt-get install python3
```

Once python is installed, you can create a new python file with the `.py` extension, for example `print_name.py`. In this file, you can write the following code to print a name 'n' times, where name and n are read from standard input:

```python
name = input("Enter a name: ")
n = int(input("Enter the number of times to print the name: "))

for i in range(n):
    print(name)
```

After saving the file, you can run the program by navigating to the directory where the file is saved and running the following command in the terminal:

```
python3 print_name.py
```

This will prompt you to enter a name and the number of times to print the name. After entering the values, the program will print the name 'n' times.