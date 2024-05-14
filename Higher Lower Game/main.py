import random
from game_data import data


def format_account(account):
    name = account["name"]
    profession = account["profession"]
    followers = account["follower"]
    return f"{name}, a {profession}"


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"

    else:
        return user_guess == "b"


def play_game():
    score = 0
    person_b = random.choice(data)
    game_on = True
    while game_on:
        person_a = person_b
        person_b = random.choice(data)
        while person_a == person_b:
            person_b = random.choice(data)
        print(f"Compare A: {format_account(person_a)}")

        print("VS")
        print(f"Against B: {format_account(person_b)}")

        guess = input("Who has more followers? A or B: ").lower()
        a_followers = person_a["follower"]
        b_followers = person_b["follower"]
        is_correct = check_answer(guess, a_followers, b_followers)

        if is_correct:
            score += 1
            print(f"That's correct! Current Score: {score}\n")

        else:
            game_on = False
            print("\nThat's wrong")
            print(f"{person_a["name"]} has {a_followers} million followers.")
            print(f"{person_b["name"]} has {b_followers} million followers.")
            print(f"Final Score: {score}")


play_game()




