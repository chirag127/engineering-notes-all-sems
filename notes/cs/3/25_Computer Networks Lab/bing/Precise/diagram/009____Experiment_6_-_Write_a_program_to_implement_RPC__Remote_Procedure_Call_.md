## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

Remote Procedure Call (RPC) is a protocol that allows a program to request a service from a program located on another computer in a network without having to understand the network's details. RPC is used to call other processes on the remote systems like a local system.

Here are the steps to implement RPC:

1. Define the remote procedure and the data structures required to pass the data.
2. Generate the client and server stubs using the RPC compiler.
3. Write the client program that calls the remote procedure.
4. Write the server program that implements the remote procedure.
5. Compile and run the server and client programs.

The client program sends a message to the server with the name of the procedure to call, along with the required parameters. The server receives the message, unpacks the parameters, and calls the procedure. Once the procedure is completed, the server packs the result in a message and sends it back to the client.

Here is an example of a simple RPC program that adds two numbers on the server and returns the result to the client:

**Interface Definition File (add.x):**
```
program ADD_PROG {
    version ADD_VERS {
        int ADD(int, int) = 1;
    } = 1;
} = 0x20000001;
```

**Server Program (add_server.c):**
```
#include <stdio.h>
#include <rpc/rpc.h>
#include "add.h"

int *add_1_svc(int *num1, int *num2, struct svc_req *req) {
    static int result;
    result = *num1 + *num2;
    return &result;
}
```

**Client Program (add_client.c):**
```
#include <stdio.h>
#include <rpc/rpc.h>
#include "add.h"

int main(int argc, char *argv[]) {
    CLIENT *cl;
    int *result;
    int num1, num2;

    if (argc != 4) {
        fprintf(stderr, "Usage: %s hostname num1 num2\n", argv[0]);
        exit(1);
    }

    num1 = atoi(argv[2]);
    num2 = atoi(argv[3]);

    cl = clnt_create(argv[1], ADD_PROG, ADD_VERS, "tcp");
    if (cl == NULL) {
        clnt_pcreateerror(argv[1]);
        exit(1);
    }

    result = add_1(&num1, &num2, cl);
    if (result == NULL) {
        clnt_perror(cl, argv[1]);
        exit(1);
    }

    printf("%d + %d = %d\n", num1, num2, *result);

    return 0;
}
```

To compile and run the program, follow these steps:

1. Run the RPC compiler on the interface definition file to generate the client and server stubs: `rpcgen add.x`
2. Compile the server program: `cc -o add_server add_server.c add_svc.c`
3. Compile the client program: `cc -o add_client add_client.c add_clnt.c`
4. Run the server program: `./add_server`
5. Run the client program: `./add_client localhost 3 4`

The client program will send the numbers 3 and 4 to the server, the server will add them and return the result 7 to the client. The client will print the result on the screen.

This is a simple example of how to implement RPC. You can modify the program to implement more complex remote procedures and data structures.