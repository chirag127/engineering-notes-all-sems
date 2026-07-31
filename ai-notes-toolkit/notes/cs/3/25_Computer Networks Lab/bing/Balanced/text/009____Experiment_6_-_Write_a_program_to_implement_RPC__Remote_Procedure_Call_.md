## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

- RPC (Remote Procedure Call) is a technique that allows a program to execute a procedure or a function on a different machine, as if it was a local call.
- RPC involves two components: a client and a server. The client sends a request to the server, specifying the name and parameters of the procedure to be executed. The server receives the request, invokes the procedure, and sends back the result to the client.
- RPC can be implemented using different protocols, such as TCP/IP, UDP, HTTP, etc. In this experiment, we will use TCP/IP as the underlying protocol.
- To implement RPC, we need to define the interface of the remote procedure, using a language-independent format, such as IDL (Interface Definition Language). The IDL compiler generates the stubs and skeletons for the client and server, respectively. The stubs and skeletons are the code that handles the communication and marshalling of the parameters and results between the client and server.
- The steps to implement RPC are as follows:

  1. Define the interface of the remote procedure in IDL. For example, suppose we want to implement a remote procedure that calculates the factorial of a given number. The IDL file can be written as:

  ```
  // factorial.idl
  interface Factorial {
    int factorial (in int n);
  };
  ```

  2. Compile the IDL file using the IDL compiler. This will generate the stubs and skeletons for the client and server in the chosen programming language. For example, if we use C as the programming language, the IDL compiler will generate the following files:

  ```
  // factorial_c.h
  // This file contains the declarations of the stubs and skeletons
  #ifndef FACTORIAL_C_H
  #define FACTORIAL_C_H

  #include <rpc/rpc.h>

  #define FACTORIAL_PROG 0x12345678 // A unique identifier for the program
  #define FACTORIAL_VERS 1 // The version number of the program
  #define FACTORIAL_PROC 1 // The procedure number of the factorial function

  // The data structure that represents the input parameter
  typedef struct {
    int n;
  } factorial_in;

  // The data structure that represents the output result
  typedef struct {
    int res;
  } factorial_out;

  // The declaration of the client stub
  factorial_out *factorial_1(factorial_in *argp, CLIENT *clnt);

  // The declaration of the server skeleton
  void *factorial_1_svc(factorial_in *argp, struct svc_req *rqstp);

  #endif
  ```

  ```
  // factorial_clnt.c
  // This file contains the definition of the client stub
  #include "factorial_c.h"

  // The definition of the client stub
  factorial_out *factorial_1(factorial_in *argp, CLIENT *clnt) {
    static factorial_out res;

    // Clear the result
    memset((char *)&res, 0, sizeof(res));

    // Call the remote procedure using TCP
    if (clnt_call(clnt, FACTORIAL_PROC, xdr_factorial_in, argp, xdr_factorial_out, &res, TIMEOUT) != RPC_SUCCESS) {
      return NULL;
    }

    // Return the result
    return &res;
  }
  ```

  ```
  // factorial_svc.c
  // This file contains the definition of the server skeleton
  #include "factorial_c.h"

  // The definition of the server skeleton
  void *factorial_1_svc(factorial_in *argp, struct svc_req *rqstp) {
    static factorial_out res;

    // Clear the result
    memset((char *)&res, 0, sizeof(res));

    // Call the local procedure that implements the factorial logic
    res.res = factorial(argp->n);

    // Return the result
    return &res;
  }
  ```

  3. Write the client and server programs that use the stubs and skeletons. For example, the client program can be written as:

  ```
  // factorial_client.c
  // This file contains the main function of the client program
  #include "factorial_c.h"

  // The main function of the client program
  int main(int argc, char *argv[]) {
    CLIENT *clnt; // The client handle
    factorial_in in; // The input parameter
    factorial_out *out; // The output result

    // Check the number of arguments
    if (argc != 3) {

```
