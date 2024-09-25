import random
from hangman_words import word_list
from hangman_art import stages, logo
import os


def clears():
    print("\033[H\033[J", end="")


chosen_word = random.choice(word_list)
lives = 6
display = []

for letter in chosen_word:
    display+= "_"
  
guessed_letters = ""
play = True
#print(logo, f"\nPsst, the word is {chosen_word}")

while play:
  guess = input("Guess a letter: ").lower()
  clears()
  if guess in guessed_letters:
    print("You have already guessed this letter...")
    
  for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
      display[i] = guess  
      
  if guess not in chosen_word:
    lives -= 1
    print(f"Yikes, {guess} is not in the word...you lose a life :(\n", stages[lives])
    
  if lives == 0:
    play = False
    print("You lose.")

  if "_" not in display:
    print("You win!")
    play = False
    
  guessed_letters += guess
  
  
  print(f"{' '.join(display)}\n") #joining elements into string
  
print(f"The word was {chosen_word}")
