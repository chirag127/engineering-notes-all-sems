# Experiment 8.2 - Chat

- The objective of this experiment is to learn how to create a simple chat application using HTML, CSS, and JavaScript.
- The chat application will allow users to send and receive messages in real time using a web browser and a server.
- The chat application will consist of the following components:
  - A web page that displays the chat interface and the messages.
  - A style sheet that defines the appearance and layout of the web page.
  - A script that handles the user input, the communication with the server, and the updating of the web page.
  - A server that receives and broadcasts the messages to all connected clients.
- The steps to create the chat application are as follows:
  - Create a web page that contains a text input field, a send button, and a message area.
  - Create a style sheet that styles the web page elements and positions them using a grid layout.
  - Create a script that adds an event listener to the send button and sends the user input to the server using an XMLHttpRequest object.
  - Create a script that creates a WebSocket object and connects to the server using the ws protocol.
  - Create a script that listens for messages from the server and appends them to the message area using the innerHTML property.
  - Create a server that creates a WebSocket server using the ws module and listens for connections on a port.
  - Create a server that listens for messages from the clients and broadcasts them to all connected clients using the send method.
- The expected outcome of this experiment is to have a functional chat application that allows users to exchange messages in real time.