 How to Test the Hotel Booking Bot

1. Open Amazon Lex console → Test window.
2. Type: "I want to book a room"
3. Fill all 4 slots:
   - RoomType (Single/Double/Suite)
   - CheckInDate (YYYY-MM-DD)
   - Nights (number)
   - GuestsCount (number)
4. Lex will call Lambda (alias `prod`).
5. Confirm final message:
"Room booking confirmed! room type for no.of guests starting from Checkin for No.of nights."
