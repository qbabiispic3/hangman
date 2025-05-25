import random

# List of words for the game
verbs = ["python", "algorithm"]
print(verbs)
words = ["python", "hangman", "challenge", "openai", "developer", "programming", "algorithm", "keyboard"]

# Function to choose a random word from the list
def get_random_word(words):
def get_random_word(words):
    return random.choice(words)
print(words)

# Function to display the current progress of the word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Main function to run 
def play_hangman():
    word = get_random_word(words)
    guessed_letters = set()
    attempts = 6

    print("Welcome to the Hangman Game!")
    print("Guess the word, one letter at a time.")

    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        print("Word:", display_word(word, guessed_letters))
        
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            if set(word) <= guessed_letters:
                print(f"\nCongratulations! You guessed the word: {word}")
                break
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    if attempts == 0:
        print(f"\nGame Over! The word was: {word}")

# Start the game
if __name__ == "__main__":
    play_hangman()
