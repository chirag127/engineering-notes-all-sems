## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

- RPC is a technique for creating distributed client-server applications .
- RPC allows a client to invoke a procedure or a function on a remote server as if it were a local call .
- RPC hides the details of network communication, such as protocols, data formats, and message passing.
- RPC can be implemented using various technologies, such as sockets, message queues, or web services.
- In this experiment, we will use RabbitMQ, a message broker that supports RPC  .
- RabbitMQ uses the Advanced Message Queuing Protocol (AMQP), a standard for message-oriented middleware  .
- We will create a dummy RPC service that returns Fibonacci numbers, and a client that requests them  .

### Steps to implement RPC using RabbitMQ

1. Install RabbitMQ and its client libraries for your preferred programming language (Python, JavaScript, or C#)   .
2. Define a queue for the RPC requests and a queue for the RPC responses   .
3. Create a server program that listens to the RPC request queue, computes the Fibonacci number for a given input, and sends the result to the RPC response queue   .
4. Create a client program that generates a unique correlation ID and a reply-to queue for each RPC request, sends the request to the RPC request queue, and waits for the response in the reply-to queue   .
5. Run the server and the client programs and test the RPC functionality   .

### Sample code for RPC using RabbitMQ

- The following code snippets are based on the Python tutorial from RabbitMQ .
- You can find similar code examples for JavaScript and C# from the RabbitMQ website  .

#### Server.py

```python
import pika
import time

# Connect to the RabbitMQ server
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the queue for the RPC requests
channel.queue_declare(queue='rpc_queue')

# Define a function to compute the Fibonacci number
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Define a callback function to handle the RPC requests
def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)

    # Send the response to the RPC response queue
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    # Acknowledge the RPC request
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Start consuming the RPC request queue
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
```

#### Client.py

```python
import pika
import uuid

# Define a class for the RPC client
class FibonacciRpcClient(object):

    def __init__(self):
        # Connect to the RabbitMQ server
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        # Declare an exclusive queue for the RPC responses
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        # Start consuming the RPC response queue
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    # Define a callback function to handle the RPC responses
    def on_response(self, ch, method, props, body):
        # Check if the correlation ID matches the request
        if self.corr_id == props.correlation_id: