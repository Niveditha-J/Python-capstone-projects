import random
import hangman_word_list
chosen_word = random.choice(hangman_word_list.word_list)

from Hangman_art import logo,stages
print(logo)
print(f"The solution is {chosen_word}")
lives=6
display=[]
word_length=len(chosen_word)

for _ in range(word_length):
    display+="_"
end_of_game=False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You have already guessed it correct!")
    for position in range(word_length):
        letter=chosen_word[position]
        if letter == guess:
            display[position]=letter
    print(display) 

    if guess not in chosen_word:
        print(f"You guessed letter {guess} is not in the word.You lose a life!")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose!") 

    if "_" not in display:
        end_of_game=True
        print("You win!")
    print(stages[lives])
