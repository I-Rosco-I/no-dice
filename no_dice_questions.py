
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

questions = [
    "What is the biggest animal in the world?\n\n    a: Blue Whale\n    b: Elephant\n    b: Sperm Whale\n    d: Hamster",
    "What is the capital of Iceland?\n\n    a: Cardiff\n    b: Reykjavík\n    c: Reykjanesbær\n    d: Garðabær",
    "What year did World War II start?\n\n    a: 1945\n    b: 1939\n    c: 1940\n    d: 1934",
    "What element is denoted by the chemical symbol Sn in the periodic table?\n\n    a: Iron\n    b: Strontium\n    c: Tin\n    d: Silicon",
    "What was the Turkish city of Istanbul called before 1930?\n\n    a: Antioch\n    b: Cairo\n    c: Edessa\n    d: Constantinople",
    "What is the currency of Denmark?\n\n    a: Krone\n    b: Euro\n    c: Dollar\n    d: Franc",
    "What is the smallest planet in our solar system?\n\n    a: Mars\n    b: Neptune\n    c: Pluto\n    d: Mercury",
    "What does a Geiger Counter measure?\n\n    a: Vibration\n    b: Radiation\n    c: Velocity\n    d: Sound",
    "What is dermatophobia the fear of?\n\n    a: Skin conditions\n    b: Dermot O'leary\n    c: Mushrooms\n    d: Loud noises",
    "If you dug a hole through the centre of the earth starting from Wellington in New Zealand, which European country would you end up in?\n\n    a: France\n    b: Spain\n    c: Denmark\n    d: Italy",
    "It's illegal in Texas to put what on your neighbour's Cow?\n\n    a: A hat\n    b: A sadle\n    c: Grafitti\n    d: People"
]

equations = [
    "5 x 7 = ?\n\n    a: 35\n    b: 45\n    c: 37\n    d: 22",
    "5 - 3 x 10 = ?\n\n    a: 50\n    b: -25\n    c: 20\n    d: 25",
    "1000 - 10 x 10 = ?\n\n    a: 900\n    b: 9900\n    c: 0\n    d: 10",
    "1 + 2 + 3 + 4 + 5 = ?\n\n    a: 12\n    b: 16\n    c: 15\n    d: 20",
    "1000 x 1000 = ?\n\n    a: 10,000\n    b: 100,000\n    c: 1,000,000\n    d: 10,000,000",
    "5 - 4 - 3 - 2 - 1 = ?\n\n    a: -5\n    b: -10\n    c: -7\n    d: -6"
]

answers = [
    Question(questions[0], "a"),
    Question(questions[1], "b"),
    Question(questions[2], "b"),
    Question(questions[3], "c"),
    Question(questions[4], "d"),
    Question(questions[5], "a"),
    Question(questions[6], "d"),
    Question(questions[7], "b"),
    Question(questions[8], "a"),
    Question(questions[9], "b"),
    Question(questions[10], "c")
]

equations_answers = [
    Question(equations[0], "a"),
    Question(equations[1], "b"),
    Question(equations[2], "a"),
    Question(equations[3], "c"),
    Question(equations[4], "c"),
    Question(equations[5], "a")
]