## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

- RPC is a technique that allows a program to invoke a procedure or a function on a different machine or process as if it were a local call.
- RPC hides the details of the network communication, such as the message formats, protocols, and data marshalling, from the application programmer.
- RPC consists of two components: a client and a server.
- The client is the program that initiates the request for a remote procedure call, and the server is the program that executes the requested procedure and returns the result to the client.
- The client and the server communicate through a stub, which is a piece of code that acts as an interface between the application and the network layer.
- The client stub prepares the parameters for the remote procedure call, encodes them into a message, and sends it to the server stub over the network.
- The server stub receives the message, decodes the parameters, invokes the appropriate procedure on the server, encodes the result into a message, and sends it back to the client stub.
- The client stub then decodes the result and returns it to the client application.

### Steps to write a program to implement RPC

- To write a program to implement RPC, we need to use a tool that can generate the stubs for the client and the server based on a common interface definition.
- One such tool is RPCGEN, which is a compiler that takes an input file containing the definitions of the remote procedures and their parameters, and produces the following files:
  - A header file that contains the declarations of the data types and the constants used by the remote procedures.
  - A client stub file that contains the code for the client stub.
  - A server stub file that contains the code for the server stub.
  - A client main file that contains the code for the client application.
  - A server main file that contains the code for the server application.
- The input file for RPCGEN has a .x extension and follows a specific syntax. It consists of three sections: definitions, declarations, and programs.
  - The definitions section contains the definitions of the data types and the constants used by the remote procedures. It uses the C syntax for defining structures, unions, enumerations, and typedefs.
  - The declarations section contains the declarations of the remote procedures and their parameters. It uses the following syntax: `return_type procedure_name(parameter_type parameter_name, ...);`
  - The programs section contains the definitions of the programs that provide the remote procedures. It uses the following syntax: `program program_name { version version_name { procedure_declaration; ... } = version_number; ... } = program_number;`
- The program_number and the version_number are unique identifiers that are used to locate and invoke the remote procedures on the server.
- The RPCGEN tool can be invoked by using the following command: `rpcgen -a input_file.x`
- This command will generate the following files: input_file.h, input_file_clnt.c, input_file_svc.c, input_file_client.c, and input_file_server.c.
- The input_file_client.c and input_file_server.c files contain the skeleton code for the client and the server applications, respectively. They need to be modified by the programmer to implement the desired functionality.
- The input_file_clnt.c and input_file_svc.c files contain the code for the client and the server stubs, respectively. They do not need to be modified by the programmer.
- The input_file.h file contains the declarations of the data types and the constants used by the remote procedures. It is included by both the client and the server applications.
- To compile and run the program, we need to use the following commands:
  - `gcc -o input_file_client input_file_client.c input_file_clnt.c -lnsl`
  - `gcc -o input_file_server input_file_server.c input_file_svc.c -lnsl`
  - `./input_file_server &`
  - `./input_file_client server_host_name`
- The -lnsl flag is used to link the network services library, which is required by the RPC library.
- The server_host_name is the name or the IP address of the machine where the server is running.
- The server program runs in the background and waits for the client requests.
- The client program takes the server host name as an argument and invokes the remote procedures on the server.

### Example of a program to implement RPC

- Suppose we want to write a program to implement RPC that provides two remote procedures: add and subtract, which take two integers as parameters and return their sum and difference, respectively.
- The input file for RPCGEN would look like this:

```c
// input_file.x
// definitions section
typedef int