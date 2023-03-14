## Unit 7 - Use case 2

- Use case 2 is a scenario where a user wants to book a flight ticket online using a travel website.
- The main actors involved in this use case are the user, the travel website, and the airline company.
- The main goal of this use case is to allow the user to find and book a suitable flight ticket for their desired destination and date.
- The main steps involved in this use case are:

  1. The user visits the travel website and enters their origin, destination, date, and number of passengers.
  2. The travel website searches for available flights from various airline companies and displays the results to the user.
  3. The user selects a flight from the results and proceeds to the payment page.
  4. The travel website verifies the user's payment details and confirms the booking with the airline company.
  5. The travel website sends a confirmation email to the user with the flight details and the booking reference number.
  6. The user receives the confirmation email and prints the flight ticket.

- The main alternative flows in this use case are:

  - If the user does not find a suitable flight from the results, they can modify their search criteria and repeat step 2.
  - If the user's payment is declined, they can enter a different payment method and repeat step 4.
  - If the travel website or the airline company encounters a technical error, they can display an error message to the user and ask them to try again later.

- The main preconditions for this use case are:

  - The user has a valid email address and a payment method.
  - The travel website and the airline company are operational and connected.

- The main postconditions for this use case are:

  - The user has a confirmed flight booking and a flight ticket.
  - The travel website and the airline company have updated their records and inventory.

- A possible mnemonic to remember the main steps of this use case is:

  - **F**ind
  - **S**elect
  - **P**ay
  - **C**onfirm
  - **R**eceive
  - **P**rint

- A possible ascii diagram to illustrate this use case is:

```
  User                  Travel Website              Airline Company
    |                          |                          |
    |----Enter search criteria---->|                          |
    |                          |----Search for flights----->|
    |                          |<---Return flight results----|
    |<---Display flight results----|                          |
    |----Select a flight---------->|                          |
    |                          |----Verify availability----->|
    |                          |<---Confirm availability-----|
    |<---Proceed to payment page---|                          |
    |----Enter payment details---->|                          |
    |                          |----Process payment--------->|
    |                          |<---Confirm payment----------|
    |<---Confirm booking---------->|                          |
    |                          |----Send confirmation email->|
    |<---Receive confirmation email|                          |
    |----Print flight ticket------>|                          |
    |                          |                          |
```