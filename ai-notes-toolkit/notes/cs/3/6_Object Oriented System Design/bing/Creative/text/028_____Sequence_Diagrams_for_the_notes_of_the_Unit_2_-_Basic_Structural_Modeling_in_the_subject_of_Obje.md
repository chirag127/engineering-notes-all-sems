### Sequence Diagrams

- Sequence diagrams are a type of interaction diagram that show how objects interact with each other in a time-ordered manner.
- Sequence diagrams are useful for modeling the dynamic behavior of a system, such as the interactions between objects in a use case or scenario.
- Sequence diagrams consist of vertical lifelines that represent the objects or classes involved in the interaction, and horizontal arrows that represent the messages exchanged between them.
- Sequence diagrams can also show the activation of objects, the creation and destruction of objects, the return of values, the use of alternative and parallel flows, and the use of loops and conditions.
- Sequence diagrams can be used to document the logic of a system, to design a new system, to validate an existing system, or to visualize the execution of a system.

#### Example of a Sequence Diagram

- The following sequence diagram shows how a hotel reservation system works.
- The diagram has four lifelines: the customer, the hotel website, the hotel, and the bank.
- The customer initiates the interaction by browsing the hotel website and selecting a room.
- The hotel website sends a request to the hotel to check the availability of the room.
- The hotel responds with a confirmation or a rejection.
- If the room is available, the customer enters the payment details and confirms the reservation.
- The hotel website sends a request to the bank to process the payment.
- The bank responds with a confirmation or a rejection.
- If the payment is successful, the hotel website sends a confirmation to the customer and the hotel.
- If the payment is unsuccessful, the hotel website sends a rejection to the customer and the hotel.

![Sequence diagram for hotel reservation](https://creately.com/blog/wp-content/uploads/2012/08/Sequence-Diagram-Hotel-Reservation-System.png)