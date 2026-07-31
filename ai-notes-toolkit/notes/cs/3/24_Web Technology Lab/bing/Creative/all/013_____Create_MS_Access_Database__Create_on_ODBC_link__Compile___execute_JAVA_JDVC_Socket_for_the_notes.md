# Create MS Access Database, Create on ODBC link, Compile & execute JAVA JDVC Socket for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

## Create MS Access Database

- To create a MS Access database, you can follow these steps:
  - Open Access. If Access is already open, select File > New.
  - Select Blank database, or select a template.
  - Enter a name for the database, select a location, and then select Create.
  - If needed, select Enable content in the yellow message bar when the database opens.
- To create tables, queries, forms, reports, and other objects in the database, you can use the Navigation Pane and the ribbon tabs.
- To enter data into the tables, you can use the datasheet view or the form view.
- To save the database, you can use the Save or Save As commands in the File tab.

## Create on ODBC link

- To create an ODBC link to the MS Access database, you can follow these steps:
  - Open the ODBC Data Source Administrator from the Control Panel or the Start menu.
  - Select the System DSN tab and click Add.
  - Select the Microsoft Access Driver (*.mdb, *.accdb) and click Finish.
  - Enter a name and a description for the data source and click Select.
  - Browse to the location of the MS Access database file and click OK.
  - Click OK to create the data source.

## Compile & execute JAVA JDVC Socket

- To compile and execute a JAVA JDVC Socket program that connects to the MS Access database, you can follow these steps:
  - Write the JAVA JDVC Socket program in a text editor or an IDE. The program should import the java.sql package and use the DriverManager, Connection, Statement, and ResultSet classes to establish a connection, execute a query, and retrieve the results from the database. The program should also handle any exceptions that may occur during the process. The connection string should use the ODBC data source name that was created in the previous step.
  - Save the program as a .java file with the same name as the class name.
  - Open a command prompt and navigate to the directory where the .java file is saved.
  - Compile the program using the javac command. For example, javac MyProgram.java
  - Run the program using the java command. For example, java MyProgram
  - The program should display the output of the query or any error messages on the console.