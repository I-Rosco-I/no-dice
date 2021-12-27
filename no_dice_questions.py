
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

questions = [
    "What is the biggest animal in the world?\n\n    a: Blue Whale\n    b: Elephant\n    b: Sperm Whale\n    d: Hamster",
    "What is the capital of Iceland?\n\n    a: Cardiff\n    b: Reykjavík\n    c: Reykjanesbær\n    d: Garðabær"
]

equations = [
    "5 x 7 = ?\n\n    a: 35\n    b: 45\n    c: 37\n    d: 22"
]

answers = [
    Question(questions[0], "a"),
    Question(questions[1], "b")
]

equations_answers = [
    Question(equations[0], "a")
]