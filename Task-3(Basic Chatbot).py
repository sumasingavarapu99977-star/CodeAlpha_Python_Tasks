
def chatbot():

    print("================================")
    print("      WELCOME TO CHATBOT")
    print("================================\n")

    while True:

        user_input = input("You: ").lower()

        # Greetings
        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "hi":
            print("Bot: Hello!")

        elif user_input == "good morning":
            print("Bot: Good Morning!")

        elif user_input == "good night":
            print("Bot: Good Night!")

        # Questions
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Bot: I am a Python chatbot.")

        elif user_input == "who created you":
            print("Bot: I was created using Python.")

        elif user_input == "what can you do":
            print("Bot: I can reply to simple messages.")

        # Thank you
        elif user_input == "thank you":
            print("Bot: You're welcome!")

        elif user_input == "thanks":
            print("Bot: Happy to help!")

        # Exit
        elif user_input == "bye":
            print("Bot: Goodbye!")
            print("Bot: Have a nice day!")
            break

        # Unknown input
        else:
            print("Bot: Sorry, I don't understand.")

# Start chatbot
chatbot()

 