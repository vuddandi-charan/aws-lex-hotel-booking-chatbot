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

            # Lex V2 can return interpretedValue OR originalValue
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
