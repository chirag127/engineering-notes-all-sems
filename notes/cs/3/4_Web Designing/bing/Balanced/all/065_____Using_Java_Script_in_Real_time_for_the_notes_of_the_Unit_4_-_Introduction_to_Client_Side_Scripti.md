# Using JavaScript in Real Time for the Notes of the Unit 4 - Introduction to Client Side Scripting in the Subject of Web Designing

- JavaScript is a scripting language that runs in the browser and can manipulate the HTML and CSS elements of a web page.
- JavaScript can also be used to create real-time applications that can communicate with the server and other clients without reloading the page.
- Real-time applications are those that can update the data and the user interface instantly as the events occur, such as chat, gaming, video conferencing, etc.
- There are different ways to build real-time applications with JavaScript, such as:

  - Long-Polling: This is when the application requests updates from the server on a schedule. The app is “polling” the server for new data. This method is simple but inefficient and can cause delays and high server load.
  - Server-Sent Events: This is when the server pushes updates to the client whenever there is new data. The client does not need to request the data, but only listens for the events from the server. This method is more efficient and faster than long-polling, but it only supports one-way communication from the server to the client.
  - Web Sockets: This is a technology that facilitates a true two-way communication channel between a client and a server. The client and the server can send and receive data at any time, without any polling or event listening. This method is the most efficient and fastest way to build real-time applications, but it requires a compatible browser and server.
  - SignalR: This is a JavaScript library that abstracts the different methods of real-time communication and provides a simple and consistent API. It can automatically detect the best method to use based on the browser and the server capabilities. It can also handle connection issues and fallbacks.
  - Azure SignalR: This is a cloud service that provides a scalable and reliable infrastructure for real-time applications. It can handle millions of concurrent connections and messages, and it integrates with other Azure services such as authentication, storage, and functions.

- Some examples of real-time applications that can be built with JavaScript are:

  - Remote assistance: This is an app that allows technicians and users to communicate and share screens, files, and annotations. It can be built with React Native and Socket.IO.
  - Chatroom: This is an app that allows users to send and receive text messages, images, and emojis. It can be built with Node.js and Socket.IO.
  - Gaming: This is an app that allows users to play online games with other players and see the game state in real time. It can be built with Phaser and Socket.IO.
  - Video conferencing: This is an app that allows users to have video and audio calls with other users and share their screens. It can be built with WebRTC and Socket.IO.
  - Dashboard: This is an app that displays real-time data and charts from various sources. It can be built with D3.js and Server-Sent Events.