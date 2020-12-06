# This is a simple game called hangman.
# Written on: Dec 5, 2020

import random
from hangman_art import stages
from hangman_word_list import word_list
from replit import clear

print("Welcom to the game, Hangman!\n")

# Get a random word from word_list.
word_to_guess = random.choice(word_list)
game_on = True
# Player has limited attempts to get correct word.
lives = len(stages) - 1

# Display how many letters in a word that the player has to guess.
display = []
for i in word_to_guess:
  display += "_"
print(f"{' '.join(display)}")

# Plays until the game ends.
while game_on:
  guess = input("Please, guess a letter: ").lower()

  # This function is for clearing the output screen after each guess.
  clear()
  
  # Check if the letter has already been guessed.
  if guess in display:
    print("You have already guess this letter.")
  
  # Check if the guess is in the word_to-guess. If so, replace "_" by the letter at that position.
  for i in range(len(word_to_guess)):
    if word_to_guess[i] == guess:
      display[i] = word_to_guess[i]
  print(f"{' '.join(display)}\n")

  # If guess is incorrect, the player loses a live.
  if guess not in word_to_guess:
    print("Your guess is incorrect.")
    lives -= 1

    # Check if the player's lives have run out.
    if lives == 0:
      print("Game Over. You lose.\n")
      print("The word to guess is: ", word_to_guess)
      game_on = False

  # Check if there are empty spaces("_") left in the display. If not, player wins.
  if "_" not in display:
    game_on = False
    print("Congratz! You win.\n")
    print("The word to guess is: ", word_to_guess)
  print(stages[lives])
