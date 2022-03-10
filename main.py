import random


from word_list import word_list
from logo import stages
from logo import logo

words = word_list
chosen_word = random.choice(words)
word_length = len(chosen_word)
print(f"the choosen word is {chosen_word}")

lives = 6
print(logo)
display = []
for _ in range(word_length):
    display += "_"
end_game = False

while not end_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"word {guess} is already entered") 
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
            
    if guess not in chosen_word:
        print(f"{guess} is not in the word. You loose a life")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose")
    
               
    print(f"{' '.join(display)}")       
    if "_" not in display:
        end_game = True
        print("You win")
    
    print(stages[lives])