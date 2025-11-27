🏨 Hotel Booking Chatbot using Amazon Lex V2 & AWS Lambda
----------------------------------------------------------

This project is a small hotel-booking chatbot built using Amazon Lex V2 and AWS Lambda.
It collects details like room type, check-in date, number of nights, and number of guests, and then confirms the booking using a Lambda function.
This project helped me understand how Lex slot elicitation works, how Lambda fulfillment is integrated, and how to debug issues using CloudWatch.


🚀 What the Chatbot Does
---------------------------

The user can simply type something like:
“I want to book a room”, and the bot automatically asks:

Room type — Single / Double / Suite

Check-in date (YYYY-MM-DD format)

Number of nights

Number of guests

Once all details are collected, Lex triggers a Lambda function.
Lambda reads the slot values, prepares a confirmation message, and sends it back to the bot.

The final response looks like:

Room booking confirmed! room type for no.of guests starting from checkin for no.of nights.



🧩 AWS Services Used
----------------------------
Amazon Lex V2

Creates the conversational bot

Handles sample utterances

Manages slot elicitation

Sends all data to Lambda for fulfillment

AWS Lambda (Python)

Processes the slot values

Generates final confirmation message

Handles errors safely

Returns JSON response back to Lex

Amazon CloudWatch

Stores all Lambda logs

Used for debugging issues (slot errors, formatting mistakes, NoneType errors, etc.)

IAM

Lex → Lambda invoke permission

Lambda → CloudWatch logging permission



📁 Project Structure
--------------------------
aws-lex-hotel-booking-chatbot/
│
├── lambda/
│   └── lambda_function.py            # Main fulfillment logic
│
├── docs/
│   ├── architecture.md               # Architecture explanation
│   ├── how_to_test.md                # Steps to test the bot
│   └── screenshots/                  # Screenshots added manually
│
├── .gitignore
└── README.md



🧪 How to Test the Bot (Quick Guide)
--------------------------------------

Open Amazon Lex console → Test window

Type: “I want to book a room”

Fill in all four slot prompts

Lex will call the Lambda alias (prod)

Final confirmation message will be shown



🔧 Lambda Code (Fulfillment)
-------------------------------
This Lambda function safely extracts Lex slot values and returns the final booking message.

import json

def lambda_handler(event, context):
    try:
        slots = event["sessionState"]["intent"]["slots"]

        def get_value(slot_name):
            slot = slots.get(slot_name)
            if not slot:
                return "unknown"
            value = slot.get("value")
            if not value:
                return "unknown"
            return value.get("interpretedValue") or value.get("originalValue") or "unknown"

        room_type = get_value("RoomType")
        date = get_value("CheckInDate")
        nights = get_value("Nights")
        guests = get_value("GuestsCount")

        msg = (
            f"Room booking confirmed! {room_type} room for {guests} guests "
            f"starting from {date} for {nights} nights."
        )

        return {
            "sessionState": {
                "dialogAction": {"type": "Close"},
                "intent": {
                    "name": event["sessionState"]["intent"]["name"],
                    "state": "Fulfilled",
                },
            },
            "messages": [{"contentType": "PlainText", "content": msg}],
        }

    except Exception as e:
        return {
            "sessionState": {
                "dialogAction": {"type": "Close"},
                "intent": {
                    "name": event["sessionState"]["intent"]["name"],
                    "state": "Failed",
                },
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": f"Error occurred: {str(e)}",
                }
            ],
        }

