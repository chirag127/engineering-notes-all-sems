## Unit 8 - Use case 3

- Use case 3 is a scenario where a user wants to book a flight ticket online using a travel website.
- The main actors involved in this use case are the user, the travel website, and the airline company.
- The main goal of this use case is to allow the user to find and book a suitable flight ticket for their desired destination and date.
- The main steps involved in this use case are:

  1. The user visits the travel website and enters their origin, destination, date, and number of passengers.
  2. The travel website searches for available flights from different airline companies that match the user's criteria and displays them on the screen.
  3. The user selects a flight from the list and clicks on the book button.
  4. The travel website redirects the user to the airline company's website and passes the flight information as a parameter.
  5. The airline company's website verifies the flight availability and price and asks the user to enter their personal and payment details.
  6. The user enters their details and confirms the booking.
  7. The airline company's website sends a confirmation email to the user and updates the flight reservation system.
  8. The travel website displays a confirmation message to the user and thanks them for using their service.

- The main alternative flows in this use case are:

  - If the user does not find a suitable flight in the list, they can modify their search criteria and repeat step 2.
  - If the user cancels the booking process at any point, they can return to the travel website and start over.
  - If the flight is not available or the price has changed, the airline company's website informs the user and asks them to choose another flight or cancel the booking.
  - If the user's payment is declined, the airline company's website informs the user and asks them to enter a valid payment method or cancel the booking.

- The main preconditions and postconditions for this use case are:

  - Preconditions:
    - The user has access to the internet and a web browser.
    - The travel website and the airline company's website are functional and secure.
    - The user has a valid email address and a payment method.
  - Postconditions:
    - The user has booked a flight ticket for their desired destination and date.
    - The user has received a confirmation email from the airline company.
    - The flight reservation system has been updated with the user's booking.

- A possible mnemonic to remember the main steps of this use case is:

  - **F**ind **F**light
  - **S**elect **F**light
  - **B**ook **F**light
  - **E**nter **D**etails
  - **C**onfirm **B**ooking
  - **R**eceive **E**mail
  - **T**hank **W**ebsite

- A possible ascii diagram to illustrate this use case is:

```
  +--------+       +---------------+       +---------------+
  |  User  |       | Travel Website|       | Airline Website|
  +--------+       +---------------+       +---------------+
     |                    |                       |
     | 1. Enter criteria |                       |
     |------------------->|                       |
     |                    |                       |
     |                    | 2. Search flights     |
     |                    |---------------------->| 
     |                    |                       |
     |                    | 3. Display flights    |
     |                    |<----------------------| 
     |                    |                       |
     | 4. Select flight   |                       |
     |<-------------------|                       |
     |                    |                       |
     | 5. Book flight     |                       |
     |------------------->|                       |
     |                    |                       |
     |                    | 6. Redirect to airline|
     |                    |---------------------->| 
     |                    |                       |
     | 7. Enter details   |                       |
     |<-------------------------------------------|
     |                    |                       |
     | 8. Confirm booking |                       |
     |------------------------------------------->|
     |                    |                       |
     |                    | 9. Send email         |
     |                    |<----------------------| 
     |                    |                       |
     |                    | 10. Display message   |
     |                    |---------------------->| 
     |                    |                       |
     | 11. Thank website  |                       |
     |<-------------------|                       |
     |                    |                       |
```