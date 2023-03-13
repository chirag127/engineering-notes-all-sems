## Unit 7 - Use case 2

- Use case 2 is a scenario where a user wants to book a flight ticket online using a travel website.
- The main actors involved in this use case are the user, the travel website, and the airline company.
- The main goal of this use case is to allow the user to find and book a suitable flight ticket for their desired destination and date.
- The main steps involved in this use case are:

  1. The user visits the travel website and enters their origin, destination, departure date, return date, and number of passengers.
  2. The travel website validates the user input and displays a list of available flights that match the user criteria, along with the prices and other details.
  3. The user selects a flight from the list and clicks on the book button.
  4. The travel website redirects the user to the airline company's website, where the user can review the flight details and enter their personal and payment information.
  5. The airline company verifies the user information and payment, and confirms the booking by sending a confirmation email to the user and the travel website.
  6. The user receives the confirmation email and can view their flight itinerary on the travel website or the airline company's website.

- The main alternative flows or exceptions in this use case are:

  - If the user input is invalid or incomplete, the travel website displays an error message and asks the user to correct their input.
  - If the user does not select a flight from the list, the travel website displays a message asking the user to select a flight or modify their search criteria.
  - If the user clicks on the cancel button at any point, the travel website cancels the booking process and returns the user to the home page.
  - If the user's payment is declined or the flight is no longer available, the airline company displays an error message and asks the user to try again or choose a different flight.
  - If the user does not receive the confirmation email, the user can contact the travel website or the airline company's customer service for assistance.

- A possible mnemonic to remember the main steps of this use case is:

  - **V**isit the travel website and enter the **V**alues
  - **S**elect a flight and click on the book button
  - **R**eview the flight details and enter the **R**equired information
  - **V**erify the information and payment and receive the **V**erification email
  - **R**eceive the confirmation email and view the **R**eservation

- A possible ascii diagram to illustrate this use case is:

```
  +--------+        +----------------+        +--------------+
  |  User  |        | Travel Website |        | Airline Co.  |
  +--------+        +----------------+        +--------------+
       |                     |                        |
       | 1. Enter values    |                        |
       |------------------->|                        |
       |                     |                        |
       |                     | 2. Validate values    |
       |                     |----------------------->|
       |                     |                        |
       |                     | 3. Display flights    |
       |                     |<-----------------------|
       |                     |                        |
       | 4. Select a flight |                        |
       |<------------------- |                        |
       |                     |                        |
       | 5. Click book      |                        |
       |-------------------> |                        |
       |                     | 6. Redirect to airline |
       |                     |----------------------->|
       |                     |                        |
       | 7. Review details  |                        |
       |<------------------- |                        |
       |                     |                        |
       | 8. Enter info      |                        |
       |-------------------> |                        |
       |                     | 9. Verify info & pay   |
       |                     |----------------------->|
       |                     |                        |
       |                     | 10. Confirm booking   |
       |                     |<-----------------------|
       |                     |                        |
       | 11. Receive email  |                        |
       |<------------------- |                        |
       |                     |                        |
```