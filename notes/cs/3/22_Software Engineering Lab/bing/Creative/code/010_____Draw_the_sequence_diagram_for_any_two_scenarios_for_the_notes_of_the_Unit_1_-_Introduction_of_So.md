# Sequence Diagram for Software Engineering Lab

A sequence diagram is a type of interaction diagram that shows the order and timing of messages exchanged between objects in a system. It is used to illustrate the functionality and behavior of a system or a use case. A sequence diagram consists of the following elements:

- **Lifelines**: vertical dashed lines that represent the existence of an object over time. They are labeled with the name and type of the object, such as `:Customer` or `c:Customer`.
- **Activation boxes**: thin rectangles on a lifeline that indicate the period of time an object is active or executing a method.
- **Messages**: horizontal arrows between lifelines that represent the communication or invocation of a method between objects. They are labeled with the name and parameters of the method, such as `makePayment(amount)`. There are different types of messages, such as synchronous, asynchronous, reply, create, and destroy.
- **Fragments**: boxes that enclose a part of the interaction to show some additional information or constraints, such as loops, alternatives, options, breaks, parallel, etc. They are labeled with the name and condition of the fragment, such as `alt [payment successful]` or `loop [while items available]`.
- **Frames**: rectangles that surround the entire diagram or a part of it to indicate the scope or context of the interaction, such as a system, a subsystem, a use case, etc. They are labeled with the name and type of the frame, such as `sd Make Online Purchase` or `ref Check Stock Availability`.

Here are two examples of sequence diagrams for the notes of the Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab:

## Example 1: Make Online Purchase

This diagram shows the interaction between a customer, a web browser, a web server, and a database when the customer makes an online purchase on a website.

![Make Online Purchase](https://i.imgur.com/8Zf8w1w.png)

The steps are as follows:

1. The customer browses the website using the web browser and selects some items to buy.
2. The web browser sends a request to the web server to add the items to the shopping cart.
3. The web server updates the shopping cart in the database and sends a response to the web browser.
4. The customer proceeds to checkout and enters the payment details.
5. The web browser sends a request to the web server to process the payment.
6. The web server validates the payment details and sends a request to the database to deduct the amount from the customer's account.
7. The database updates the customer's account and sends a response to the web server.
8. The web server sends a response to the web browser to confirm the payment and the order.
9. The web browser displays a confirmation message to the customer.

## Example 2: Withdraw Cash from ATM

This diagram shows the interaction between a customer, an ATM, and a bank when the customer withdraws cash from the ATM.

![Withdraw Cash from ATM](https://i.imgur.com/0fz0Z0F.png)

The steps are as follows:

1. The customer inserts the card into the ATM and enters the PIN.
2. The ATM sends a request to the bank to verify the card and the PIN.
3. The bank checks the card and the PIN and sends a response to the ATM.
4. The ATM displays the available options to the customer.
5. The customer selects the option to withdraw cash and enters the amount.
6. The ATM sends a request to the bank to check the balance and authorize the withdrawal.
7. The bank checks the balance and authorizes the withdrawal and sends a response to the ATM.
8. The ATM dispenses the cash and prints the receipt to the customer.
9. The ATM sends a request to the bank to update the balance and record the transaction.
10. The bank updates the balance and records the transaction and sends a response to the ATM.
11. The ATM ejects the card and displays a thank you message to the customer.