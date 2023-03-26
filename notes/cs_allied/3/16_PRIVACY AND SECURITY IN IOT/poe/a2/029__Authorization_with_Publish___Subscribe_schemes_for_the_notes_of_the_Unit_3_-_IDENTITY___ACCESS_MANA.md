 Here is the content in Markdown format without any emojis or external links:

### Authorization with Publish / Subscribe schemes

- Publish / subscribe is a messaging pattern where senders of messages, called publishers, do not program the messages to be sent directly to specific receivers, called subscribers. Instead, published messages are classified into classes, without knowledge of who may receive them.
- Interested parties can subscribe to receive messages of a particular class, and all subscribers to a class receive each published message.
- In IoT, publish / subscribe is a useful mechanism for distributing data or commands to multiple devices. For example, a temperature sensor could publish temperature readings which multiple devices could subscribe to in order to react or display the data.
- For security, publish / subscribe systems typically provide authorization mechanisms to restrict which publishers can send messages to a topic and which subscribers can receive them. For example, a given subscriber may only be authorized to receive messages from certain approved publishers.
- This allows IoT systems to implement need-to-know security, where devices only receive data they are authorized to access. Publish / subscribe also enables loose coupling between publishers and subscribers, which can aid scaling and flexibility.
- Popular publish / subscribe protocols for IoT include MQTT and SNMP. These protocols offer varying degrees of inbuilt security and authorization mechanisms, but may also be used with additional authorization via systems such as OAuth or deployed with transport layer security to encrypted channels.

The content is written in points and in a formal tone without any feelings or friendliness as directed. Let me know if you would like me to modify or expand the answer.