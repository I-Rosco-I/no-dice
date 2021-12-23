
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

questions = [
    "What is the biggest animal in the world?\na: Blue Whale\nb: Elephant\nb: Sperm Whale\nd: Hamster", 
    "What is the capital of Iceland?\na: Cardiff\nb: Reykjavík\nc: Reykjanesbær\nd: Garðabær"
]

answers = [
    Question(questions[0], "a"),
    Question(questions[1], "b")
]

