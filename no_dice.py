import random
from no_dice_dares import dares
from no_dice_questions import answers, equations_answers

def game_startup():
    print("""
        .-----------------. .----------------.   .----------------.  .----------------.  .----------------.  .-----------------.
        | .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. |
        | | ____  _____  | || |     ____     | | | |  ________    | || |     _____    | || |     ______   | || |  _________   | |
        | ||_   \|_   _| | || |   .'    `.   | | | | |_   ___ `.  | || |    |_   _|   | || |   .' ___  |  | || | |_   ___  |  | |
        | |  |   \ | |   | || |  /  .--.  \  | | | |   | |   `. \ | || |      | |     | || |  / .'   \_|  | || |   | |_  \_|  | |
        | |  | |\ \| |   | || |  | |    | |  | | | |   | |    | | | || |      | |     | || |  | |         | || |   |  _|  _   | |
        | | _| |_\   |_  | || |  \  `--'  /  | | | |  _| |___.' / | || |     _| |_    | || |  \ `.___.'\  | || |  _| |___/ |  | |
        | ||_____|\____| | || |   `.____.'   | | | | |________.'  | || |    |_____|   | || |   `._____.'  | || | |_________|  | |
        | |              | || |              | | | |              | || |              | || |              | || |              | |
        | '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' |
        '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '-----------------'

        Take turns to roll the dice and complete the challenges. First player to 10 points wins!
    """)

    number_of_players = input("How many people are playing? ")
    players = []

    for player in range(int(number_of_players)):
        players.append({"name": input("Enter player name: "), "score": 0})

    player_turn(players)

def player_turn(players):
    game_end = False

    for player in players:
        player_ready = input(player["name"] + " are you ready to roll? y or n: ")

        if player_ready == "n":
            print("Then take a shot, and play anyway!")

        if roll_dice(random.randint(1, 6), player):
            game_end = True
            break

    if game_end:
        print("WINNER! Everyone else finish your drinks!")
    else:
        player_turn(players)

def roll_dice(random_number, player):
    def update_score(add=True):
        if add:
            player["score"] += 1
        else:
            player["score"] -= 1

        print(player["name"] + ", your score is now ", player["score"])

    games = [
        "You get 1 point! Everyone else has to drink a shot!",
        "Answer the following question. If you get this wrong, you take a shot!",
        "You lose 1 point! Take a shot!",
        "Perform the following dare. Your friends decide if you pass!",
        "Answer the following equation. If you get this wrong, you take a shot!"
    ]

    if random_number == 1:
        print("""
        ###########
        |         |
        |    *    |
        |         |
        ########### """ + games[0])
        update_score()

    if random_number == 2:
        question_answer = random.choice(answers)
        print("""
        ###########
        |  *      |
        |         |
        |      *  |
        ########### """ + games[1] + "\n" + question_answer.question + "\nChoose an answer!")

        answer = input()

        if answer == question_answer.answer:
            print("Correct!")
            update_score()
        else:
            print("Wrong! Take a shot!")

    if random_number == 3:
        print("""
        ###########
        |  *      |
        |    *    |
        |      *  |
        ########### """ + games[2])
        update_score(False)

    if random_number == 4:
        print("""
        ###########
        |  *   *  |
        |         |
        |  *   *  |
        ########### """ + games[3] + "\n" + random.choice(dares))

        if input("Did " + player["name"] + " complete the dare? y or n: ") == "y":
            update_score()

    if random_number == 5:
        question_answer = random.choice(equations_answers)
        print("""
        ###########
        |  *   *  |
        |    *    |
        |  *   *  |
        ########### """ + games[4] + "\n" + question_answer.question + "\nChoose an answer!")

        answer = input()

        if answer == question_answer.answer:
            print("Correct!")
            update_score()
        else:
            print("Wrong! Take a shot!")

    if random_number == 6:
        print("""
        ###########
        |  *   *  |
        |  *   *  |
        |  *   *  |
        ###########
        Random game! """)

        roll_dice(random.randint(1,5), player)

    return player["score"] == 2

game_startup()