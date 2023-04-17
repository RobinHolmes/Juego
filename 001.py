import random

# Define a list of words to choose from
word_list = ["apple", "banana", "cherry", "dragonfruit", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Choose a random word from the list
word = random.choice(word_list)

# Define the number of guesses allowed
max_guesses = 6

# Initialize the guessed word with underscores
guessed_word = ["_" for i in range(len(word))]

# Define a list to keep track of the guessed letters
guessed_letters = []

# Define a function to print the current status of the game
def print_status():
    print(" ".join(guessed_word))
    print("Guessed letters:", " ".join(guessed_letters))

# Start the game
print("Welcome to Wordle!")
print("Guess the word in", max_guesses, "tries or less.")
print_status()

# Loop through the guesses
for guess_count in range(max_guesses):
    guess = input("Enter your guess: ")
    
    # Check if the guess is a letter and if it has already been guessed
    if guess.isalpha() and guess not in guessed_letters:
        guessed_letters.append(guess)
        
        # Check if the guess is in the word
        if guess in word:
            print("Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print_status()
            
            # Check if the word has been completely guessed
            if "_" not in guessed_word:
                print("Congratulations, you guessed the word!")
                break
                
        # If the guess is not in the word, print a message and update the status
        else:
            print("Sorry, that letter is not in the word.")
            print_status()
            
    # If the guess is not a valid letter or has already been guessed, print a message and update the status
    else:
        print("Invalid guess or letter already guessed.")
        print_status()

# If the player has used all their guesses and not guessed the word, print a message with the correct word
else:
    print("Sorry, you ran out of guesses. The word was", word)
