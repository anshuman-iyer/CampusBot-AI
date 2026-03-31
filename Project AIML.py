import difflib
import random
import json
import re
import os
from datetime import datetime

class CampusBot:

    def __init__(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        req_dir = os.path.join(base_dir, "Requirements")

        os.makedirs(req_dir, exist_ok=True)

        self.knowledge_path = os.path.join(req_dir, "knowledge.json")
        self.chatlog_path = os.path.join(req_dir, "chat_history.txt")

        if not os.path.exists(self.knowledge_path):
            default_data = {
                "fees": [
                    "The fee is ₹100000 per semester.",
                    "Semester fee is ₹100000.",
                    "You need to pay ₹100000 each semester."
                ],
                "hostel": [
                    "Hostels are available.",
                    "Accommodation is provided on campus.",
                    "Hostel facility is available for students."
                ],
                "library": [
                    "Library is open from 8 AM to 8 PM.",
                    "Students can access the library all day.",
                    "Library timing is 8 AM to 8 PM."
                ],
                "exam": [
                    "Exams are conducted every semester.",
                    "You will have exams twice a year.",
                    "Semester exams happen regularly."
                ]
            }

            with open(self.knowledge_path, "w", encoding="utf-8") as f:
                json.dump(default_data, f, indent=2)

        if not os.path.exists(self.chatlog_path):
            open(self.chatlog_path, "w", encoding="utf-8").close()

        with open(self.knowledge_path, encoding="utf-8") as f:
            self.responses = json.load(f)

        self.keywords = {
            "fees": ["fees","fee","cost","price","tuition"],
            "hostel": ["hostel","room","accommodation"],
            "library": ["library","books"],
            "exam": ["exam","test"],
            "placement": ["placement","job","package"],
            "admission": ["admission","apply","enroll"]
        }

        self.help_phrases = [
            "help",
            "help me",
            "what can you do",
            "how do you help",
            "how do you help me",
            "what do i do",
            "what should i do",
            "what can i ask"
        ]

        self.small_talk = {
            "hi": "Hello. How can I help you?",
            "hello": "Hi. Ask me anything about the college.",
            "hey": "Hey. What would you like to know?",
            "how are you": "I am working perfectly.",
            "thanks": "You're welcome.",
            "thank you": "Happy to help."
        }

        self.last_intent = None
        self.username = None

    def normalize(self, text):
        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)
        return text.strip()

    def log_chat(self, user, bot):
        with open(self.chatlog_path, "a", encoding="utf-8") as f:
            f.write(f"You: {user}\nBot: {bot}\n")

    def greeting(self):
        hour = datetime.now().hour
        if hour < 12:
            return "Good morning"
        if hour < 18:
            return "Good afternoon"
        return "Good evening"

    def check_smalltalk(self, text):
        for key in self.small_talk:
            if key in text:
                return self.small_talk[key]
        return None

    def is_help_request(self, text):
        for phrase in self.help_phrases:
            if phrase in text:
                return True
            score = difflib.SequenceMatcher(None, text, phrase).ratio()
            if score > 0.75:
                return True
        return False

    def find_intent(self, text):
        best = None
        best_score = 0

        for intent, words in self.keywords.items():
            for word in words:
                score_full = difflib.SequenceMatcher(None, text, word).ratio()

                for token in text.split():
                    score_token = difflib.SequenceMatcher(None, token, word).ratio()
                    score = max(score_full, score_token)

                    if score > best_score:
                        best_score = score
                        best = intent

        if best_score >= 0.70:
            return best, best_score

        return None, best_score

    def help(self):
        return (
            "I can help with:\n"
            "- Fees\n"
            "- Hostel\n"
            "- Library\n"
            "- Exam\n"
            "- Placement\n"
            "- Admission\n"
            "You can also ask for contact or timings."
        )

    def contact(self):
        return "Contact: 9876543210 | email: info@college.edu"

    def timings(self):
        return "College timing is 9 AM to 5 PM."

    def respond(self, text):
        text = self.normalize(text)

        if not self.username:
            self.username = text
            return f"{self.greeting()} {self.username}. How can I help you?"

        if self.is_help_request(text):
            return self.help()

        if "contact" in text:
            return self.contact()

        if "timing" in text:
            return self.timings()

        small = self.check_smalltalk(text)
        if small:
            return small

        if text in ["how much","cost","price"] and self.last_intent:
            return random.choice(self.responses[self.last_intent])

        intent, score = self.find_intent(text)

        if intent:
            self.last_intent = intent
            return random.choice(self.responses[intent]) + f" (confidence {score:.2f})"

        return "Sorry, I did not understand. Type help."

def main():
    bot = CampusBot()

    print("CampusBot Ready")
    print("Enter your name:")

    while True:
        user = input("You: ")

        if user.lower() == "bye":
            print("Bot: Goodbye")
            break

        response = bot.respond(user)
        print("Bot:", response)
        bot.log_chat(user, response)

if __name__ == "__main__":
    main()
