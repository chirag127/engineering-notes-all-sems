### Using JavaScript in Real Time for the Notes of the Unit 4 - Introduction to Client Side Scripting in the Subject of Web Designing

- JavaScript is a scripting language that runs in the browser and can manipulate the HTML and CSS elements of a web page.
- JavaScript can also be used to create real-time applications that can communicate with the server and other clients without reloading the page.
- Real-time applications are useful for scenarios such as chat, gaming, collaboration, live streaming, etc.
- There are different ways to build real-time applications with JavaScript, such as:

  - **Long-Polling**: This is when the application requests updates from the server on a schedule. The app is "polling" the server for new data. This method is simple but inefficient and can cause high server load and network latency. 
  - **Server-Sent Events**: This is when the server pushes updates to the client whenever there is new data. The client does not need to poll the server, but only listens for events. This method is more efficient than long-polling, but it only supports one-way communication from the server to the client. 
  - **Web Sockets**: This is a technology that facilitates a true two-way communication channel between a client and a server. The client and the server can send and receive messages at any time, without any polling or HTTP requests. This method is the most efficient and flexible for real-time applications, but it requires a compatible browser and server. 
  - **SignalR**: This is a JavaScript library that abstracts the underlying communication methods and provides a simple API for real-time applications. It can use web sockets, server-sent events, long-polling, or other techniques depending on the browser and server capabilities. It also provides features such as connection management, groups, authentication, etc. 
  - **Azure SignalR**: This is a cloud service that provides a scalable and reliable infrastructure for real-time applications. It uses SignalR to handle the communication between the client and the server, and it can scale up or down depending on the demand. It also provides features such as security, monitoring, logging, etc. 

- Some examples of real-time applications built with JavaScript are:

  - **Remote Assistance**: This is an app that allows technicians and users to communicate and share screens, files, and annotations. It is built with React Native and uses web sockets for real-time communication. 
  - **Real-time Chatroom**: This is an app that allows users to join chat rooms and send messages to other connected users. It is built with Node.js and uses web sockets for real-time communication. 
  - **Real-time Dashboard**: This is an app that displays live data and charts from various sources. It is built with Angular and uses server-sent events for real-time updates.