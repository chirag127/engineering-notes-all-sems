

# KOT 551 INTERNET OF THINGS LAB

- Internet of Things (IoT) is the concept of connecting any device with an on and off switch to the Internet and/or to each other.
- IoT can enable various applications such as smart home, smart city, smart health, smart agriculture, etc.
- IoT can also enhance the research and innovation in the laboratory by allowing remote monitoring, data collection, automation, and collaboration.
- KOT 551 Internet of Things Lab is a course that aims to provide students with the theoretical and practical knowledge of IoT and its applications.
- The course covers the following topics:
  - Introduction to IoT and its architecture
  - IoT devices, sensors, and actuators
  - IoT communication protocols and standards
  - IoT cloud platforms and services
  - IoT security and privacy issues
  - IoT applications and case studies
- The course also involves hands-on experiments with various IoT devices and platforms such as Arduino, Raspberry Pi, ESP32, AWS IoT, Google Cloud IoT, etc.
- The course objectives are:
  - To understand the basic concepts and principles of IoT and its architecture
  - To learn how to design, implement, and test IoT systems using various devices, sensors, actuators, and platforms
  - To explore the current and emerging IoT applications and challenges
  - To develop the skills and competencies for IoT research and innovation



# KCS

KCS stands for Knowledge-Centered Service, a methodology that aims to improve service delivery and knowledge management in service organizations . Some of the main features and benefits of KCS are:

- It integrates the creation and maintenance of knowledge articles with the resolution of customer issues, making knowledge a by-product of service delivery.
- It empowers service agents to capture, structure, reuse, and improve knowledge articles based on their interactions with customers and their feedback.
- It enables service organizations to leverage the collective experience and expertise of their agents, reducing the dependency on a few experts and improving the consistency and quality of service.
- It reduces the costs and time of service delivery, increases customer satisfaction and loyalty, and enhances the learning and collaboration of service agents .

KCS is based on a set of principles, practices, and techniques that guide the implementation and adoption of the methodology. Some of the key elements of KCS are:

- The KCS Solve Loop, which describes the process of capturing, structuring, reusing, and improving knowledge articles during the resolution of customer issues.
- The KCS Evolve Loop, which describes the process of measuring, analyzing, and improving the performance and value of the KCS system and the service organization.
- The KCS Content Standard, which defines the quality criteria and best practices for creating and maintaining effective and reusable knowledge articles.
- The KCS Roles and Competencies, which define the responsibilities and skills of the different participants in the KCS system, such as agents, coaches, publishers, and managers.
- The KCS Adoption Framework, which provides a roadmap and a set of tools and resources for planning and executing a successful KCS initiative.

KCS is a registered service mark of the Consortium for Service Innovation, a non-profit organization that develops and promotes innovative service practices. The Consortium provides the KCS Academy, a certification and training program for KCS practitioners and organizations.



## Course Outcome (CO) Bloom's Knowledge Level (KL)

- Course outcome (CO) is a statement that describes what students are expected to know, understand, or be able to do at the end of a course.
- Bloom's knowledge level (KL) is a classification of the cognitive domain of learning objectives, based on the level of complexity and specificity of the knowledge required.
- Bloom's knowledge level (KL) consists of six categories: remember, understand, apply, analyze, evaluate, and create. Each category has a number of verbs that can be used to formulate learning objectives.
- The table below shows the relationship between course outcome (CO) and Bloom's knowledge level (KL), with some examples of verbs and learning objectives for each category.

| CO | KL | Verbs | Learning Objectives |
| --- | --- | --- | --- |
| CO1 | Remember | Define, list, recall, identify, recognize, etc. | The student can recall the basic concepts and terminology of the course. |
| CO2 | Understand | Explain, describe, summarize, illustrate, interpret, etc. | The student can comprehend the meaning and implications of the course content. |
| CO3 | Apply | Use, demonstrate, solve, calculate, apply, etc. | The student can apply the learned knowledge and skills to new or familiar situations. |
| CO4 | Analyze | Compare, contrast, classify, categorize, differentiate, etc. | The student can break down the course material into its components and examine their relationships and functions. |
| CO5 | Evaluate | Assess, judge, critique, justify, argue, etc. | The student can make judgments based on criteria and standards, and support them with evidence and reasoning. |
| CO6 | Create | Design, create, produce, construct, synthesize, etc. | The student can generate new or original products, solutions, or ideas based on the course content. |



### At the end of the course, the student will be able to

- Demonstrate an understanding of the main concepts and principles of the subject matter.
- Apply the acquired knowledge and skills to solve problems and perform tasks related to the course objectives.
- Communicate effectively using appropriate terminology and formats for the course discipline.
- Analyze and evaluate information from various sources and perspectives critically and creatively.
- Collaborate with others in a respectful and constructive manner to achieve common goals.
- Reflect on their own learning process and outcomes and identify areas for improvement and further development.



#### CO 1 Understand the concept of Internet of Things K3

- Internet of Things (IoT) is the interconnection of computing devices embedded in everyday objects, enabling them to send and receive data over the internet or other communications networks .
- IoT devices can range from simple sensors and actuators to complex smart appliances and wearable devices that can monitor, control, and automate various aspects of our lives.
- IoT devices can communicate with each other, with cloud services, or with human users, using various protocols and standards, such as Wi-Fi, Bluetooth, Zigbee, MQTT, HTTP, etc.
- IoT devices can generate large amounts of data that can be processed, analyzed, and acted upon using artificial intelligence, machine learning, cloud computing, edge computing, and other technologies.
- IoT applications can span across various domains, such as smart homes, smart cities, smart health, smart agriculture, smart industry, smart transportation, etc.
- IoT can provide various benefits, such as improved efficiency, convenience, safety, security, sustainability, and quality of life, but also pose various challenges, such as privacy, security, interoperability, scalability, reliability, and ethics.



#### CO2 Implement interfacing of various sensors with Arduino/Raspberry Pi K4, K5

- CO2 sensors are devices that can measure the concentration of carbon dioxide in the air. They are useful for monitoring indoor air quality, greenhouse gas emissions, plant growth, and other applications.
- There are different types of CO2 sensors, such as infrared (NDIR), electrochemical, metal oxide, and chemical. Each type has its own advantages and disadvantages, such as accuracy, power consumption, response time, and cost.
- Arduino and Raspberry Pi are popular microcontroller and microcomputer platforms that can be used to interface with various sensors, including CO2 sensors. They can read the sensor data, process it, display it, or send it to other devices or services.
- To interface a CO2 sensor with Arduino or Raspberry Pi, the following steps are required:

  - Choose a suitable CO2 sensor that is compatible with the chosen platform. For example, some CO2 sensors have digital output pins that use I2C or UART protocols, while others have analog output pins that require an analog-to-digital converter (ADC). Some CO2 sensors also have integrated temperature and humidity sensors that can provide additional data.    
  - Connect the CO2 sensor to the Arduino or Raspberry Pi using the appropriate pins and wires. For example, if the CO2 sensor has an I2C interface, it can be connected to the SDA and SCL pins of the Arduino or Raspberry Pi, along with the power and ground pins. If the CO2 sensor has an analog interface, it can be connected to an analog input pin of the Arduino, or to an external ADC module that is connected to the Raspberry Pi.    
  - Install the necessary libraries and drivers for the CO2 sensor on the Arduino or Raspberry Pi. For example, some CO2 sensors have official or third-party libraries that can be downloaded and installed using the Arduino IDE or the Python package manager. These libraries provide functions and classes that can simplify the communication and calibration of the CO2 sensor.    
  - Write the code to read and process the CO2 sensor data on the Arduino or Raspberry Pi. For example, the code can use the library functions to initialize the CO2 sensor, read the CO2 concentration, temperature, and humidity values, and print them to the serial monitor or the LCD screen. The code can also perform some calculations or conversions on the data, such as converting the CO2 concentration from ppm to mg/m3, or calculating the indoor air quality index.    
  - Test and debug the code and the sensor on the Arduino or Raspberry Pi. For example, the code can be uploaded to the Arduino or run on the Raspberry Pi, and the sensor can be exposed to different levels of CO2 in the air. The sensor data can be checked for accuracy, consistency, and stability, and the code can be modified if there are any errors or issues.



#### CO 3 Demonstrate the ability to transmit data wirelessly between different devices. K4

- Wireless data transmission is the process of sending and receiving data without using physical wires or cables.
- Wireless data transmission can be classified into two main types: radio frequency (RF) and optical.
- RF transmission uses electromagnetic waves to carry data through the air, such as Wi-Fi, Bluetooth, and cellular networks . RF signals are easily generated, ranging from 3 kHz to 300 GHz.
- Optical transmission uses light to send data, such as infrared, visible light, and laser. Infrared radiations are electromagnetic radiations with longer wavelengths than visible light.
- Wireless data transmission can be used for various devices, such as wireless phones, wireless adapters, wireless repeaters, and other devices.
- Wireless data transmission has advantages and disadvantages compared to wired data transmission. Some of the advantages are:
  - Mobility and flexibility: Wireless devices can move freely and access data from anywhere within the range of the wireless network.
  - Cost and convenience: Wireless devices do not require cables or wires, which can reduce installation and maintenance costs and avoid clutter and hazards.
  - Scalability and expandability: Wireless devices can easily join or leave the wireless network, which can accommodate changing needs and demands.
- Some of the disadvantages are:
  - Security and privacy: Wireless data transmission is more vulnerable to interception, eavesdropping, and hacking, which can compromise the confidentiality, integrity, and availability of data.
  - Interference and noise: Wireless data transmission can be affected by various sources of interference and noise, such as other wireless devices, physical obstacles, weather conditions, and electromagnetic fields, which can degrade the quality and reliability of data.
  - Bandwidth and speed: Wireless data transmission has limited bandwidth and speed compared to wired data transmission, which can affect the performance and efficiency of data transfer.



#### CO 4 Show an ability to upload/download sensor data on cloud and server K2

- Sensor data is the information collected by various types of sensors that measure physical phenomena such as temperature, humidity, pressure, light, sound, motion, etc.
- Cloud and server K2 are two different platforms that can store and process sensor data remotely, without requiring the sensor devices to have high computing power or memory.
- To upload sensor data on cloud and server K2, the following steps are required:
  - Establish a connection between the sensor device and the cloud or server K2 using a suitable communication protocol, such as Wi-Fi, Bluetooth, cellular, or LoRaWAN.
  - Encode the sensor data in a format that is compatible with the cloud or server K2, such as JSON, XML, CSV, or binary.
  - Send the sensor data to the cloud or server K2 using a secure and reliable method, such as HTTP, MQTT, CoAP, or WebSocket.
  - Receive an acknowledgment from the cloud or server K2 that the sensor data has been successfully received and stored.
- To download sensor data from cloud and server K2, the following steps are required:
  - Establish a connection between the sensor device and the cloud or server K2 using a suitable communication protocol, as mentioned above.
  - Request the sensor data from the cloud or server K2 using a specific query or command, such as REST API, SQL, or GraphQL.
  - Receive the sensor data from the cloud or server K2 in a format that is compatible with the sensor device, as mentioned above.
  - Decode the sensor data and use it for further processing, analysis, or visualization on the sensor device or another application.



#### CO 5 Examine various SQL queries from MySQL database K4, K5

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- MySQL is one of the most popular open-source relational database management systems (RDBMS) that supports SQL.
- SQL queries are statements that specify what data to retrieve, insert, update, delete, or manipulate from a database.
- SQL queries can be classified into four categories: Data Definition Language (DDL), Data Manipulation Language (DML), Data Query Language (DQL), and Data Control Language (DCL).
- DDL is used to define the structure and schema of the database, such as creating, altering, or dropping tables, views, indexes, or constraints.
- DML is used to manipulate the data in the database, such as inserting, updating, deleting, or merging records.
- DQL is used to query or retrieve data from the database, such as selecting, joining, filtering, sorting, or grouping data.
- DCL is used to control the access and permissions of the database, such as granting, revoking, or denying privileges or roles to users or groups.
- Some examples of SQL queries from MySQL database are:

  - To create a table named `students` with four columns: `id` (primary key), `name` (varchar), `age` (int), and `grade` (char):

    ```sql
    CREATE TABLE students (
      id INT NOT NULL AUTO_INCREMENT,
      name VARCHAR(50) NOT NULL,
      age INT NOT NULL,
      grade CHAR(1) NOT NULL,
      PRIMARY KEY (id)
    );
    ```

  - To insert a new record into the `students` table with values: `1`, `Alice`, `18`, and `A`:

    ```sql
    INSERT INTO students (id, name, age, grade) VALUES (1, 'Alice', 18, 'A');
    ```

  - To update the `grade` of the student with `id` = `1` to `B`:

    ```sql
    UPDATE students SET grade = 'B' WHERE id = 1;
    ```

  - To delete the record of the student with `id` = `1` from the `students` table:

    ```sql
    DELETE FROM students WHERE id = 1;
    ```

  - To select all the records from the `students` table:

    ```sql
    SELECT * FROM students;
    ```

  - To select only the `name` and `grade` of the students who are older than `20` and sort them by `grade` in descending order:

    ```sql
    SELECT name, grade FROM students WHERE age > 20 ORDER BY grade DESC;
    ```

  - To create a view named `top_students` that contains the `name` and `grade` of the students who have `grade` = `A`:

    ```sql
    CREATE VIEW top_students AS
    SELECT name, grade FROM students WHERE grade = 'A';
    ```

  - To grant the `SELECT` and `UPDATE` privileges on the `students` table to the user `bob`:

    ```sql
    GRANT SELECT, UPDATE ON students TO bob;
    ```

  - To revoke the `UPDATE` privilege on the `students` table from the user `bob`:

    ```sql
    REVOKE UPDATE ON students FROM bob;
    ```

  - To deny the `DELETE` privilege on the `students` table to the user `bob`:

    ```sql
    DENY DELETE ON students TO bob;
    ```



## DETAILED SYLLABUS

- A detailed syllabus is a document that outlines the topics, objectives, assignments, assessments, and policies of a course.
- A detailed syllabus can help students to understand the expectations and requirements of the course, as well as to plan their study time and workload accordingly.
- A detailed syllabus can also help instructors to organize and structure their course content, as well as to communicate their teaching philosophy and goals to the students.
- A detailed syllabus typically includes the following sections:

  - Course information: This section provides the basic information about the course, such as the course title, code, number, credits, prerequisites, instructor name, contact details, office hours, meeting times, and location.
  - Course description: This section gives an overview of the course content, scope, and purpose, as well as the main themes, questions, or problems that the course will address.
  - Course objectives: This section states the specific learning outcomes or competencies that the students are expected to achieve by the end of the course, as well as how they will be measured or assessed.
  - Course materials: This section lists the required and recommended texts, readings, resources, or materials that the students will need to access or purchase for the course, as well as how and where to obtain them.
  - Course schedule: This section provides a tentative outline of the course topics, activities, assignments, and assessments, along with their due dates and weightings, for each week or unit of the course. It may also indicate the readings or preparations that the students need to complete before each class session.
  - Course policies: This section specifies the rules and expectations that the students need to follow and respect in the course, such as the attendance, participation, late submission, academic integrity, grading, feedback, communication, and accessibility policies.
  - Course support: This section identifies the available sources of academic and personal support for the students, such as the instructor, teaching assistants, tutors, counselors, librarians, or other services or resources on campus or online.



### The student should have hands on experience in using various sensors like temperature, humidity, smoke, light, etc.

- Sensors are devices that detect and measure physical quantities such as temperature, humidity, smoke, light, etc. and convert them into electrical signals that can be processed by a microcontroller or a computer.
- Hands on experience in using various sensors means that the student should be able to:
  - Identify the types and specifications of different sensors and how they work.
  - Connect the sensors to a microcontroller or a computer using appropriate wires, resistors, capacitors, etc.
  - Write and upload code to the microcontroller or the computer to read and display the sensor data.
  - Analyze and interpret the sensor data and use it for various applications such as monitoring, control, automation, etc.
- Hands on experience in using various sensors is important for the student because it helps them to:
  - Develop practical skills and knowledge in electronics, programming, and data analysis.
  - Understand the principles and applications of sensors in real-world scenarios.
  - Enhance their creativity and problem-solving abilities by designing and implementing sensor-based projects.
  - Prepare for future careers or studies in fields such as robotics, IoT, smart systems, etc.



### Should be able to use control web camera, network, and relays connected to the Pi.

- A web camera is a device that captures images or videos and sends them to a computer or a network. A web camera can be used for various purposes, such as video conferencing, surveillance, or entertainment.
- A network is a system of interconnected devices that can communicate and share data with each other. A network can be wired or wireless, local or global, public or private. A network can be used for various purposes, such as accessing the internet, transferring files, or streaming media.
- A relay is a device that switches an electrical circuit on or off based on a signal from another device. A relay can be used for various purposes, such as controlling lights, motors, or sensors.
- A Pi is a small, low-cost, and versatile computer that can run various operating systems and applications. A Pi can be used for various purposes, such as learning programming, creating projects, or experimenting with electronics.
- To use control web camera, network, and relays connected to the Pi, one should be able to:
  - Connect the web camera, network, and relays to the Pi using the appropriate cables, adapters, or modules.
  - Install and configure the software and drivers for the web camera, network, and relays on the Pi using the command line or a graphical interface.
  - Write and run programs or scripts on the Pi that can capture and display images or videos from the web camera, send and receive data over the network, and switch the relays on or off based on the input or output signals.
  - Test and troubleshoot the web camera, network, and relays connected to the Pi using the tools and methods available on the Pi or the computer.



#### 1. Start Raspberry Pi and try various Linix commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small, low-cost computer that can run Linux, a free and open-source operating system.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard, and a mouse. You also need to insert a microSD card with a Linux operating system installed on it.
- Once Raspberry Pi boots up, you will see a desktop environment with icons and menus. You can launch applications from the desktop or from the main menu.
- To open a command terminal window, you can either click on the terminal icon on the desktop or on the main menu, or press Ctrl+Alt+T on the keyboard.
- A command terminal window is a text-based interface that allows you to interact with the Linux operating system using commands. Commands are instructions that tell the computer what to do.
- Some of the basic Linux commands that you can try in the command terminal window are:

  - `ls`: This command lists the files and folders in the current directory. A directory is a folder that contains other files and folders. The current directory is the one that you are currently in. You can see the name of the current directory at the prompt, which is the symbol that indicates where you can type commands. For example, if the prompt is `pi@raspberrypi:~ $`, then the current directory is `~`, which is a shortcut for your home directory, where your personal files are stored.
  - `cd`: This command changes the current directory to another one. You can specify the name of the directory that you want to go to after the command. For example, if you type `cd Documents`, you will change the current directory to the Documents folder inside your home directory. You can also use `..` to go up one level in the directory hierarchy, or `/` to go to the root directory, which is the topmost directory in the system. To go back to your home directory, you can type `cd` without any arguments.
  - `touch`: This command creates a new, empty file with the name that you specify after the command. For example, if you type `touch hello.txt`, you will create a new file called hello.txt in the current directory. You can also use this command to update the timestamp of an existing file, which is the date and time when the file was last modified.
  - `mv`: This command moves or renames a file or a directory. You can specify the name of the file or directory that you want to move or rename, and the name of the destination file or directory after the command. For example, if you type `mv hello.txt goodbye.txt`, you will rename the file hello.txt to goodbye.txt. If you type `mv hello.txt Documents`, you will move the file hello.txt to the Documents folder. You can also use this command to move or rename multiple files or directories at once, by separating them with spaces.
  - `rm`: This command removes or deletes a file or a directory. You can specify the name of the file or directory that you want to remove after the command. For example, if you type `rm goodbye.txt`, you will delete the file goodbye.txt. If you type `rm -r Documents`, you will delete the Documents folder and all its contents. Be careful with this command, as there is no undo option for deleting files or directories in Linux.
  - `man`: This command shows the manual page for another command. A manual page is a document that explains how to use a command, what arguments and options it accepts, and what it does. You can specify the name of the command that you want to learn more about after the man command. For example, if you type `man ls`, you will see the manual page for the ls command. You can use the arrow keys to scroll up and down the manual page, and press Q to quit.



#### mkdir, rmdir, tar, gzip, cat, more, less, ps, sudo, cron, chown, chgrp, ping etc.

These are some of the common Linux commands that can be used to perform various tasks on the command terminal window. Here is a brief description of each command and some examples of their usage:

- **mkdir**: This command is used to create directories (also known as folders). The syntax is `mkdir [options] [directory_name]`. For example, `mkdir new_folder` will create a new directory called new_folder in the current working directory. To create multiple directories at once, we can use `mkdir dir1 dir2 dir3` .
- **rmdir**: This command is used to remove empty directories. The syntax is `rmdir [options] [directory_name]`. For example, `rmdir new_folder` will delete the new_folder directory if it is empty. To remove multiple directories at once, we can use `rmdir dir1 dir2 dir3`.
- **tar**: This command is used to create or extract compressed archive files. The syntax is `tar [options] [archive_name] [file_name]`. For example, `tar -cvf archive.tar file1 file2 file3` will create a compressed archive file called archive.tar that contains file1, file2 and file3. To extract the files from the archive, we can use `tar -xvf archive.tar`.
- **gzip**: This command is used to compress or decompress files using the gzip algorithm. The syntax is `gzip [options] [file_name]`. For example, `gzip file1` will compress file1 and rename it to file1.gz. To decompress the file, we can use `gzip -d file1.gz`.
- **cat**: This command is used to display the contents of a file or concatenate multiple files. The syntax is `cat [options] [file_name]`. For example, `cat file1` will print the contents of file1 on the screen. To concatenate file1 and file2 and display the result, we can use `cat file1 file2` .
- **more**: This command is used to display the contents of a file or output of another command one page at a time. The syntax is `more [options] [file_name]`. For example, `more file1` will show the first page of file1 and wait for the user to press the space bar to show the next page. To quit, the user can press q. To display the output of another command, we can use `| more`. For example, `ls | more` will show the list of files in the current directory one page at a time.
- **less**: This command is similar to the more command but provides more features. One important feature is that it allows backward as well as forward movement in the file or output, even with pipes. The syntax is `less [options] [file_name]`. For example, `less file1` will show the first page of file1 and allow the user to navigate using the arrow keys, page up, page down, home, end, etc. To quit, the user can press q. To display the output of another command, we can use `| less`. For example, `ls | less` will show the list of files in the current directory and allow the user to navigate.
- **ps**: This command is used to display information about the processes running on the system. The syntax is `ps [options]`. For example, `ps` will show the process ID, terminal, CPU time and command for the current user's processes. To show all the processes on the system, we can use `ps -e`. To show more details about the processes, we can use `ps -f`.
- **sudo**: This command is used to execute a command as another user, usually the superuser or root. The syntax is `sudo [options] [command]`. For example, `sudo apt-get update` will run the apt-get update command as the root user and update the system's package list. To run a command as a different user, we can use `sudo -u [user_name] [command]`. For example, `sudo -u bob ls` will run the ls command as the user bob.
- **cron**: This command is used to schedule commands or



#### 2. Run some python programs on Pi like:

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- You also need to have a text editor or an IDE (Integrated Development Environment) to write and edit your python code. You can use the default text editor on Pi, which is called `nano`, or you can install other editors like `Thonny` or `Mu`. To install Thonny, type `sudo apt install thonny`. To install Mu, type `pip3 install mu-editor`.
- To write a python program, you need to create a file with the `.py` extension, such as `hello.py`. You can use any text editor to create and save the file in a directory of your choice. To run the program, you need to navigate to the directory where the file is located, and type `python3 hello.py` in the terminal. This will execute the code in the file and display the output on the screen.
- A simple python program that prints "Hello, world!" on the screen is:

```python
# This is a comment. It starts with a # symbol and is ignored by the interpreter.
# Comments are useful to explain your code or add notes.

# The print() function is used to display text or values on the screen.
# The text or values are enclosed in parentheses and quotation marks.
# You can use single or double quotation marks, but they should match.
print("Hello, world!")
```

