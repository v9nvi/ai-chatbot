import random

print("AI Chatbot Ready!")
print("Type 'bye' to exit.\n")

greetings = ["hi", "hello", "hey"]
greeting_responses = ["Hello!", "Hi there!", "Hey!", "Nice to meet you!"]

how_are_you = ["how are you", "how r u"]
how_responses = ["I'm good!", "Doing great!", "I'm fine, thanks!"]

about_ai = ["what is ai", "tell me about ai"]
ai_responses = [
    "AI stands for Artificial Intelligence.",
    "Artificial Intelligence allows machines to learn and make decisions.",
    "AI is the future of technology!"
]

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye!")
        break

    elif user in greetings:
        print("Bot:", random.choice(greeting_responses))

    elif user in how_are_you:
        print("Bot:", random.choice(how_responses))

    elif user in about_ai:
        print("Bot:", random.choice(ai_responses))

    else:
        print("Bot: I don't understand yet, but I'm learning!")
