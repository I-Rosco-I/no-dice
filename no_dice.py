import random
from no_dice_dares import dares
from no_dice_questions import answers, equations_answers

def player_turn():
    print("Are you ready to roll?")
    player_ready = input()

    if player_ready == "no":
        print("Then take a shot, and play anyway!")

    roll_dice(random.randint(1, 6))

def roll_dice(random_number):
    
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
        else:
            print("Wrong! Take a shot!")

    if random_number == 3:
        print("""
        ###########
        |  *      |
        |    *    |
        |      *  |  
        ########### """ + games[2])

    if random_number == 4:
        print("""
        ###########
        |  *   *  |
        |         |
        |  *   *  |  
        ########### """ + games[3] + "\n" + random.choice(dares))

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

        roll_dice(random.randint(1,5))
        

player_turn()
