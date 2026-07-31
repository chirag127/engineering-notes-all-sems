### Using JavaScript in Real Time

JavaScript is a scripting language that can run in the browser and interact with the web page elements. It can also be used to create real-time applications that update the data or the user interface without reloading the page. Some examples of real-time applications are chat apps, online games, live streaming, etc.

There are different ways to build real-time apps with JavaScript, depending on the communication model and the technology used. Here are some of the common methods:

- **Long-Polling**: This is when the application requests updates from the server on a schedule. The app is “polling” the server for new data at regular intervals. This method is simple to implement, but it can be inefficient and consume a lot of bandwidth and resources. 
- **Server-Sent Events**: Server-Sent Events (SSE) is similar to long-polling in so much as the client asks the server for information. However, instead of sending a response and closing the connection, the server keeps the connection open and sends data whenever there is an update. The client listens for these events and updates the UI accordingly. This method is more efficient than long-polling, but it only supports one-way communication from the server to the client. 
- **Web Sockets**: Web Sockets is a technology that facilitates a true two-way communication channel between a client and a server. The client and the server can send and receive data at any time, without polling or waiting for a response. This method is the most suitable for real-time applications that require bidirectional and low-latency communication. However, it also requires more complex implementation and compatibility issues. 
- **SignalR**: SignalR is a library that simplifies the development of real-time applications with JavaScript. It abstracts the underlying communication technology and provides a consistent API for the client and the server. It also supports fallback mechanisms for browsers that do not support Web Sockets or SSE. SignalR can be used with any JavaScript framework or library, such as React, Angular, Vue, etc.  
- **Azure SignalR**: Azure SignalR is a cloud service that provides a scalable and reliable infrastructure for real-time applications. It leverages the SignalR library and handles the connection management, authentication, load balancing, and security for the app. Azure SignalR can be integrated with other Azure services, such as Functions, App Service, Logic Apps, etc.  

To show date and time in real-time in JavaScript, one can use the following steps:

- Create a time interval with `setInterval` function, which executes a function repeatedly after a specified time.
- Start or iterate a `Date` object, which represents the current date and time.
- Display the formatted date on the screen or console, using the `innerHTML` property or the `console.log` method. 

For example, the following code displays the current time in the format of HH:MM:SS in a span element with the id of "time":

```javascript
// Get the span element by id
let timeSpan = document.getElementById("time");

// Create a function to update the time
function updateTime() {
  // Create a new Date object
  let date = new Date();

  // Get the hours, minutes, and seconds
  let hours = date.getHours();
  let minutes = date.getMinutes();
  let seconds = date.getSeconds();

  // Format the time with leading zeros
  hours = hours < 10 ? "0" + hours : hours;
  minutes = minutes < 10 ? "0" + minutes : minutes;
  seconds = seconds < 10 ? "0" + seconds : seconds;

  // Display the time in the span element
  timeSpan.innerHTML = hours + ":" + minutes + ":" + seconds;
}

// Call the function once to display the initial time
updateTime();

// Set an interval to call the function every second
setInterval(updateTime, 1000);
```

To create real-time charts and graphs with JavaScript, one can use various libraries and frameworks that provide interactive and dynamic visualization features. Some of the popular options are:

- **Chart.js**: Chart.js is a simple and lightweight library that uses HTML5 canvas to render various types of charts, such as line, bar, pie, doughnut, radar, polar, etc. It supports animation, responsiveness, interactivity, and customization. 
- **D3.js**: D3.js is a powerful and flexible library that uses SVG