
import random

word_list = ["ardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
chosen_word = random.choice(word_list)
print(f"{chosen_word}")
blanks = []
for i in range(len(chosen_word)):
    blanks += "_"
print(f"Guess this Word: {blanks}")

lives = 6
end_game = False
while not end_game:
    guess = input("Guess a Letter\n").lower()
    j = 0;
    for i in chosen_word:
        if (guess == i):
            blanks[j] = guess;
        j = j + 1
    print(f"{blanks}")
    if (guess not in chosen_word):
        lives = lives - 1
        print(stages[lives])
    if lives == 0:
        end_game = True
        print("You Lose")
    if not "_" in blanks:
        end_game = True
        print("You win")
print("".join(blanks))



