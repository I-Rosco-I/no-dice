import random
from no_dice_dares import dares
from no_dice_questions import answers, equations_answers

total_points = 10

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

        Take turns to roll the dice and complete the challenges. First player to {} points wins!
    """.format(total_points))

    number_of_players = input("How many people are playing? ")
    players = []

    for player in range(int(number_of_players)):
        players.append({"name": input("Enter player name: "), "score": 0})

    player_turn(players)

def player_turn(players):
    game_end = False

    for player in players:
        player_ready = input("\n" + player["name"] + " are you ready to roll? y or n: ")

        if player_ready == "n":
            print("Then take a shot, and play anyway!")

        if roll_dice(random.randint(1, 6), player, players):
            game_end = True
            break

    if game_end:
        print("WINNER! Everyone else finish your drinks!")
    else:
        player_turn(players)

def roll_dice(random_number, player, players):
    def update_score(add=True):
        if add:
            player["score"] += 1
        else:
            player["score"] -= 1

        print("\033[1;32m" + player["name"] + ", your score is now:", player["score"], "\n\x1b[0m")

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
        ###########

    {}

        """.format(games[0]))
        update_score()

    if random_number == 2:
        question_answer = random.choice(answers)
        print("""
        ###########
        |  *      |
        |         |
        |      *  |
        ###########

    {}

    {}
        """.format(games[1], question_answer.question))

        answer = input("Choose an answer! ")

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
        ###########

    {}

        """.format(games[2]))
        update_score(False)

    if random_number == 4:
        print("""
        ###########
        |  *   *  |
        |         |
        |  *   *  |
        ###########

    {}

    {}
        """.format(games[3], random.choice(dares)))

        if input("Did " + player["name"] + " complete the dare? y or n: ") == "y":
            update_score()

    if random_number == 5:
        question_answer = random.choice(equations_answers)
        print("""
        ###########
        |  *   *  |
        |    *    |
        |  *   *  |
        ###########

    {}

    {}
        """.format(games[4], question_answer.question))

        answer = input("Choose an answer! ")

        if answer == question_answer.answer:
            print("Correct!")
            update_score()
        else:
            print("Wrong! Take a shot!")

    if random_number == 6:
        random_player = random.choice(players)
        print("""
        ###########
        |  *   *  |
        |  *   *  |
        |  *   *  |
        ###########

        Random game! The player chosen for this game is {}.""".format(random_player["name"]))

        roll_dice(random.randint(1,5), random_player, players)

    return player["score"] == total_points

game_startup()