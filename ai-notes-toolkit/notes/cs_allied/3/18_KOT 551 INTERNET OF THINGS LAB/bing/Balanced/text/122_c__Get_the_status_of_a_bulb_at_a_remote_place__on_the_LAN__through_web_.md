# Get the status of a bulb at a remote place (on the LAN) through web

- To get the status of a bulb at a remote place (on the LAN) through web, the following steps are required:

  - The bulb must be connected to a device that can communicate with the web, such as a microcontroller, a computer, or a smart plug.
  - The device must have a unique IP address or hostname on the LAN, and a web server that can handle HTTP requests and responses.
  - The device must also have a program or script that can read and write the status of the bulb, such as on, off, or dimmed, and send it back to the web client.
  - The web client, such as a browser or an app, must send an HTTP request to the device's IP address or hostname, with a specific path or query that indicates the desired action, such as get status, turn on, turn off, or set brightness.
  - The device must receive the HTTP request, parse it, and execute the corresponding action on the bulb, such as reading or writing its status.
  - The device must then send an HTTP response back to the web client, with a status code and a message that indicates the result of the action, such as OK, Not Found, or Internal Server Error.
  - The web client must receive the HTTP response, parse it, and display the result to the user, such as the current status of the bulb, or an error message.

- An example of a possible HTTP request and response for getting the status of a bulb at a remote place (on the LAN) through web is:

  - HTTP request:

    ```
    GET /bulb/status HTTP/1.1
    Host: 192.168.1.100
    ```

  - HTTP response:

    ```
    HTTP/1.1 200 OK
    Content-Type: text/plain

    Bulb is on
    ```