class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def take_quiz(self):
        for question in self.questions:
            answer = input(question.prompt)
            if answer.lower() == question.answer.lower():
                self.score += 1
        print(f"You scored {self.score}/{len(self.questions)}")


# Example usage
quiz = Quiz()
quiz.add_question(Question("What is the capital of France? ", "Paris"))
quiz.add_question(Question("What is 2 + 2? ", "4"))

quiz.take_quiz()
