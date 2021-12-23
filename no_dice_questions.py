
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

questions = [
    "What is the biggest animal in the world?\na: Blue Whale\nb: Elephant\nb: Sperm Whale\nd: Hamster", 
    "What is the capital of Iceland?\na: Cardiff\nb: Reykjavík\nc: Reykjanesbær\nd: Garðabær"
]

equations = [
    "5 x 7 = ?\na: 35\nb: 45\nc: 37\nd: 22"
]

answers = [
    Question(questions[0], "a"),
    Question(questions[1], "b")
]

equations_answers = [
    Question(equations[0], "a")
]