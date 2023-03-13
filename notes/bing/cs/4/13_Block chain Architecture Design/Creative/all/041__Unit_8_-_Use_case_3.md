## Unit 8 - Use case 3

- Use case 3 is a scenario where a user wants to book a flight ticket online using a travel website.
- The main actors involved in this use case are the user, the travel website, and the airline company.
- The main goal of this use case is to allow the user to find and book a suitable flight ticket for their desired destination and date.
- The main steps involved in this use case are:

  1. The user visits the travel website and enters their origin, destination, departure date, return date, and number of passengers.
  2. The travel website validates the user input and displays a list of available flights that match the user criteria, along with the prices and other details.
  3. The user selects a flight from the list and clicks on the book button.
  4. The travel website redirects the user to the airline company's website, where the user has to provide their personal and payment information.
  5. The airline company verifies the user information and confirms the booking.
  6. The airline company sends a confirmation email to the user with the booking details and the ticket number.
  7. The user receives the confirmation email and prints the ticket or saves it on their device.

- The main alternative flows or exceptions in this use case are:

  - If the user enters invalid or incomplete input, the travel website displays an error message and asks the user to correct their input.
  - If the user does not select a flight from the list, the travel website displays a message asking the user to select a flight or modify their search criteria.
  - If the user clicks on the cancel button at any point, the travel website cancels the booking process and returns the user to the home page.
  - If the airline company's website is down or unavailable, the travel website displays a message informing the user of the issue and asks them to try again later.
  - If the user's payment is declined or unsuccessful, the airline company displays a message informing the user of the problem and asks them to provide a different payment method or contact their bank.

- A possible mnemonic or learning trick for this use case is to remember the acronym FABRIC, which stands for:

  - Find flights
  - Book flight
  - Redirect to airline
  - Confirm booking
  - Receive confirmation

- A possible ascii diagram for this use case is:

```
    +--------+       +---------------+       +--------------+
    |  User  |       | Travel Website|       | Airline      |
    +--------+       +---------------+       +--------------+
         |                   |                      |
         | 1. Enter search   |                      |
         |    criteria       |                      |
         |------------------>|                      |
         |                   |                      |
         |                   | 2. Validate input    |
         |                   |    and display       |
         |                   |    available flights |
         |                   |<---------------------|
         |                   |                      |
         | 3. Select flight  |                      |
         |    and book       |                      |
         |------------------>|                      |
         |                   |                      |
         |                   | 4. Redirect to       |
         |                   |    airline website   |
         |<------------------------------------------|
         |                   |                      |
         | 5. Provide        |                      |
         |    personal and   |                      |
         |    payment info   |                      |
         |------------------------------------------>|
         |                   |                      |
         |                   | 6. Verify info and   |
         |                   |    confirm booking   |
         |<------------------------------------------|
         |                   |                      |
         |                   | 7. Send confirmation |
         |                   |    email             |
         |<------------------------------------------|
         |                   |                      |
         | 8. Receive        |                      |
         |    confirmation   |                      |
         |    email          |                      |
         |------------------>|                      |
         |                   |                      |
```