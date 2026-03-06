import json
import random
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGetQuote(Action):

    def name(self) -> Text:
        return "action_get_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get user intent
        intent = tracker.latest_message.get("intent", {}).get("name")

        # Map intent to category
        category_map = {
            "request_motivation": "motivation",
            "request_love": "love",
            "request_success": "success",
            "request_humor": "humor"
        }

        category = category_map.get(intent)

        # Load quotes from JSON file
        with open("quotes.json", "r") as file:
            quotes = json.load(file)

        # Select random quote
        selected_quote = random.choice(quotes[category])

        # Send quote back to user
        dispatcher.utter_message(text=selected_quote)

        return []