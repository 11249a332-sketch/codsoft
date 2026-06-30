import datetime
import random
import re
import math
import string

# ==========================
# USER DATA
# ==========================
name = ""
age = ""
address = ""

# ==========================
# BOT DATA
# ==========================
BOT_NAME = "SmartBot"
BOT_AGE = "1 Year"
BOT_ADDRESS = "Cloud Server"

print("=" * 60)
print("🤖 SMART CHATBOT")
print("=" * 60)

print("Bot: Hello! 👋")
print("Bot: What is your name?")

while True:

    user = input("You: ")
    text = user.lower().strip()

    # ==========================
    # EXIT
    # ==========================
    if text in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! 👋 Have a great day!")
        break

    # ==========================
    # NAME
    # ==========================
    elif name == "":
        name = user
        print(f"Bot: Nice to meet you, {name}! 😊")
        print("Bot: How old are you?")

    # ==========================
    # AGE
    # ==========================
    elif age == "":
        nums = re.findall(r"\d+", text)

        if nums:
            age = nums[0]
            print(f"Bot: Great! You are {age} years old.")
            print("Bot: Where are you from?")
        else:
            print("Bot: Please enter a valid age.")

    # ==========================
    # ADDRESS
    # ==========================
    elif address == "":
        address = user

        print(f"Bot: Nice! You are from {address}.")
        print("Bot: Your details have been saved.\n")

        print("===== BOT DETAILS =====")
        print("Bot Name :", BOT_NAME)
        print("Bot Age :", BOT_AGE)
        print("Bot Address :", BOT_ADDRESS)
        print("=======================\n")

        print("Bot: Ask me anything!")

    # ==========================
    # USER DETAILS
    # ==========================
    elif "my details" in text or "who am i" in text:
        print("\n===== YOUR DETAILS =====")
        print("Name :", name)
        print("Age :", age)
        print("Address :", address)
        print("========================")

    # ==========================
    # BOT DETAILS
    # ==========================
    elif "your details" in text or "who are you" in text:
        print("\n===== BOT DETAILS =====")
        print("Name :", BOT_NAME)
        print("Age :", BOT_AGE)
        print("Address :", BOT_ADDRESS)
        print("=======================")

    # ==========================
    # TIME
    # ==========================
    elif "time" in text:
        print("Bot:", datetime.datetime.now().strftime("%I:%M:%S %p"))

    # ==========================
    # DATE
    # ==========================
    elif "date" in text:
        print("Bot:", datetime.datetime.now().strftime("%d-%m-%Y"))

    # ==========================
    # JOKES
    # ==========================
    elif "joke" in text:
        jokes = [
            "Why was six afraid of seven? Because seven ate nine! 😂",
            "Why do programmers prefer dark mode? Because light attracts bugs! 😆",
            "What do you call fake spaghetti? An impasta! 😂",
            "Why did the computer go to the doctor? Because it had a virus! 🤣",
            "Why can't a bicycle stand alone? Because it is two tired! 🚲😄"
        ]
        print("Bot:", random.choice(jokes))

    # ==========================
    # MOTIVATION
    # ==========================
    elif "motivate" in text or "motivation" in text:
        quotes = [
            "Believe in yourself. 💪",
            "Every expert was once a beginner. 🚀",
            "Success comes from consistency. ⭐",
            "Never stop learning. 📚",
            "Small progress is still progress. 😊"
        ]
        print("Bot:", random.choice(quotes))

    # ==========================
    # GREETINGS
    # ==========================
    elif text in ["hi", "hello", "hey"]:
        replies = [
            "Hello again! 👋",
            "Nice to see you! 😊",
            "Hey there! 😄"
        ]
        print("Bot:", random.choice(replies))

    elif "how are you" in text:
        print("Bot: I'm doing great! Thanks for asking. 😊")

    elif "thanks" in text:
        print("Bot: You're welcome! 😄")

    # ==========================
    # ADDITION
    # ==========================
    elif "add" in text:
        nums = re.findall(r"\d+", text)

        if len(nums) >= 2:
            print("Bot:", int(nums[0]) + int(nums[1]))
        else:
            print("Bot: Example -> add 10 and 20")

    # ==========================
    # SUBTRACTION
    # ==========================
    elif "subtract" in text:
        nums = re.findall(r"\d+", text)

        if len(nums) >= 2:
            print("Bot:", int(nums[0]) - int(nums[1]))
        else:
            print("Bot: Example -> subtract 50 and 10")

    # ==========================
    # MULTIPLICATION
    # ==========================
    elif "multiply" in text:
        nums = re.findall(r"\d+", text)

        if len(nums) >= 2:
            print("Bot:", int(nums[0]) * int(nums[1]))
        else:
            print("Bot: Example -> multiply 5 and 6")

    # ==========================
    # DIVISION
    # ==========================
    elif "divide" in text:
        nums = re.findall(r"\d+", text)

        if len(nums) >= 2:

            if int(nums[1]) != 0:
                print("Bot:", int(nums[0]) / int(nums[1]))
            else:
                print("Bot: Cannot divide by zero.")
        else:
            print("Bot: Example -> divide 20 by 5")

    # ==========================
    # PERCENTAGE CALCULATOR
    # ==========================
    elif "percentage" in text:
        try:
            marks = float(input("Enter obtained marks: "))
            total = float(input("Enter total marks: "))

            percentage = (marks / total) * 100

            print(f"Bot: Percentage = {percentage:.2f}%")

        except:
            print("Bot: Invalid input.")

    # ==========================
    # PASSWORD GENERATOR
    # ==========================
    elif "password" in text:

        chars = string.ascii_letters + string.digits + "@#$%"

        password = "".join(random.choice(chars) for _ in range(10))

        print("Bot: Generated Password =", password)

    # ==========================
    # SQUARE ROOT
    # ==========================
    elif "square root" in text:

        nums = re.findall(r"\d+", text)

        if nums:
            print("Bot:", math.sqrt(int(nums[0])))

    # ==========================
    # SYMBOL CALCULATOR
    # ==========================
    elif any(op in text for op in ["+", "-", "*", "/"]):

        try:
            result = eval(text)
            print("Bot:", result)

        except:
            print("Bot: Invalid calculation.")

    # ==========================
    # GK QUESTIONS
    # ==========================
    elif "capital of india" in text:
        print("Bot: New Delhi is the capital of India.")

    elif "capital of usa" in text:
        print("Bot: Washington D.C.")

    elif "largest planet" in text:
        print("Bot: Jupiter is the largest planet.")

    elif "what is ai" in text:
        print("Bot: AI means Artificial Intelligence.")

    elif "what is python" in text:
        print("Bot: Python is a popular programming language.")

    elif "who invented python" in text:
        print("Bot: Guido van Rossum invented Python.")

    # ==========================
    # RANDOM CHAT
    # ==========================
    elif "study" in text:
        print("Bot: Keep studying consistently. You'll do great! 📚")

    elif "game" in text:
        print("Bot: I like Tic-Tac-Toe and Chess! 🎮")

    elif "movie" in text:
        print("Bot: I enjoy hearing about movies! 🍿")

    elif "music" in text:
        print("Bot: Music can be very relaxing. 🎵")

    elif "nice move" in text:
        print("Bot: Thank you! 😎")

    elif "i will win" in text:
        print("Bot: Challenge accepted! 😁")

    elif "love you" in text:
        print("Bot: Thank you! I'm happy to chat with you. 😊")

    # ==========================
    # RANDOM RESPONSES
    # ==========================
    elif "tell me something" in text:

        facts = [
            "Honey never spoils. 🍯",
            "The Earth revolves around the Sun. 🌍",
            "Python was released in 1991. 🐍",
            "Octopuses have three hearts. ❤️",
            "Bananas are berries. 🍌"
        ]

        print("Bot:", random.choice(facts))

    # ==========================
    # DEFAULT
    # ==========================
    else:
        responses = [
            "Interesting! Tell me more.",
            "I'm still learning that.",
            "Can you explain differently?",
            "That's cool! 😄",
            "I understand a little bit."
        ]

        print("Bot:", random.choice(responses))