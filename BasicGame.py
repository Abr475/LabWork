import random
MyName = input("Please Enter Your Name : ")
Age = input("Please Enter Your Age : ")
def hangman():
    words = ["tyrant", "hangman", "nightmare", "mountain", "travel"]

    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 8
    
    numberOfLetter = ["_"] * len(word)
    
    while wrong_guesses < max_wrong_guesses and "_" in numberOfLetter:
        print(" ".join(numberOfLetter))
        guess = input("Guess a letter: ").lower()

        if guess == guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            # Update the current state of the word
            for i in range(len(word)):
                if word[i] == guess:
                    numberOfLetter[i] = guess
        else:
            # Increment the number of incorrect guesses
            wrong_guesses += 1
            print("Incorrect! You have", {max_wrong_guesses - incorrect_guesses},"guesses left")
    
    # Check if the user won or lost
    if "_" not in numberOfLetter:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Sorry, you ran out of guesses. The word was:", word)

hangman()
