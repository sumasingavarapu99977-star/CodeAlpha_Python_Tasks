import random

words = ["python", "computer", "programming", "hangman", "keyboard"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("=== Welcome to Hangman Game ===")

while wrong_guesses < max_guesses:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")
        print("Remaining chances:", max_guesses - wrong_guesses)

else:
    print("\n❌ Game Over!")
    print("The word was:", word)