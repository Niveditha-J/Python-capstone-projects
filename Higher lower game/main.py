#display art
from art import logo,vs
from game_data import data
import random

def format_data(account):
    #format the account data into printable format
    account_name=account["name"]
    account_desc=account["description"]
    account_coun=account["country"]
    return f"{account_name},a {account_desc}, from{account_coun}"
#check if user is correct
def check_answer(user_guess,a_followers,b_followers):
    """Take a user's guess and the follower counts and return if they got it right."""
    #A>B  ->guess A  and B>A   ->guess B
    if a_followers>b_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"
print(logo)
score=0


#Make the game repeatable.
game_shd_cont=True

account_b=random.choice(data)

while game_shd_cont:
    #generate a random account from the game data
    #Making account at position B become the next account at Position A
    account_a=account_b
    account_b=random.choice(data)
    
    if account_a==account_b: #if both are equal then regenerate
        account_b=random.choice(data)

    print(f"Compare A:{format_data(account_a)}.")
    print(vs)
    print(f"Against B:{format_data(account_b)}.")


    #ask user for a guess
    #Get follower count of each acc
    guess=input("Who has more followers?Type 'A' or 'B': ").lower()
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]


    ##use if stt to check if user is correct
    is_correct=check_answer(guess,a_follower_count,b_follower_count)


    #give user feedback on their guess.
    #score keeping
    if is_correct:
        score+=1
        print(f"You're right!Current score:{score}")
    else:
        print(f"Sorry,that's wrong.Final score:{score}") 
        game_shd_cont=False