- To run this program, save it as `hello.py` and type `python3 hello.py` in the terminal. You should see `Hello, world!` on the screen.
- You can write more complex python programs that use variables, data types, operators, expressions, statements, functions, modules, libraries, etc. You can also use python to interact with the hardware and sensors on your Pi, such as the GPIO pins, the camera, the LED, the button, etc. You can find more examples and tutorials on the official python website (https://www.python.org/) or the Raspberry Pi website (https://www.raspberrypi.org/).



#### a) Read your name and print Hello message with name

- To read your name, you need to use an input function that takes a string as an argument and returns the user's input as another string.
- For example, in Python, you can use the input() function to read your name from the keyboard and store it in a variable called name.
- To print a Hello message with your name, you need to use a print function that takes a string as an argument and displays it on the screen.
- For example, in Python, you can use the print() function to print a Hello message with your name by concatenating the strings "Hello" and name with a comma or a plus sign.
- Here is an example of a Python program that reads your name and prints a Hello message with your name:

```python
# Read your name and store it in a variable called name
name = input("Enter your name: ")

# Print a Hello message with your name
print("Hello", name) # Using a comma to separate the strings
# or
print("Hello" + name) # Using a plus sign to concatenate the strings
```

- The output of this program will look something like this:

```
Enter your name: Sydney
Hello Sydney
```



#### b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the `input()` function in Python, which returns a string value that can be converted to a numeric type using `int()` or `float()`.
- To print the sum, difference, product and division of two numbers, we can use the arithmetic operators `+`, `-`, `*` and `/` in Python, which perform the corresponding operations on the operands and return the result.
- To print the result, we can use the `print()` function in Python, which displays the value passed to it on the standard output device, such as the console or the screen.
- An example of a Python program that reads two numbers and prints their sum, difference, product and division is:

```python
# Read two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate and print the sum, difference, product and division
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

print("The sum of the two numbers is", sum)
print("The difference of the two numbers is", difference)
print("The product of the two numbers is", product)
print("The division of the two numbers is", division)
```



#### c) Word and character count of a given string.

- A string is a sequence of characters enclosed in quotation marks, such as "Hello" or "This is a string".
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "This is a word".
- A character is a single symbol, such as "H" or "." or " ".
- The word count of a string is the number of words in the string, such as 4 for "This is a string".
- The character count of a string is the number of characters in the string, including spaces and punctuation marks, such as 16 for "This is a string".
- To count the words and characters of a given string, one can use the following steps:
  - Initialize two variables, word_count and char_count, to zero.
  - Loop through each character in the string, using a for loop or a while loop.
  - If the current character is a space or a punctuation mark, increment word_count by one, and continue to the next character.
  - Otherwise, increment char_count by one, and continue to the next character.
  - After the loop ends, increment word_count by one, to account for the last word in the string.
  - Return or print word_count and char_count as the output.



#### d) Area of a given shape (rectangle, triangle and circle) reading shape and appropriate values from standard

- The area of a shape is the amount of space inside the shape. It is measured in square units, such as square centimeters, square meters, square inches, etc.
- To find the area of a given shape, we need to know the shape and the appropriate values, such as length, width, base, height, radius, etc. We can read these values from the standard input, such as keyboard, mouse, microphone, etc.
- The formula for the area of a rectangle is `A = length * width`. We need to read the length and width of the rectangle from the standard input and multiply them to get the area.
- The formula for the area of a triangle is `A = (base * height) / 2`. We need to read the base and height of the triangle from the standard input and multiply them and divide by 2 to get the area.
- The formula for the area of a circle is `A = pi * radius * radius`. We need to read the radius of the circle from the standard input and multiply it by itself and by pi (approximately 3.14) to get the area.



#### Input

- Input is the process of providing data or instructions to a computer system so that it can perform a task or operation.
- Input is important because it allows users to interact with a computer system and provide information that can be processed and analyzed.
- Input can be given in various forms, such as text, images, sound, video, gestures, etc.
- Input devices are hardware components that enable users to input data or instructions to a computer system.
- The most common input devices are the keyboard, mouse, and touch screen.
- Some other examples of input devices are microphones, scanners, cameras, joysticks, sensors, etc.
- Input devices can be categorized into different types based on their functionality, such as pointing devices, scanning devices, audio devices, etc.



#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- To write a python program, you need to use a text editor such as nano, vim, or idle. You can launch any of these editors from the terminal by typing their name followed by the name of the file you want to create or edit. For example, `nano hello.py` will open a new file called hello.py in nano editor.
- To print a name 'n' times, where name and n are read from standard input, you need to use the `input` function to get the user input and store it in variables. Then you need to use a `for` loop to repeat the printing 'n' times. You also need to use the `print` function to display the name on the screen. Here is an example of a python program that does this:

```python
# get the name from the user
name = input("Enter your name: ")

# get the number of times to print from the user
n = int(input("Enter the number of times to print: "))

# use a for loop to print the name n times
for i in range(n):
    print(name)
```

- To run the python program, you need to save the file and exit the editor. Then you need to type `python3` followed by the name of the file in the terminal. For example, `python3 hello.py` will run the hello.py program. You will see the output on the screen. You can press Ctrl+C to stop the program.



#### Using for and while loops
- A for loop is a repetition control structure that allows you to efficiently write a loop that needs to execute a specific number of times.
- A while loop is a repetition control structure that allows you to write a loop that will repeat as long as a condition is true.
- The syntax of a for loop is:

```python
for variable in range(start, end, step):
    # loop body
```
- The syntax of a while loop is:

```python
while condition:
    # loop body
```
- To exit a loop prematurely, you can use the break statement.
- To skip the current iteration of a loop, you can use the continue statement.

#### Handle Divided by Zero Exception
- A divided by zero exception is a runtime error that occurs when you try to divide a number by zero.
- To handle a divided by zero exception, you can use a try-except block.
- A try-except block is a structure that allows you to catch and handle errors that may occur during the execution of a program.
- The syntax of a try-except block is:

```python
try:
    # code that may cause an error
except ExceptionType as e:
    # code that handles the error
```
- To handle a divided by zero exception, you can use the ZeroDivisionError exception type.
- An example of a try-except block that handles a divided by zero exception is:

```python
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    z = x / y
    print("The result is", z)
except ZeroDivisionError as e:
    print("You cannot divide by zero!")
    print("The error message is:", e)
```

#### Print current time for 10 times with an interval of 1 second
- To print the current time, you can use the datetime module.
- The datetime module provides various classes and functions to manipulate dates and times.
- To get the current date and time, you can use the datetime.now() function.
- To format the date and time, you can use the strftime() method.
- To pause the execution of a program for a certain amount of time, you can use the time module.
- The time module provides various functions to deal with time-related tasks.
- To pause the execution of a program for a certain amount of time, you can use the time.sleep() function.
- An example of a program that prints the current time for 10 times with an interval of 1 second is:

```python
import datetime
import time

for i in range(10):
    # get the current date and time
    now = datetime.datetime.now()
    # format the date and time
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    # print the date and time
    print(formatted)
    # pause the execution for 1 second
    time.sleep(1)
```



#### Interval of 10 seconds
- An interval of 10 seconds is a measure of time that is equal to 10 units of one second each.
- A second is the base unit of time in the International System of Units (SI) and is defined as the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.
- An interval of 10 seconds can be represented by various symbols, such as 10 s, 10 sec, or 10".
- An interval of 10 seconds can be used to measure various phenomena, such as the frequency of sound waves, the speed of a moving object, or the duration of an event.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one can use a programming language such as Python, which has built-in functions and modules for working with files and strings.
- The following steps can be followed to achieve the task:
  - Open the file in read mode using the `open()` function, which returns a file object.
  - Use a `for` loop to iterate over the file object, which yields one line at a time.
  - Use the `split()` method on each line, which returns a list of words separated by whitespace characters.
  - Use the `len()` function on the list, which returns the number of elements in the list, which is equivalent to the word count of the line.
  - Print the word count of the line using the `print()` function, which writes the output to the standard output stream.
  - Close the file using the `close()` method on the file object, which frees up the resources associated with the file.
- The following is an example of Python code that implements the task:

```python
# Open the file in read mode
file = open("example.txt", "r")

# Loop over the file object
for line in file:
  # Split the line into words
  words = line.split()
  # Get the word count of the line
  word_count = len(words)
  # Print the word count of the line
  print(word_count)

# Close the file
file.close()
```



#### 4. a) Light an LED through Python program

- To light an LED through Python program, you need to have a hardware device that can be controlled by Python, such as an Arduino, a Raspberry Pi, or a MicroPython board.
- You also need to have an LED, a resistor, some wires, and a breadboard to connect the LED to the device.
- Depending on the device you use, you may need to install some libraries or drivers to communicate with it from Python.
- The basic steps to light an LED through Python program are:

  1. Connect the LED to the device using the resistor, wires, and the breadboard. The resistor is used to limit the current and protect the LED from burning out. The positive leg of the LED (the longer one) should be connected to a digital pin of the device, and the negative leg (the shorter one) should be connected to the ground (GND) pin of the device. For example, if you use an Arduino, you can connect the LED to pin 13 and GND.
  2. Write a Python program that can send commands to the device to turn the LED on and off. The commands may vary depending on the device and the library you use, but they usually involve setting the pin mode (output or input), writing a high or low value to the pin, and adding some delay between the commands. For example, if you use an Arduino and the pyserial library, you can write a program like this:

```python
import serial
import time

# create a serial object to communicate with the Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)

# loop forever
while True:
    # send 'H' to turn the LED on
    ser.write(b'H')
    # wait for one second
    time.sleep(1)
    # send 'L' to turn the LED off
    ser.write(b'L')
    # wait for one second
    time.sleep(1)
```

  3. Run the Python program on your computer and observe the LED blinking on and off. You may need to use some commands or tools to run the program, such as sudo, python, or IDLE. For example, if you use a Raspberry Pi and the RPi.GPIO library, you can run the program like this:

```bash
sudo python LED.py
```

- You can modify the Python program to change the blinking pattern, the duration, or the number of LEDs you want to control. You can also use other Python features, such as functions, loops, or variables, to make your program more flexible and reusable. For example, you can write a function that takes the pin number and the delay time as parameters and blinks the LED accordingly:

```python
import pyb
import time

# define a function that blinks an LED
def blink(led, delay):
    # create an LED object
    led = pyb.LED(led)
    # loop forever
    while True:
        # toggle the LED state
        led.toggle()
        # wait for the delay time
        time.sleep(delay)

# blink the red LED with one second delay
blink(2, 1)
```

- You can also use other Python libraries or modules to control the LEDs, such as gpiozero, tkinter, or pygame, to create more interactive and graphical programs. For example, you can write a program that turns the LED on and off based on the mouse clicks on a button:

```python
from gpiozero import LED
from tkinter import *

# create an LED object
led = LED(17)

# create a tkinter window
window = Tk()
window.title("LED Control")

# create a button to toggle the LED
button = Button(window, text="Toggle LED", command=led.toggle)
button.pack()

# start the main loop
window.mainloop()
```



#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to two switches and two LEDs using wires and resistors.
- The switches are used to provide digital input signals to the microcontroller, which can be either HIGH (5V) or LOW (0V) depending on whether the switch is pressed or not.
- The LEDs are used to provide digital output signals from the microcontroller, which can be either HIGH (5V) or LOW (0V) depending on whether the LED is turned on or off.
- The microcontroller can read the input signals from the switches using digitalRead() function and write the output signals to the LEDs using digitalWrite() function.
- The logic of the program is to check the state of each switch and turn on the corresponding LED if the switch is pressed, or turn off the LED if the switch is not pressed.
- The circuit diagram and the code for this project are shown below:

```markdown
Circuit diagram:

    +5V
     |
     |
    [ ]  Switch 1
     |
     |    10K
     +---/\/\/\---+--- Pin 2
     |            |
     |            |
    [ ]  LED 1    |
     |            |
     |    220     |
     +---/\/\/\---+
     |
    GND

    +5V
     |
     |
    [ ]  Switch 2
     |
     |    10K
     +---/\/\/\---+--- Pin 3
     |            |
     |            |
    [ ]  LED 2    |
     |            |
     |    220     |
     +---/\/\/\---+
     |
    GND
```

```markdown
Code:

// Define the pins for switches and LEDs
const int switch1 = 2;
const int switch2 = 3;
const int led1 = 4;
const int led2 = 5;

void setup() {
  // Set the switch pins as inputs with pull-up resistors
  pinMode(switch1, INPUT_PULLUP);
  pinMode(switch2, INPUT_PULLUP);
  // Set the LED pins as outputs
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  // Read the state of each switch
  int state1 = digitalRead(switch1);
  int state2 = digitalRead(switch2);
  // Turn on the corresponding LED if the switch is pressed, or turn off the LED if the switch is not pressed
  if (state1 == LOW) {
    digitalWrite(led1, HIGH);
  } else {
    digitalWrite(led1, LOW);
  }
  if (state2 == LOW) {
    digitalWrite(led2, HIGH);
  } else {
    digitalWrite(led2, LOW);
  }
}
```



#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, some jumper wires, and a file that contains the on time and off time values in milliseconds.
- The microcontroller is a device that can execute a program that controls the output pins. We can use any microcontroller that has a digital output pin, such as Arduino, Raspberry Pi, or ESP32.
- The LED is a light-emitting diode that can turn on or off depending on the voltage applied to its terminals. We need to connect the LED to the microcontroller's output pin through a resistor to limit the current and protect the LED from burning out.
- The resistor is a component that reduces the current flow in a circuit. The value of the resistor depends on the LED's voltage drop and the microcontroller's output voltage. A common value is 220 ohms.
- The breadboard is a board that allows us to connect components without soldering. We can use the breadboard to connect the microcontroller, the LED, the resistor, and the jumper wires.
- The jumper wires are wires that can connect different parts of the circuit. We need to use jumper wires to connect the microcontroller's output pin to the resistor, the resistor to the LED, the LED to the ground, and the microcontroller to the power supply.
- The file is a text file that contains two numbers separated by a comma. The first number is the on time and the second number is the off time for the LED in milliseconds. For example, the file could contain 1000,500, which means the LED should be on for 1000 milliseconds and off for 500 milliseconds. We need to store the file in the microcontroller's memory or on an external storage device, such as a microSD card or a USB flash drive.

- The steps to flash an LED at a given on time and off time cycle are:

  - Connect the microcontroller to the computer and upload the program that reads the file and controls the output pin.
  - Connect the microcontroller to the power supply and the LED circuit.
  - The program will read the file and store the on time and off time values in two variables, such as onTime and offTime.
  - The program will enter a loop that repeats indefinitely.
  - In the loop, the program will set the output pin to high, which means the LED will turn on.
  - The program will wait for the on time duration using a delay function, such as delay(onTime).
  - The program will set the output pin to low, which means the LED will turn off.
  - The program will wait for the off time duration using a delay function, such as delay(offTime).
  - The program will repeat the loop until the power is turned off or the program is stopped.



#### 5. a) Flash an LED based on cron output (acts as an alarm)

- To flash an LED based on cron output, we need to use a Raspberry Pi, an LED, a resistor, some jumper wires, and a breadboard.
- We also need to install the WiringPi library on the Raspberry Pi, which provides a command-line utility called `gpio` to control the GPIO pins.
- We need to connect the LED and the resistor to the GPIO pin 17 and the ground pin on the Raspberry Pi using the jumper wires and the breadboard. The resistor is used to limit the current and protect the LED from burning out.
- We need to write a shell script that uses the `gpio` command to turn the LED on and off. For example, we can create a file called `flash.sh` with the following content:

```bash
#!/bin/bash
# flash.sh: a script to flash an LED on GPIO pin 17

# set the pin 17 to output mode
gpio -g mode 17 out

# loop 10 times
for i in {1..10}
do
  # turn the LED on
  gpio -g write 17 1
  # wait for 0.5 seconds
  sleep 0.5
  # turn the LED off
  gpio -g write 17 0
  # wait for 0.5 seconds
  sleep 0.5
done
```

- We need to make the script executable by running the command `chmod +x flash.sh`.
- We need to edit the crontab file to schedule the script to run at a specific time. For example, we can run the command `crontab -e` and add the following line to the end of the file:

```bash
# flash the LED at 8:00 AM every day
0 8 * * * /home/pi/flash.sh
```

- We need to save and exit the crontab file. The cron daemon will automatically run the script at the specified time and flash the LED as an alarm.



#### b) Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

- A relay is an electromechanical device that can be used to switch on or off a load (such as a light, a fan, a motor, etc.) by applying a voltage to its coil terminals.
- Cron is a software utility that allows users to schedule commands or scripts to run at specified times or intervals on a Linux system.
- To switch on a relay at a given time using cron, the following steps are required:

  1. Connect the relay's coil terminals to a GPIO pin and a ground pin of a Raspberry Pi or any other microcontroller board that can run Linux and has GPIO pins.
  2. Connect the relay's contact terminals to the load and a power source, such as a battery or a wall outlet, according to the relay's specifications and the load's requirements.
  3. Write a Python script that can control the GPIO pin and set it to high or low to switch on or off the relay. For example, the script can be named relay.py and have the following content:

```python
# Import the GPIO library
import RPi.GPIO as GPIO

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that is connected to the relay
relay_pin = 17

# Set the relay pin as an output
GPIO.setup(relay_pin, GPIO.OUT)

# Set the relay pin to high to switch on the relay
GPIO.output(relay_pin, GPIO.HIGH)

# Clean up the GPIO pins
GPIO.cleanup()
```

  4. Make the script executable by running the command `chmod +x relay.py` in the terminal.
  5. Edit the crontab file by running the command `crontab -e` in the terminal. This will open the file in a text editor, where you can add a line to schedule the script to run at a given time. For example, to run the script every day at 8:00 AM, you can add the following line:

```bash
0 8 * * * /home/pi/relay.py
```

  6. Save and exit the crontab file. The script will run at the specified time and switch on the relay, which will in turn switch on the load.



#### c) Get the status of a bulb at a remote place (on the LAN) through web.

- To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

  - The bulb should be connected to a microcontroller that can communicate with the web server using HTTP protocol. The microcontroller should also have a sensor to detect the bulb's state (on or off).
  - The web server should have a web page that can display the bulb's status and send requests to the microcontroller to change the bulb's state. The web page should also have a refresh button to update the bulb's status periodically.
  - The user should access the web page using a web browser on a device that is connected to the same LAN as the microcontroller and the bulb. The user should be able to see the bulb's status and toggle it on or off by clicking on the web page.

- The following diagram illustrates the components and the data flow involved in this process:

```
  +----------------+        +----------------+        +----------------+
  |                |        |                |        |                |
  |     Bulb       |<------>|  Microcontroller  |<----->|    Web Server  |
  |                |        |                |        |                |
  +----------------+        +----------------+        +----------------+
                                   ^                          ^
                                   |                          |
                                   |                          |
                                   |                          |
                                   v                          v
                              +----------------+        +----------------+
                              |                |        |                |
                              |    Sensor      |        |    Web Page    |
                              |                |        |                |
                              +----------------+        +----------------+
                                                         ^
                                                         |
                                                         |
                                                         |
                                                         v
                                                   +----------------+
                                                   |                |
                                                   |    Web Browser |
                                                   |                |
                                                   +----------------+
```

- The following code snippets show an example of how to implement this functionality using Arduino and Node.js:

  - Arduino code for the microcontroller:

```c
// Include the libraries for the Ethernet shield and the sensor
#include <SPI.h>
#include <Ethernet.h>
#include <DHT.h>

// Define the pin for the sensor and the bulb
#define DHTPIN 2
#define BULBPIN 3

// Initialize the sensor
DHT dht(DHTPIN, DHT11);

// Initialize the Ethernet client
EthernetClient client;

// Define the IP address and the MAC address of the microcontroller
byte ip[] = { 192, 168, 1, 177 };
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

// Define the IP address and the port of the web server
byte server[] = { 192, 168, 1, 100 };
int port = 3000;

// Define a variable to store the bulb's state
int bulbState = 0;

void setup() {
  // Initialize the serial monitor
  Serial.begin(9600);

  // Initialize the Ethernet shield
  Ethernet.begin(mac, ip);

  // Initialize the sensor
  dht.begin();

  // Initialize the bulb pin as output
  pinMode(BULBPIN, OUTPUT);

  // Turn off the bulb initially
  digitalWrite(BULBPIN, LOW);
}

void loop() {
  // Check if the client is connected to the server
  if (client.connect(server, port)) {
    // Read the sensor data
    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();

    // Send a GET request to the server with the sensor data and the bulb state
    client.print("GET /?humidity=");
    client.print(humidity);
    client.print("&temperature=");
    client.print(temperature);
    client.print("&bulbState=");
    client.print(bulbState);
    client.println(" HTTP/1.1");
    client.println("Host: 192.168.1.100");
    client.println("Connection: close");
    client.println();

    // Wait for the server's response
    while (client.connected()) {
      // Read a line from the server
      String line = client.readStringUntil('\n');

      // Check if the line contains the command to change the bulb state
      if (line.startsWith("BULB:")) {
        // Get the new bulb state from the line
        int newBulbState = line.substring(5).toInt();

        // Check if the new bulb state is different from the current one
        if (newBulbState != bulbState) {
          // Update the bulb state
          bulbState = newBulbState;

          // Turn on or

```




#### Note: The Instructor may add/delete/modify/tune experiments

- This note indicates that the instructor has the authority and discretion to change the experiments that are part of the course syllabus or curriculum.
- The instructor may add new experiments, delete existing ones, modify the objectives, procedures, or outcomes of the experiments, or tune the parameters, settings, or equipment of the experiments.
- The instructor may do so for various reasons, such as to align the experiments with the latest developments in the field, to accommodate the availability of resources, to enhance the learning outcomes, or to address any feedback or issues.
- The note implies that the students should be flexible and adaptable to the changes in the experiments, and should follow the instructions and guidelines of the instructor accordingly.
- The note also suggests that the students should check the course website or communication channels regularly for any updates or announcements regarding the experiments.



# The topic is

- The topic is a general term for the subject or theme of a text, speech, or conversation.
- The topic can be expressed in different ways, such as a word, a phrase, a question, or a statement.
- The topic can be identified by looking for clues in the text, such as the title, the introduction, the main idea, the keywords, or the summary.
- The topic can be used to organize and structure the information in the text, such as by using headings, subheadings, paragraphs, or bullet points.
- The topic can be used to guide the research and writing process, such as by formulating a research question, a thesis statement, an outline, or a conclusion.
- The topic can be used to evaluate the relevance and quality of the text, such as by checking if the text answers the research question, supports the thesis statement, follows the outline, or summarizes the main points.



# The topic is

- The topic is a general term for the subject or theme of a text, speech, or conversation.
- A topic can be broad or narrow, depending on the scope and purpose of the communication.
- A topic can be expressed explicitly or implicitly, depending on the context and the audience.
- A topic can be derived from a question, a problem, a goal, an interest, or a curiosity.
- A topic can be related to other topics, forming a network of associations and connections.
- A topic can be developed and explored in various ways, such as by providing examples, evidence, arguments, opinions, facts, or perspectives.
- A topic can be organized and structured in various ways, such as by using headings, subheadings, paragraphs, bullet points, or outlines.
- A topic can be evaluated and revised in various ways, such as by checking for clarity, relevance, accuracy, completeness, coherence, and consistency.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have not specified the topic you want to write about. Please enter a topic in the following format:

# Topic: <your topic here>

For example:

# Topic: Nuclear fusion

I will then write the content in markdown format for you.



# KOT 552 INTERNET OF THINGS LAB KCS

- Internet of Things (IoT) is the concept of connecting physical devices, sensors, actuators, and other objects to the internet and enabling them to communicate and exchange data with each other.
- IoT has various applications in different domains, such as smart homes, smart cities, smart agriculture, smart healthcare, smart manufacturing, smart transportation, etc.
- IoT devices can collect, process, and transmit data using various protocols, such as MQTT, CoAP, HTTP, etc.
- IoT devices can also interact with cloud services, such as AWS IoT, Azure IoT, Google Cloud IoT, etc., to store, analyze, and visualize the data.
- IoT devices can also use edge computing, fog computing, or blockchain technologies to enhance their performance, security, and scalability.
- IoT devices can also leverage artificial intelligence, machine learning, and deep learning techniques to perform tasks such as object detection, face recognition, speech recognition, natural language processing, etc.

## Lab Objectives

- To understand the basic concepts and principles of IoT.
- To learn how to design, develop, and deploy IoT applications using various hardware and software platforms.
- To gain hands-on experience in using sensors, actuators, microcontrollers, communication modules, cloud services, and data analysis tools for IoT.
- To explore the challenges and opportunities of IoT in different domains and scenarios.

## Lab Outcomes

- After completing this lab, the students will be able to:
  - Explain the architecture, components, and protocols of IoT.
  - Identify and select appropriate hardware and software platforms for IoT applications.
  - Program and interface sensors, actuators, microcontrollers, and communication modules for IoT applications.
  - Connect and communicate IoT devices with cloud services and data analysis tools.
  - Develop and deploy IoT applications for various domains and scenarios.
  - Evaluate and compare the performance, security, and scalability of IoT applications.

## Lab Syllabus

- The lab syllabus consists of the following topics and experiments:

  - Introduction to IoT: Overview, architecture, components, protocols, applications, and challenges of IoT.
  - Hardware Platforms for IoT: Arduino, Raspberry Pi, ESP32, etc.
  - Software Platforms for IoT: Arduino IDE, Python, Node-RED, etc.
  - Sensors and Actuators for IoT: Temperature, humidity, light, motion, sound, etc.
  - Communication Modules for IoT: Bluetooth, Wi-Fi, LoRa, ZigBee, etc.
  - Protocols for IoT: MQTT, CoAP, HTTP, etc.
  - Cloud Services for IoT: AWS IoT, Azure IoT, Google Cloud IoT, etc.
  - Data Analysis Tools for IoT: ThingSpeak, Grafana, etc.
  - Artificial Intelligence for IoT: Object detection, face recognition, speech recognition, natural language processing, etc.
  - IoT Applications: Smart home, smart city, smart agriculture, smart healthcare, smart manufacturing, smart transportation, etc.

## Lab Evaluation

- The lab evaluation will be based on the following criteria:

  - Attendance and participation: 10%
  - Lab assignments and reports: 40%
  - Lab quizzes and tests: 20%
  - Lab project: 30%

## Lab References

: What is the Internet of Things? - KCS Technologies Inc. Knowledge Base
: DR. A.P.J. ABDUL KALAM TECHNICAL UNIVERSITY LUCKNOW Evaluation Scheme
: How the Internet of Things Is Affecting Laboratory Equipment



# Course Outcome (CO) Bloom's Knowledge Level (KL)

- Course Outcome (CO) is a statement that describes what a learner should be able to do at the end of a course or a unit of instruction.
- Bloom's Knowledge Level (KL) is a classification of cognitive skills that learners can demonstrate in relation to a given topic or domain.
- Bloom's Knowledge Level (KL) consists of six levels: remember, understand, apply, analyze, evaluate, and create. Each level represents a higher order of thinking and requires more complex cognitive processes than the previous one.
- Course Outcome (CO) can be aligned with Bloom's Knowledge Level (KL) to ensure that the learning objectives are clear, measurable, and appropriate for the level of the course or the unit of instruction.
- For example, a Course Outcome (CO) for a course on computer programming could be: "The learner will be able to design, implement, test, and debug a simple program using a high-level programming language." This CO can be mapped to the create level of Bloom's Knowledge Level (KL), as it involves synthesizing, generating, and producing a new product or artifact.
- Similarly, a Course Outcome (CO) for a course on history could be: "The learner will be able to compare and contrast the causes and effects of major historical events and movements." This CO can be mapped to the analyze level of Bloom's Knowledge Level (KL), as it involves breaking down, differentiating, and organizing information into parts and relationships.



# At the end of course, the student will be able to

- Define the basic concepts and principles of the subject matter.
- Apply the learned knowledge and skills to solve problems and perform tasks related to the course objectives.
- Analyze and evaluate information, arguments, and evidence from various sources and perspectives.
- Communicate effectively and appropriately in written and oral forms using the language and terminology of the discipline.
- Demonstrate ethical, professional, and social responsibility in academic and real-world contexts.
- Collaborate with others and work independently to achieve learning outcomes and goals.
- Reflect on their own learning process and progress and identify areas for improvement and further development.



# CO 1 Understand the concept of Internet of Things K3

- Internet of Things (IoT) is the interconnection of computing devices embedded in everyday objects, enabling them to send and receive data over the internet or other communications networks .
- IoT devices can range from sensors, actuators, cameras, smart phones, smart watches, smart home appliances, wearable devices, medical devices, industrial machines, vehicles, etc.
- IoT devices can communicate with each other, with other devices, with cloud services, or with humans, using various protocols and standards, such as Wi-Fi, Bluetooth, Zigbee, MQTT, HTTP, etc.
- IoT devices can collect, process, store, and analyze data from their environment, and perform actions based on the data or commands received.
- IoT devices can enable remote monitoring, control, automation, optimization, personalization, and intelligence of various applications and domains, such as smart cities, smart homes, smart health, smart agriculture, smart transportation, smart manufacturing, etc.
- IoT devices can also pose challenges and risks, such as security, privacy, interoperability, scalability, reliability, etc.



# CO2 Implement interfacing of various sensors with Arduino/Raspberry Pi

- CO2 sensors are devices that can measure the concentration of carbon dioxide in the air. They are useful for monitoring air quality, plant growth, and chemical reactions.
- There are different types of CO2 sensors available, such as electrochemical, infrared, and metal oxide sensors. Each type has its own advantages and disadvantages, such as accuracy, sensitivity, power consumption, and cost.
- To interface a CO2 sensor with an Arduino or a Raspberry Pi, you need to connect the sensor's output signal to one of the analog or digital input pins of the microcontroller. Depending on the type of sensor, you may also need to connect the sensor's power supply and ground pins to the microcontroller's 5V and GND pins, respectively.
- You also need to write a program that can read the sensor's output signal and convert it to a CO2 concentration value. The program may also perform some calibration, filtering, or averaging operations to improve the accuracy and stability of the measurement. The program can then display the CO2 value on a screen, store it on an SD card, or send it to another device via wireless communication.
- Some examples of CO2 sensors that can be interfaced with Arduino or Raspberry Pi are:

  - Gravity: Analog CO2 Gas Sensor (MG-811 Sensor): This is an electrochemical sensor that outputs a voltage that varies with the CO2 concentration. It has a potentiometer to adjust the threshold voltage and a Gravity interface to plug and play with Arduino. It is suitable for qualitative analysis and has a range of 0-10000 ppm.
  - DFRobot Gravity: Analog Infrared CO2 Sensor for Arduino (400~5000 ppm): This is an infrared sensor that uses a non-dispersive infrared (NDIR) technique to measure CO2. It has a high sensitivity, low power consumption, and long service life. It has a range of 400-5000 ppm and an accuracy of ±50 ppm or ±5% of reading.
  - Adafruit SCD-40 and SCD-41: These are NDIR sensors that use a photoacoustic technique to measure CO2. They have a high accuracy, low drift, and low noise. They also measure temperature and relative humidity. They have a range of 0-40000 ppm and an accuracy of ±(30 ppm + 3% of reading). They use I2C communication to interface with Arduino or Raspberry Pi.



# CO 3 Demonstrate the ability to transmit data wirelessly between different devices. K4

- Wireless data transmission is the process of sending and receiving data without using physical wires or cables.
- Wireless data transmission can be classified into two main types: radio frequency (RF) and optical.
- RF transmission uses electromagnetic waves to carry data through the air, such as Wi-Fi, Bluetooth, and cellular networks .
- Optical transmission uses light to send data, such as infrared, visible light, and laser .
- Some of the devices that use wireless data transmission are wireless phones, wireless adapters, wireless repeaters, and wireless routers .
- Some of the advantages of wireless data transmission are mobility, flexibility, scalability, and cost-effectiveness .
- Some of the challenges of wireless data transmission are interference, security, reliability, and power consumption .
- To demonstrate the ability to transmit data wirelessly between different devices, one should be able to:
  - Identify the types and modes of wireless transmission and communication .
  - Understand the principles and protocols of wireless networks .
  - Configure and troubleshoot wireless devices and connections .
  - Evaluate the performance and energy efficiency of wireless data transmission .



# CO 4 Show an ability to upload/download sensor data on cloud and server K2

- Sensor data is the information collected by various types of sensors that measure physical phenomena such as temperature, humidity, pressure, light, sound, motion, etc.
- Cloud and server are two types of platforms that can store and process sensor data remotely over the internet.
- Uploading sensor data means sending the data from the sensor device to the cloud or server platform, while downloading sensor data means receiving the data from the cloud or server platform to the sensor device or another device.
- To upload/download sensor data on cloud and server, the following steps are required:

  - **Step 1:** Choose a suitable cloud or server platform that can handle the sensor data according to the requirements of the project, such as data volume, frequency, format, security, etc. Some examples of cloud platforms are AWS, Azure, Google Cloud, ThingSpeak, etc. Some examples of server platforms are Apache, Nginx, Node.js, etc.
  - **Step 2:** Connect the sensor device to the internet using a wired or wireless connection, such as Ethernet, Wi-Fi, Bluetooth, cellular, satellite, etc. The connection should be reliable, fast, and secure enough to transmit the sensor data without loss or interference.
  - **Step 3:** Configure the sensor device to send the sensor data to the cloud or server platform using a specific protocol, such as HTTP, MQTT, CoAP, etc. The protocol should be compatible with both the sensor device and the cloud or server platform, and should support the data format, such as JSON, XML, CSV, etc.
  - **Step 4:** Configure the cloud or server platform to receive the sensor data from the sensor device and store it in a database, such as DynamoDB, MongoDB, MySQL, etc. The database should be able to handle the data volume, frequency, and format, and should provide features such as indexing, querying, filtering, etc.
  - **Step 5:** Configure the cloud or server platform to send the sensor data to the sensor device or another device using the same or a different protocol as in step 3. The protocol should be compatible with both the cloud or server platform and the sensor device or another device, and should support the data format, such as JSON, XML, CSV, etc.
  - **Step 6:** Configure the sensor device or another device to receive the sensor data from the cloud or server platform and display it on a user interface, such as a web page, a mobile app, a dashboard, etc. The user interface should be able to visualize the sensor data in a meaningful way, such as graphs, charts, tables, etc.

- Some examples of projects that upload/download sensor data on cloud and server are:

  - A weather station that uploads temperature and humidity data to AWS IoT and downloads the data to a web page that shows the current and historical weather conditions.
  - A smart home system that uploads motion and light data to Google Cloud and downloads the data to a mobile app that controls the lighting and security of the home.
  - A health monitor that uploads heart rate and blood pressure data to ThingSpeak and downloads the data to a dashboard that alerts the user of any abnormal readings.



# CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and is a standard language for manipulating and querying data in relational databases. MySQL is an open-source relational database management system that supports SQL. In this section, we will examine some of the basic and commonly used SQL queries from MySQL database.

## SQL Queries

A SQL query is an expression, similar to an English sentence, that defines the set of data to be retrieved from the database. You can think of a SQL query as a question you sent to the database; after that, you expect the database will respond to the question by sending back the data. The best way to learn SQL is by practicing with interactive SQL courses or online SQL editors.

The basic syntax of a SQL query is:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

The `SELECT` clause specifies which columns of data you want to retrieve from the table. You can use `*` to select all columns. The `FROM` clause specifies which table you want to query from. The `WHERE` clause specifies a condition that filters the rows of data. You can use logical operators such as `AND`, `OR`, and `NOT` to combine multiple conditions. You can also use comparison operators such as `=`, `<>`, `<`, `>`, `<=`, `>=`, `LIKE`, and `IN` to compare values. You can end a SQL query with a semicolon `;`.

For example, the following SQL query selects the name and age columns from the table `students` where the age is greater than 18.

```sql
SELECT name, age
FROM students
WHERE age > 18;
```

## Types of SQL Queries

There are different types of SQL queries based on the purpose and functionality. Some of the common types of SQL queries are:

- DDL (Data Definition Language): These are the queries that define the structure and schema of the database, such as creating, altering, renaming, dropping, and truncating tables. Some of the DDL commands are `CREATE`, `ALTER`, `RENAME`, `DROP`, and `TRUNCATE`.
- DML (Data Manipulation Language): These are the queries that manipulate the data in the database, such as inserting, updating, deleting, and selecting records. Some of the DML commands are `INSERT`, `UPDATE`, `DELETE`, and `SELECT`.
- DCL (Data Control Language): These are the queries that control the access and permissions of the database, such as granting and revoking privileges and roles. Some of the DCL commands are `GRANT` and `REVOKE`.
- TCL (Transaction Control Language): These are the queries that manage the transactions in the database, such as committing, rolling back, and saving changes. Some of the TCL commands are `COMMIT`, `ROLLBACK`, and `SAVEPOINT`.
- DQL (Data Query Language): These are the queries that query the data from the database, such as selecting, joining, grouping, and ordering data. Some of the DQL commands are `SELECT`, `JOIN`, `GROUP BY`, and `ORDER BY`.

## Examples of SQL Queries from MySQL Database

Here are some examples of SQL queries from MySQL database that demonstrate the different types of SQL queries.

- DDL: Create a table called `employees` with four columns: `id` (integer, primary key, auto-increment), `name` (varchar, not null), `salary` (decimal, not null), and `department` (varchar, not null).

```sql
CREATE TABLE employees (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  salary DECIMAL(10,2) NOT NULL,
  department VARCHAR(50) NOT NULL
);
```

- DML: Insert three records into the table `employees` with the following values: (1, 'Alice', 5000.00, 'Sales'), (2, 'Bob', 6000.00, 'Marketing'), and (3, 'Charlie', 7000.00, 'IT').

```sql
INSERT INTO employees (id, name, salary, department)
VALUES (1, 'Alice', 5000.00, 'Sales'),
       (2, 'Bob', 6000.00, 'Marketing'),
       (3, 'Charlie', 7000.00, 'IT');
```

- DCL: Grant the `SELECT` and `UPDATE` privileges on the table `employees` to the



# DETAILED SYLLABUS

- A detailed syllabus is a document that outlines the topics, objectives, learning outcomes, assessment methods, and resources for a specific course or module.
- A detailed syllabus can help students to understand the expectations and requirements of the course, as well as to plan their study time and activities accordingly.
- A detailed syllabus can also help instructors to design and deliver the course in a coherent and consistent way, as well as to communicate with students and other stakeholders about the course content and goals.
- A detailed syllabus typically includes the following sections:

  - Course title, code, credits, and prerequisites
  - Instructor name, contact information, office hours, and availability
  - Course description, objectives, and learning outcomes
  - Course format, schedule, and delivery mode
  - Course materials, such as textbooks, readings, software, and equipment
  - Course policies, such as attendance, participation, late submission, academic integrity, and grading
  - Course assessment, such as assignments, quizzes, exams, projects, and rubrics
  - Course resources, such as online platforms, support services, and references
  - Course calendar, such as weekly topics, readings, activities, and deadlines

- A detailed syllabus should be clear, concise, accurate, and updated. It should also be aligned with the course curriculum and the institutional standards and regulations. It should be distributed to the students at the beginning of the course and made available throughout the course. It should also be reviewed and revised periodically to reflect any changes or feedback.



# Using Various Sensors

- Sensors are devices that detect and measure physical phenomena, such as temperature, humidity, smoke, light, etc.
- Sensors can be used for various applications, such as monitoring environmental conditions, detecting hazards, controlling devices, etc.
- Sensors can be classified into different types based on their working principle, output signal, measurement range, accuracy, etc.
- Some common types of sensors are:

  - **Temperature sensors**: These sensors measure the heat or coldness of an object or environment. They can be based on different principles, such as thermocouples, thermistors, resistance temperature detectors, infrared thermometers, etc.
  - **Humidity sensors**: These sensors measure the amount of water vapor in the air or other gases. They can be based on different principles, such as capacitive, resistive, thermal, optical, etc.
  - **Smoke sensors**: These sensors detect the presence of smoke or fire in the environment. They can be based on different principles, such as ionization, photoelectric, infrared, etc.
  - **Light sensors**: These sensors measure the intensity or wavelength of light in the environment. They can be based on different principles, such as photodiodes, phototransistors, photovoltaic cells, etc.

- The student should have hands-on experience in using various sensors for the following reasons:

  - To understand the working principle and characteristics of different types of sensors.
  - To learn how to interface sensors with microcontrollers, computers, or other devices.
  - To develop skills in designing, testing, and troubleshooting sensor-based systems.
  - To explore the potential applications and challenges of using sensors in real-world scenarios.



# How to use control web camera, network, and relays connected to the Pi

- A web camera is a device that captures images or videos and sends them to a computer or a network. A web camera can be connected to the Pi using a USB cable or a wireless connection.
- A network is a system of devices that can communicate with each other using protocols and standards. A network can be wired or wireless, local or global, private or public. A network can be connected to the Pi using an Ethernet cable, a Wi-Fi adapter, or a Bluetooth module.
- A relay is a device that switches an electric circuit on or off by using an electromagnet. A relay can be used to control devices that require high voltage or current, such as motors, lights, or fans. A relay can be connected to the Pi using a GPIO pin, a transistor, and a diode.

To use control web camera, network, and relays connected to the Pi, you need to:

- Install the necessary software and drivers for the web camera, the network, and the relay on the Pi. You can use the `apt-get` command or the `raspi-config` tool to install the packages.
- Configure the settings for the web camera, the network, and the relay on the Pi. You can use the `raspi-config` tool, the `ifconfig` command, or the `crontab` command to configure the parameters.
- Write a program or a script to control the web camera, the network, and the relay on the Pi. You can use Python, C, or Bash to write the code. You can use the `picamera` module, the `socket` module, or the `RPi.GPIO` module to interact with the devices.
- Run the program or the script on the Pi. You can use the `python` command, the `gcc` command, or the `bash` command to execute the code. You can use the `ssh` command, the `scp` command, or the `VNC` tool to access the Pi remotely.



# Start Raspberry Pi and try various Linux commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small, affordable computer that can run various operating systems, such as Linux.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard, and a mouse. You also need to insert a microSD card with a Linux operating system installed on it.
- Once Raspberry Pi boots up, you will see a desktop environment or a command line interface, depending on the operating system you chose.
- To open a command terminal window, you can either click on the terminal icon on the desktop or press Ctrl+Alt+T on the keyboard.
- In the command terminal window, you can type various Linux commands to perform different tasks, such as navigating the file system, creating and deleting files, moving and renaming files, and getting help on commands.
- Here are some examples of Linux commands and their functions:

  - `ls`: This command lists the files and directories in the current working directory. You can use various options with this command, such as `-l` to show more details, `-a` to show hidden files, and `-h` to show human-readable file sizes.
  - `cd`: This command changes the current working directory to the one specified. You can use `.` to refer to the current directory, `..` to refer to the parent directory, and `~` to refer to the home directory. If you do not specify a directory, it will change to the home directory by default.
  - `touch`: This command creates a new, empty file with the name specified. If the file already exists, it updates its modification time to the current time.
  - `mv`: This command moves or renames a file or directory. You need to specify the source and the destination of the file or directory. If the destination is an existing directory, it will move the file or directory into it. If the destination is an existing file, it will overwrite it. If the destination does not exist, it will rename the file or directory to the destination name.
  - `rm`: This command removes or deletes a file or directory. You need to specify the name of the file or directory to remove. You can use various options with this command, such as `-r` to remove directories and their contents recursively, `-f` to force removal without prompting, and `-i` to prompt before each removal.
  - `man`: This command shows the manual page for a given command or topic. You can use the arrow keys or the space bar to scroll through the manual page, and press `q` to quit. You can also use `/` to search for a keyword in the manual page, and `n` to go to the next occurrence of the keyword.



# Linux Commands

## mkdir
- mkdir stands for make directory.
- It is used to create a new directory or folder in the current working directory or in a specified path.
- Syntax: `mkdir [options] directory_name`
- Example: `mkdir test` will create a folder named test in the current directory.
- Options: 
  - `-p` or `--parents` will create parent directories as needed.
  - `-v` or `--verbose` will print a message for each created directory.
  - `-m` or `--mode` will set the file mode (permissions) of the created directory.

## rmdir
- rmdir stands for remove directory.
- It is used to delete an empty directory or folder.
- Syntax: `rmdir [options] directory_name`
- Example: `rmdir test` will delete the folder named test if it is empty.
- Options: 
  - `-p` or `--parents` will remove directory and its ancestors.
  - `-v` or `--verbose` will print a message for each removed directory.
  - `--ignore-fail-on-non-empty` will ignore errors when trying to remove non-empty directories.

## tar
- tar stands for tape archive.
- It is used to create or extract compressed archive files that contain multiple files or directories.
- Syntax: `tar [options] [archive_file] [file_or_directory ...]`
- Example: `tar -czvf test.tar.gz test` will create a compressed archive file named test.tar.gz that contains the folder test and its contents.
- Options: 
  - `-c` or `--create` will create a new archive file.
  - `-x` or `--extract` or `--get` will extract files from an archive file.
  - `-z` or `--gzip` or `--gunzip` or `--ungzip` will use gzip compression or decompression.
  - `-v` or `--verbose` will print the names of the files being processed.
  - `-f` or `--file` will specify the name of the archive file.
  - `-t` or `--list` will list the contents of an archive file.

## gzip
- gzip stands for GNU zip.
- It is used to compress or decompress files using the Lempel-Ziv coding (LZ77) algorithm.
- Syntax: `gzip [options] [file ...]`
- Example: `gzip test.txt` will compress the file test.txt and rename it to test.txt.gz.
- Options: 
  - `-d` or `--decompress` or `--uncompress` will decompress the file.
  - `-k` or `--keep` will keep the original file and not delete it.
  - `-l` or `--list` will list the compressed file name, size, ratio, uncompressed size, and modification date.
  - `-r` or `--recursive` will recursively compress or decompress all files in a directory and its subdirectories.
  - `-t` or `--test` will test the integrity of the compressed file.

## cat
- cat stands for concatenate.
- It is used to display the contents of a file or multiple files, or to concatenate files and redirect the output to another file or device.
- Syntax: `cat [options] [file ...]`
- Example: `cat test.txt` will display the contents of test.txt on the standard output (screen).
- Options: 
  - `-b` or `--number-nonblank` will number the non-blank output lines.
  - `-n` or `--number` will number all the output lines.
  - `-s` or `--squeeze-blank` will suppress repeated empty output lines.
  - `-E` or `--show-ends` will display a $ at the end of each line.
  - `-T` or `--show-tabs` will display TAB characters as ^I.

## more
- more is a command that displays the contents of a file or multiple files one screen at a time.
- Syntax: `more [options] [file ...]`
- Example: `more test.txt` will display the contents of test.txt one screen at a time and wait for the user to press a key to continue or quit.
- Options: 
  - `-d` or `--silent` or `--quiet` will print a message instead of ringing the bell when an invalid key is pressed.
  - `-l` or `--logical` will count logical rather than screen lines.
  - `-p` or `--clean` or `--print-over` will not scroll the screen, but clear it and then display the text.



# 2. Run some python programs on Pi like:

- Python is a popular programming language that can be used to create various applications on Raspberry Pi, such as games, web servers, robots, etc.
- To run a python program on Pi, you need to have a text editor and a terminal window open.
- A text editor is a software that allows you to write and edit code. You can use any text editor you like, such as Thonny, IDLE, nano, etc.
- A terminal window is a software that allows you to execute commands and run programs on Pi. You can open a terminal window by clicking on the icon that looks like a black screen with a white cursor on the taskbar.
- To create a python program, you need to write your code in a text editor and save it with a .py extension, such as hello.py, game.py, etc.
- To run a python program, you need to open a terminal window and navigate to the directory where you saved your program using the cd command, such as cd Desktop, cd Documents, etc.
- Then, you need to type python followed by the name of your program, such as python hello.py, python game.py, etc. and press enter.
- The program will run and display the output on the terminal window. You can stop the program by pressing Ctrl+C on your keyboard.



# Read your name and print Hello message with name

- This is a simple program that takes the user's name as an input and prints a greeting message with the name.
- To read the user's name, we can use the `input()` function in Python, which returns a string value that the user enters.
- To print the greeting message, we can use the `print()` function in Python, which displays the value inside the parentheses to the standard output.
- To concatenate the greeting message and the user's name, we can use the `+` operator, which joins two strings together.
- Here is an example of the program:

```python
# Read the user's name
name = input("Enter your name: ")

# Print the greeting message with the name
print("Hello, " + name + "!")
```

- If the user enters `Alice`, the output will be:

```
Enter your name: Alice
Hello, Alice!
```



# b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the input() function in Python, which returns a string that can be converted to a numeric type such as int or float.
- To print the sum, difference, product and division of two numbers, we can use the arithmetic operators +, -, *, and / in Python, which perform the corresponding operations on the operands and return the result.
- To print the result, we can use the print() function in Python, which displays the value of the expression inside the parentheses to the standard output.
- For example, if we want to read two numbers x and y, and print their sum, difference, product and division, we can write the following code in Python:

```python
# Read two numbers from the user input and convert them to float
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

# Calculate and print the sum, difference, product and division of x and y
print("The sum of", x, "and", y, "is", x + y)
print("The difference of", x, "and", y, "is", x - y)
print("The product of", x, "and", y, "is", x * y)
print("The division of", x, "and", y, "is", x / y)
```

- The output of the code will depend on the values entered by the user. For example, if the user enters 10 and 5, the output will be:

```
Enter the first number: 10
Enter the second number: 5
The sum of 10.0 and 5.0 is 15.0
The difference of 10.0 and 5.0 is 5.0
The product of 10.0 and 5.0 is 50.0
The division of 10.0 and 5.0 is 2.0
```



# Word and character count of a given string

- A string is a sequence of characters, such as "Hello, world!" or "This is a sentence.".
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "world" or "sentence".
- A character is a single symbol, such as "H" or "!" or ".".
- To count the number of words and characters in a given string, we can use the following steps:

  - Initialize two variables, word_count and char_count, to zero.
  - Loop through each character in the string, and do the following:
    - Increment char_count by one, since each character adds to the character count.
    - If the character is a space or a punctuation mark, then increment word_count by one, since each space or punctuation mark indicates the end of a word.
    - If the character is the last one in the string, then increment word_count by one, since the last word does not have a space or a punctuation mark after it.
  - Return word_count and char_count as the final results.

- For example, given the string "Hello, world!", the word count is 2 and the character count is 13. The steps are as follows:

  - word_count = 0, char_count = 0
  - Loop through each character in "Hello, world!":
    - "H": char_count = 1, word_count = 0
    - "e": char_count = 2, word_count = 0
    - "l": char_count = 3, word_count = 0
    - "l": char_count = 4, word_count = 0
    - "o": char_count = 5, word_count = 0
    - ",": char_count = 6, word_count = 1 (end of a word)
    - " ": char_count = 7, word_count = 1
    - "w": char_count = 8, word_count = 1
    - "o": char_count = 9, word_count = 1
    - "r": char_count = 10, word_count = 1
    - "l": char_count = 11, word_count = 1
    - "d": char_count = 12, word_count = 1
    - "!": char_count = 13, word_count = 2 (end of a word and the last character)
  - Return word_count = 2 and char_count = 13



# Area of a given shape (rectangle, triangle and circle) reading shape and appropriate values from standard

- The area of a shape is the amount of space that it covers.
- Different shapes have different formulas for calculating their areas.
- To find the area of a given shape, we need to read the shape and the appropriate values from the standard input, and then apply the corresponding formula.

## Area of a rectangle

- A rectangle is a four-sided shape with opposite sides equal and right angles.
- To find the area of a rectangle, we need to read the length and the width from the standard input, and then multiply them.
- The formula for the area of a rectangle is:

    `Area = length * width`

- For example, if the length is 10 units and the width is 5 units, then the area is:

    `Area = 10 * 5 = 50 square units`

## Area of a triangle

- A triangle is a three-sided shape with three angles.
- To find the area of a triangle, we need to read the base and the height from the standard input, and then multiply them by half.
- The formula for the area of a triangle is:

    `Area = (base * height) / 2`

- For example, if the base is 12 units and the height is 9 units, then the area is:

    `Area = (12 * 9) / 2 = 54 square units`

## Area of a circle

- A circle is a shape with a curved boundary that is equidistant from a fixed point called the center.
- To find the area of a circle, we need to read the radius from the standard input, and then multiply it by itself and by a constant called pi.
- The formula for the area of a circle is:

    `Area = pi * radius * radius`

- Pi is an irrational number that is approximately equal to 3.14 or 22/7.
- For example, if the radius is 7 units, then the area is:

    `Area = 3.14 * 7 * 7 = 153.86 square units`



# Input

- Input is the process of receiving data or instructions from a user or another device.
- Input devices are hardware components that allow the user or the device to enter data or commands into a computer system.
- Examples of input devices are keyboard, mouse, microphone, scanner, webcam, barcode reader, etc.
- Input devices can be classified into different types based on their functionality, such as:
  - Text input devices: These devices allow the user to enter text or characters, such as keyboard, touch screen, stylus, etc.
  - Pointing input devices: These devices allow the user to control the cursor or pointer on the screen, such as mouse, trackball, touchpad, joystick, etc.
  - Audio input devices: These devices allow the user to record or transmit sound, such as microphone, headset, voice recognition software, etc.
  - Image input devices: These devices allow the user to capture or scan images, such as scanner, webcam, digital camera, etc.
  - Video input devices: These devices allow the user to record or stream video, such as webcam, camcorder, video capture card, etc.
  - Biometric input devices: These devices allow the user to authenticate or identify themselves using their physical or behavioral characteristics, such as fingerprint scanner, face recognition camera, iris scanner, etc.



# 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- To write a python program, you need to use a text editor such as nano, vim, or idle. You can launch a text editor by typing its name in the terminal, such as `nano` or `idle3`.
- To save a python program, you need to give it a name with a `.py` extension, such as `print_name.py`. You can save your program by pressing `Ctrl+O` in nano, or by choosing `File -> Save` in idle.
- To run a python program, you need to type `python3` followed by the name of your program, such as `python3 print_name.py`. You can run your program by pressing `Enter` in the terminal, or by choosing `Run -> Run Module` in idle.
- To print a name 'n' times, where name and n are read from standard input, you need to use the `input` function to get the user input, and the `print` function to display the output. You also need to use a `for` loop to repeat the print statement 'n' times. Here is an example of a python program that does this:

```python
# print_name.py
# This program prints a name 'n' times, where name and n are read from standard input

# Get the name from the user
name = input("Enter a name: ")

# Get the number of times to print from the user
n = int(input("Enter a number: "))

# Use a for loop to print the name 'n' times
for i in range(n):
    print(name)
```

- To test your program, you can run it and enter some values for name and n, such as `Alice` and `5`. You should see the output like this:

```
Enter a name: Alice
Enter a number: 5
Alice
Alice
Alice
Alice
Alice
```



# Using for and while loops

- A for loop is a repetition control structure that allows you to efficiently write a loop that needs to execute a specific number of times.
- A while loop is a repetition control structure that allows you to write a loop that will repeat as long as a condition is true.
- The syntax of a for loop is:

```python
for variable in range(start, end, step):
    # loop body
```

- The syntax of a while loop is:

```python
while condition:
    # loop body
```

- To handle a divided by zero exception, you can use a try-except block that catches the ZeroDivisionError and handles it gracefully.
- The syntax of a try-except block is:

```python
try:
    # code that may raise an exception
except ZeroDivisionError:
    # code that handles the exception
```

- To print the current time for 10 times with an interval of 5 seconds, you can use the datetime module to get the current time and the time module to pause the execution.
- The code for this task is:

```python
import datetime
import time

# loop 10 times
for i in range(10):
    # get the current time
    now = datetime.datetime.now()
    # print the time in a formatted way
    print(now.strftime("%H:%M:%S"))
    # pause for 5 seconds
    time.sleep(5)
```



# How to read a file line by line and print the word count of each line

- To read a file line by line, we can use a loop with the `readline()` method of the file object.
- The `readline()` method returns a string containing one line of the file, or an empty string if the end of the file is reached.
- To print the word count of each line, we can use the `split()` method of the string object, which returns a list of words separated by whitespace characters.
- The `len()` function can be used to get the number of elements in a list, which is equal to the word count of the line.
- We can use a variable to keep track of the line number, and increment it by one in each iteration of the loop.
- We can use the `format()` method of the string object to print the line number and the word count in a formatted way.
- Here is an example of the code in Python:

```python
# Open the file in read mode
file = open("example.txt", "r")

# Initialize the line number
line_number = 1

# Loop through the file line by line
while True:
  # Read one line of the file
  line = file.readline()

  # Break the loop if the end of the file is reached
  if line == "":
    break

  # Split the line into words
  words = line.split()

  # Get the word count of the line
  word_count = len(words)

  # Print the line number and the word count
  print("Line {}: {} words".format(line_number, word_count))

  # Increment the line number
  line_number += 1

# Close the file
file.close()
```



# 4. a) Light an LED through Python program

- To light an LED through Python program, you need to have a hardware device that can control the LED, such as an Arduino, a Raspberry Pi, or a MicroPython board.
- You also need to connect the LED to the device using wires, resistors, and a breadboard, following the appropriate circuit diagram for your device.
- You need to install Python and the necessary libraries on your computer and on your device, such as pyserial, RPi.GPIO, or pyb.
- You need to write a Python program that can communicate with your device and send commands to turn the LED on and off.
- You need to upload the Python program to your device or run it from your computer, depending on your device and configuration.
- You need to test your program and observe the LED blinking or changing colors, according to your program logic.

## Example: Light an LED with Raspberry Pi and Python

- Connect the LED to the Raspberry Pi using a 330 ohm resistor, a breadboard, and jumper wires. Connect the anode (longer leg) of the LED to GPIO pin 18 of the Raspberry Pi, and the cathode (shorter leg) to the ground (GND) pin.
- Install Python and the RPi.GPIO library on your Raspberry Pi, following the instructions from https://sourceforge.net/p/raspberry-gpio-python/wiki/install/.
- Write a Python program that can control the LED using the RPi.GPIO library. For example, save the following code as LED.py:

```python
import RPi.GPIO as GPIO # Import the library
import time # Import the time module

GPIO.setmode(GPIO.BCM) # Set the numbering scheme to BCM
GPIO.setup(18, GPIO.OUT) # Set pin 18 as an output pin

while True: # Loop forever
    GPIO.output(18, GPIO.HIGH) # Turn on the LED
    time.sleep(1) # Wait for 1 second
    GPIO.output(18, GPIO.LOW) # Turn off the LED
    time.sleep(1) # Wait for 1 second
```

- Run the Python program from the Raspberry Pi terminal using the command: `sudo python LED.py`
- You should see the LED blinking on and off once every second. To stop the program, press Ctrl+C.



# Get input from two switches and switch on corresponding LEDs

- This topic is about how to use two switches and two LEDs to create a simple logic circuit.
- A switch is a device that can open or close an electrical circuit, allowing current to flow or stop.
- An LED (light-emitting diode) is a device that emits light when current passes through it.
- To get input from two switches and switch on corresponding LEDs, we need to connect them in a certain way using wires, resistors, and a power source.
- The following diagram shows one possible way to connect the switches and LEDs:

```
    +V
    |
    R
    |
    o----o S1 o----o LED1 o----o
    |    |    |    |      |    |
    |    |    |    R      |    |
    |    |    |    |      |    |
    o----o S2 o----o LED2 o----o
    |    |    |    |      |    |
    |    |    |    R      |    |
    |    |    |    |      |    |
    o----o----o----o----o GND
```

- In this diagram, +V is the positive terminal of the power source, GND is the ground or negative terminal, R is a resistor, S1 and S2 are switches, and LED1 and LED2 are LEDs.
- The o symbols represent the nodes or junctions where wires are connected.
- The switches and LEDs are connected in parallel, meaning they have two common nodes each.
- The resistors are connected in series with the LEDs, meaning they have one common node each.
- The resistors limit the current flowing through the LEDs, preventing them from burning out.
- The switches control the current flowing through the LEDs, turning them on or off.
- When a switch is closed, it creates a closed circuit, allowing current to flow from +V to GND through the resistor and the LED.
- When a switch is open, it creates an open circuit, stopping current from flowing through the resistor and the LED.
- The following table shows the possible states of the switches and LEDs:

| S1 | S2 | LED1 | LED2 |
|----|----|------|------|
| Open | Open | Off | Off |
| Open | Closed | Off | On |
| Closed | Open | On | Off |
| Closed | Closed | On | On |

- This table shows that the LEDs are switched on corresponding to the switches, meaning LED1 is on when S1 is closed, and LED2 is on when S2 is closed.
- This logic circuit can be used to demonstrate the concept of Boolean algebra, where switches represent binary variables (0 or 1), and LEDs represent logical outputs (false or true).
- For example, the table can be interpreted as:

| S1 | S2 | LED1 | LED2 |
|----|----|------|------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 |

- This means that LED1 is equal to S1, and LED2 is equal to S2, in terms of Boolean logic.
- This logic circuit can also be used to create different logic functions, such as AND, OR, XOR, etc., by changing the way the switches and LEDs are connected.
- For example, the following diagram shows how to create an AND function, where LED1 is on only when both S1 and S2 are closed:

```
    +V
    |
    R
    |
    o----o S1 o----o
    |    |    |    |
    |    |    |    R
    |    |    |    |
    o----o S2 o----o LED1 o----o
    |    |    |    |      |    |
    |    |    |    R      |    |
    |    |    |    |      |    |
    o----o----o----o----o GND
```

- The following table shows the states of the switches and LED1 for the AND function:

| S1 | S2 | LED1 |
|----|----|------|
| Open | Open | Off |
| Open | Closed | Off |
| Closed | Open | Off |
| Closed | Closed | On |

- This means that LED1 is equal to S1 AND S2, in terms of Boolean logic.



# Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, some wires, and a file that contains the on time and off time values in milliseconds.
- The microcontroller is a device that can execute a program that controls the output pins. We can use any microcontroller that supports digital output, such as Arduino, Raspberry Pi, or ESP32.
- The LED is a light-emitting diode that can turn on or off depending on the voltage applied to its terminals. We need to connect the LED to one of the output pins of the microcontroller through a resistor, which limits the current and protects the LED from burning out.
- The breadboard is a board that allows us to make temporary connections between components without soldering. We can use the breadboard to connect the microcontroller, the LED, the resistor, and the wires.
- The wires are used to connect the components on the breadboard. We need to use different colors of wires to distinguish the positive and negative terminals of the LED and the microcontroller.
- The file is a text file that contains two numbers separated by a comma, which represent the on time and off time of the LED in milliseconds. For example, the file could contain "500, 1000", which means the LED should be on for 500 milliseconds and off for 1000 milliseconds. We need to store the file in the same folder as the program that we will write for the microcontroller.
- The program is a set of instructions that tells the microcontroller what to do. We need to write the program in a language that the microcontroller can understand, such as C, Python, or Arduino. The program should do the following steps:

  - Initialize the output pin that is connected to the LED and set it to low (off) state.
  - Open the file that contains the on time and off time values and read them into two variables.
  - Start a loop that repeats indefinitely.
  - Set the output pin to high (on) state and wait for the on time duration.
  - Set the output pin to low (off) state and wait for the off time duration.
  - End the loop.

- The following is an example of the program written in Arduino language, which is based on C. The program assumes that the LED is connected to pin 13, and the file is named "times.txt".

```c
// Define the output pin
#define LED_PIN 13

// Define the file name
#define FILE_NAME "times.txt"

// Declare the variables for on time and off time
int onTime;
int offTime;

// Declare the file object
File file;

void setup() {
  // Initialize the output pin and set it to low
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  // Initialize the serial communication
  Serial.begin(9600);

  // Initialize the SD card
  if (!SD.begin()) {
    // If the SD card is not detected, print an error message and stop the program
    Serial.println("SD card initialization failed");
    while (true);
  }

  // Open the file
  file = SD.open(FILE_NAME);

  // If the file is not found, print an error message and stop the program
  if (!file) {
    Serial.println("File not found");
    while (true);
  }

  // Read the on time and off time values from the file
  onTime = file.parseInt();
  offTime = file.parseInt();

  // Close the file
  file.close();

  // Print the on time and off time values
  Serial.print("On time: ");
  Serial.println(onTime);
  Serial.print("Off time: ");
  Serial.println(offTime);
}

void loop() {
  // Set the output pin to high and wait for the on time duration
  digitalWrite(LED_PIN, HIGH);
  delay(onTime);

  // Set the output pin to low and wait for the off time duration
  digitalWrite(LED_PIN, LOW);
  delay(offTime);
}
```



# Flash an LED based on cron output (acts as an alarm)

- Cron is a software utility that allows users to schedule tasks to run periodically at fixed times, dates, or intervals.
- An LED (light-emitting diode) is a semiconductor device that emits light when an electric current passes through it.
- To flash an LED based on cron output, we need to connect an LED to a GPIO (general-purpose input/output) pin of a microcontroller or a single-board computer, such as Raspberry Pi, Arduino, or ESP32.
- We also need to write a script that can control the LED by setting the GPIO pin to high or low voltage levels, and make it executable by using the `chmod` command.
- Then, we need to edit the crontab file by using the `crontab -e` command, and add a line that specifies when and how often we want to run the script, and the path to the script.
- For example, if we want to flash the LED every minute for 10 seconds, we can add the following line to the crontab file:

`* * * * * /home/pi/flash_led.sh`

- Where `/home/pi/flash_led.sh` is the path to the script that controls the LED.
- The script can be written in any programming language that can access the GPIO pins, such as Python, C, or Bash.
- For example, in Python, the script can look something like this:

```python
import RPi.GPIO as GPIO # Import the GPIO library
import time # Import the time library

GPIO.setmode(GPIO.BCM) # Set the GPIO mode to BCM
GPIO.setwarnings(False) # Disable warnings
LED_PIN = 17 # Set the LED pin number
GPIO.setup(LED_PIN, GPIO.OUT) # Set the LED pin as output

GPIO.output(LED_PIN, GPIO.HIGH) # Turn on the LED
time.sleep(10) # Wait for 10 seconds
GPIO.output(LED_PIN, GPIO.LOW) # Turn off the LED
GPIO.cleanup() # Clean up the GPIO pins
```

- This script will turn on the LED connected to pin 17 for 10 seconds, and then turn it off.
- The script can be modified to flash the LED in different patterns, such as blinking, fading, or pulsing, by using loops and PWM (pulse-width modulation) techniques.
- The crontab file can be modified to run the script at different times, such as every hour, every day, every week, or every month, by using different cron expressions.
- For example, to run the script every hour at 15 minutes past the hour, we can use the following cron expression:

`15 * * * * /home/pi/flash_led.sh`

- To run the script every day at 8:00 AM, we can use the following cron expression:

`0 8 * * * /home/pi/flash_led.sh`

- To run the script every Monday at 9:30 AM, we can use the following cron expression:

`30 9 * * 1 /home/pi/flash_led.sh`

- To run the script on the first day of every month at 10:00 AM, we can use the following cron expression:

`0 10 1 * * /home/pi/flash_led.sh`

- To learn more about cron expressions, we can use online tools such as [Crontab Guru](https://crontab.guru/) or [Cron Expression Generator](https://www.freeformatter.com/cron-expression-generator-quartz.html).
- By flashing an LED based on cron output, we can create a simple alarm system that can remind us of important events, such as taking medication, watering plants, or checking emails.



# Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

- A relay is an electromechanical device that can be used to switch on or off a load (such as a light bulb, a fan, a motor, etc.) by applying a voltage to its coil terminals.
- A cron is a software utility that can be used to schedule tasks to run at a specified time or interval on a Linux-based system.
- To switch on a relay at a given time using cron, the following steps are required:

  1. Connect the relay's coil terminals to a GPIO (General Purpose Input Output) pin and a ground pin of a microcontroller (such as a Raspberry Pi, an Arduino, etc.) that can run Linux.
  2. Connect the relay's contact terminals to the load and a power source (such as a battery, a wall outlet, etc.) according to the relay's specifications and the load's requirements.
  3. Write a script (such as a Python script, a Bash script, etc.) that can control the GPIO pin to switch on the relay by setting it to high (or low, depending on the relay's type) and switch off the relay by setting it to low (or high, depending on the relay's type).
  4. Test the script to make sure it can switch on and off the relay and the load as expected.
  5. Use the `crontab -e` command to edit the cron table and add a line that specifies the time and the script to run. For example, if the script is named `relay_on.py` and is located in the home directory, and the desired time to switch on the relay is 8:00 AM every day, the line would be:

     ```
     0 8 * * * python /home/relay_on.py
     ```

  6. Save and exit the cron table. The cron daemon will automatically run the script at the specified time and switch on the relay and the load.



# Get the status of a bulb at a remote place (on the LAN) through web

- To get the status of a bulb at a remote place (on the LAN) through web, we need to have the following components:
  - A bulb that can be controlled by a microcontroller such as Arduino or Raspberry Pi.
  - A microcontroller that can connect to the LAN and run a web server.
  - A device that can access the web server and send requests to the microcontroller.
- The steps to get the status of a bulb are as follows:
  - Connect the bulb to the microcontroller using a relay or a transistor circuit.
  - Connect the microcontroller to the LAN using an Ethernet shield or a Wi-Fi module.
  - Write a sketch or a program for the microcontroller that can read the state of the bulb (on or off) and send it as a response to a web request.
  - Upload the sketch or the program to the microcontroller and run it.
  - Find the IP address of the microcontroller on the LAN using a network scanner or a ping command.
  - On the device that can access the web server, open a web browser and enter the IP address of the microcontroller followed by a slash and a query parameter, such as `http://192.168.1.100/?status`.
  - The web browser will send a request to the microcontroller and receive a response that contains the status of the bulb, such as `on` or `off`.
  - The web browser will display the response on the screen.



# Note: The Instructor may add/delete/modify/tune experiments

- This note implies that the instructor has the authority and flexibility to design the experiments according to the course objectives, the availability of resources, and the level of difficulty.
- The instructor may add new experiments to cover topics that are not included in the existing ones, or to provide more practice or challenge for the students.
- The instructor may delete experiments that are redundant, outdated, or irrelevant to the course content, or that are too easy or too hard for the students.
- The instructor may modify or tune experiments to adjust the parameters, the instructions, the expected outcomes, or the evaluation criteria, to make them more suitable, clear, realistic, or fair.
- The instructor should inform the students about any changes in the experiments before they start working on them, and explain the reasons and the expectations behind the changes.
- The instructor should also provide feedback and guidance to the students throughout the experiments, and assess their performance and learning outcomes.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn about. You have chosen the topic:

# The topic is

- The topic is a general term for the subject or theme of a text, speech, or conversation.
- The topic can be expressed in different ways, such as a word, a phrase, a question, or a statement.
- The topic can be explicit or implicit, depending on how clearly it is stated or implied by the speaker or writer.
- The topic can be broad or narrow, depending on how much detail or scope it covers.
- The topic can be related to different fields or disciplines, such as science, history, literature, or art.
- The topic can be informative or persuasive, depending on the purpose or goal of the communication.
- The topic can be interesting or boring, depending on the personal preference or relevance of the audience.

Some examples of topics are:

- How does photosynthesis work?
- The causes and effects of climate change.
- The life and works of William Shakespeare.
- The advantages and disadvantages of social media.
- Why do we dream?
- How to write a good essay.

To learn more about a topic, you can:

- Do some research on reliable sources, such as books, journals, websites, or podcasts.
- Take notes of the main ideas, facts, arguments, or examples related to the topic.
- Organize your notes into an outline or a mind map.
- Review your notes and summarize the key points or questions about the topic.
- Discuss the topic with others who have different perspectives or opinions.
- Apply the topic to your own experience or situation.



# KOT 552 INTERNET OF THINGS LAB KCS

- Internet of Things (IoT) is the concept of connecting physical devices, sensors, actuators, and other objects to the internet and enabling them to communicate and exchange data with each other.
- IoT has various applications in different domains, such as smart homes, smart cities, smart agriculture, smart healthcare, smart manufacturing, smart transportation, etc.
- IoT devices can collect, process, and transmit data using various protocols, such as MQTT, CoAP, HTTP, etc.
- IoT devices can also interact with cloud services, such as AWS IoT, Azure IoT, Google Cloud IoT, etc., to store, analyze, and visualize the data.
- IoT devices can also use edge computing, fog computing, or blockchain technologies to enhance the performance, security, and scalability of the IoT system.
- IoT devices can be programmed using various languages, such as Python, C, Java, etc., and various platforms, such as Arduino, Raspberry Pi, NodeMCU, etc.
- IoT lab is a course that aims to provide hands-on experience and practical skills to the students on designing, developing, and testing IoT applications using various hardware and software tools.
- IoT lab consists of various experiments, such as:
  - Setting up and configuring IoT devices and sensors
  - Establishing wireless communication between IoT devices and the internet
  - Sending and receiving data from IoT devices to cloud services
  - Implementing IoT protocols and standards
  - Developing IoT applications using various programming languages and platforms
  - Analyzing and visualizing IoT data using various tools
  - Securing and optimizing IoT systems
- IoT lab also involves project work, where the students have to design and implement an IoT solution for a real-world problem or scenario.
- IoT lab helps the students to gain theoretical and practical knowledge of IoT concepts, technologies, and applications, and to develop their creativity, problem-solving, and teamwork skills.



## Course Outcome (CO) Bloom's Knowledge Level (KL)

- Course outcome (CO) is a statement that describes what students are expected to know, understand, or be able to do at the end of a course.
- Bloom's knowledge level (KL) is a classification of cognitive skills that students can demonstrate in relation to a given topic or domain.
- Bloom's taxonomy consists of six levels of knowledge: remember, understand, apply, analyze, evaluate, and create.
- Each level of knowledge requires a different type of cognitive process and has a different degree of complexity and difficulty.
- The higher the level of knowledge, the more challenging and sophisticated the learning outcome is.
- Course outcomes should be aligned with the appropriate level of knowledge that matches the course objectives and the intended learning experiences.
- Course outcomes should also be measurable, observable, and achievable by the students within the duration of the course.
- Course outcomes should be written using action verbs that indicate the level of knowledge and the cognitive process involved.
- For example, a course outcome that requires students to remember factual information can use verbs such as define, list, recall, identify, etc.
- A course outcome that requires students to apply concepts or principles can use verbs such as solve, demonstrate, perform, implement, etc.
- A course outcome that requires students to create original products or solutions can use verbs such as design, construct, compose, synthesize, etc.
- The following table shows some examples of course outcomes and their corresponding level of knowledge:

| Course Outcome | Level of Knowledge |
| -------------- | ------------------ |
| Define the key terms and concepts of computer science. | Remember |
| Explain the basic functions and components of a computer system. | Understand |
| Write a simple program using a programming language. | Apply |
| Compare and contrast different programming paradigms and languages. | Analyze |
| Evaluate the quality and efficiency of a program using various criteria and tools. | Evaluate |
| Design and develop a software project that meets the user requirements and specifications. | Create |



### At the end of the course, the student will be able to

- Demonstrate an understanding of the basic concepts and principles of the subject matter.
- Apply the acquired knowledge and skills to solve problems and perform tasks related to the course objectives.
- Analyze and evaluate information, arguments, and evidence from various sources and perspectives.
- Communicate effectively and appropriately in written and oral forms using the language and terminology of the discipline.
- Collaborate with others in a respectful and constructive manner to achieve common goals.
- Reflect on their own learning process and outcomes and identify areas for improvement and further development.



#### CO 1 Understand the concept of Internet of Things K3

- Internet of Things (IoT) is the interconnection of computing devices embedded in everyday objects, enabling them to send and receive data over the internet or other communications networks .
- IoT devices can range from simple sensors and actuators to complex smart appliances and wearable devices that can monitor, control, and automate various aspects of our lives.
- IoT devices can communicate with each other, with cloud services, or with human users through various protocols and platforms, such as Wi-Fi, Bluetooth, Zigbee, MQTT, CoAP, etc.
- IoT devices can generate and process large amounts of data, which can be used for various purposes, such as improving efficiency, enhancing security, providing insights, creating new services, etc.
- IoT devices can also pose challenges and risks, such as privacy, security, interoperability, scalability, reliability, etc.
- IoT is a multidisciplinary field that involves various technologies, such as embedded systems, wireless communications, cloud computing, data analytics, artificial intelligence, etc.
- IoT is a rapidly evolving and expanding domain that has applications in various sectors, such as smart homes, smart cities, smart agriculture, smart healthcare, smart manufacturing, smart transportation, etc.



#### CO 2 Implement interfacing of various sensors with Arduino/Raspberry Pi K4, K5

- CO2 sensors are devices that can measure the concentration of carbon dioxide in the air. They are useful for monitoring air quality, plant growth, fermentation, and other applications.
- There are different types of CO2 sensors, such as electrochemical, infrared, and metal oxide. Each type has its own advantages and disadvantages, such as accuracy, sensitivity, power consumption, and cost.
- Arduino and Raspberry Pi are popular platforms for interfacing with various sensors, including CO2 sensors. They are microcontrollers that can read analog or digital signals from sensors, process them, and communicate with other devices or computers.
- To interface a CO2 sensor with Arduino or Raspberry Pi, the following steps are required:

  - Choose a suitable CO2 sensor for your project. Some factors to consider are the range, resolution, response time, output type, and calibration method of the sensor. For example, the MG-811 sensor is an analog CO2 sensor that can measure from 0 to 10000 ppm with a resolution of 10 ppm. The SCD-30 sensor is a digital CO2 sensor that can measure from 400 to 10000 ppm with a resolution of 30 ppm, and also provides temperature and humidity readings.
  - Connect the CO2 sensor to the Arduino or Raspberry Pi according to the wiring diagram of the sensor. Some sensors may require additional components, such as resistors, capacitors, or voltage regulators, to work properly. For example, the MG-811 sensor needs a 6 V power supply, which can be obtained from a voltage divider or a boost converter. The SCD-30 sensor uses the I2C protocol, which requires pull-up resistors on the data and clock lines.
  - Install the library or driver for the CO2 sensor, if available. Some sensors have dedicated libraries or drivers that make it easier to communicate with them and access their features. For example, the Adafruit SCD-30 library provides functions to read the CO2, temperature, and humidity values, as well as to set the altitude, pressure, and calibration parameters.
  - Write the code to read the CO2 sensor data and perform the desired actions. Depending on the output type of the sensor, the code may vary. For example, the MG-811 sensor outputs an analog voltage that needs to be converted to a CO2 concentration using a formula or a lookup table. The SCD-30 sensor outputs a digital value that can be directly read using the I2C protocol.
  - Test and debug the code and the sensor. Make sure the sensor is working correctly and the code is producing the expected results. Some sensors may need to be calibrated or adjusted for different environmental conditions, such as temperature, pressure, or humidity. For example, the MG-811 sensor needs to be calibrated in fresh air before use, and the SCD-30 sensor can be calibrated using a known CO2 concentration or a self-calibration mode .



#### CO 3 Demonstrate the ability to transmit data wirelessly between different devices. K4

- Wireless data transmission is the process of sending and receiving data without using physical wires or cables.
- Wireless data transmission can be classified into two main types: radio frequency (RF) and optical.
- RF transmission uses electromagnetic waves to carry data through the air, such as Wi-Fi, Bluetooth, and cellular networks .
- Optical transmission uses light to send data, such as infrared, visible light, and laser .
- Wireless data transmission has advantages such as mobility, convenience, scalability, and cost-effectiveness, but also disadvantages such as interference, security, and power consumption.
- To transmit data wirelessly between different devices, the following steps are required:
  - Choose a suitable wireless transmission method and medium based on the data rate, distance, bandwidth, and environment.
  - Configure the devices to use the same wireless protocol, frequency, channel, and encryption settings.
  - Establish a wireless connection between the devices using a pairing process, a network name, or a password.
  - Send and receive data using the wireless connection, and monitor the signal strength, quality, and speed.
  - Terminate the wireless connection when the data transmission is completed or no longer needed.
- Some examples of wireless devices that can transmit data wirelessly are wireless phones, wireless adapters, wireless repeaters, wireless routers, and wireless sensors  .



#### CO 4 Show an ability to upload/download sensor data on cloud and server K2

- Sensor data is the information collected by various types of sensors that measure physical phenomena such as temperature, humidity, pressure, light, sound, motion, etc.
- Cloud and server are two types of computing platforms that can store, process, and analyze sensor data remotely over the internet.
- Cloud is a network of servers that provide on-demand computing resources and services such as storage, databases, analytics, etc. Server is a single computer that hosts a specific application or service such as a web server, a database server, etc.
- To upload sensor data to cloud or server, the sensor device needs to have a network connection such as Wi-Fi, Ethernet, cellular, satellite, etc. and a protocol such as HTTP, MQTT, CoAP, etc. that defines how the data is formatted and transmitted.
- To download sensor data from cloud or server, the sensor device or another device such as a computer or a smartphone needs to have a network connection and a protocol that allows requesting and receiving data from the cloud or server.
- Some examples of cloud platforms that can store and analyze sensor data are AWS IoT, Azure IoT, Google Cloud IoT, ThingSpeak, etc. Some examples of servers that can host sensor data applications are Apache, MySQL, MongoDB, Node.js, etc.
- Some benefits of uploading and downloading sensor data to cloud or server are:
  - Scalability: Cloud and server can handle large and variable amounts of sensor data without requiring additional hardware or maintenance.
  - Accessibility: Cloud and server can make sensor data available to multiple devices and users across different locations and time zones.
  - Security: Cloud and server can protect sensor data from unauthorized access and loss using encryption, authentication, backup, etc.
  - Analytics: Cloud and server can perform complex and real-time analysis of sensor data using various tools and techniques such as machine learning, artificial intelligence, data visualization, etc.



#### CO 5 Examine various SQL queries from MySQL database K4, K5

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- MySQL is one of the most popular open-source relational database management systems (RDBMS) that supports SQL.
- SQL queries are statements that specify what data to retrieve, insert, update, or delete from a database.
- SQL queries can be classified into four categories: Data Definition Language (DDL), Data Manipulation Language (DML), Data Query Language (DQL), and Data Control Language (DCL).
- DDL is used to define the structure and schema of the database, such as creating, altering, or dropping tables, indexes, views, etc.
- DML is used to manipulate the data in the database, such as inserting, updating, or deleting records, etc.
- DQL is used to query the data in the database, such as selecting, joining, filtering, sorting, grouping, etc.
- DCL is used to control the access and permissions of the database, such as granting, revoking, or denying privileges, roles, etc.
- Some examples of SQL queries from MySQL database are:

  - To create a table named `students` with four columns: `id`, `name`, `age`, and `grade`:

    ```sql
    CREATE TABLE students (
      id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      age INT,
      grade CHAR(1)
    );
    ```

  - To insert a record into the `students` table with values: `1`, `Alice`, `18`, and `A`:

    ```sql
    INSERT INTO students (id, name, age, grade) VALUES (1, 'Alice', 18, 'A');
    ```

  - To select all the records from the `students` table:

    ```sql
    SELECT * FROM students;
    ```

  - To select only the `name` and `grade` columns from the `students` table where the `age` is greater than or equal to `20`:

    ```sql
    SELECT name, grade FROM students WHERE age >= 20;
    ```

  - To update the `grade` column of the `students` table to `B` where the `id` is `1`:

    ```sql
    UPDATE students SET grade = 'B' WHERE id = 1;
    ```

  - To delete the record from the `students` table where the `id` is `1`:

    ```sql
    DELETE FROM students WHERE id = 1;
    ```

  - To create a view named `top_students` that contains the `name` and `grade` columns of the `students` table where the `grade` is `A`:

    ```sql
    CREATE VIEW top_students AS
    SELECT name, grade FROM students WHERE grade = 'A';
    ```

  - To grant the `SELECT` privilege on the `students` table to the user `bob`:

    ```sql
    GRANT SELECT ON students TO bob;
    ```

  - To revoke the `SELECT` privilege on the `students` table from the user `bob`:

    ```sql
    REVOKE SELECT ON students FROM bob;
    ```

  - To deny the `DELETE` privilege on the `students` table to the user `bob`:

    ```sql
    DENY DELETE ON students TO bob;
    ```



## DETAILED SYLLABUS

- A detailed syllabus is a document that outlines the topics, objectives, learning outcomes, assessment methods, and resources for a specific course or module.
- A detailed syllabus can help students to understand the expectations and requirements of the course, as well as to plan their study time and activities accordingly.
- A detailed syllabus can also help instructors to design and deliver the course in a coherent and consistent way, as well as to communicate with students and other stakeholders about the course content and goals.
- A detailed syllabus typically includes the following sections:

  - Course title, code, credits, and prerequisites
  - Instructor name, contact information, office hours, and availability
  - Course description, objectives, and learning outcomes
  - Course format, schedule, and delivery mode
  - Course materials, textbooks, and resources
  - Course policies, rules, and expectations
  - Course assessment, grading, and feedback
  - Course activities, assignments, and projects
  - Course calendar, deadlines, and important dates
  - Course support, assistance, and resources

- A detailed syllabus should be clear, concise, accurate, and updated. It should also be aligned with the course curriculum, learning outcomes, and standards. It should be accessible and inclusive for all students, and respect their diversity and needs. It should be reviewed and revised regularly, and shared with students at the beginning of the course and throughout the course as needed.



### The student should have hands on experience in using various sensors like temperature, humidity, smoke, light, etc. and

- Understand the basic principles and working of each sensor.
- Learn how to connect the sensors to a microcontroller or a computer using appropriate wires, pins, and protocols.
- Learn how to program the microcontroller or the computer to read the sensor data and perform some actions based on the data.
- Learn how to calibrate the sensors and deal with noise, interference, and errors in the sensor data.
- Learn how to use the sensor data for various applications such as monitoring, control, automation, security, etc.
- Learn how to design and implement a sensor network using wireless communication and networking protocols.
- Learn how to analyze and visualize the sensor data using software tools and libraries.



### Should be able to use control web camera, network, and relays connected to the Pi.

- A web camera is a device that captures images or videos and sends them to a computer or a network. A web camera can be used for various purposes, such as video conferencing, surveillance, or entertainment.
- A network is a system of interconnected devices that can communicate and exchange data. A network can be wired or wireless, local or global, public or private. A network can be used for various purposes, such as sharing resources, accessing information, or collaborating.
- A relay is a device that switches an electric circuit on or off based on a signal. A relay can be used for various purposes, such as controlling devices, amplifying signals, or isolating circuits.
- A Pi is a small, low-cost, and versatile computer that can run various operating systems and applications. A Pi can be used for various purposes, such as learning programming, creating projects, or experimenting.
- To use control web camera, network, and relays connected to the Pi, one should be able to:
  - Connect the web camera, the network, and the relays to the Pi using the appropriate cables, ports, and adapters.
  - Install and configure the software and drivers needed to operate the web camera, the network, and the relays on the Pi.
  - Write and run programs or scripts that can control the web camera, the network, and the relays on the Pi using the appropriate libraries, commands, and interfaces.
  - Test and troubleshoot the web camera, the network, and the relays on the Pi using the appropriate tools, methods, and feedback.



#### 1. Start Raspberry Pi and try various Linux commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small, low-cost computer that can run Linux operating systems such as Raspbian, Ubuntu, or Fedora.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard, and a mouse. You also need to insert a microSD card with a Linux operating system installed on it.
- Once Raspberry Pi boots up, you will see a graphical user interface (GUI) or a command line interface (CLI) depending on the operating system you are using.
- To open a command terminal window, you can either click on the terminal icon on the GUI or press Ctrl+Alt+T on the keyboard.
- A command terminal window is a text-based interface that allows you to interact with the operating system using commands. Commands are instructions that tell the computer what to do.
- Some of the basic Linux commands that you can try in the command terminal window are:

  - `ls`: This command lists the files and directories in the current working directory. You can use options such as `-l` to show more details, `-a` to show hidden files, or `-h` to show human-readable sizes.
  - `cd`: This command changes the current working directory to the one specified. You can use `.` to refer to the current directory, `..` to refer to the parent directory, or `~` to refer to the home directory.
  - `touch`: This command creates a new, empty file with the name specified. You can also use it to update the modification time of an existing file.
  - `mv`: This command moves or renames a file or directory. You need to specify the source and the destination of the file or directory. You can also use options such as `-i` to prompt before overwriting, `-n` to not overwrite, or `-v` to show verbose output.
  - `rm`: This command removes or deletes a file or directory. You need to specify the name of the file or directory to be removed. You can also use options such as `-i` to prompt before removing, `-r` to remove recursively, or `-f` to force removal.
  - `man`: This command shows the manual page for a command or a topic. You can use it to learn more about the syntax, options, and examples of a command or a topic. You can navigate the manual page using the arrow keys, the space bar, or the Enter key. You can exit the manual page by pressing Q.

- To execute a command, you need to type it in the command terminal window and press Enter. You can also use the up and down arrow keys to scroll through the history of commands you have entered. You can use the Tab key to autocomplete the name of a file or directory. You can use the Ctrl+C key to interrupt or cancel a command. You can use the Ctrl+Z key to suspend a command. You can use the Ctrl+D key to exit the command terminal window.



#### mkdir, rmdir, tar, gzip, cat, more, less, ps, sudo, cron, chown, chgrp, ping etc.

- These are some common commands used in Linux operating systems to perform various tasks.
- `mkdir` is used to create a new directory in the current or specified location. For example, `mkdir newdir` will create a directory named newdir in the current working directory.
- `rmdir` is used to remove an empty directory. For example, `rmdir newdir` will delete the directory named newdir if it is empty. To remove a directory that is not empty, use the `-r` option with `rmdir` or use the `rm` command.
- `tar` is used to create or extract compressed archive files. For example, `tar -czvf archive.tar.gz files` will create a compressed archive file named archive.tar.gz containing the files specified. To extract the files from the archive, use `tar -xzvf archive.tar.gz`.
- `gzip` is used to compress or decompress files using the gzip algorithm. For example, `gzip file.txt` will compress the file named file.txt and create a file named file.txt.gz. To decompress the file, use `gzip -d file.txt.gz`.
- `cat` is used to concatenate files and print them to the standard output. For example, `cat file1 file2` will print the contents of file1 and file2 to the screen. `cat` can also be used to create or append files. For example, `cat > file3` will create a file named file3 and write the input from the keyboard to it until Ctrl-D is pressed. `cat >> file3` will append the input from the keyboard to the existing file3.
- `more` and `less` are used to view the contents of a file or the output of a command one page at a time. For example, `more file.txt` will display the file named file.txt one screen at a time and wait for the user to press a key to continue. `less file.txt` will do the same but also allow the user to scroll back and forth using the arrow keys or the Page Up and Page Down keys.
- `ps` is used to display information about the processes running on the system. For example, `ps -aux` will show all the processes along with their user, CPU, memory, and other details. `ps` can also be used to filter or sort the processes based on various criteria. For example, `ps -u root` will show only the processes owned by the root user.
- `sudo` is used to execute a command as another user, usually the superuser or root. For example, `sudo apt-get update` will run the command `apt-get update` as the root user and update the system's package list. `sudo` requires the user to enter their password and may also require the user to be in the sudoers file, which specifies which users can run which commands as which users.
- `cron` is used to schedule commands or scripts to run at a specified time or interval. For example, `crontab -e` will open the user's crontab file, which contains the list of commands or scripts to run and the time or frequency to run them. For example, `0 0 * * * /home/user/backup.sh` will run the script named backup.sh in the user's home directory every day at midnight. `cron` uses a special syntax to specify the time or frequency, which consists of five fields: minute, hour, day of month, month, and day of week.
- `chown` is used to change the owner of a file or directory. For example, `chown user1 file.txt` will change the owner of the file named file.txt to user1. `chown` can also be used to change the group of a file or directory using the `:` syntax. For example, `chown user1:group1 file.txt` will change the owner and the group of the file named file.txt to user1 and group1 respectively.
- `chgrp` is used to change the group of a file or directory. For example, `chgrp group1 file.txt` will change the group of the file named file.txt to group1. `chgrp` can also be used to change the group of multiple files or directories using the `-R` option. For example, `chgrp -R group1 dir1` will change the group of the directory named dir1 and all its contents to group1.
- `ping` is used to test the connectivity and latency between two hosts on a network. For example,



#### 2. Run some python programs on Pi like:

- To run python programs on Pi, you need to have a Raspberry Pi device, a microSD card with an operating system installed, a power supply, a keyboard, a mouse, and a monitor. You also need to install python on your Pi if it is not already included in your operating system.
- To install python on your Pi, you can use the following command in the terminal: `sudo apt install python3`
- To write python programs on your Pi, you can use any text editor or IDE (Integrated Development Environment) that supports python syntax. Some examples are Thonny, IDLE, PyCharm, or Visual Studio Code. You can also use the nano editor in the terminal to create and edit python files.
- To run python programs on your Pi, you can use the following command in the terminal: `python3 filename.py`, where filename.py is the name of your python file. You can also run python programs directly from your text editor or IDE if they have a run or execute option.
- Some examples of python programs that you can run on your Pi are:

  - A program that prints "Hello, world!" to the screen: `print("Hello, world!")`
  - A program that blinks an LED connected to the Pi's GPIO (General Purpose Input Output) pins: `import RPi.GPIO as GPIO # Import the GPIO library
GPIO.setmode(GPIO.BCM) # Set the GPIO numbering mode
GPIO.setup(18, GPIO.OUT) # Set pin 18 as an output
while True: # Loop forever
  GPIO.output(18, GPIO.HIGH) # Turn on the LED
  time.sleep(1) # Wait for one second
  GPIO.output(18, GPIO.LOW) # Turn off the LED
  time.sleep(1) # Wait for one second`
  - A program that takes user input and prints it back: `user_input = input("Enter something: ") # Ask the user for input
print("You entered: " + user_input) # Print the user input`



#### a) Read your name and print Hello message with name

- To read your name, you need to use an input function that takes a string as an argument and returns the user's input as a string.
- For example, in Python, you can use the input() function to read your name from the keyboard and store it in a variable called name.
- To print a Hello message with your name, you need to use a print function that takes a string as an argument and displays it on the screen.
- For example, in Python, you can use the print() function to print a Hello message with your name by concatenating the strings "Hello" and name with a comma or a plus sign.
- Here is an example of a Python program that reads your name and prints a Hello message with your name:

```python
# Read your name and store it in a variable called name
name = input("Enter your name: ")

# Print a Hello message with your name
print("Hello", name) # Using a comma to separate the strings
# or
print("Hello" + name) # Using a plus sign to concatenate the strings
```

- The output of the program will look something like this:

```text
Enter your name: Sydney
Hello Sydney
```



#### b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the input() function in Python, which returns a string that can be converted to a numerical type such as int or float.
- To print the sum, difference, product and division of two numbers, we can use the arithmetic operators +, -, *, and / in Python, which perform the corresponding operations on the operands and return the result.
- To print the result, we can use the print() function in Python, which displays the value of the expression inside the parentheses to the standard output.
- An example of a Python program that reads two numbers and prints their sum, difference, product and division is:

```python
# Read two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and print the sum, difference, product and division
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

print("The sum of the two numbers is", sum)
print("The difference of the two numbers is", difference)
print("The product of the two numbers is", product)
print("The division of the two numbers is", division)
```

- The output of the program will depend on the input values given by the user. For example, if the user enters 10 and 5, the output will be:

```
Enter the first number: 10
Enter the second number: 5
The sum of the two numbers is 15
The difference of the two numbers is 5
The product of the two numbers is 50
The division of the two numbers is 2.0
```



#### c) Word and character count of a given string.

- A string is a sequence of characters enclosed in quotation marks, such as "Hello" or "This is a string".
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "This is a word".
- A character is a single symbol, such as "H" or "." or " ".
- To count the number of words in a string, we can split the string by spaces or punctuation marks and count the length of the resulting list.
- To count the number of characters in a string, we can simply count the length of the string itself.
- For example, the string "This is a string." has 4 words and 16 characters, including the space and the period.
- Here is a possible pseudocode algorithm to count the words and characters in a string:

```
# Input: a string s
# Output: the number of words and characters in s

# Initialize word_count and char_count to zero
word_count = 0
char_count = 0

# Loop through each character in s
for each char in s:
  # Increment char_count by one
  char_count = char_count + 1

  # If char is a space or a punctuation mark
  if char is " " or char is "." or char is "," or char is ";" or char is ":" or char is "?" or char is "!":
    # Increment word_count by one
    word_count = word_count + 1

# Return word_count and char_count
return word_count, char_count
```



#### d) Area of a given shape (rectangle, triangle and circle) reading shape and appropriate values from standard

- The area of a shape is the amount of space inside the boundary of the shape. It is measured in square units, such as square centimeters, square meters, square inches, etc.
- To find the area of a given shape, we need to know the shape and the appropriate values from the standard input, such as the length, width, base, height, or radius of the shape.
- The formula for the area of a rectangle is `A = length * width`, where `length` and `width` are the dimensions of the rectangle. For example, if a rectangle has a length of 10 cm and a width of 5 cm, then its area is `A = 10 * 5 = 50 cm^2`.
- The formula for the area of a triangle is `A = (base * height) / 2`, where `base` and `height` are the dimensions of the triangle. For example, if a triangle has a base of 12 cm and a height of 9 cm, then its area is `A = (12 * 9) / 2 = 54 cm^2`.
- The formula for the area of a circle is `A = pi * radius^2`, where `pi` is a constant value approximately equal to 3.14 and `radius` is the distance from the center of the circle to any point on the circle. For example, if a circle has a radius of 7 cm, then its area is `A = pi * 7^2 = 153.86 cm^2`.
- To read the shape and the appropriate values from the standard input, we can use the `input()` function in Python, which returns a string of the user's input. For example, we can write:

```python
# Ask the user to enter the shape
shape = input("Enter the shape (rectangle, triangle, or circle): ")

# Check the shape and calculate the area accordingly
if shape == "rectangle":
  # Ask the user to enter the length and width of the rectangle
  length = float(input("Enter the length of the rectangle: "))
  width = float(input("Enter the width of the rectangle: "))
  # Calculate the area of the rectangle
  area = length * width
  # Print the area of the rectangle
  print(f"The area of the rectangle is {area} square units.")
elif shape == "triangle":
  # Ask the user to enter the base and height of the triangle
  base = float(input("Enter the base of the triangle: "))
  height = float(input("Enter the height of the triangle: "))
  # Calculate the area of the triangle
  area = (base * height) / 2
  # Print the area of the triangle
  print(f"The area of the triangle is {area} square units.")
elif shape == "circle":
  # Ask the user to enter the radius of the circle
  radius = float(input("Enter the radius of the circle: "))
  # Calculate the area of the circle
  area = 3.14 * radius**2
  # Print the area of the circle
  print(f"The area of the circle is {area} square units.")
else:
  # Print an error message if the shape is not valid
  print("Invalid shape. Please enter rectangle, triangle, or circle.")
```



#### Input

- Input is the process of providing data or instructions to a computer system so that it can perform a task or operation.
- Input is important because it allows users to interact with a computer system and provide information that can be processed and analyzed.
- Input can come from various sources, such as keyboards, mice, touch screens, microphones, scanners, cameras, sensors, etc .
- Input devices are hardware components that enable users to input data or commands to a computer system.
- Input can be categorized into different types, such as text, numeric, audio, image, video, etc.
- Input can also be classified into different modes, such as direct, indirect, discrete, continuous, etc.
- Input can affect the performance, usability, and functionality of a computer system.



#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- To write a python program, you need to use a text editor such as nano, vim, or idle. You can launch any of these editors from the terminal by typing their name followed by the name of the file you want to create or edit. For example, `nano hello.py` will open a new file called hello.py in nano editor.
- To print a name 'n' times, where name and n are read from standard input, you can use the following python code:

```python
# Read the name from the user
name = input("Enter your name: ")

# Read the number of times to print from the user
n = int(input("Enter the number of times to print: "))

# Use a for loop to print the name n times
for i in range(n):
    print(name)
```

- To run the python program, you need to save the file and exit the editor. Then, you can type `python3 hello.py` in the terminal and press enter. You will see the prompts for the name and the number, and then the output of the program.
- You can modify the program to print different messages or use different input methods as you wish.



#### Using for and while loops
- A for loop is a control structure that allows you to repeat a block of code a fixed number of times.
- A while loop is a control structure that allows you to repeat a block of code as long as a condition is true.
- The syntax of a for loop is:

```python
for variable in iterable:
    # do something with variable
```

- The syntax of a while loop is:

```python
while condition:
    # do something
```

- For example, to print the numbers from 1 to 10 using a for loop, you can write:

```python
for i in range(1, 11):
    print(i)
```

- To print the numbers from 1 to 10 using a while loop, you can write:

```python
i = 1
while i <= 10:
    print(i)
    i = i + 1
```

#### Handle Divided by Zero Exception
- An exception is an error that occurs during the execution of a program.
- A divided by zero exception is an error that occurs when you try to divide a number by zero, which is mathematically undefined.
- To handle an exception, you can use a try-except block, which allows you to catch and handle the error gracefully, instead of crashing the program.
- The syntax of a try-except block is:

```python
try:
    # try to do something that may cause an exception
except ExceptionType as e:
    # handle the exception of type ExceptionType
```

- For example, to handle a divided by zero exception, you can write:

```python
try:
    x = 10 / 0 # this will cause a ZeroDivisionError
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
```

#### Print current time for 10 times with an interval of 1 second
- To print the current time, you can use the datetime module, which provides various functions and classes to work with dates and times.
- To print the current time for 10 times with an interval of 1 second, you can use a for loop and the time module, which provides various functions to work with time.
- The syntax to print the current time is:

```python
from datetime import datetime
print(datetime.now())
```

- The syntax to wait for 1 second is:

```python
import time
time.sleep(1)
```

- For example, to print the current time for 10 times with an interval of 1 second, you can write:

```python
from datetime import datetime
import time
for i in range(10):
    print(datetime.now())
    time.sleep(1)
```



#### Interval of 10 seconds
- An interval of 10 seconds is a measure of time that is equal to 10 units of one second each.
- A second is the base unit of time in the International System of Units (SI) and is defined as the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.
- An interval of 10 seconds can be used to measure the duration of events or processes that are relatively short, such as human reaction time, sprinting speed, or heart rate.
- An interval of 10 seconds can also be used to divide a longer period of time into smaller segments, such as a minute, an hour, or a day, for the purpose of counting, timing, or scheduling.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one possible algorithm is as follows:
  - Open the file in read mode and assign it to a variable, such as `file`.
  - Initialize a variable, such as `line_number`, to store the current line number, and set it to 1.
  - Use a loop, such as a `while` loop, to iterate over the lines of the file until the end of the file is reached.
  - For each iteration of the loop, do the following:
    - Read the next line from the file and assign it to a variable, such as `line`.
    - Split the line into a list of words by using a delimiter, such as a space, and assign it to a variable, such as `words`.
    - Count the number of elements in the list of words and assign it to a variable, such as `word_count`.
    - Print the line number, a colon, and the word count, separated by spaces, to the standard output.
    - Increment the line number by 1.
  - Close the file.



#### 4. a) Light an LED through Python program

- To light an LED through Python program, you need to have a hardware device that can be controlled by Python, such as an Arduino, a Raspberry Pi, or a MicroPython board.
- You also need to connect the LED to the device using a resistor, wires and a breadboard, following the appropriate circuit diagram for your device.
- You need to write a Python program that can communicate with the device and send commands to turn the LED on and off.
- Depending on your device, you may need to use different Python modules or libraries to control the LED, such as `pyserial`, `RPi.GPIO`, or `pyb`.
- You can use a loop, a conditional statement, or a function to control the LED behavior, such as blinking, fading, or changing colors.
- You can run the Python program on your computer or on the device itself, depending on your device and setup.
- Here are some examples of Python programs that can light an LED through different devices:

  - Arduino :

    ```python
    # Import the pyserial module
    import serial

    # Create a serial object and connect to the Arduino
    ser = serial.Serial('/dev/ttyACM0', 9600)

    # Turn the LED on and off by sending 'H' or 'L' to the Arduino
    while True:
        # Ask the user to enter 'H' or 'L'
        user_input = input("Enter 'H' to turn LED on, 'L' to turn LED off: ")

        # Check if the user input is valid
        if user_input == 'H' or user_input == 'L':
            # Send the user input to the Arduino
            ser.write(user_input.encode())
        else:
            # Print an error message
            print("Invalid input")
    ```

  - Raspberry Pi  :

    ```python
    # Import the RPi.GPIO module
    import RPi.GPIO as GPIO

    # Import the time module
    import time

    # Set the GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Set the GPIO pin 18 as output
    GPIO.setup(18, GPIO.OUT)

    # Turn the LED on and off by changing the output state of pin 18
    while True:
        # Turn the LED on
        GPIO.output(18, GPIO.HIGH)
        # Wait for one second
        time.sleep(1)
        # Turn the LED off
        GPIO.output(18, GPIO.LOW)
        # Wait for one second
        time.sleep(1)
    ```

  - MicroPython:

    ```python
    # Import the pyb module
    import pyb

    # Create an LED object for the built-in LED 2 (red)
    led = pyb.LED(2)

    # Turn the LED on and off by toggling its state
    while True:
        # Toggle the LED state
        led.toggle()
        # Wait for one second
        pyb.delay(1000)
    ```



#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to two switches and two LEDs using wires and resistors.
- The switches are used to provide digital input signals to the microcontroller, which can be either HIGH (5V) or LOW (0V) depending on whether the switch is pressed or not.
- The LEDs are used to provide digital output signals from the microcontroller, which can be either HIGH (5V) or LOW (0V) depending on whether the LED is turned on or off.
- The microcontroller can read the input signals from the switches using digitalRead() function and write the output signals to the LEDs using digitalWrite() function.
- The logic of the program is to check the state of each switch and turn on the corresponding LED if the switch is pressed, and turn off the LED if the switch is not pressed.
- The circuit diagram and the code for this task are shown below:

```markdown
Circuit diagram:

    +5V  +5V
     |    |
     |    |
    ---  ---
    | |  | |  Switches
    ---  ---
     |    |
     |    |
    10k  10k  Resistors
     |    |
     |    |
     |    |
    D2   D3  Digital pins for input
     |    |
     |    |
    ---  ---
    | |  | |  LEDs
    ---  ---
     |    |
     |    |
    220  220  Resistors
     |    |
     |    |
    GND  GND
     |    |
     |    |
    ---  ---
    | |  | |  Ground
    ---  ---

Code:

// Define the pin numbers for switches and LEDs
#define SWITCH1 2
#define SWITCH2 3
#define LED1 4
#define LED2 5

// Set up the pins as input or output
void setup() {
  pinMode(SWITCH1, INPUT);
  pinMode(SWITCH2, INPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

// Loop the program to read and write the signals
void loop() {
  // Read the state of each switch
  int switch1State = digitalRead(SWITCH1);
  int switch2State = digitalRead(SWITCH2);

  // Write the state of each LED
  digitalWrite(LED1, switch1State);
  digitalWrite(LED2, switch2State);
}
```



#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, some jumper wires, and a text file that contains the on time and off time values in milliseconds.
- The microcontroller is a device that can execute a program that controls the output pins. We can use any microcontroller that has a digital output pin, such as Arduino, Raspberry Pi, or ESP32.
- The LED is a light-emitting diode that can turn on or off depending on the voltage applied to its terminals. We need to connect one terminal of the LED to the output pin of the microcontroller, and the other terminal to the ground through a resistor. The resistor limits the current that flows through the LED and prevents it from burning out.
- The breadboard is a board that has holes that are connected internally by metal strips. We can use it to make temporary connections between the components without soldering them.
- The jumper wires are wires that have metal pins at both ends. We can use them to connect the components on the breadboard or to the microcontroller pins.
- The text file is a file that has two numbers separated by a comma. The first number is the on time and the second number is the off time for the LED. For example, if the file has 1000,500, it means the LED should be on for 1000 milliseconds and off for 500 milliseconds. We need to store this file in the same folder as the program that we will write for the microcontroller.
- The program for the microcontroller is a set of instructions that tells the microcontroller what to do. We can write the program in any programming language that is compatible with the microcontroller, such as C, Python, or Arduino. The program should do the following steps:
  - Define a variable to store the output pin number that is connected to the LED. For example, if we use pin 13 on Arduino, we can write `int ledPin = 13;`.
  - Define two variables to store the on time and off time values that are read from the file. For example, we can write `int onTime = 0;` and `int offTime = 0;`.
  - Set the output pin mode to output. For example, if we use Arduino, we can write `pinMode(ledPin, OUTPUT);` in the setup function.
  - Open the text file and read the two numbers from it. For example, if we use Arduino, we can write `File file = SD.open("times.txt");` to open the file, and then use `file.parseInt()` to read the numbers and store them in the variables. We also need to close the file after reading it by writing `file.close();`.
  - Use a loop to repeat the following steps indefinitely. For example, if we use Arduino, we can write `void loop() {` to start the loop and `}` to end it.
    - Turn on the LED by writing a high voltage to the output pin. For example, if we use Arduino, we can write `digitalWrite(ledPin, HIGH);`.
    - Wait for the on time duration by using a delay function. For example, if we use Arduino, we can write `delay(onTime);`.
    - Turn off the LED by writing a low voltage to the output pin. For example, if we use Arduino, we can write `digitalWrite(ledPin, LOW);`.
    - Wait for the off time duration by using a delay function. For example, if we use Arduino, we can write `delay(offTime);`.
- The result is that the LED will flash at the given on time and off time cycle, as specified by the file. We can change the file contents to change the cycle. For example, if we change the file to 500,1000, the LED will be on for 500 milliseconds and off for 1000 milliseconds.



#### 5. a) Flash an LED based on cron output (acts as an alarm)

- To flash an LED based on cron output, we need to use a Raspberry Pi, an LED, a resistor, some jumper wires, and a breadboard.
- We also need to install the WiringPi library on the Raspberry Pi, which provides a command-line utility called `gpio` to control the GPIO pins.
- We need to connect the LED to the GPIO pin 17 (BCM numbering) and the resistor to the ground pin using the jumper wires and the breadboard. The resistor is used to limit the current and protect the LED from burning out.
- We need to write a shell script that uses the `gpio` command to turn the LED on and off. For example, we can create a file called `flash_led.sh` with the following content:

```bash
#!/bin/bash
# flash_led.sh - a script to flash an LED on GPIO 17

# set the GPIO 17 to output mode
gpio -g mode 17 out

# loop 10 times
for i in {1..10}
do
  # turn the LED on
  gpio -g write 17 1
  # wait for 0.5 seconds
  sleep 0.5
  # turn the LED off
  gpio -g write 17 0
  # wait for 0.5 seconds
  sleep 0.5
done
```

- We need to make the script executable by running the command `chmod +x flash_led.sh`.
- We need to use the `crontab` command to schedule the script to run at a specific time or interval. For example, we can run the command `crontab -e` to edit the crontab file and add the following line:

```bash
# flash the LED at 8:00 AM every day
0 8 * * * /home/pi/flash_led.sh
```

- This will flash the LED 10 times at 8:00 AM every day, acting as an alarm. We can save and exit the crontab file and verify that the cron job is set up by running the command `crontab -l`.
- We can also test the script manually by running the command `./flash_led.sh` and observe the LED flashing.



#### b) Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

- A relay is an electromechanical device that can be used to control high-voltage or high-current devices with low-voltage or low-current signals.
- A relay has two main parts: a coil and a set of contacts. The coil is an electromagnet that can be energized by applying a voltage across its terminals. The contacts are metal pieces that can be opened or closed by the magnetic field of the coil.
- A relay can be connected to a Raspberry Pi GPIO pin to control its coil. The GPIO pin can be set to high or low to turn on or off the relay. The relay's contact terminals can be connected to a load, such as a lamp, a fan, or a motor.
- Cron is a time-based scheduler that can be used to run commands or scripts at specified times or intervals on a Raspberry Pi  . Cron has a configuration file called crontab, which contains the scheduled tasks and their corresponding times using a special syntax  .
- To switch on a relay at a given time using cron, the following steps are required:
  - Connect the relay to the Raspberry Pi GPIO pin and the load to the relay's contact terminals. Make sure the relay and the load are compatible with the Raspberry Pi's voltage and current ratings.
  - Write a Python script that can control the relay by setting the GPIO pin to high or low. For example, the script can be named relay_on.py and contain the following code:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # use BCM numbering scheme for GPIO pins
GPIO.setup(18, GPIO.OUT) # set GPIO 18 as output
GPIO.output(18, GPIO.HIGH) # set GPIO 18 to high to turn on relay
```

  - Make the script executable by running the command `chmod +x relay_on.py` in the terminal.
  - Edit the crontab file by running the command `crontab -e` in the terminal  . This will open the file in a text editor, such as nano or vi.
  - Add a line to the crontab file that specifies the time and the command to run the script. The line should follow the format `minute hour day month weekday command`  . For example, to run the script at 8:00 AM every day, the line can be:

```bash
0 8 * * * /home/pi/relay_on.py
```

  - Save and exit the crontab file. The cron service will automatically reload the file and execute the scheduled tasks  .
- To switch off the relay at a given time using cron, the same steps can be followed, except that the Python script should set the GPIO pin to low to turn off the relay, and the crontab line should specify a different time. For example, the script can be named relay_off.py and contain the following code:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # use BCM numbering scheme for GPIO pins
GPIO.setup(18, GPIO.OUT) # set GPIO 18 as output
GPIO.output(18, GPIO.LOW) # set GPIO 18 to low to turn off relay
```

And the crontab line can be:

```bash
0 20 * * * /home/pi/relay_off.py
```

This will run the script at 8:00 PM every day  .

: Cron Jobs and Task Scheduling on Raspberry Pi OS | Delft Stack
: Raspberry Pi: Control Relay switch via GPIO
: Cron and GPIO relay SOLVED - Raspberry Pi Forums
: Setting Up A Cron Job On The Raspberry Pi - BC Robotics
: Raspberry Pi - Crontab tutorial (How to Schedule Cron jobs)



#### c) Get the status of a bulb at a remote place (on the LAN) through web.

- To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

  - The bulb should be connected to a microcontroller that can communicate with the web server using HTTP protocol. The microcontroller should also have a sensor to detect the bulb's state (on or off).
  - The web server should have a web page that can display the bulb's status and allow the user to control it. The web page should also have a script that can send and receive HTTP requests to the microcontroller.
  - The user should access the web page using a web browser on a device that is connected to the same LAN as the bulb and the web server. The user should also have the IP address or the hostname of the web server.
  - The web page should send a GET request to the microcontroller to get the bulb's status. The microcontroller should respond with a JSON object that contains the bulb's state and other information.
  - The web page should parse the JSON object and display the bulb's status on the web page. The web page should also update the bulb's status periodically by sending GET requests to the microcontroller at regular intervals.
  - The user should be able to toggle the bulb's state by clicking a button on the web page. The web page should send a POST request to the microcontroller with the desired state of the bulb. The microcontroller should change the bulb's state accordingly and send a confirmation message to the web page. The web page should update the bulb's status accordingly.



#### Note: The Instructor may add/delete/modify/tune experiments

- This note indicates that the instructor has the authority and discretion to change the experiments that are part of the course curriculum.
- The instructor may add new experiments, delete existing ones, modify the objectives, procedures, or outcomes of the experiments, or tune the parameters, settings, or equipment of the experiments.
- The instructor may do so for various reasons, such as to align the experiments with the course objectives, to update the experiments with the latest developments in the field, to accommodate the availability of resources, or to enhance the learning experience of the students.
- The students should be aware of this note and be prepared to adapt to any changes in the experiments that the instructor may introduce. The students should also follow the instructions and guidelines of the instructor for each experiment.



# The topic is

- The topic is a general term for the subject or theme of a text, speech, or conversation.
- The topic can be expressed in different ways, such as a word, a phrase, a question, or a statement.
- The topic can be identified by looking for the main idea, the purpose, or the focus of the text, speech, or conversation.
- The topic can be used to organize, summarize, or evaluate the text, speech, or conversation.
- The topic can be related to other topics by using categories, subtopics, or keywords.



# The topic is

- The topic is a general term for the subject or theme of a text, speech, or conversation.
- The topic can be expressed in different ways, such as a word, a phrase, a question, or a statement.
- The topic can be identified by looking for clues in the text, such as the title, the introduction, the main idea, the keywords, or the summary.
- The topic can be used to organize and structure the information in the text, such as by using headings, subheadings, paragraphs, or bullet points.
- The topic can be used to guide the reader's attention and interest, such as by using hooks, transitions, examples, or questions.
- The topic can be used to communicate the purpose and goal of the text, such as by using a thesis statement, a claim, an argument, or a conclusion.



# The topic is

- The topic is a general term for the subject or theme of a text, speech, or conversation.
- A topic can be broad or narrow, depending on the scope and purpose of the communication.
- A topic can be expressed as a word, a phrase, a question, or a statement.
- A topic can be chosen by the speaker or writer, or assigned by a teacher, editor, or audience.
- A topic can be influenced by the context, the genre, the audience, and the purpose of the communication.
- A topic can be developed by using various strategies, such as brainstorming, researching, outlining, drafting, revising, and editing.
- A topic can be supported by using various types of evidence, such as facts, statistics, examples, anecdotes, quotations, and arguments.
- A topic can be organized by using various patterns, such as chronological, spatial, topical, problem-solution, cause-effect, compare-contrast, and classification.
- A topic can be evaluated by using various criteria, such as relevance, clarity, coherence, accuracy, completeness, and originality.



# KOT 553 INTERNET OF THINGS LAB KCS

- KOT 553 is a lab course for the third year students of Computer Science and Engineering (IoT) at Dr. A.P.J. Abdul Kalam Technical University (AKTU).
- The course aims to provide hands-on experience and practical skills in developing and deploying IoT applications using various hardware devices and sensors.
- The course covers the following topics:
  - Introduction to IoT and its applications
  - IoT architecture and protocols
  - IoT hardware devices and sensors
  - IoT platforms and cloud services
  - IoT data analytics and visualization
  - IoT security and privacy
- The course has a total of 60 hours of lab work, divided into 15 sessions of 4 hours each.
- The course has a total of 100 marks, divided into 50 marks for internal assessment and 50 marks for external assessment.
- The internal assessment consists of 10 marks for attendance, 10 marks for lab records, 10 marks for viva, and 20 marks for lab tests.
- The external assessment consists of 50 marks for a practical exam, which includes a demonstration of an IoT project and a viva.
- The course outcomes are as follows:
  - CO1: Demonstrate basic concepts, principles and challenges in IoT.
  - CO2: Illustrate functioning of hardware devices and sensors used for IoT.
  - CO3: Design and implement IoT applications using various IoT platforms and cloud services.
  - CO4: Analyze and visualize IoT data using appropriate tools and techniques.
  - CO5: Apply security and privacy measures for IoT applications.



# Course Outcome (CO) Bloom's Knowledge Level (KL)

- Course Outcome (CO) is a statement that describes what a learner should be able to do at the end of a course or a unit of instruction.
- Bloom's Knowledge Level (KL) is a classification of cognitive skills that learners can demonstrate in relation to a given topic or domain.
- Bloom's Knowledge Level (KL) consists of six levels: remember, understand, apply, analyze, evaluate, and create. Each level represents a higher order of thinking and requires more complex cognitive processes than the previous one.
- Course Outcome (CO) can be aligned with Bloom's Knowledge Level (KL) to ensure that the learning objectives are clear, measurable, and appropriate for the level of the course or the unit of instruction.
- For example, a Course Outcome (CO) for a course on computer programming could be: "Write, compile, and debug a simple program using a programming language of your choice." This CO can be mapped to the Bloom's Knowledge Level (KL) of apply, as it requires the learner to use the knowledge and skills of programming to solve a specific problem.
- Another example of a Course Outcome (CO) for a course on history could be: "Compare and contrast the causes and effects of the American Revolution and the French Revolution." This CO can be mapped to the Bloom's Knowledge Level (KL) of analyze, as it requires the learner to break down the information into parts and examine the relationships and differences between them.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the content in markdown format on the topic "At the end of course, the student will be able to". Here is my attempt:

# At the end of course, the student will be able to

- Define the main concepts and principles of the course subject.
- Apply the learned skills and knowledge to solve problems and complete tasks related to the course subject.
- Analyze and evaluate the information and arguments presented in the course materials and sources.
- Communicate effectively and professionally using the appropriate language and format for the course subject.
- Demonstrate ethical and responsible behavior in academic and professional settings related to the course subject.
- Reflect on their own learning process and outcomes and identify areas for improvement and further development.



# CO 1 Understand the concept of Internet of Things K3

- Internet of Things (IoT) is the interconnection of physical objects with computing devices, sensors, software and other technologies that enable them to communicate and exchange data over the internet or other networks  .
- IoT allows information to be sent and received from objects and devices that are embedded in everyday objects, such as fixtures and kitchen appliances.
- IoT integrates people, processes and technology to enable remote monitoring, status, manipulation and evaluation of trends of such devices.
- IoT can be applied to various domains, such as smart homes, smart cities, smart agriculture, smart health, smart industry, smart transportation, smart energy, smart environment, etc.
- IoT can provide benefits such as improved efficiency, convenience, safety, security, quality, productivity, innovation, etc.



# CO2 Implement interfacing of various sensors with Arduino/Raspberry Pi

- CO2 sensors are devices that can measure the concentration of carbon dioxide in the air. They are useful for monitoring air quality, plant growth, fermentation, and other applications.
- There are different types of CO2 sensors available, such as electrochemical, infrared, and metal oxide. Each type has its own advantages and disadvantages, such as accuracy, power consumption, response time, and cost.
- Arduino and Raspberry Pi are popular platforms for interfacing with various sensors, including CO2 sensors. They are microcontrollers that can read analog or digital signals from sensors, process them, and communicate with other devices or computers.
- To interface a CO2 sensor with Arduino or Raspberry Pi, the following steps are required:

  - Choose a suitable CO2 sensor for your project. Consider the sensor specifications, such as output voltage, range, resolution, calibration, and compatibility with your platform.
  - Connect the CO2 sensor to your Arduino or Raspberry Pi using the appropriate pins and wires. Depending on the sensor type, you may need to use analog or digital pins, or a communication protocol such as I2C or UART.
  - Install the necessary libraries and drivers for your platform and sensor. Some sensors may have existing libraries or code examples that you can use or modify for your project. Otherwise, you may need to write your own code to read and interpret the sensor data.
  - Write the code to read the sensor data, perform any calculations or conversions, and display or store the results. You can use the serial monitor, an LCD screen, an SD card, or a web server to display or store the data. You can also add other features, such as alarms, graphs, or controls, depending on your project requirements.
  - Test and troubleshoot your code and connections. Make sure the sensor is working properly and giving reasonable values. Check for any errors or bugs in your code and fix them. Adjust any parameters or settings as needed.



# CO 3 Demonstrate the ability to transmit data wirelessly between different devices. K4

- Wireless data transmission is the process of sending and receiving data without using physical wires or cables.
- Wireless data transmission can be classified into two main types: radio frequency (RF) and optical.
- RF transmission uses electromagnetic waves to carry data through the air, such as Wi-Fi, Bluetooth, and cellular networks .
- Optical transmission uses light to send data, such as infrared, visible light, and laser .
- Wireless data transmission has many advantages, such as mobility, convenience, scalability, and cost-effectiveness.
- Wireless data transmission also has some challenges, such as interference, security, reliability, and power consumption.

## How to transmit data wirelessly between different devices

- To transmit data wirelessly between different devices, the following steps are required:
  - Choose a suitable wireless transmission method, such as RF or optical, based on the distance, bandwidth, and environment of the communication.
  - Use a wireless transmitter and receiver that are compatible with the chosen wireless transmission method and the data format.
  - Establish a wireless connection between the transmitter and receiver, such as pairing, authentication, or encryption.
  - Send and receive data using the wireless connection, such as packets, frames, or signals.
  - Monitor and troubleshoot the wireless connection, such as signal strength, quality, and errors.



# CO 4 Show an ability to upload/download sensor data on cloud and server K2

- Sensor data is the information collected by various types of sensors that measure physical phenomena such as temperature, humidity, pressure, light, sound, motion, etc.
- Cloud and server are two types of computing platforms that can store, process, and analyze sensor data remotely over the internet.
- Uploading sensor data means sending the data from the sensor device to the cloud or server, while downloading sensor data means receiving the data from the cloud or server to the sensor device or another device.
- To upload/download sensor data on cloud and server, the following steps are usually involved:

  - **Step 1:** Connect the sensor device to the internet using a wired or wireless communication protocol, such as Ethernet, Wi-Fi, Bluetooth, Zigbee, LoRa, cellular, satellite, etc. The choice of protocol depends on factors such as data rate, power consumption, range, cost, and availability.
  - **Step 2:** Choose a cloud or server platform that can receive, store, and process sensor data, such as AWS, Azure, Google Cloud, IBM Cloud, ThingSpeak, etc. The choice of platform depends on factors such as scalability, security, reliability, compatibility, and pricing.
  - **Step 3:** Configure the sensor device and the cloud or server platform to establish a connection and exchange data using a common data format and protocol, such as JSON, XML, MQTT, HTTP, etc. The choice of format and protocol depends on factors such as data structure, bandwidth, latency, and interoperability.
  - **Step 4:** Upload the sensor data from the sensor device to the cloud or server platform using the configured connection and protocol. The frequency and size of the data upload depend on factors such as sensor type, application, and network conditions.
  - **Step 5:** Download the sensor data from the cloud or server platform to the sensor device or another device using the configured connection and protocol. The frequency and size of the data download depend on factors such as sensor type, application, and network conditions.
  - **Step 6:** Analyze the sensor data on the cloud or server platform or on the device using various tools and techniques, such as dashboards, charts, graphs, statistics, machine learning, etc. The purpose of the data analysis is to extract meaningful insights and actions from the sensor data.

- Some examples of uploading/downloading sensor data on cloud and server are:

  - A smart thermostat that uploads temperature and humidity data to a cloud platform and downloads commands to adjust the heating or cooling system.
  - A weather station that uploads atmospheric pressure and wind speed data to a server platform and downloads weather forecasts and alerts.
  - A wildlife tracker that uploads GPS and accelerometer data to a satellite platform and downloads location and activity data of the animals.



# CO 5 Examine various SQL queries from MySQL database K4, K5

- SQL stands for Structured Query Language and is a standard language for accessing and manipulating data in relational databases.
- MySQL is one of the most popular open-source relational database management systems (RDBMS) that uses SQL to query, manipulate, and analyze data.
- SQL queries are commands that are used to retrieve, insert, update, delete, or modify data in a database .
- SQL queries can be classified into five types based on their purpose and functionality:
  - DDL (Data Definition Language): These are queries that define the structure and schema of the database, such as creating, altering, renaming, dropping, or truncating tables or databases. Examples of DDL commands are `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, etc.
  - DML (Data Manipulation Language): These are queries that manipulate the data in the database, such as inserting, updating, deleting, or selecting data from tables. Examples of DML commands are `INSERT INTO`, `UPDATE`, `DELETE`, `SELECT`, etc.
  - DCL (Data Control Language): These are queries that control the access and permissions of the data in the database, such as granting, revoking, or denying privileges to users or roles. Examples of DCL commands are `GRANT`, `REVOKE`, `DENY`, etc.
  - TCL (Transaction Control Language): These are queries that manage the transactions in the database, such as committing, rolling back, or saving the changes made by the queries. Examples of TCL commands are `COMMIT`, `ROLLBACK`, `SAVEPOINT`, etc.
  - DQL (Data Query Language): These are queries that query the data in the database, such as retrieving, filtering, sorting, grouping, or aggregating data from tables. Examples of DQL commands are `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`, etc.
- To write SQL queries in MySQL, one needs to have a database management application (such as MySQL Workbench, Sequel Pro, etc.) that can connect to the MySQL server and execute the queries .
- The basic syntax of a SQL query in MySQL is as follows:

  ```sql
  SELECT column1, column2, ...
  FROM table_name
  WHERE condition
  GROUP BY column1, column2, ...
  HAVING condition
  ORDER BY column1, column2, ...
  LIMIT number;
  ```
- The `SELECT` clause specifies the columns or expressions to be retrieved from the table.
- The `FROM` clause specifies the table or tables from which to retrieve the data.
- The `WHERE` clause specifies the condition or criteria to filter the rows of the table.
- The `GROUP BY` clause specifies the columns or expressions to group the rows of the table by a common value.
- The `HAVING` clause specifies the condition or criteria to filter the groups of the table.
- The `ORDER BY` clause specifies the columns or expressions to sort the rows of the table in ascending or descending order.
- The `LIMIT` clause specifies the maximum number of rows to be returned by the query.
- The `;` symbol marks the end of the query.

- Here are some examples of SQL queries in MySQL :

  - To create a database named `students`:

    ```sql
    CREATE DATABASE students;
    ```

  - To create a table named `student_info` with four columns: `id`, `name`, `age`, and `grade`:

    ```sql
    CREATE TABLE student_info (
      id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      age INT,
      grade CHAR(1)
    );
    ```

  - To insert a new row into the `student_info` table with the values `1`, `Alice`, `18`, and `A`:

    ```sql
    INSERT INTO student_info (id, name, age, grade)
    VALUES (1, 'Alice', 18, 'A');
    ```

  - To update the `grade` column of the `student_info` table to `B` where the `id` is `1`:

    ```sql
    UPDATE student_info
    SET grade = 'B'
    WHERE id = 1;
    ```

  - To delete the row from the `student_info` table where the `id` is



# DETAILED SYLLABUS

- A detailed syllabus is a document that outlines the topics, objectives, learning outcomes, assessment methods, and resources for a specific course or module.
- A detailed syllabus can help students to understand the expectations and requirements of the course, as well as to plan their study time and activities accordingly.
- A detailed syllabus can also help instructors to design and deliver the course in a coherent and consistent way, as well as to communicate with students and other stakeholders about the course content and goals.
- A detailed syllabus typically includes the following sections:

  - Course information: This section provides basic information about the course, such as the course title, code, credits, level, prerequisites, co-requisites, instructor name and contact details, office hours, course website, etc.
  - Course description: This section provides a brief overview of the course, its purpose, scope, and main themes or topics. It may also include a rationale for why the course is important or relevant for the students or the discipline.
  - Course objectives: This section lists the specific learning objectives or outcomes that the students are expected to achieve by the end of the course. These objectives should be clear, measurable, and aligned with the course level and the program outcomes.
  - Course schedule: This section provides a tentative outline of the course content and activities, organized by week or session. It may include the topics, readings, assignments, quizzes, exams, projects, presentations, etc. that the students need to complete or prepare for each week or session. It may also indicate the due dates, weightings, and formats of the assessments.
  - Course policies: This section specifies the rules and expectations that the students and the instructor need to follow in the course, such as the attendance, participation, late submission, academic integrity, grading, feedback, communication, etc. policies. It may also include the procedures for requesting extensions, accommodations, appeals, etc.
  - Course resources: This section lists the required and recommended materials and resources that the students need to access or purchase for the course, such as the textbooks, articles, websites, software, etc. It may also provide information on how and where to access or obtain these resources, such as the library, online platforms, etc.



# The student should have hands on experience in using various sensors like temperature, humidity, smoke, light, etc.

- Sensors are devices that detect and measure physical quantities such as temperature, humidity, smoke, light, etc. and convert them into electrical signals.
- Sensors are essential components of many applications such as smart homes, environmental monitoring, security systems, robotics, etc.
- Hands on experience in using various sensors can help the student to:
  - Understand the working principles, characteristics, and limitations of different types of sensors.
  - Learn how to interface sensors with microcontrollers, computers, or other devices using appropriate circuits, protocols, and software.
  - Develop skills in designing, testing, and troubleshooting sensor-based systems and projects.
  - Explore the possibilities and challenges of using sensors for various purposes and contexts.
- Some examples of sensors that the student can use for hands on experience are:
  - Temperature sensor: A device that measures the temperature of an object or environment. There are different types of temperature sensors such as thermocouples, thermistors, resistance temperature detectors (RTDs), infrared thermometers, etc. Each type has its own advantages and disadvantages in terms of accuracy, range, response time, cost, etc.
  - Humidity sensor: A device that measures the amount of water vapor in the air. There are different types of humidity sensors such as capacitive, resistive, thermal, optical, etc. Each type has its own advantages and disadvantages in terms of accuracy, range, response time, cost, etc.
  - Smoke sensor: A device that detects the presence of smoke or fire. There are different types of smoke sensors such as ionization, photoelectric, thermal, etc. Each type has its own advantages and disadvantages in terms of sensitivity, specificity, reliability, cost, etc.
  - Light sensor: A device that measures the intensity or color of light. There are different types of light sensors such as photodiodes, phototransistors, photovoltaic cells, color sensors, etc. Each type has its own advantages and disadvantages in terms of accuracy, range, response time, cost, etc.



# How to use control web camera, network, and relays connected to the Pi

- A web camera is a device that captures images or videos and sends them to a computer or a network. A web camera can be connected to the Pi using a USB cable or a wireless connection.
- A network is a system of devices that communicate with each other using protocols and standards. A network can be wired or wireless, local or global, private or public. A network can be connected to the Pi using an Ethernet cable, a Wi-Fi adapter, or a Bluetooth module.
- A relay is a device that switches an electric circuit on or off by using an electromagnet. A relay can be connected to the Pi using GPIO pins, a breadboard, and jumper wires.

To use control web camera, network, and relays connected to the Pi, you need to:

- Install the necessary software and drivers for the web camera, the network, and the relays on the Pi. You can use the command `sudo apt-get update` and `sudo apt-get install` to install the packages from the terminal.
- Configure the settings and parameters for the web camera, the network, and the relays on the Pi. You can use the command `raspi-config` to access the configuration menu from the terminal, or use the graphical user interface (GUI) to change the settings from the desktop.
- Write a program or a script to control the web camera, the network, and the relays on the Pi. You can use any programming language that supports the Pi, such as Python, C, or Java. You can use the libraries and modules that provide the functions and methods to interact with the web camera, the network, and the relays, such as `picamera`, `socket`, or `RPi.GPIO`.
- Run the program or the script on the Pi and test the functionality of the web camera, the network, and the relays. You can use the command `python`, `gcc`, or `javac` to run the program or the script from the terminal, or use the IDE or the editor to run the program or the script from the desktop. You can use the monitor, the keyboard, and the mouse to view the output and input the commands, or use a remote access tool such as `ssh` or `vnc` to control the Pi from another device.



# 1. Start Raspberry Pi and try various Linux commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small, low-cost computer that can run Linux and other operating systems. It can be used for various projects, such as robotics, gaming, web development, etc.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard, and a mouse. You also need to insert a microSD card with a Linux operating system installed on it. The Raspberry Pi will boot up and display a desktop environment or a command line interface, depending on the operating system you chose.
- To access the command terminal window, you can either press Ctrl+Alt+T on the keyboard, or click on the terminal icon on the desktop or the menu bar. The command terminal window is where you can type and execute Linux commands to perform various tasks on the Raspberry Pi.
- Linux commands are case-sensitive, meaning that uppercase and lowercase letters are treated differently. For example, `ls` and `LS` are not the same command. Linux commands also have options or flags that modify their behavior, such as `-a` or `-l`. Options are usually preceded by a dash (-) or two dashes (--). For example, `ls -a` or `ls --all` will list all files and directories, including hidden ones, in the current directory.
- Some of the most common and useful Linux commands are:

  - `ls`: lists the files and directories in the current directory. You can use options such as `-a`, `-l`, `-h`, etc. to change the output format. You can also specify a different directory to list, such as `ls /home/pi` or `ls ..`.
  - `cd`: changes the current directory to the one specified. For example, `cd /home/pi` will change the current directory to `/home/pi`. You can also use `cd ..` to go up one level, or `cd ~` to go to your home directory.
  - `touch`: creates a new, empty file with the name specified. For example, `touch hello.txt` will create a file named `hello.txt` in the current directory. You can also use `touch` to update the timestamp of an existing file, without changing its content.
  - `mv`: moves or renames a file or directory. For example, `mv hello.txt goodbye.txt` will rename the file `hello.txt` to `goodbye.txt`. You can also use `mv` to move a file or directory to a different location, such as `mv goodbye.txt /home/pi/Documents`.
  - `rm`: removes or deletes a file or directory. For example, `rm goodbye.txt` will delete the file `goodbye.txt`. You can use options such as `-i`, `-f`, `-r`, etc. to change the behavior of `rm`. For example, `rm -i goodbye.txt` will prompt you for confirmation before deleting the file, `rm -f goodbye.txt` will force the deletion without prompting, and `rm -r Documents` will delete the directory `Documents` and all its contents recursively.
  - `man`: displays the manual page for a command or a topic. For example, `man ls` will show you the usage, options, and examples of the `ls` command. You can use the arrow keys, Page Up, Page Down, Home, End, etc. to scroll through the manual page. You can also use `/` to search for a keyword, such as `/hidden`. To exit the manual page, press `q`.

- To practice using these commands, you can create, move, rename, delete, and list files and directories on your Raspberry Pi. You can also use `man` to learn more about other commands and topics.



# Linux Commands

## mkdir
- mkdir stands for make directory.
- It is used to create new directories in the file system.
- Syntax: `mkdir [options] directory_name`
- Options:
  - `-p`: create parent directories if they do not exist.
  - `-v`: print a message for each created directory.
  - `-m`: set the mode (permissions) of the created directory.

## rmdir
- rmdir stands for remove directory.
- It is used to delete empty directories from the file system.
- Syntax: `rmdir [options] directory_name`
- Options:
  - `-p`: remove directory and its ancestors if they are empty.
  - `-v`: print a message for each removed directory.

## tar
- tar stands for tape archive.
- It is used to create or extract compressed archive files.
- Syntax: `tar [options] [archive_file] [file_list]`
- Options:
  - `-c`: create a new archive file.
  - `-x`: extract files from an archive file.
  - `-f`: specify the name of the archive file.
  - `-v`: print the names of the files being processed.
  - `-z`: use gzip compression or decompression.
  - `-j`: use bzip2 compression or decompression.

## gzip
- gzip stands for GNU zip.
- It is used to compress or decompress files using the Lempel-Ziv coding (LZ77) algorithm.
- Syntax: `gzip [options] file_name`
- Options:
  - `-c`: write the compressed output to standard output.
  - `-d`: decompress the file instead of compressing it.
  - `-k`: keep the original file and create a new compressed file.
  - `-l`: list the compressed file name, size, ratio, and uncompressed size.
  - `-r`: recursively compress or decompress files in directories.

## cat
- cat stands for concatenate.
- It is used to read, write, or append data to files or standard input/output.
- Syntax: `cat [options] file_name`
- Options:
  - `-n`: number the output lines starting from 1.
  - `-b`: number the non-blank output lines starting from 1.
  - `-s`: suppress repeated empty output lines.
  - `-E`: display a $ at the end of each line.
  - `-T`: display TAB characters as ^I.

## more
- more is a command that displays the contents of a file or standard input one screen at a time.
- Syntax: `more [options] file_name`
- Options:
  - `-d`: display a help message at the bottom of the screen.
  - `-l`: ignore form feed characters (^L) in the file.
  - `-s`: squeeze multiple blank lines into one.
  - `-u`: suppress underlining and bolding of text.
- Commands:
  - `Space`: display the next screen of text.
  - `Enter`: display the next line of text.
  - `b`: go back one screen of text.
  - `q`: quit more and return to the shell.

## less
- less is a command that displays the contents of a file or standard input one screen at a time, with more features than more.
- Syntax: `less [options] file_name`
- Options:
  - `-N`: display line numbers at the beginning of each line.
  - `-i`: ignore case in searches.
  - `-S`: chop long lines instead of wrapping them.
  - `-X`: do not clear the screen after quitting less.
- Commands:
  - `Space`: display the next screen of text.
  - `Enter`: display the next line of text.
  - `b`: go back one screen of text.
  - `q`: quit less and return to the shell.
  - `/pattern`: search forward for a pattern in the file.
  - `?pattern`: search backward for a pattern in the file.
  - `n`: repeat the previous search in the same direction.
  - `N`: repeat the previous search in the opposite direction.

## ps
- ps stands for process status.
- It is used to display information about the processes running on the system.
- Syntax: `ps [options]`
- Options:
  - `-e`: display information about all processes.
  - `-f`: display full format listing, including command line arguments and parent process ID.
  - `-l`: display long format listing, including priority, nice value, and memory usage.
  - `-u user`: display information about processes owned by a specific user.
  - `-p pid`: display information about a specific process ID.



# 2. Run some python programs on Pi like:

- Python is a popular programming language that can be used to create various applications on the Raspberry Pi, such as games, web servers, robots, etc.
- To run a python program on the Pi, you need to have a python interpreter installed on the Pi. The Pi comes with two versions of python: python 2 and python 3. You can check which version you have by typing `python --version` or `python3 --version` in the terminal.
- To write a python program, you can use any text editor, such as nano, vim, or IDLE. IDLE is an integrated development environment (IDE) for python that provides syntax highlighting, debugging, and other features. You can launch IDLE by typing `idle` or `idle3` in the terminal, depending on the python version you want to use.
- To save a python program, you need to give it a name with the `.py` extension, such as `hello.py`. You can save the program in any directory, but it is recommended to create a separate folder for your python projects, such as `~/python_projects`.
- To run a python program, you need to navigate to the directory where you saved the program, and then type `python hello.py` or `python3 hello.py` in the terminal, depending on the python version you used to write the program. You can also run the program from IDLE by pressing F5 or clicking on Run -> Run Module.
- A simple python program that prints "Hello, world!" to the screen is:

```python
# This is a comment. Comments start with a # symbol and are ignored by the interpreter.
# The first line of a python program is usually a shebang line that tells the operating system which interpreter to use.
# The shebang line is optional, but it is good practice to include it.
# The shebang line for python 2 is #!/usr/bin/env python
# The shebang line for python 3 is #!/usr/bin/env python3

# The print function is used to display output to the screen.
# In python 2, print is a statement and does not need parentheses.
# In python 3, print is a function and needs parentheses.
# To make the program compatible with both versions, you can use parentheses for print.

print("Hello, world!")
```

- Some examples of python programs that you can run on the Pi are:

  - A program that blinks an LED connected to the Pi's GPIO pin 17:

  ```python
  #!/usr/bin/env python3

  # Import the GPIO library
  import RPi.GPIO as GPIO
  # Import the time library
  import time

  # Set the GPIO mode to BCM
  GPIO.setmode(GPIO.BCM)
  # Set the GPIO pin 17 as output
  GPIO.setup(17, GPIO.OUT)

  # Create a loop that runs forever
  while True:
    # Turn on the LED
    GPIO.output(17, GPIO.HIGH)
    # Wait for one second
    time.sleep(1)
    # Turn off the LED
    GPIO.output(17, GPIO.LOW)
    # Wait for one second
    time.sleep(1)
  ```

  - A program that displays the current date and time on the Pi's Sense HAT LED matrix:

  ```python
  #!/usr/bin/env python3

  # Import the Sense HAT library
  from sense_hat import SenseHat
  # Import the datetime library
  from datetime import datetime

  # Create a Sense HAT object
  sense = SenseHat()

  # Create a loop that runs forever
  while True:
    # Get the current date and time
    now = datetime.now()
    # Format the date and time as a string
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    # Display the date and time on the LED matrix
    sense.show_message(date_time)
  ```

  - A program that plays a random sound from a list of sound files stored in a folder:

  ```python
  #!/usr/bin/env python3

  # Import the pygame library
  import pygame
  # Import the random library
  import random
  # Import the os library
  import os

  # Initialize the pygame mixer
  pygame.mixer.init()
  # Create a list of sound files in the sounds folder
  sounds = os.listdir("sounds")
  # Remove any files that are not .wav or .mp3
  sounds = [s for s in sounds if s.endswith(".wav") or s.endswith(".mp3")]

```




# Read your name and print Hello message with name

- This is a basic programming task that can be done in different languages such as Python, Java, C++, etc.
- The task involves two steps: reading the user's input and printing the output.
- Reading the user's input means taking a string value from the keyboard or the console and storing it in a variable.
- Printing the output means displaying a message on the screen or the console that includes the user's input.
- The syntax and the functions for reading and printing may vary depending on the language.
- Here are some examples of how to do this task in different languages:

## Python
- In Python, we can use the `input()` function to read the user's input and store it in a variable.
- We can use the `print()` function to print the output and concatenate the user's input with the string `"Hello"` using the `+` operator.
- For example:

```python
# Read the user's name and store it in a variable called name
name = input("Enter your name: ")

# Print the output with the user's name
print("Hello " + name)
```

## Java
- In Java, we can use the `Scanner` class to read the user's input and store it in a variable.
- We need to import the `java.util.Scanner` package and create an object of the `Scanner` class.
- We can use the `nextLine()` method to read the user's input as a string and store it in a variable.
- We can use the `System.out.println()` method to print the output and concatenate the user's input with the string `"Hello"` using the `+` operator.
- For example:

```java
// Import the Scanner class
import java.util.Scanner;

// Create a Scanner object
Scanner sc = new Scanner(System.in);

// Read the user's name and store it in a variable called name
System.out.print("Enter your name: ");
String name = sc.nextLine();

// Print the output with the user's name
System.out.println("Hello " + name);
```

## C++
- In C++, we can use the `cin` object to read the user's input and store it in a variable.
- We need to include the `<iostream>` header file and use the `std` namespace.
- We can use the `getline()` function to read the user's input as a string and store it in a variable.
- We can use the `cout` object to print the output and concatenate the user's input with the string `"Hello"` using the `<<` operator.
- For example:

```cpp
// Include the iostream header file
#include <iostream>

// Use the std namespace
using namespace std;

// Read the user's name and store it in a variable called name
cout << "Enter your name: ";
string name;
getline(cin, name);

// Print the output with the user's name
cout << "Hello " << name << endl;
```



# b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the input() function in Python, which returns a string that can be converted to a numeric type such as int or float.
- To print the sum, difference, product and division of two numbers, we can use the arithmetic operators +, -, *, and / in Python, which perform the corresponding operations on the operands and return the result.
- To print the result, we can use the print() function in Python, which displays the value of the expression inside the parentheses to the standard output.
- For example, if we want to read two numbers x and y and print their sum, difference, product and division, we can write the following code in Python:

```python
# Read two numbers
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Print their sum, difference, product and division
print("The sum of", x, "and", y, "is", x + y)
print("The difference of", x, "and", y, "is", x - y)
print("The product of", x, "and", y, "is", x * y)
print("The division of", x, "and", y, "is", x / y)
```

- The output of the code will depend on the values entered by the user. For example, if the user enters 10 and 5, the output will be:

```
Enter the first number: 10
Enter the second number: 5
The sum of 10 and 5 is 15
The difference of 10 and 5 is 5
The product of 10 and 5 is 50
The division of 10 and 5 is 2.0
```



# Word and character count of a given string

- A string is a sequence of characters, such as "Hello, world!" or "This is a sentence.".
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "world" or "sentence".
- A character is a single symbol, such as "H" or "!" or ".".
- To count the number of words and characters in a given string, we can use the following steps:

  - Initialize two variables, word_count and char_count, to zero.
  - Loop through each character in the string, using a variable i to keep track of the index.
  - If the character at index i is a space or a punctuation mark, and the character at index i-1 is not a space or a punctuation mark, then increment word_count by one. This means we have reached the end of a word.
  - Increment char_count by one for every character in the string, regardless of whether it is a space or a punctuation mark or not. This means we are counting all the symbols in the string.
  - After the loop ends, check if the last character in the string is not a space or a punctuation mark. If so, increment word_count by one, since we have one more word at the end of the string that was not counted by the loop.
  - Return word_count and char_count as the final results.

- For example, given the string "Hello, world! This is a sentence.", we can apply the steps as follows:

  - word_count = 0, char_count = 0
  - i = 0, character = "H", char_count = 1
  - i = 1, character = "e", char_count = 2
  - i = 2, character = "l", char_count = 3
  - i = 3, character = "l", char_count = 4
  - i = 4, character = "o", char_count = 5
  - i = 5, character = ",", char_count = 6, word_count = 1 (since the previous character was not a space or a punctuation mark)
  - i = 6, character = " ", char_count = 7
  - i = 7, character = "w", char_count = 8
  - i = 8, character = "o", char_count = 9
  - i = 9, character = "r", char_count = 10
  - i = 10, character = "l", char_count = 11
  - i = 11, character = "d", char_count = 12
  - i = 12, character = "!", char_count = 13, word_count = 2 (since the previous character was not a space or a punctuation mark)
  - i = 13, character = " ", char_count = 14
  - i = 14, character = "T", char_count = 15
  - i = 15, character = "h", char_count = 16
  - i = 16, character = "i", char_count = 17
  - i = 17, character = "s", char_count = 18
  - i = 18, character = " ", char_count = 19, word_count = 3 (since the previous character was not a space or a punctuation mark)
  - i = 19, character = "i", char_count = 20
  - i = 20, character = "s", char_count = 21
  - i = 21, character = " ", char_count = 22, word_count = 4 (since the previous character was not a space or a punctuation mark)
  - i = 22, character = "a", char_count = 23
  - i = 23, character = " ", char_count = 24, word_count = 5 (since the previous character was not a space or a punctuation mark)
  - i = 24, character = "s", char_count = 25
  - i = 25, character = "e", char_count = 26
  - i = 26, character = "n", char_count = 27
  - i = 27, character = "t", char_count = 28
  - i = 28, character = "e", char_count = 29
  - i = 29, character = "n", char_count = 30
  - i = 30, character = "c", char_count



# Area of a given shape (rectangle, triangle and circle) reading shape and appropriate values from standard

- The area of a shape is the amount of space that it covers.
- Different shapes have different formulas for calculating their areas.
- To find the area of a given shape, we need to read the shape name and the appropriate values from the standard input, such as length, width, base, height, or radius.
- Here are some examples of how to find the area of a rectangle, a triangle, and a circle.

## Area of a rectangle

- A rectangle is a four-sided shape with opposite sides equal and right angles.
- The area of a rectangle is given by the formula: `Area = length * width`
- To find the area of a rectangle, we need to read the length and the width from the standard input, and then multiply them.
- For example, if the length is 10 units and the width is 5 units, then the area is 10 * 5 = 50 square units.

## Area of a triangle

- A triangle is a three-sided shape with three angles.
- The area of a triangle is given by the formula: `Area = (base * height) / 2`
- To find the area of a triangle, we need to read the base and the height from the standard input, and then multiply them and divide by 2.
- For example, if the base is 12 units and the height is 9 units, then the area is (12 * 9) / 2 = 54 square units.

## Area of a circle

- A circle is a shape with a curved boundary that is equidistant from a fixed point called the center.
- The area of a circle is given by the formula: `Area = pi * radius * radius`
- To find the area of a circle, we need to read the radius from the standard input, and then multiply it by itself and by pi, which is approximately 3.14.
- For example, if the radius is 7 units, then the area is 3.14 * 7 * 7 = 153.86 square units.



# Input

- Input is the process of receiving data or information from an external source, such as a user, a device, a file, or a network.
- Input can be categorized into different types, such as:
  - Keyboard input: The user enters data or commands using a keyboard, such as typing text, numbers, or symbols.
  - Mouse input: The user interacts with a graphical user interface (GUI) using a mouse, such as clicking, dragging, or scrolling.
  - Touch input: The user touches a screen or a surface with one or more fingers, such as tapping, swiping, or pinching.
  - Voice input: The user speaks to a microphone or a device, such as dictating text, asking questions, or giving commands.
  - Scanner input: The device scans an image or a document and converts it into digital data, such as scanning a barcode, a photo, or a text.
  - Camera input: The device captures an image or a video and stores it as digital data, such as taking a picture, recording a video, or scanning a face.
  - Sensor input: The device measures a physical quantity or a condition and converts it into digital data, such as measuring temperature, pressure, motion, or light.
- Input can be used for different purposes, such as:
  - Data entry: The user or the device enters data into a system or a program, such as filling a form, entering a password, or uploading a file.
  - Data processing: The system or the program processes the input data and produces an output, such as calculating a result, displaying a message, or generating a report.
  - Data communication: The system or the program sends or receives input data over a network, such as sending an email, downloading a file, or streaming a video.
  - Data storage: The system or the program saves the input data in a memory or a disk, such as saving a document, creating a backup, or archiving a record.
  - Data analysis: The system or the program analyzes the input data and extracts useful information, such as finding patterns, trends, or anomalies.
  - Data visualization: The system or the program presents the input data in a graphical or a numerical form, such as creating a chart, a table, or a map.



# 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- To write a python program, you need to use a text editor such as nano, vim, or idle. You can launch any of these editors from the terminal by typing their name followed by the name of the file you want to create or edit. For example, `nano hello.py` will open a new file called hello.py in nano editor.
- To save and exit the editor, you need to use the keyboard shortcuts specific to each editor. For nano, you can press Ctrl+X, then Y, then Enter. For vim, you can press Esc, then :wq, then Enter. For idle, you can click on File, then Save, then Quit.
- To run the python program, you need to type `python3` followed by the name of the file in the terminal. For example, `python3 hello.py` will run the hello.py program.
- To print a name 'n' times, where name and n are read from standard input, you need to use the `input` function to get the user input, and the `print` function to display the output. You also need to use a `for` loop to repeat the print statement n times. Here is an example of a python program that does this:

```python
# get the name from the user
name = input("Enter your name: ")

# get the number of times to print from the user
n = int(input("Enter the number of times to print: "))

# use a for loop to print the name n times
for i in range(n):
    print(name)
```

- To test the program, you can run it and enter some values for the name and n. For example, if you enter Alice and 3, you should see the following output:

```text
Enter your name: Alice
Enter the number of times to print: 3
Alice
Alice
Alice
```



# Using for and while loops

- A for loop is a control structure that allows you to repeat a block of code a fixed number of times.
- A while loop is a control structure that allows you to repeat a block of code as long as a condition is true.
- The syntax of a for loop is:

```python
for variable in iterable:
    # do something with variable
```

- The syntax of a while loop is:

```python
while condition:
    # do something
```

- An iterable is an object that can be iterated over, such as a list, a string, a range, etc.
- A condition is an expression that evaluates to a boolean value (True or False).
- You can use the break statement to exit a loop prematurely, and the continue statement to skip the current iteration and move to the next one.

# Handling Divided by Zero Exception

- An exception is an error that occurs during the execution of a program, and interrupts the normal flow of control.
- A divided by zero exception is an error that occurs when you try to divide a number by zero, which is mathematically undefined.
- In Python, a divided by zero exception is represented by the ZeroDivisionError class, which inherits from the ArithmeticError class, which in turn inherits from the Exception class.
- You can handle exceptions using the try-except-finally construct, which has the following syntax:

```python
try:
    # try to execute some code that may raise an exception
except ExceptionType as e:
    # handle the exception of type ExceptionType
    # e is the exception object that contains information about the error
finally:
    # execute some code that will always run, regardless of whether an exception occurred or not
```

- You can have multiple except clauses to handle different types of exceptions, or use a generic except clause to catch any exception.
- The finally clause is optional, but useful for performing cleanup actions or releasing resources.
- To handle a divided by zero exception, you can use the following code:

```python
try:
    # try to divide two numbers
    result = num1 / num2
except ZeroDivisionError as e:
    # handle the divided by zero exception
    print("Cannot divide by zero")
    print(e)
finally:
    # execute some code that will always run
    print("End of program")
```

# Printing current time for 10 times with an interval of 1 second

- To print the current time, you can use the datetime module, which provides various classes and functions for working with dates and times.
- To import the datetime module, you can use the following statement:

```python
import datetime
```

- To get the current date and time as a datetime object, you can use the datetime.now() function, which returns a datetime object with the current local date and time.
- To format a datetime object as a string, you can use the strftime() method, which takes a format string as an argument and returns a formatted string according to the given format.
- To pause the execution of a program for a certain amount of time, you can use the time module, which provides various functions for working with time.
- To import the time module, you can use the following statement:

```python
import time
```

- To sleep for a specified number of seconds, you can use the time.sleep() function, which takes a number of seconds as an argument and suspends the execution of the current thread for that duration.
- To print the current time for 10 times with an interval of 1 second, you can use the following code:

```python
import datetime
import time

# use a for loop to repeat 10 times
for i in range(10):
    # get the current date and time as a datetime object
    now = datetime.datetime.now()
    # format the datetime object as a string
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    # print the formatted string
    print(formatted_now)
    # sleep for 1 second
    time.sleep(1)
```



# How to read a file line by line and print the word count of each line

- To read a file line by line, we need to open the file in read mode and use a loop to iterate over the lines of the file.
- To print the word count of each line, we need to split the line by whitespace characters and count the length of the resulting list.
- Here is an example of how to do this in Python:

```python
# Open the file in read mode
file = open("example.txt", "r")

# Loop over the lines of the file
for line in file:
  # Split the line by whitespace characters
  words = line.split()
  # Count the length of the list
  word_count = len(words)
  # Print the word count of the line
  print(word_count)

# Close the file
file.close()
```



# Light an LED through Python program

- To light an LED through Python program, you need to have a hardware device that can communicate with your computer and control the LED. For example, you can use an Arduino, a Raspberry Pi, or a MicroPython board.
- Depending on the device you use, you need to install the appropriate software and libraries to interact with it from Python. For example, you can use the `pyserial` library to communicate with the Arduino, the `RPi.GPIO` library to control the Raspberry Pi's GPIO pins, or the `pyb` module to access the MicroPython board's features.
- You also need to wire the LED to the device using a resistor, wires and a breadboard. The resistor is needed to limit the current and protect the LED from burning out. The breadboard is a convenient way to connect the components without soldering. The wiring diagram may vary depending on the device and the pin you use, but a typical example is shown below:

Wiring diagram for LED and Raspberry Pi

- In this example, the LED is connected to the GPIO pin 18 of the Raspberry Pi, and the other end is connected to the ground (GND) pin. The resistor is connected in series with the LED, and its value can be between 220 and 1000 ohms.
- To control the LED from Python, you need to write a program that imports the library for your device, sets up the pin as an output, and turns it on and off using a loop or a user input. For example, the following program will blink the LED on and off once every second using the Raspberry Pi:

```python
# Import the RPi.GPIO library
import RPi.GPIO as GPIO
# Import the time library
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
# Set the pin 18 as an output
GPIO.setup(18, GPIO.OUT)

# Loop forever
while True:
  # Turn the LED on
  GPIO.output(18, GPIO.HIGH)
  # Wait for one second
  time.sleep(1)
  # Turn the LED off
  GPIO.output(18, GPIO.LOW)
  # Wait for one second
  time.sleep(1)
```

- To run the program, you need to save it as a file, such as `LED.py`, and execute it from the terminal using the command `sudo python LED.py`. You should see the LED blinking on and off once every second.
- To stop the program, you can press `Ctrl+C` on the keyboard, or close the terminal window. You should also clean up the GPIO pins by adding the line `GPIO.cleanup()` at the end of the program, or by running it separately from the Python shell.
- You can modify the program to change the blinking pattern, the pin number, or the user input. For example, you can use the `input()` function to ask the user to enter `L` or `H` to turn the LED on and off, or use the `random` library to generate random intervals for the blinking. You can also use multiple LEDs and pins to create more complex patterns or effects.



# Get input from two switches and switch on corresponding LEDs

- This topic is about how to use two switches and two LEDs to create a simple logic circuit that can perform basic operations such as AND, OR, XOR, etc.
- To get input from two switches, we need to connect them to two digital pins on an Arduino board, such as pin 2 and pin 3. We also need to enable the internal pull-up resistors for these pins, so that they will read HIGH when the switches are open and LOW when they are closed.
- To switch on corresponding LEDs, we need to connect them to two other digital pins on the Arduino board, such as pin 8 and pin 9. We also need to add current-limiting resistors in series with the LEDs, to prevent them from burning out.
- The code for this project is as follows:

```c
// Define the pin numbers for the switches and LEDs
const int switch1 = 2;
const int switch2 = 3;
const int led1 = 8;
const int led2 = 9;

void setup() {
  // Set the switch pins as inputs with pull-up resistors
  pinMode(switch1, INPUT_PULLUP);
  pinMode(switch2, INPUT_PULLUP);
  // Set the LED pins as outputs
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  // Read the state of the switches
  int state1 = digitalRead(switch1);
  int state2 = digitalRead(switch2);
  // Perform a logic operation on the switch states and write the result to the LEDs
  // For example, this is an AND operation
  digitalWrite(led1, state1 && state2);
  // For example, this is an OR operation
  digitalWrite(led2, state1 || state2);
  // You can also try other operations such as XOR, NAND, NOR, etc.
}
```
- The circuit diagram for this project is as follows:

```markdown
Circuit diagram
```

- The circuit diagram shows how to connect the switches and LEDs to the Arduino board using a breadboard and jumper wires. The switches are connected to pins 2 and 3, and the LEDs are connected to pins 8 and 9, with 220 ohm resistors in series. The Arduino board is powered by a USB cable or a battery.

- The expected output of this project is as follows:

```markdown
| Switch 1 | Switch 2 | LED 1 | LED 2 |
|----------|----------|-------|-------|
|    0     |    0     |   0   |   0   |
|    0     |    1     |   0   |   1   |
|    1     |    0     |   0   |   1   |
|    1     |    1     |   1   |   1   |
```

- The output table shows the state of the LEDs for each combination of the switch states. LED 1 performs an AND operation, and LED 2 performs an OR operation. You can change the code to perform other operations and see the results on the LEDs.



# Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, some wires, and a file that contains the on time and off time values in milliseconds.
- The microcontroller is a device that can run a program to control the output pins, which can be connected to the LED. The resistor is used to limit the current flowing through the LED and protect it from burning out. The breadboard is a platform that allows us to connect the components easily. The wires are used to make the connections between the components and the microcontroller.
- The file that contains the on time and off time values can be stored in the microcontroller's memory or on an external storage device, such as a microSD card. The file can have any name and format, as long as the program can read it and extract the values. For example, the file can be a text file with two numbers separated by a comma, such as `1000,500`, which means the LED should be on for 1000 milliseconds and off for 500 milliseconds.
- The program that runs on the microcontroller can be written in any programming language that is compatible with the microcontroller, such as C, Python, or Arduino. The program should perform the following steps:
  - Initialize the output pin that is connected to the LED and set it to low (off) state.
  - Open the file that contains the on time and off time values and read the values into two variables, such as `onTime` and `offTime`.
  - Start a loop that repeats indefinitely or until a condition is met, such as a button press or a sensor input.
  - Inside the loop, set the output pin to high (on) state and wait for `onTime` milliseconds.
  - Then, set the output pin to low (off) state and wait for `offTime` milliseconds.
  - End the loop and close the file.
- The following is an example of a program written in Arduino that flashes an LED at a given on time and off time cycle, where the two times are taken from a file named `times.txt` stored on a microSD card. The LED is connected to pin 13 and a microSD card module is connected to pins 10, 11, 12, and 4.

```c
// Include the library for the microSD card module
#include <SPI.h>
#include <SD.h>

// Define the output pin for the LED
#define LED_PIN 13

// Define the chip select pin for the microSD card module
#define CS_PIN 4

// Define the variables for the on time and off time
int onTime = 0;
int offTime = 0;

// Define the file object for the file that contains the times
File timesFile;

void setup() {
  // Initialize the output pin and set it to low
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  // Initialize the serial monitor for debugging
  Serial.begin(9600);

  // Initialize the microSD card module
  if (!SD.begin(CS_PIN)) {
    // If the initialization fails, print an error message and stop the program
    Serial.println("Card initialization failed!");
    return;
  }

  // Open the file that contains the times
  timesFile = SD.open("times.txt");

  // If the file is opened successfully, read the times into the variables
  if (timesFile) {
    // Read the first number until the comma and convert it to an integer
    onTime = timesFile.parseInt();

    // Read the second number until the end of the line and convert it to an integer
    offTime = timesFile.parseInt();

    // Print the times for debugging
    Serial.print("On time: ");
    Serial.println(onTime);
    Serial.print("Off time: ");
    Serial.println(offTime);

    // Close the file
    timesFile.close();
  }
  else {
    // If the file cannot be opened, print an error message and stop the program
    Serial.println("File not found!");
    return;
  }
}

void loop() {
  // Set the output pin to high and wait for the on time
  digitalWrite(LED_PIN, HIGH);
  delay(onTime);

  // Set the output pin to low and wait for the off time
  digitalWrite(LED_PIN, LOW);
  delay(offTime);
}
```



# Flash an LED based on cron output (acts as an alarm)

- To flash an LED based on cron output, we need to use a Raspberry Pi, an LED, a resistor, some jumper wires, and a breadboard.
- A Raspberry Pi is a small computer that can run Linux and interact with hardware devices through its GPIO pins.
- An LED is a light-emitting diode that can turn on and off when current flows through it.
- A resistor is a component that limits the current flow and protects the LED from burning out.
- A breadboard is a board that allows us to connect components without soldering.
- Jumper wires are wires that can connect the components on the breadboard and the Raspberry Pi.
- Cron is a Linux utility that can schedule tasks to run at specific times or intervals.
- To flash an LED based on cron output, we need to do the following steps:

  1. Connect the LED and the resistor to the breadboard and the Raspberry Pi. The positive leg of the LED (the longer one) should go to a GPIO pin (for example, pin 18) and the negative leg (the shorter one) should go to the resistor. The other end of the resistor should go to a ground pin (for example, pin 6).
  2. Write a Python script that can control the LED. The script should import the GPIO library, set the pin mode to BCM, and set the LED pin as an output. Then, it should use a loop to turn the LED on and off with a delay. For example:

```python
import RPi.GPIO as GPIO
import time

LED_PIN = 18 # change this to the pin you are using
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
  GPIO.output(LED_PIN, GPIO.HIGH) # turn on the LED
  time.sleep(1) # wait for 1 second
  GPIO.output(LED_PIN, GPIO.LOW) # turn off the LED
  time.sleep(1) # wait for 1 second
```
  3. Save the script as led.py and make it executable with the command `chmod +x led.py`.
  4. Test the script by running it with the command `./led.py`. You should see the LED flashing on and off every second.
  5. To schedule the script to run at a specific time or interval, we need to use cron. To edit the cron table, use the command `crontab -e`. This will open a text editor where you can add your cron jobs. A cron job has the following format:

```bash
minute hour day month weekday command
```
  - minute: the minute when the command should run (0-59)
  - hour: the hour when the command should run (0-23)
  - day: the day of the month when the command should run (1-31)
  - month: the month when the command should run (1-12)
  - weekday: the day of the week when the command should run (0-6, where 0 is Sunday)
  - command: the command to execute

  For example, to run the led.py script every day at 8:00 AM, we can add the following line to the cron table:

```bash
0 8 * * * /home/pi/led.py
```
  6. Save and exit the cron table. The cron job will be activated and the LED will flash at the specified time. To stop the LED from flashing, we can either kill the script process or remove the cron job.



# Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

- A relay is an electromechanical device that can be used to switch on or off a load (such as a light, a fan, a motor, etc.) by applying a voltage to its coil terminals.
- A cron is a software utility that can be used to schedule commands or scripts to run at a specified time or interval on a Linux-based system.
- To switch on a relay at a given time using cron, the following steps are required:

  1. Connect the relay's coil terminals to a GPIO (General Purpose Input Output) pin and a ground pin of a microcontroller or a single-board computer (such as Arduino, Raspberry Pi, etc.) that can run Linux.
  2. Connect the relay's contact terminals to the load and a power source (such as a battery, a wall outlet, etc.) according to the relay's specifications and the load's requirements.
  3. Write a script or a command that can control the GPIO pin to turn on or off the relay by setting its output to high or low voltage. For example, in Python, the following code can be used to turn on a relay connected to GPIO pin 17:

     ```python
     import RPi.GPIO as GPIO # Import the GPIO library
     GPIO.setmode(GPIO.BCM) # Set the GPIO numbering mode to BCM
     GPIO.setup(17, GPIO.OUT) # Set GPIO pin 17 as an output
     GPIO.output(17, GPIO.HIGH) # Set GPIO pin 17 to high voltage
     ```

  4. Save the script or the command in a file (such as relay_on.py) and make it executable by running the following command in the terminal:

     ```bash
     chmod +x relay_on.py # Make the file executable
     ```

  5. Edit the crontab file by running the following command in the terminal:

     ```bash
     crontab -e # Edit the crontab file
     ```

  6. Add a line to the crontab file that specifies the time and the script or the command to run. For example, to run the relay_on.py script at 8:00 AM every day, the following line can be added:

     ```bash
     0 8 * * * /home/pi/relay_on.py # Run the relay_on.py script at 8:00 AM every day
     ```

  7. Save and exit the crontab file. The cron service will automatically run the script or the command at the specified time and switch on the relay.



# Get the status of a bulb at a remote place (on the LAN) through web

- To get the status of a bulb at a remote place (on the LAN) through web, we need to have the following components:
  - A bulb that can be controlled by a microcontroller such as Arduino or Raspberry Pi.
  - A microcontroller that can connect to the LAN and run a web server.
  - A device that can access the web server and send requests to the microcontroller.
- The steps to get the status of a bulb are as follows:
  - Connect the bulb to the microcontroller using a relay or a transistor circuit.
  - Connect the microcontroller to the LAN using an Ethernet shield or a Wi-Fi module.
  - Write a sketch or a program for the microcontroller that can read the state of the bulb (on or off) and send it as a response to a web request.
  - Upload the sketch or the program to the microcontroller and run it.
  - Find the IP address of the microcontroller on the LAN using a network scanner or a ping command.
  - On the device that can access the web server, open a web browser and enter the IP address of the microcontroller followed by a slash and a query parameter, such as `http://192.168.1.10/?status`.
  - The web browser will send a request to the microcontroller and receive a response that contains the status of the bulb, such as `ON` or `OFF`.
  - Display the status of the bulb on the web browser.



# Note: The Instructor may add/delete/modify/tune experiments

- This note implies that the instructor has the authority and discretion to change the experiments that are part of the course curriculum.
- The instructor may do so for various reasons, such as:
  - To align the experiments with the latest developments and trends in the field of study.
  - To accommodate the availability and suitability of the resources and equipment needed for the experiments.
  - To adjust the difficulty and complexity of the experiments according to the level and progress of the students.
  - To enhance the learning outcomes and objectives of the experiments.
- The instructor should communicate any changes to the experiments to the students in advance and provide clear instructions and expectations for the modified experiments.
- The instructor should also justify the rationale and benefits of the changes and address any questions or concerns that the students may have.
- The students should respect the instructor's decision and follow the guidelines and instructions for the experiments accordingly.
- The students should also be prepared to adapt to the changes and learn from the new or different experiments.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have not specified the topic you want to write about. Please enter the topic name after the colon:

The topic is:



# KOT 553 INTERNET OF THINGS LAB KCS

- Internet of Things (IoT) is the network of physical objects or things embedded with sensors, actuators, and software that enable them to exchange data with other devices or systems over the internet.
- IoT Lab is a place where students can learn and practice the concepts, principles, and challenges of IoT, as well as the functioning of hardware devices and sensors used for IoT applications.
- KOT 553 is a course code for Internet of Things Lab offered by the Department of Computer Science and Engineering (CSE) at Dr. A.P.J. Abdul Kalam Technical University (AKTU) in Lucknow, India.
- The course objectives are:
  - To provide hands-on experience on IoT devices and platforms.
  - To develop skills for designing, developing, and testing IoT applications.
  - To expose students to various IoT domains and use cases.
- The course outcomes are:
  - Students will be able to demonstrate basic concepts, principles, and challenges in IoT.
  - Students will be able to illustrate functioning of hardware devices and sensors used for IoT.
  - Students will be able to design and implement IoT applications using various platforms and tools.
  - Students will be able to analyze and evaluate the performance and security of IoT applications.
- The course syllabus covers the following topics:
  - Introduction to IoT: Definition, characteristics, architecture, components, applications, and challenges of IoT.
  - IoT Devices and Sensors: Types, features, functions, and interfacing of IoT devices and sensors such as Arduino, Raspberry Pi, ESP32, NodeMCU, etc.
  - IoT Platforms and Protocols: Overview, comparison, and usage of various IoT platforms and protocols such as AWS IoT, Google Cloud IoT, Azure IoT, MQTT, CoAP, HTTP, etc.
  - IoT Application Development: Steps, tools, and techniques for developing IoT applications using Arduino IDE, Python, Node-RED, etc.
  - IoT Application Domains: Examples and case studies of IoT applications in various domains such as smart home, smart city, smart agriculture, smart health, etc.
  - IoT Security and Privacy: Issues, threats, and solutions for ensuring security and privacy of IoT systems and data.
- The course assessment is based on the following components:
  - Lab Assignments: 10 marks
  - Mid Semester Exam: 15 marks
  - End Semester Exam: 25 marks
  - Total: 50 marks



## Course Outcome (CO) Bloom's Knowledge Level (KL)

- A course outcome (CO) is a statement that describes what a learner should be able to do or demonstrate after completing a course or a unit of instruction.
- A course outcome should be specific, measurable, achievable, relevant and time-bound (SMART).
- A course outcome should align with the course objectives, the program outcomes and the institutional mission and vision.
- A course outcome should be assessed using appropriate methods and tools to measure the learner's achievement and performance.
- Bloom's knowledge level (KL) is a classification of the cognitive domain of learning, which describes the types and levels of knowledge that learners can acquire and demonstrate.
- Bloom's knowledge level consists of six categories: remember, understand, apply, analyze, evaluate and create. Each category represents a different level of cognitive complexity and difficulty.
- Bloom's knowledge level can be used to design and assess course outcomes, by matching the verbs and actions in the outcome statements with the corresponding knowledge level.
- Bloom's knowledge level can also be used to guide the instructional strategies and activities, by providing a framework for selecting and sequencing the learning tasks and materials.
- Bloom's knowledge level can help learners to monitor and improve their own learning, by identifying their strengths and weaknesses and setting appropriate goals and strategies.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss.

Some possible responses for the topic are:

### At the end of the course, the student will be able to

- Apply the concepts and principles of the subject to solve problems and analyze situations.
- Demonstrate the skills and techniques required for the subject, such as experiments, calculations, simulations, etc.
- Communicate effectively the results and arguments of the subject, using appropriate terminology, formats, and references.
- Evaluate the validity, reliability, and limitations of the sources and methods used in the subject, and identify ethical and social implications.
- Compare and contrast different perspectives, approaches, and theories related to the subject, and develop critical thinking and creativity.



#### CO 1 Understand the concept of Internet of Things K3

- Internet of Things (IoT) is the interconnection of physical objects with computing devices, sensors, software and other technologies that enable them to communicate and exchange data over the internet or other networks .
- IoT allows information to be sent and received from objects and devices that are embedded in everyday objects, such as appliances, vehicles, wearables, etc .
- IoT enables remote monitoring, control, manipulation and analysis of the status and trends of such devices and objects.
- IoT can provide various benefits, such as improved efficiency, convenience, security, quality of life, etc., by automating tasks, optimizing processes, enhancing services, etc.
- IoT can also pose various challenges, such as privacy, security, interoperability, scalability, reliability, etc., by increasing the complexity, vulnerability, diversity and quantity of devices and data involved.



#### CO 2 Implement interfacing of various sensors with Arduino/Raspberry Pi K4, K5

- CO2 sensors are devices that can measure the concentration of carbon dioxide in the air. They are useful for monitoring air quality, plant growth, and chemical reactions.
- There are different types of CO2 sensors, such as electrochemical, infrared, and metal oxide. Each type has its own advantages and disadvantages, such as accuracy, sensitivity, power consumption, and cost.
- Arduino and Raspberry Pi are popular microcontroller platforms that can be used to interface with CO2 sensors and perform various tasks, such as data logging, display, and control.
- To interface a CO2 sensor with Arduino or Raspberry Pi, the following steps are required:

  - Choose a suitable CO2 sensor for your project. Some factors to consider are the output signal, the operating voltage, the measurement range, and the calibration method.
  - Connect the CO2 sensor to the Arduino or Raspberry Pi using the appropriate pins and wires. Depending on the type of sensor, you may need to use analog or digital pins, or a communication protocol such as I2C or UART.
  - Install the necessary libraries and drivers for the CO2 sensor. Some sensors may have official or third-party libraries that make it easier to use them with Arduino or Raspberry Pi. You can find these libraries online or in the Arduino IDE or Raspberry Pi OS.
  - Write the code to read the CO2 sensor data and perform the desired actions. You can use the examples provided by the libraries or write your own code. You can also use other components, such as LCD screens, LEDs, or buzzers, to display or alert the CO2 level.
  - Test and debug your code and circuit. Make sure the CO2 sensor is working properly and giving accurate readings. You can use a multimeter, a serial monitor, or a CO2 meter to verify the sensor output. You can also adjust the sensor settings, such as the sampling rate, the resolution, or the calibration, to improve the performance.

- Some examples of CO2 sensors that can be interfaced with Arduino or Raspberry Pi are:

  - Gravity: Analog CO2 Gas Sensor (MG-811 Sensor): This is an electrochemical sensor that outputs an analog voltage that varies with the CO2 concentration. It has a measurement range of 0-10000 ppm and a resolution of 10 ppm. It requires a 6 V power supply and a potentiometer to set the threshold voltage.
  - DFRobot Gravity: Analog Infrared CO2 Sensor for Arduino (400~5000 ppm): This is an infrared sensor that outputs an analog voltage that varies with the CO2 concentration. It has a measurement range of 400-5000 ppm and a resolution of 10 ppm. It requires a 5 V power supply and has a built-in temperature and humidity compensation.
  - Adafruit SCD-30 - NDIR CO2 Temperature and Humidity Sensor: This is an infrared sensor that outputs the CO2 concentration, temperature, and humidity via I2C. It has a measurement range of 400-10000 ppm and a resolution of 30 ppm. It requires a 3.3 V or 5 V power supply and has a built-in calibration and self-test function.



#### CO 3 Demonstrate the ability to transmit data wirelessly between different devices. K4

- Wireless data transmission is the process of sending and receiving data without using physical wires or cables.
- Wireless data transmission can be classified into two main types: radio frequency (RF) and optical.
- RF transmission uses electromagnetic waves to carry data through the air, such as Wi-Fi, Bluetooth, and cellular networks .
- Optical transmission uses light to send data, such as infrared, visible light, and laser .
- Some of the devices that use wireless data transmission are wireless phones, wireless adapters, wireless repeaters, and wireless routers .
- Wireless data transmission has some advantages and disadvantages over wired data transmission, such as mobility, flexibility, scalability, security, interference, and energy consumption .
- To demonstrate the ability to transmit data wirelessly between different devices, one should be able to:
  - Understand the basic principles and concepts of wireless data transmission, such as frequency, modulation, encoding, multiplexing, and encryption .
  - Identify and compare the different types and modes of wireless data transmission, such as RF and optical, analog and digital, simplex and duplex, point-to-point and point-to-multipoint, and broadcast and multicast  .
  - Select and use the appropriate wireless data transmission technology and device for a given scenario, such as Wi-Fi, Bluetooth, cellular, infrared, visible light, and laser  .
  - Configure and troubleshoot the wireless data transmission devices and networks, such as setting up the wireless access point, pairing the wireless devices, testing the wireless signal strength and quality, and resolving the wireless interference and security issues .
  - Evaluate and optimize the wireless data transmission performance and energy efficiency, such as measuring the wireless data rate, latency, reliability, and power consumption, and applying the wireless data compression, modulation, and coding techniques  .



#### CO 4 Show an ability to upload/download sensor data on cloud and server K2

- Sensor data is the information collected by various types of sensors that measure physical phenomena such as temperature, humidity, pressure, light, sound, motion, etc.
- Cloud and server are two types of platforms that can store and process sensor data remotely over the internet.
- Cloud is a network of servers that provide on-demand computing resources and services such as storage, databases, analytics, etc. Server is a single computer that hosts a specific application or service such as a web server, a database server, etc.
- To upload sensor data on cloud and server, one needs to follow these steps:
  - Connect the sensor to a device that can communicate with the internet, such as a microcontroller, a computer, a smartphone, etc.
  - Write a program or use an existing software to read the sensor data and format it in a suitable way, such as JSON, XML, CSV, etc.
  - Choose a cloud or server platform that can receive and store the sensor data, such as AWS, Google Cloud, Azure, Firebase, etc.
  - Establish a connection between the device and the cloud or server platform using a protocol such as HTTP, MQTT, CoAP, etc.
  - Send the sensor data to the cloud or server platform using a method such as POST, PUT, GET, etc.
  - Verify that the sensor data is successfully uploaded and stored on the cloud or server platform.
- To download sensor data from cloud and server, one needs to follow these steps:
  - Choose a device that can communicate with the internet, such as a computer, a smartphone, a tablet, etc.
  - Write a program or use an existing software to request and receive the sensor data from the cloud or server platform using a protocol such as HTTP, MQTT, CoAP, etc.
  - Choose a method to download the sensor data, such as GET, SUBSCRIBE, OBSERVE, etc.
  - Parse and process the sensor data in a suitable way, such as JSON, XML, CSV, etc.
  - Display or use the sensor data for further analysis, visualization, or action.



#### CO 5 Examine various SQL queries from MySQL database K4, K5

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- MySQL is one of the most popular open-source relational database management systems (RDBMS) that supports SQL.
- SQL queries are statements that specify what data to retrieve, insert, update, or delete from a database.
- SQL queries can be classified into four categories: Data Definition Language (DDL), Data Manipulation Language (DML), Data Query Language (DQL), and Data Control Language (DCL).
- DDL is used to define the structure and schema of the database, such as creating, altering, or dropping tables, indexes, views, etc.
- DML is used to manipulate the data in the database, such as inserting, updating, or deleting records, etc.
- DQL is used to query the data in the database, such as selecting, joining, filtering, sorting, grouping, etc.
- DCL is used to control the access and privileges of the database, such as granting, revoking, or denying permissions, etc.
- Some examples of SQL queries from MySQL database are:

  - To create a table named `students` with four columns: `id`, `name`, `age`, and `grade`:

    ```sql
    CREATE TABLE students (
      id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      age INT,
      grade CHAR(1)
    );
    ```

  - To insert a record into the `students` table with values: `1`, `Alice`, `18`, and `A`:

    ```sql
    INSERT INTO students (id, name, age, grade) VALUES (1, 'Alice', 18, 'A');
    ```

  - To select all the records from the `students` table:

    ```sql
    SELECT * FROM students;
    ```

  - To select only the `name` and `grade` columns from the `students` table where the `age` is greater than or equal to `20`:

    ```sql
    SELECT name, grade FROM students WHERE age >= 20;
    ```

  - To update the `grade` column of the `students` table to `B` where the `id` is `1`:

    ```sql
    UPDATE students SET grade = 'B' WHERE id = 1;
    ```

  - To delete the record from the `students` table where the `id` is `1`:

    ```sql
    DELETE FROM students WHERE id = 1;
    ```

  - To create a view named `top_students` that contains the `name` and `grade` columns of the `students` table where the `grade` is `A`:

    ```sql
    CREATE VIEW top_students AS
    SELECT name, grade FROM students WHERE grade = 'A';
    ```

  - To grant the `SELECT` and `UPDATE` privileges on the `students` table to a user named `bob`:

    ```sql
    GRANT SELECT, UPDATE ON students TO bob;
    ```



## DETAILED SYLLABUS

- A detailed syllabus is a document that outlines the topics, objectives, learning outcomes, assessment methods, and resources for a specific course or module.
- A detailed syllabus can help students to understand the expectations and requirements of the course, as well as to plan their study time and activities accordingly.
- A detailed syllabus can also help instructors to design and deliver the course in a coherent and consistent way, as well as to communicate with students and other stakeholders about the course content and goals.
- A detailed syllabus typically includes the following sections:

  - Course title, code, credits, and prerequisites
  - Instructor name, contact information, office hours, and communication policy
  - Course description, objectives, and learning outcomes
  - Course schedule, topics, and readings
  - Course policies, such as attendance, participation, late submission, academic integrity, etc.
  - Assessment methods, criteria, and weights
  - Grading scale and feedback policy
  - Required and recommended materials, such as textbooks, software, etc.
  - Additional resources, such as online platforms, library services, tutoring, etc.
  - Disclaimer and revision statement

- A detailed syllabus should be clear, concise, accurate, and updated. It should also be aligned with the course level, program outcomes, and institutional standards. It should reflect the instructor's teaching philosophy and approach, as well as the students' needs and interests. It should be distributed to the students at the beginning of the course and reviewed periodically throughout the course.



### The student should have hands on experience in using various sensors like temperature, humidity, smoke, light, etc. and

- understand the basic principles and working of each sensor
- learn how to connect the sensors to a microcontroller or a computer using appropriate wires, pins, and protocols
- learn how to read and process the sensor data using programming languages such as Python, C, or Arduino
- learn how to calibrate, test, and troubleshoot the sensors in case of errors or malfunctions
- learn how to use the sensor data for various applications such as monitoring, control, automation, or visualization
- learn how to integrate multiple sensors and combine their data for more complex tasks or systems
- learn how to document and present the sensor projects using diagrams, charts, graphs, or reports



### Should be able to use control web camera, network, and relays connected to the Pi.

- A web camera is a device that captures images or videos and sends them to a computer or a network.
- A network is a system of interconnected devices that can communicate and share data with each other.
- A relay is a device that switches an electric circuit on or off based on a signal from another device.
- A Pi is a small, low-cost computer that can run various operating systems and programs.
- To use control web camera, network, and relays connected to the Pi, one should:
  - Connect the web camera to the Pi using a USB cable or a wireless adapter.
  - Connect the Pi to the network using an Ethernet cable or a Wi-Fi dongle.
  - Connect the relays to the Pi using jumper wires and a breadboard.
  - Install the necessary software and libraries on the Pi to control the web camera, network, and relays.
  - Write a program or use an existing one to capture images or videos from the web camera, send or receive data over the network, and switch the relays on or off.
  - Run the program on the Pi and monitor the output on a screen or a web browser.



#### 1. Start Raspberry Pi and try various Linix commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small computer that can run Linux operating system and perform various tasks.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard and a mouse. You also need to insert a microSD card with a Linux operating system installed on it.
- Once Raspberry Pi boots up, you will see a desktop environment with various icons and menus. You can use the mouse and the keyboard to interact with the graphical user interface (GUI).
- To open a command terminal window, you can either click on the terminal icon on the desktop or the taskbar, or press Ctrl+Alt+T on the keyboard.
- A command terminal window is a text-based interface that allows you to enter commands and see the output. You can use various Linux commands to perform different operations on the files and directories on your Raspberry Pi.
- Some of the common Linux commands are:

  - `ls`: This command lists the files and directories in the current working directory. You can use various options with this command to change the format and the information displayed. For example, `ls -l` shows the long listing format with details such as permissions, size, owner, group, date and time of modification. `ls -a` shows the hidden files and directories that start with a dot (.). `ls -R` shows the files and directories recursively, that is, it also lists the contents of the subdirectories.
  - `cd`: This command changes the current working directory to the one specified as an argument. For example, `cd Documents` changes the current working directory to the Documents directory. You can use `cd ..` to go back to the parent directory, or `cd ~` to go to the home directory. You can also use absolute or relative paths with this command. For example, `cd /home/pi/Desktop` changes the current working directory to the Desktop directory in the home directory of the user pi. `cd ../Pictures` changes the current working directory to the Pictures directory in the same level as the current working directory.
  - `touch`: This command creates a new empty file with the name specified as an argument. For example, `touch test.txt` creates a new file named test.txt in the current working directory. You can also use this command to change the access and modification times of an existing file. For example, `touch -a test.txt` updates the access time of test.txt to the current time, and `touch -m test.txt` updates the modification time of test.txt to the current time.
  - `mv`: This command moves or renames a file or a directory. For example, `mv test.txt new.txt` renames the file test.txt to new.txt. `mv test.txt Documents` moves the file test.txt to the Documents directory. You can also use this command to move or rename multiple files or directories at once. For example, `mv test.txt new.txt Documents` moves and renames the file test.txt to new.txt in the Documents directory. `mv *.txt Documents` moves all the files with the .txt extension to the Documents directory.
  - `rm`: This command removes or deletes a file or a directory. For example, `rm test.txt` removes the file test.txt. `rm -r Documents` removes the Documents directory and all its contents recursively. You can also use this command to remove multiple files or directories at once. For example, `rm test.txt new.txt` removes both the files test.txt and new.txt. `rm -r *` removes all the files and directories in the current working directory. Be careful with this command as it does not ask for confirmation and the deleted files or directories cannot be recovered easily.
  - `man`: This command shows the manual page for a given command or topic. For example, `man ls` shows the manual page for the ls command, which explains its syntax, options, arguments, examples and other information. `man man` shows the manual page for the man command itself. You can use the arrow keys, the Page Up and Page Down keys, or the spacebar to scroll through the manual page. You can also use the / key to search for a keyword in the manual page. To exit the manual page, press the Q key.



#### mkdir, rmdir, tar, gzip, cat, more, less, ps, sudo, cron, chown, chgrp, ping etc.

These are some of the common Linux commands that can be used to perform various tasks on the command terminal window. Here is a brief description of each command and some examples of their usage:

- **mkdir**: This command is used to create directories (also referred to as folders in some operating systems). The syntax is `mkdir [options] [directory_name]`. For example, `mkdir new_folder` will create a directory called `new_folder` in the current working directory. To create multiple directories at once, we can use `mkdir dir1 dir2 dir3`. To create a directory with a specific permission, we can use the `-m` option, such as `mkdir -m 755 dir4` .
- **rmdir**: This command is used to remove empty directories. The syntax is `rmdir [options] [directory_name]`. For example, `rmdir dir4` will delete the directory `dir4` if it is empty. To remove multiple directories at once, we can use `rmdir dir1 dir2 dir3`. To remove directories recursively, we can use the `-p` option, such as `rmdir -p dir5/dir6/dir7`.
- **tar**: This command is used to create or extract compressed archive files. The syntax is `tar [options] [archive_name] [file_name]`. For example, `tar -cvf archive.tar file1 file2 file3` will create a compressed archive file called `archive.tar` containing the files `file1`, `file2`, and `file3`. To extract the files from the archive, we can use `tar -xvf archive.tar`. To create a compressed archive file using gzip or bzip2, we can use the `-z` or `-j` option, such as `tar -cvzf archive.gz file1 file2 file3` or `tar -cvjf archive.bz2 file1 file2 file3`.
- **gzip**: This command is used to compress or decompress files using the gzip algorithm. The syntax is `gzip [options] [file_name]`. For example, `gzip file1` will compress the file `file1` and rename it to `file1.gz`. To decompress the file, we can use `gzip -d file1.gz` or `gunzip file1.gz`. To compress multiple files at once, we can use `gzip file1 file2 file3`. To compress a directory, we can use `gzip -r dir1`.
- **cat**: This command is used to display the contents of a file or concatenate multiple files. The syntax is `cat [options] [file_name]`. For example, `cat file1` will print the contents of `file1` on the standard output. To concatenate two files and display the result, we can use `cat file1 file2`. To concatenate two files and save the result in a new file, we can use `cat file1 file2 > file3`. To append the contents of a file to another file, we can use `cat file1 >> file2`.
- **more**: This command is used to display the contents of a file or a command output one page at a time. The syntax is `more [options] [file_name]`. For example, `more file1` will display the first page of `file1` and wait for the user to press the space bar to display the next page. To quit the command, we can press `q`. To display the output of another command, we can use a pipe, such as `ls -l | more` .
- **less**: This command is similar to the more command but provides more features. One important feature is that it allows backward as well as forward movement in the file, even with pipes. Also, since it does not read the entire file before starting, it starts up faster compared to text editors — especially when we’re viewing large files. The syntax is `less [options] [file_name]`. For example, `less file1` will display the first page of `file1` and wait for the user to press the space bar to display the next page or the `b` key to display the previous page. To quit the command, we can press `q`. To display the output of another



#### 2. Run some python programs on Pi like:

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- You also need to have a text editor or an IDE (Integrated Development Environment) to write and edit your python code. You can use the default text editor on Pi, which is called **Leafpad**, or you can install other editors like **Thonny** or **Mu**. To install Thonny, type `sudo apt install thonny` in the terminal. To install Mu, type `pip3 install mu-editor`.
- To write a python program, you need to create a file with the extension `.py`, such as `hello.py`. You can use any text editor to create and save the file in a folder of your choice. You can also use the `touch` command in the terminal to create an empty file, such as `touch hello.py`.
- To run a python program, you need to open the terminal and navigate to the folder where your file is located. You can use the `cd` command to change directories, such as `cd Documents`. You can also use the `ls` command to list the files and folders in your current directory. To run the python program, you need to type `python3` followed by the name of your file, such as `python3 hello.py`. This will execute the code in your file and display the output in the terminal.
- You can also run a python program from a text editor or an IDE, if they have a run button or a menu option to run the code. For example, in Thonny, you can click on the green triangle button to run the code. In Mu, you can click on the **Run** button to run the code. This will also execute the code in your file and display the output in a separate window.



#### a) Read your name and print Hello message with name

- To read your name, you need to use an input function that takes a string as an argument and returns the user's input as another string.
- For example, in Python, you can use the input() function to read your name from the keyboard and store it in a variable called name.
- To print a Hello message with your name, you need to use a print function that takes a string as an argument and displays it on the screen.
- For example, in Python, you can use the print() function to print a Hello message with your name by concatenating the strings "Hello" and name with a comma or a plus sign.
- Here is an example of a Python program that reads your name and prints a Hello message with your name:

```python
# Read your name and store it in a variable called name
name = input("Enter your name: ")

# Print a Hello message with your name
print("Hello", name) # Using a comma to separate the strings
# or
print("Hello" + name) # Using a plus sign to concatenate the strings
```

- Here is an example of the output of the program:

```
Enter your name: Sydney
Hello Sydney
```



#### b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the `input()` function in Python, which returns a string value that can be converted to a numeric type using `int()` or `float()`.
- For example, we can write:

```python
# Read two numbers from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert the input strings to integers
num1 = int(num1)
num2 = int(num2)
```

- To print their sum, difference, product and division, we can use the arithmetic operators `+`, `-`, `*` and `/` in Python, which perform the corresponding operations on the operands and return the result.
- For example, we can write:

```python
# Print the sum of the two numbers
print("The sum is", num1 + num2)

# Print the difference of the two numbers
print("The difference is", num1 - num2)

# Print the product of the two numbers
print("The product is", num1 * num2)

# Print the division of the two numbers
print("The division is", num1 / num2)
```

- Note that the division operator `/` in Python returns a floating-point value, even if the operands are integers. To get an integer division, we can use the floor division operator `//`, which returns the quotient of the division without the remainder.
- For example, we can write:

```python
# Print the integer division of the two numbers
print("The integer division is", num1 // num2)
```

- Here is the complete program that reads two numbers and prints their sum, difference, product and division:

```python
# Read two numbers from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert the input strings to integers
num1 = int(num1)
num2 = int(num2)

# Print the sum of the two numbers
print("The sum is", num1 + num2)

# Print the difference of the two numbers
print("The difference is", num1 - num2)

# Print the product of the two numbers
print("The product is", num1 * num2)

# Print the division of the two numbers
print("The division is", num1 / num2)

# Print the integer division of the two numbers
print("The integer division is", num1 // num2)
```

- Here is an example of the output of the program:

```
Enter the first number: 12
Enter the second number: 4
The sum is 16
The difference is 8
The product is 48
The division is 3.0
The integer division is 3
```



#### c) Word and character count of a given string.

- A string is a sequence of characters enclosed in quotation marks, such as "Hello" or "This is a string".
- A word is a group of characters separated by spaces or punctuation marks, such as "Hello" or "This is a word".
- A character is a single symbol, such as "H" or "." or " ".
- To count the number of words in a string, we can split the string by spaces or punctuation marks and count the length of the resulting list.
- To count the number of characters in a string, we can simply count the length of the string itself.
- For example, the string "This is a string with 7 words and 29 characters." has 7 words and 29 characters.
- Here is a possible pseudocode algorithm to count the words and characters in a string:

```
# Input: a string s
# Output: the number of words and characters in s

# Initialize word_count and char_count to zero
word_count = 0
char_count = 0

# Loop through each character in s
for each character in s:
  # Increment char_count by one
  char_count = char_count + 1

  # If the character is a space or a punctuation mark
  if character is " " or character is "." or character is "," or character is "?" or character is "!" or character is ":" or character is ";":
    # Increment word_count by one
    word_count = word_count + 1

# Return word_count and char_count
return word_count, char_count
```



#### d) Area of a given shape (rectangle, triangle and circle) reading shape and appropriate values from standard

- The area of a shape is the amount of space that it covers in a two-dimensional plane.
- To calculate the area of a given shape, we need to know the shape and the appropriate values from the standard input, such as length, width, base, height, or radius.
- The formula for the area of a rectangle is `A = length * width`, where `length` is the longer side and `width` is the shorter side of the rectangle.
- The formula for the area of a triangle is `A = (base * height) / 2`, where `base` is the length of the bottom side and `height` is the perpendicular distance from the base to the opposite vertex of the triangle.
- The formula for the area of a circle is `A = pi * radius^2`, where `pi` is a constant value approximately equal to 3.14 and `radius` is the distance from the center to any point on the circle.
- To read the shape and the appropriate values from the standard input, we can use the `input()` function in Python, which returns a string that the user enters.
- We can convert the string to a numerical value using the `float()` function, which returns a floating-point number that represents the string.
- We can use conditional statements, such as `if`, `elif`, and `else`, to check the shape and apply the corresponding formula for the area.
- We can use the `print()` function to display the result of the calculation to the standard output.

Here is an example of a Python program that calculates the area of a given shape:

```python
# Read the shape from the standard input
shape = input("Enter the shape (rectangle, triangle, or circle): ")

# Check the shape and apply the corresponding formula
if shape == "rectangle":
  # Read the length and width from the standard input
  length = float(input("Enter the length: "))
  width = float(input("Enter the width: "))
  # Calculate the area of the rectangle
  area = length * width
elif shape == "triangle":
  # Read the base and height from the standard input
  base = float(input("Enter the base: "))
  height = float(input("Enter the height: "))
  # Calculate the area of the triangle
  area = (base * height) / 2
elif shape == "circle":
  # Read the radius from the standard input
  radius = float(input("Enter the radius: "))
  # Calculate the area of the circle
  area = 3.14 * radius**2
else:
  # Invalid shape
  print("Invalid shape")
  # Exit the program
  exit()

# Display the result to the standard output
print("The area of the", shape, "is", area)
```



#### Input

- Input is the process of providing data or instructions to a computer system so that it can perform a task or operation.
- Input is important because it allows users to interact with a computer system and provide information that can be processed and analyzed.
- Input can be given in various forms, such as text, images, sound, video, gestures, etc.
- Input devices are hardware components that enable users to input data or instructions to a computer system.
- The most common input devices are the keyboard, mouse, and touch screen.
- Some other examples of input devices are microphones, scanners, cameras, joysticks, sensors, etc.
- Input devices can be categorized into different types, such as manual, automatic, direct, indirect, discrete, continuous, etc.
- Manual input devices require human intervention to input data or instructions, such as keyboards, mice, touch screens, etc.
- Automatic input devices do not require human intervention to input data or instructions, such as sensors, barcode readers, RFID tags, etc.
- Direct input devices allow users to input data or instructions directly into the computer system, such as touch screens, scanners, cameras, etc.
- Indirect input devices require an intermediate device or software to input data or instructions into the computer system, such as keyboards, mice, joysticks, etc.
- Discrete input devices input data or instructions that have a finite number of values, such as keyboards, mice, buttons, etc.
- Continuous input devices input data or instructions that have an infinite number of values, such as touch screens, microphones, sensors, etc.



#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- To write a python program, you need to use a text editor such as nano, vim, or idle. You can launch a text editor by typing its name in the terminal, such as `nano` or `idle3`.
- To save a python program, you need to give it a name with a `.py` extension, such as `print_name.py`. You can save your program by pressing `Ctrl+O` in nano, or by choosing `File -> Save` in idle.
- To run a python program, you need to type `python3` followed by the name of your program, such as `python3 print_name.py`. You can run your program by pressing `Enter` in the terminal, or by choosing `Run -> Run Module` in idle.
- To print a name 'n' times, where name and n are read from standard input, you need to use the `input` function to get the user input, and the `print` function to display the output. You also need to use a `for` loop to repeat the printing 'n' times. Here is an example of a python program that does this:

```python
# print_name.py
# This program prints a name 'n' times, where name and n are read from standard input

# Get the name from the user
name = input("Enter a name: ")

# Get the number of times to print from the user
n = int(input("Enter a number: ")) # Convert the input to an integer

# Use a for loop to print the name 'n' times
for i in range(n):
    print(name)
```

- To test your program, you can run it and enter some values for the name and the number. For example, if you enter `Alice` and `5`, you should see the following output:

```python
Enter a name: Alice
Enter a number: 5
Alice
Alice
Alice
Alice
Alice
```



#### Using for and while loops
- A for loop is a repetition control structure that allows you to efficiently write a loop that needs to execute a specific number of times.
- A while loop is a repetition control structure that allows you to write a loop that will repeat as long as a condition is true.
- The syntax of a for loop is:

```python
for variable in range(start, end, step):
    # loop body
```
- The syntax of a while loop is:

```python
while condition:
    # loop body
```
- For example, to print the numbers from 1 to 10 using a for loop, you can write:

```python
for i in range(1, 11):
    print(i)
```
- To print the numbers from 1 to 10 using a while loop, you can write:

```python
i = 1
while i <= 10:
    print(i)
    i = i + 1
```
#### Handle Divided by Zero Exception
- An exception is an error that occurs during the execution of a program.
- A divided by zero exception is an error that occurs when you try to divide a number by zero, which is not allowed in mathematics.
- To handle an exception, you can use a try-except block, which allows you to catch and handle the error gracefully, without terminating the program.
- The syntax of a try-except block is:

```python
try:
    # code that may cause an exception
except ExceptionType as e:
    # code that handles the exception
```
- For example, to handle a divided by zero exception, you can write:

```python
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    z = x / y
    print("The result is", z)
except ZeroDivisionError as e:
    print("You cannot divide by zero!")
    print("The error message is:", e)
```
#### Print current time for 10 times with an interval of 1 second
- To print the current time, you can use the datetime module, which provides various functions and classes to deal with dates and times.
- To import the datetime module, you can write:

```python
import datetime
```
- To get the current time, you can use the datetime.now() function, which returns a datetime object that represents the current date and time.
- To print the current time, you can use the print() function, which displays the value of its argument to the standard output.
- To print the current time for 10 times, you can use a for loop or a while loop, as explained above.
- To print the current time with an interval of 1 second, you can use the time module, which provides various functions and classes to deal with time-related tasks.
- To import the time module, you can write:

```python
import time
```
- To pause the execution of the program for 1 second, you can use the time.sleep() function, which takes a number of seconds as an argument and suspends the program for that duration.
- For example, to print the current time for 10 times with an interval of 1 second using a for loop, you can write:

```python
import datetime
import time

for i in range(10):
    print(datetime.datetime.now())
    time.sleep(1)
```
- To print the current time for 10 times with an interval of 1 second using a while loop, you can write:

```python
import datetime
import time

i = 0
while i < 10:
    print(datetime.datetime.now())
    time.sleep(1)
    i = i + 1
```



#### Interval of 10 seconds
- An interval of 10 seconds is a measure of time that is equal to 10 units of one second each.
- A second is the base unit of time in the International System of Units (SI) and is defined as the duration of 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium-133 atom.
- An interval of 10 seconds can be used to measure the duration of events or processes that are relatively short, such as the reaction time of a person, the frequency of a sound wave, or the speed of a moving object.
- An interval of 10 seconds can also be used to divide a longer period of time into smaller segments, such as a minute, an hour, or a day. For example, a minute has 6 intervals of 10 seconds, an hour has 360 intervals of 10 seconds, and a day has 8,640 intervals of 10 seconds.

#### Read a file line by line and print the word count of each line
- To read a file line by line and print the word count of each line, one possible algorithm is as follows:
  - Open the file in read mode and assign it to a variable, such as `file`.
  - Initialize a variable, such as `line_number`, to store the current line number, and set it to 1.
  - Use a loop, such as a `while` loop, to iterate over the lines of the file until the end of the file is reached.
    - In each iteration, read the next line of the file and assign it to a variable, such as `line`.
    - Use a function, such as `split()`, to split the line into a list of words, and assign it to a variable, such as `words`.
    - Use a function, such as `len()`, to get the length of the list of words, and assign it to a variable, such as `word_count`.
    - Print the line number, the line, and the word count, separated by commas or other delimiters, such as `print(line_number, line, word_count)`.
    - Increment the line number by 1, such as `line_number += 1`.
  - Close the file, such as `file.close()`.
- For example, if the file contains the following text:

```
This is the first line.
This is the second line, with more words.
This is the third and final line.
```

- The output of the algorithm would be:

```
1, This is the first line., 5
2, This is the second line, with more words., 8
3, This is the third and final line., 6
```



#### 4. a) Light an LED through Python program

- To light an LED through Python program, you need to have a hardware device that can control the LED, such as an Arduino, a Raspberry Pi, or a MicroPython board.
- You also need to connect the LED to the device using wires, resistors, and a breadboard, following the appropriate circuit diagram for your device.
- You need to install Python and the necessary libraries on your computer and on your device, such as pyserial, RPi.GPIO, or pyb.
- You need to write a Python program that can communicate with your device and send commands to turn the LED on and off, using the serial port, the GPIO pins, or the LED object, depending on your device.
- You need to upload the Python program to your device or run it from your computer, and observe the LED blinking according to your program logic.

Here is an example of a Python program that can light an LED connected to an Arduino board:

```python
# Import the serial library
import serial

# Create a serial object and connect to the Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)

# Define a function to turn the LED on and off
def led_on_off():
    # Ask the user to enter L or H
    user_input = input("\n Type L to turn LED on or H to turn LED off :")
    # If the user enters L, send L to the Arduino
    if user_input == 'L':
        print("LED is on...")
        ser.write(b'L')
        led_on_off()
    # If the user enters H, send H to the Arduino
    elif user_input == 'H':
        print("LED is off...")
        ser.write(b'H')
        led_on_off()
    # If the user enters anything else, ask again
    else:
        print("Invalid input. Type L or H.")
        led_on_off()

# Call the function
led_on_off()
```



#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to connect the switches and the LEDs to the input and output pins of a microcontroller, such as Arduino.
- We also need to write a program that reads the state of the switches and controls the state of the LEDs accordingly.
- The program can be written in Arduino IDE, which is a software that allows us to write and upload code to the microcontroller.
- The program can use the `digitalRead()` function to read the state of the switches, which can be either HIGH or LOW, depending on whether they are pressed or not.
- The program can also use the `digitalWrite()` function to set the state of the LEDs, which can be either HIGH or LOW, depending on whether they are on or off.
- The program can use `if` statements to check the state of the switches and set the state of the LEDs accordingly.
- For example, if switch 1 is pressed and switch 2 is not pressed, then LED 1 should be on and LED 2 should be off.
- The program can use a `void setup()` function to initialize the input and output pins, and a `void loop()` function to run the code repeatedly.
- The program can be uploaded to the microcontroller using a USB cable and the Arduino IDE.
- The following is an example of the program:

```c
// Define the input and output pins
#define SWITCH_1 2 // Switch 1 is connected to pin 2
#define SWITCH_2 3 // Switch 2 is connected to pin 3
#define LED_1 4 // LED 1 is connected to pin 4
#define LED_2 5 // LED 2 is connected to pin 5

// Initialize the input and output pins
void setup() {
  pinMode(SWITCH_1, INPUT); // Set pin 2 as input
  pinMode(SWITCH_2, INPUT); // Set pin 3 as input
  pinMode(LED_1, OUTPUT); // Set pin 4 as output
  pinMode(LED_2, OUTPUT); // Set pin 5 as output
}

// Run the code repeatedly
void loop() {
  // Read the state of the switches
  int switch_1_state = digitalRead(SWITCH_1); // Read pin 2
  int switch_2_state = digitalRead(SWITCH_2); // Read pin 3

  // Check the state of the switches and set the state of the LEDs accordingly
  if (switch_1_state == HIGH && switch_2_state == LOW) {
    // If switch 1 is pressed and switch 2 is not pressed
    digitalWrite(LED_1, HIGH); // Turn on LED 1
    digitalWrite(LED_2, LOW); // Turn off LED 2
  } else if (switch_1_state == LOW && switch_2_state == HIGH) {
    // If switch 1 is not pressed and switch 2 is pressed
    digitalWrite(LED_1, LOW); // Turn off LED 1
    digitalWrite(LED_2, HIGH); // Turn on LED 2
  } else if (switch_1_state == HIGH && switch_2_state == HIGH) {
    // If both switches are pressed
    digitalWrite(LED_1, HIGH); // Turn on LED 1
    digitalWrite(LED_2, HIGH); // Turn on LED 2
  } else {
    // If both switches are not pressed
    digitalWrite(LED_1, LOW); // Turn off LED 1
    digitalWrite(LED_2, LOW); // Turn off LED 2
  }
}
```



#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

To flash an LED at a given on time and off time cycle, where the two times are taken from a file, the following steps are required:

- Connect an LED to a digital output pin of a microcontroller, such as Arduino, and a resistor to limit the current.
- Create a text file with two numbers separated by a comma, representing the on time and off time in milliseconds, for example: 500,1000
- Save the file in the same folder as the Arduino sketch, and name it as "times.txt".
- Use the `File` and `SD` libraries to access the file from the microcontroller's memory card.
- Use the `parseInt()` function to read the two numbers from the file and store them in variables, for example: `int onTime = file.parseInt(); int offTime = file.parseInt();`
- Use the `digitalWrite()` function to turn the LED on and off according to the on time and off time variables, for example: `digitalWrite(ledPin, HIGH); delay(onTime); digitalWrite(ledPin, LOW); delay(offTime);`
- Use a `while` loop to repeat the flashing cycle indefinitely, for example: `while (true) { // flash the LED }`

The following is an example of an Arduino sketch that implements the above steps:

```c
// include the libraries for file and SD card access
#include <File.h>
#include <SD.h>

// define the pin number for the LED
const int ledPin = 13;

// define the variables for the on time and off time
int onTime;
int offTime;

// define the file object
File file;

void setup() {
  // initialize the LED pin as an output
  pinMode(ledPin, OUTPUT);

  // initialize the serial communication for debugging
  Serial.begin(9600);

  // initialize the SD card and check if it is ready
  if (!SD.begin()) {
    Serial.println("SD card initialization failed");
    return;
  }

  // open the file and check if it exists
  file = SD.open("times.txt");
  if (!file) {
    Serial.println("File not found");
    return;
  }

  // read the on time and off time from the file
  onTime = file.parseInt();
  offTime = file.parseInt();

  // close the file
  file.close();

  // print the on time and off time for debugging
  Serial.print("On time: ");
  Serial.println(onTime);
  Serial.print("Off time: ");
  Serial.println(offTime);
}

void loop() {
  // flash the LED according to the on time and off time
  digitalWrite(ledPin, HIGH);
  delay(onTime);
  digitalWrite(ledPin, LOW);
  delay(offTime);
}
```



#### 5. a) Flash an LED based on cron output (acts as an alarm)

- To flash an LED based on cron output, we need to use a Raspberry Pi, an LED, a resistor, some jumper wires, and a breadboard.
- We also need to install the WiringPi library on the Raspberry Pi, which provides a simple way to control the GPIO pins using the command line.
- The steps to flash an LED based on cron output are:

  1. Connect the LED to the GPIO pin 17 and the resistor to the ground pin on the breadboard, using the jumper wires. Refer to the diagram below for the wiring.

  ```
  +3.3V  +5V
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |
  |      |  +5V
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |
  |      |  |  GND
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |
  |      |  |  |  GPIO 17
  |      |  |  |  |
  |      |  |  |  |
  |      |  |  |  |
  |      |  |  |  |
  |      |  |  |  |
  |      |  |  |  |  GND
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  +------+--+--+--+--+
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  +------+--+--+--+--+
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  +------+--+--+--+--+
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  +------+--+--+--+--+
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |
  +------+--+--+--+--+
  |      |  |  |  |  |
  |      |  |  |  |  |
  |      |  |  |  |  |  LED
  |      |  |  |  |  |

```




#### b) Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

- A relay is an electromechanical device that can be used to switch on or off a load using an electric signal.
- A cron is a software utility that can be used to schedule tasks to run at a specified time or interval on a Linux system.
- To switch on a relay at a given time using cron, the following steps are required:

  1. Connect the relay's coil terminals to a GPIO pin and a ground pin of a Raspberry Pi or any other microcontroller that can run Linux.
  2. Connect the relay's contact terminals to the load and a power source, such as a battery or a wall outlet.
  3. Write a Python script that can control the GPIO pin to turn on or off the relay. For example, the script can use the RPi.GPIO module to set the GPIO pin as an output and set its value to high or low.
  4. Save the script in a suitable location, such as the home directory, and make it executable by running the command `chmod +x script.py` in the terminal.
  5. Edit the crontab file by running the command `crontab -e` in the terminal. This will open the file in a text editor, where you can add a new line to specify the time and the command to run the script. For example, the line `0 8 * * * /home/pi/script.py` will run the script at 8:00 am every day.
  6. Save and exit the crontab file. The cron service will automatically reload the file and execute the scheduled tasks.
  7. To verify that the cron job is working, you can check the syslog file by running the command `tail -f /var/log/syslog` in the terminal. This will show the latest messages from the cron service and the script output. You can also observe the relay and the load to see if they are switched on or off at the given time.



#### c) Get the status of a bulb at a remote place (on the LAN) through web.

- To get the status of a bulb at a remote place (on the LAN) through web, we need to have the following components:
  - A bulb that can be controlled by a microcontroller such as Arduino or Raspberry Pi.
  - A microcontroller that can connect to the LAN and send or receive data through HTTP requests.
  - A web server that can host a web page that displays the status of the bulb and allows the user to change it.
  - A web browser that can access the web page and interact with the web server.

- The steps to get the status of a bulb at a remote place (on the LAN) through web are as follows:
  - Connect the bulb to the microcontroller using appropriate wires and circuits. For example, if we use an Arduino, we can connect the bulb to a digital pin and use the digitalWrite() function to turn it on or off.
  - Connect the microcontroller to the LAN using an Ethernet shield or a Wi-Fi module. For example, if we use an Arduino, we can use the Ethernet library or the WiFi library to initialize the network connection and assign an IP address to the microcontroller.
  - Write a sketch or a program for the microcontroller that can handle HTTP requests from the web server. For example, if we use an Arduino, we can use the EthernetServer or the WiFiServer class to create a server object that can listen for incoming connections and respond to them. The sketch or the program should be able to read the status of the bulb from the digital pin and send it as a response to the web server, or change the status of the bulb according to the request from the web server.
  - Upload the sketch or the program to the microcontroller and test the connection by sending HTTP requests from a web browser or a tool such as Postman. For example, if we use an Arduino, we can type the IP address of the microcontroller in the web browser and append a query string such as ?status=on or ?status=off to turn the bulb on or off, or ?status=read to read the current status of the bulb.
  - Set up a web server that can host a web page that displays the status of the bulb and allows the user to change it. For example, we can use a platform such as Node.js, Python, or PHP to create a web server that can serve static or dynamic web pages. The web page should be able to send HTTP requests to the microcontroller using JavaScript or a library such as jQuery or Axios, and update the web page accordingly.
  - Access the web page from a web browser and interact with the web server and the microcontroller. For example, we can type the IP address or the domain name of the web server in the web browser and see the status of the bulb on the web page. We can also click a button or a switch on the web page to change the status of the bulb and see the result on the web page and the bulb.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the content in markdown format on the topic #### Note: The Instructor may add/delete/modify/tune experiments. Here is my attempt:

#### Note: The Instructor may add/delete/modify/tune experiments

- This note is a disclaimer that the instructor of a course or a lab has the authority and the flexibility to change the experiments according to the learning objectives, the availability of resources, the level of difficulty, or the feedback from the students.
- The instructor may add new experiments to introduce new concepts, skills, or applications that are relevant to the course or the lab.
- The instructor may delete existing experiments if they are outdated, redundant, or irrelevant to the course or the lab.
- The instructor may modify existing experiments to update the content, the instructions, the data, the tools, or the expected outcomes of the experiments.
- The instructor may tune existing experiments to adjust the parameters, the variables, the settings, or the criteria of the experiments.
- The instructor may also combine, split, or reorder the experiments to create a logical and coherent sequence of learning activities.
- The instructor should inform the students about any changes in the experiments in advance and provide clear and consistent guidelines for performing the experiments.
- The instructor should also explain the rationale and the benefits of the changes in the experiments and how they align with the learning outcomes of the course or the lab.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss.

Some possible topics are:

- History
- Science
- Literature
- Art
- Music
- Sports
- Politics
- Philosophy
- Religion
- Culture

Please choose a topic or type your own.



# The topic is

- The topic is a general term for the subject or theme of a conversation, text, or presentation.
- The topic can be expressed in different ways, such as a word, a phrase, a question, or a statement.
- The topic can be explicit or implicit, depending on how clearly it is stated or implied by the speaker or writer.
- The topic can be broad or narrow, depending on how much information or detail it covers or excludes.
- The topic can be related to different domains, such as science, history, art, politics, etc.
- The topic can be chosen by the speaker or writer, or assigned by someone else, such as a teacher, a boss, or a client.
- The topic can be influenced by various factors, such as the purpose, audience, context, and genre of the communication.
- The topic can be developed or changed over the course of the conversation, text, or presentation, depending on the feedback, questions, or arguments of the interlocutors or readers.



# The topic is

- The topic is a general term for the subject or theme of a text, speech, or conversation.
- The topic can be expressed in different ways, such as a word, a phrase, a question, or a statement.
- The topic can be identified by looking for clues in the text, such as the title, the introduction, the main idea, the keywords, or the summary.
- The topic can be used to organize and structure the information in the text, such as by using headings, subheadings, paragraphs, or bullet points.
- The topic can be used to guide the reader's or listener's attention and interest, such as by using hooks, transitions, examples, or questions.
- The topic can be used to communicate the purpose and goal of the text, such as by using a thesis statement, a claim, an argument, or a conclusion.



# KOT 554 INTERNET OF THINGS LAB KCS

- Internet of Things (IoT) is a course that introduces the concepts and applications of connecting physical objects to the internet and to each other.
- The course covers the following topics:
  - Introduction to IoT and its architecture, components, and protocols.
  - IoT devices and sensors, their types, characteristics, and interfacing methods.
  - IoT communication technologies and standards, such as Wi-Fi, Bluetooth, ZigBee, LoRa, MQTT, CoAP, etc.
  - IoT cloud platforms and services, such as AWS IoT, Google Cloud IoT, IBM Watson IoT, etc.
  - IoT data processing and analytics, such as data acquisition, storage, visualization, and machine learning.
  - IoT security and privacy, such as encryption, authentication, authorization, and attack prevention and detection.
  - IoT applications and case studies, such as smart home, smart city, smart agriculture, smart health, etc.
- The course has a lab component that involves hands-on experiments and projects using various IoT devices, sensors, communication modules, and cloud platforms.
- The course objectives are:
  - To understand the basic concepts and principles of IoT and its architecture, components, and protocols.
  - To learn how to design, implement, and test IoT systems using various IoT devices, sensors, communication modules, and cloud platforms.
  - To develop skills in IoT data processing and analytics using various tools and techniques.
  - To explore the challenges and opportunities of IoT in various domains and applications.
  - To enhance the creativity and problem-solving abilities of the students in IoT domain.
- The course outcomes are:
  - The students will be able to explain the basic concepts and principles of IoT and its architecture, components, and protocols.
  - The students will be able to design, implement, and test IoT systems using various IoT devices, sensors, communication modules, and cloud platforms.
  - The students will be able to perform IoT data processing and analytics using various tools and techniques.
  - The students will be able to identify the challenges and opportunities of IoT in various domains and applications.
  - The students will be able to demonstrate their creativity and problem-solving abilities in IoT domain.



# Course Outcome (CO) Bloom's Knowledge Level (KL)

- Course Outcome (CO) is a statement that describes what a learner should be able to do at the end of a course or a unit of instruction.
- Bloom's Knowledge Level (KL) is a classification of cognitive skills that learners can demonstrate in relation to a given topic or domain.
- Bloom's Knowledge Level (KL) consists of six levels: remember, understand, apply, analyze, evaluate, and create. Each level represents a higher order of thinking and requires more complex cognitive processes than the previous one.
- Course Outcome (CO) can be aligned with Bloom's Knowledge Level (KL) to ensure that the learning objectives are clear, measurable, and appropriate for the level of the course or the unit of instruction.
- For example, a Course Outcome (CO) for a course on computer programming could be: "Write, compile, and debug a simple program using a programming language of your choice." This CO can be aligned with the apply level of Bloom's Knowledge Level (KL), as it requires the learner to use the knowledge and skills of programming to solve a specific problem.
- Aligning Course Outcome (CO) with Bloom's Knowledge Level (KL) can help instructors design effective learning activities, assessments, and feedback that match the intended learning outcomes and the cognitive skills of the learners. It can also help learners monitor their own progress and identify their strengths and weaknesses.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss.

Some possible responses for the topic are:

# At the end of the course, the student will be able to:

- Apply the concepts and principles of the subject to solve problems and analyze situations.
- Demonstrate the skills and techniques required for the subject, such as experiments, calculations, simulations, etc.
- Communicate effectively the results and arguments of the subject, using appropriate terminology, formats, and references.
- Evaluate the validity, reliability, and limitations of the sources and methods used in the subject, and identify ethical and social implications.
- Compare and contrast different perspectives, approaches, and theories related to the subject, and develop critical thinking and creativity.



# CO 1 Understand the concept of Internet of Things K3

- Internet of Things (IoT) is the interconnection of physical objects with sensors, software and other technologies that enable them to communicate and exchange data with other devices and systems over the internet or other networks .
- IoT can be used for various purposes, such as remote monitoring, control, automation, optimization, security, personalization, and analytics of devices and systems.
- IoT can be applied to various domains, such as smart homes, smart cities, smart agriculture, smart healthcare, smart manufacturing, smart transportation, smart energy, and smart environment.
- IoT can be classified into different types, such as consumer IoT, industrial IoT, enterprise IoT, and public IoT, based on the users, applications, and characteristics of the devices and systems.
- IoT can be composed of different components, such as devices, gateways, networks, platforms, applications, and services, that perform different functions, such as sensing, processing, transmitting, storing, analyzing, and acting on the data.
- IoT can be characterized by different features, such as heterogeneity, scalability, interoperability, security, privacy, reliability, and intelligence, that pose different challenges and opportunities for the design, development, and deployment of IoT solutions.



# CO2 Implement interfacing of various sensors with Arduino/Raspberry Pi

- CO2 sensors are devices that can measure the concentration of carbon dioxide in the air. They are useful for monitoring air quality, plant growth, fermentation, and other applications that involve CO2 production or consumption.
- There are different types of CO2 sensors available, such as electrochemical, infrared, and metal oxide. Each type has its own advantages and disadvantages, such as accuracy, sensitivity, power consumption, and cost.
- To interface a CO2 sensor with an Arduino or a Raspberry Pi, you need to connect the sensor's output signal to one of the analog or digital input pins of the microcontroller. Depending on the type of sensor, you may also need to provide a power supply and a reference voltage for the sensor.
- Some CO2 sensors have a Gravity Interface, which is a standard connector that allows plug and play with Arduino boards. For example, the Gravity: Analog CO2 Gas Sensor (MG-811 Sensor)  is compatible with Arduino and can be easily connected to the Arduino IO expansion shield.
- Other CO2 sensors may require some additional components, such as resistors, capacitors, or amplifiers, to adjust the signal level and quality. For example, the MQ-7 Carbon Monoxide CO Gas Sensor Module  needs a load resistor and a capacitor to filter out the noise and stabilize the output voltage.
- To read the data from the CO2 sensor, you need to use the analogRead() or digitalRead() functions in Arduino, or the GPIO library in Raspberry Pi. You may also need to calibrate the sensor and convert the raw data to the actual CO2 concentration using a formula or a lookup table.
- To display or store the data from the CO2 sensor, you can use the Serial Monitor or the SD card module in Arduino, or the terminal or the file system in Raspberry Pi. You can also use other modules or devices, such as LCD screens, LEDs, buzzers, or speakers, to create visual or auditory feedback based on the CO2 level.
- To learn more about how to interface various CO2 sensors with Arduino or Raspberry Pi, you can refer to the following tutorials and examples:

  - [Gravity: Analog CO2 Gas Sensor (MG-811 Sensor) - Arduino Online Shop](https://store-usa.arduino.cc/products/gravity-analog-co2-gas-sensor-mg-811-sensor) 
  - [Measuring CO2 with an Arduino: Creating a Low-Cost, Pocket-Sized Device for Science Education](https://pubs.acs.org/doi/10.1021/acs.jchemed.8b00473) 
  - [Arduino UNO And Carbon Dioxide (CO2) Sensor - Makerguides.com](https://www.makerguides.com/arduino-uno-and-carbon-dioxide-co2-sensor/) 
  - [Arduino | Adafruit SCD-40 and SCD-41 - Adafruit Learning System](https://learn.adafruit.com/adafruit-scd-40-and-scd-41/arduino)



# CO 3 Demonstrate the ability to transmit data wirelessly between different devices. K4

- Wireless data transmission is the process of sending and receiving data without using physical wires or cables.
- Wireless data transmission can be classified into two main types: radio frequency (RF) and optical.
  - RF transmission uses electromagnetic waves to carry data through the air, such as Wi-Fi, Bluetooth, and cellular networks .
  - Optical transmission uses light to send data, such as infrared, visible light, and laser .
- Wireless data transmission can be achieved using different devices, such as wireless phones, wireless adapters, wireless repeaters, and other devices .
  - Wireless phones are devices that use cellular networks or voice over IP (VoIP) to make and receive calls.
  - Wireless adapters are devices that enable a computer or other device to connect to a wireless network, such as a Wi-Fi router or a hotspot .
  - Wireless repeaters are devices that extend the range of a wireless network by receiving and retransmitting the signals .
  - Other devices that can transmit data wirelessly include smartwatches, wireless headphones, wireless keyboards, wireless mice, and wireless printers .
- To demonstrate the ability to transmit data wirelessly between different devices, one should be able to:
  - Identify the types and modes of wireless transmission and communication, such as RF and optical, and their advantages and disadvantages.
  - Understand the basic concepts and principles of wireless transmission, such as frequency, modulation, encoding, multiplexing, and encryption .
  - Compare and contrast the different wireless standards and protocols, such as IEEE 802.11, Bluetooth, ZigBee, and NFC, and their applications and limitations .
  - Configure and troubleshoot wireless devices and networks, such as setting up security, authentication, and encryption, and resolving interference and connectivity issues .
  - Evaluate the performance and energy efficiency of wireless data transmission, such as measuring throughput, latency, bandwidth, and power consumption .



# CO 4 Show an ability to upload/download sensor data on cloud and server K2

- Sensor data is the information collected by various types of sensors that measure physical phenomena such as temperature, humidity, pressure, light, sound, motion, etc.
- Cloud and server are two types of computing platforms that can store, process, and analyze sensor data remotely over the internet.
- Uploading sensor data means sending the data from the sensor device to the cloud or server, while downloading sensor data means receiving the data from the cloud or server to the sensor device or another device.
- To upload/download sensor data on cloud and server, the following steps are required:

  - **Step 1:** Choose a suitable cloud or server platform that can handle the sensor data according to the requirements of the project, such as data volume, frequency, format, security, etc. Some examples of cloud platforms are AWS, Azure, Google Cloud, ThingSpeak, etc. Some examples of server platforms are Apache, Nginx, Node.js, etc.
  - **Step 2:** Connect the sensor device to the internet using a wired or wireless connection, such as Ethernet, Wi-Fi, Bluetooth, cellular, satellite, etc. The connection should be reliable, fast, and secure enough to transmit the sensor data without loss or delay.
  - **Step 3:** Configure the sensor device to upload the sensor data to the cloud or server using a specific protocol, such as HTTP, MQTT, CoAP, etc. The protocol should be compatible with the cloud or server platform and should support the data format, such as JSON, XML, CSV, etc. The sensor device should also have a unique identifier, such as a MAC address, IP address, or device name, to authenticate itself to the cloud or server.
  - **Step 4:** Configure the cloud or server to receive the sensor data from the sensor device and store it in a database, such as DynamoDB, MongoDB, MySQL, etc. The database should be able to handle the data volume, frequency, and format, and should provide features such as indexing, querying, filtering, aggregation, etc. The cloud or server should also provide a dashboard or an API to visualize and analyze the sensor data, such as graphs, charts, tables, etc.
  - **Step 5:** Configure the sensor device or another device to download the sensor data from the cloud or server using the same or a different protocol as in step 3. The device should also have a unique identifier to authenticate itself to the cloud or server. The device should be able to display or process the sensor data according to the needs of the project, such as alerts, notifications, actions, etc.

- Some examples of projects that use sensor data upload/download on cloud and server are:

  - Smart home: A sensor device can upload temperature and humidity data to a cloud platform, and another device can download the data and control the thermostat or the air conditioner accordingly.
  - Weather station: A sensor device can upload atmospheric pressure and wind speed data to a server platform, and another device can download the data and display it on a website or an app.
  - Health monitor: A sensor device can upload heart rate and blood pressure data to a cloud platform, and another device can download the data and send it to a doctor or a hospital.



# CO 5 Examine various SQL queries from MySQL database K4, K5

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- MySQL is one of the most popular open-source relational database management systems (RDBMS) that supports SQL.
- SQL queries are statements that specify what data to retrieve, insert, update, or delete from a database.
- SQL queries can be classified into four categories: Data Definition Language (DDL), Data Manipulation Language (DML), Data Query Language (DQL), and Data Control Language (DCL).
- DDL is used to define the structure and schema of the database, such as creating, altering, or dropping tables, indexes, views, etc.
- DML is used to manipulate the data in the database, such as inserting, updating, or deleting records, etc.
- DQL is used to query the data in the database, such as selecting, joining, filtering, sorting, grouping, etc.
- DCL is used to control the access and privileges of the database, such as granting, revoking, or denying permissions, etc.
- Some examples of SQL queries from MySQL database are:

  - Create a table named `students` with four columns: `id`, `name`, `age`, and `grade`:

    ```sql
    CREATE TABLE students (
      id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      age INT,
      grade CHAR(1)
    );
    ```

  - Insert three records into the `students` table:

    ```sql
    INSERT INTO students (id, name, age, grade) VALUES
    (1, 'Alice', 18, 'A'),
    (2, 'Bob', 19, 'B'),
    (3, 'Charlie', 20, 'C');
    ```

  - Select all the records from the `students` table:

    ```sql
    SELECT * FROM students;
    ```

  - Select the name and grade of the students who are older than 18:

    ```sql
    SELECT name, grade FROM students WHERE age > 18;
    ```

  - Update the grade of Bob to 'A':

    ```sql
    UPDATE students SET grade = 'A' WHERE name = 'Bob';
    ```

  - Delete the record of Charlie from the `students` table:

    ```sql
    DELETE FROM students WHERE name = 'Charlie';
    ```

  - Create a view named `top_students` that shows the name and grade of the students who have grade 'A':

    ```sql
    CREATE VIEW top_students AS
    SELECT name, grade FROM students WHERE grade = 'A';
    ```

  - Grant the SELECT privilege on the `students` table to a user named `user1`:

    ```sql
    GRANT SELECT ON students TO user1;
    ```

  - Revoke the SELECT privilege on the `students` table from `user1`:

    ```sql
    REVOKE SELECT ON students FROM user1;
    ```



# DETAILED SYLLABUS

- A detailed syllabus is a document that outlines the topics, objectives, learning outcomes, assessment methods, and resources for a specific course or module.
- A detailed syllabus can help students to understand the expectations and requirements of the course, as well as to plan their study time and activities accordingly.
- A detailed syllabus can also help instructors to design and deliver the course in a coherent and consistent way, as well as to communicate with students and other stakeholders about the course content and goals.
- A detailed syllabus typically includes the following sections:

  - Course title, code, credits, and prerequisites
  - Instructor name, contact information, office hours, and availability
  - Course description, objectives, and learning outcomes
  - Course schedule, topics, and readings
  - Course policies, rules, and expectations
  - Course assignments, assessments, and grading criteria
  - Course resources, materials, and support services
  - Course evaluation and feedback mechanisms

- A detailed syllabus should be clear, concise, accurate, and updated. It should also be aligned with the course curriculum and the institutional standards and regulations. It should be distributed to the students at the beginning of the course and made available online or in print throughout the course duration.



# The student should have hands on experience in using various sensors like temperature, humidity, smoke, light, etc.

- Sensors are devices that detect and measure physical quantities such as temperature, humidity, smoke, light, etc. and convert them into electrical signals.
- Sensors are widely used in various applications such as home automation, environmental monitoring, security, robotics, etc.
- Hands on experience in using sensors can help the student to:
  - Understand the working principle, characteristics, and limitations of different types of sensors.
  - Learn how to interface sensors with microcontrollers, computers, or other devices using appropriate circuits, protocols, and software.
  - Develop skills in designing, testing, and troubleshooting sensor-based systems and projects.
  - Explore the possibilities and challenges of using sensors for solving real-world problems.
- Some examples of sensors that the student can use are:
  - Temperature sensor: A device that measures the temperature of an object or environment. Examples are thermistors, thermocouples, infrared sensors, etc.
  - Humidity sensor: A device that measures the amount of water vapor in the air. Examples are capacitive, resistive, or gravimetric sensors, etc.
  - Smoke sensor: A device that detects the presence of smoke or fire. Examples are optical, ionization, or thermal sensors, etc.
  - Light sensor: A device that measures the intensity or color of light. Examples are photodiodes, phototransistors, color sensors, etc.



# How to use control web camera, network, and relays connected to the Pi

- A web camera is a device that captures images or videos and sends them to a computer or a network. A web camera can be used for various purposes, such as video conferencing, surveillance, or entertainment.
- A network is a system of interconnected devices that can communicate and exchange data. A network can be wired or wireless, local or global, private or public. A network can be used for various purposes, such as sharing resources, accessing information, or collaborating.
- A relay is a device that switches an electrical circuit on or off based on a signal. A relay can be used for various purposes, such as controlling devices, amplifying signals, or isolating circuits.
- A Pi is a small, low-cost, and versatile computer that can run various operating systems and applications. A Pi can be used for various purposes, such as learning, experimenting, or prototyping.
- To use control web camera, network, and relays connected to the Pi, you need to follow these steps:

  - Connect the web camera to the Pi using a USB cable or a wireless adapter.
  - Connect the Pi to the network using an Ethernet cable or a wireless adapter.
  - Connect the relays to the Pi using jumper wires or a breadboard.
  - Install the necessary software and drivers on the Pi to operate the web camera, the network, and the relays.
  - Write or download a program on the Pi that can control the web camera, the network, and the relays according to your needs.
  - Run the program on the Pi and test the functionality of the web camera, the network, and the relays.



# Start Raspberry Pi and try various Linux commands in command terminal window: ls, cd, touch, mv, rm, man

- Raspberry Pi is a small, affordable computer that can run various operating systems, such as Linux.
- To start Raspberry Pi, you need to connect it to a power source, a monitor, a keyboard, and a mouse. You also need to insert a microSD card with a Linux operating system installed on it.
- Once Raspberry Pi boots up, you will see a desktop environment or a command line interface, depending on the operating system you are using.
- To open a command terminal window, you can either click on the terminal icon on the desktop or press Ctrl+Alt+T on the keyboard.
- In the command terminal window, you can type various Linux commands to perform different tasks, such as navigating the file system, creating and deleting files, moving and renaming files, and getting help on commands.
- Some of the common Linux commands are:

  - `ls`: This command lists the files and directories in the current working directory. You can use various options with this command, such as `-l` to show more details, `-a` to show hidden files, and `-h` to show human-readable file sizes.
  - `cd`: This command changes the current working directory to the one specified. You can use `.` to refer to the current directory, `..` to refer to the parent directory, and `~` to refer to the home directory. If you do not specify a directory, it will change to the home directory by default.
  - `touch`: This command creates a new, empty file with the name specified. If the file already exists, it updates its modification time to the current time.
  - `mv`: This command moves or renames a file or directory. You need to specify the source and the destination of the file or directory. If the destination is an existing directory, it will move the file or directory into it. If the destination is an existing file, it will overwrite it. If the destination does not exist, it will rename the file or directory to the destination name.
  - `rm`: This command removes or deletes a file or directory. You need to specify the name of the file or directory to remove. You can use various options with this command, such as `-r` to remove directories and their contents recursively, `-f` to force removal without prompting, and `-i` to prompt before each removal.
  - `man`: This command shows the manual page for a given command or topic. You can use the arrow keys or the space bar to scroll through the manual page, and the `q` key to quit. You can also search for a keyword by typing `/` followed by the keyword, and press `n` to go to the next match or `N` to go to the previous match.



# mkdir, rmdir, tar, g

- mkdir is a command that creates a new directory in the current working directory or a specified path.
- rmdir is a command that removes an empty directory from the file system.
- tar is a command that creates or extracts compressed archive files that can contain multiple files or directories.
- g is a command that is an alias for git, a version control system that tracks changes in source code and allows collaboration among developers.

Some examples of using these commands are:

- To create a new directory named "project" in the current working directory, use `mkdir project`.
- To remove an empty directory named "temp" from the current working directory, use `rmdir temp`.
- To create a compressed archive file named "backup.tar.gz" that contains all the files and directories in the current working directory, use `tar czvf backup.tar.gz *`.
- To clone a remote repository named "repo" from GitHub to the current working directory, use `g clone https://github.com/user/repo.git`.

