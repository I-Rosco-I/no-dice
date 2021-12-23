import random
from no_dice_questions import answers, equations_answers

class Questions:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

def roll_dice(random_number):
    
    games = [
        "You get 1 point! Everyone else has to drink a shot!", 
        "Answer the following question. If you get this wrong, you take a shot!", 
        "You lose 1 point! Take a shot!",
        "Perform the following dare. Your friends decide if you pass!",
        "Answer the following equation. If you get this wrong, you take a shot!"
    ]

    if random_number == 1:
        return """
        ###########
        |         |
        |    *    |
        |         |  
        ########### """ + games[0]
        
    if random_number == 2:
        return """
        ###########
        |  *      |
        |         |
        |      *  |  
        ########### """ + games[1] + "\n" + random.choice(answers).question

    if random_number == 3:
        return """
        ###########
        |  *      |
        |    *    |
        |      *  |  
        ########### """ + games[2]

    if random_number == 4:
        return """
        ###########
        |  *   *  |
        |         |
        |  *   *  |  
        ########### """ + games[3]

    if random_number == 5:
        return """
        ###########
        |  *   *  |
        |    *    |
        |  *   *  |  
        ########### """ + games[4] + "\n" + random.choice(equations_answers).question

    if random_number == 6:
        return """
        ###########
        |  *   *  |
        |  *   *  |
        |  *   *  |  
        ###########
        Random game! """ + roll_dice(random.randint(1,5))
        

print(roll_dice(random.randint(1, 6)))
