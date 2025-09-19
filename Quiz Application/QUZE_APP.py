# How to Run the Application
# Copy the code into a Python file, e.g., quiz_app.py.
# Run the file using Python 3: python quiz_app.py.
# Follow the prompts to answer the questions.
# Features of the Quiz Application
# Multiple Choice Questions: Users can select answers from multiple options.
# Score Tracking: The application keeps track of the user's score.
# Results Display: After completing the quiz, the user receives feedback based on their performance.
# Restart Functionality: Users can restart the quiz by running the application again


class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self.user_answer = None

    def check_answer(self, answer):
        self.user_answer = answer
        return answer == self.correct_answer


class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.score = 0
        self.initialize_questions()

    def initialize_questions(self):
        self.questions = [
            Question("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], "Paris"),
            Question("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], "Mars"),
            Question("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "Blue Whale"),
            Question("Who painted the Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"], "Leonardo da Vinci"),
            Question("What is the chemical symbol for gold?", ["Go", "Gd", "Au", "Ag"], "Au")
        ]

    def get_current_question(self):
        return self.questions[self.current_question_index]

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            return True
        return False

    def previous_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            return True
        return False

    def submit_answer(self, answer):
        current_question = self.get_current_question()
        if current_question.check_answer(answer):
            self.score += 1

    def is_last_question(self):
        return self.current_question_index == len(self.questions) - 1

    def get_results(self):
        return {
            "score": self.score,
            "total": len(self.questions),
            "percentage": (self.score / len(self.questions)) * 100
        }

    def restart(self):
        self.current_question_index = 0
        self.score = 0
        for question in self.questions:
            question.user_answer = None


class QuizUI:
    def __init__(self):
        self.quiz = Quiz()
        self.start_quiz()

    def start_quiz(self):
        while True:
            self.display_question()
            answer = input("Your answer: ")
            self.quiz.submit_answer(answer)

            if self.quiz.is_last_question():
                self.show_results()
                break
            else:
                next_question = input("Do you want to go to the next question? (y/n): ")
                if next_question.lower() != 'y':
                    break

    def display_question(self):
        question = self.quiz.get_current_question()
        print(f"\nQuestion {self.quiz.current_question_index + 1}: {question.text}")
        for idx, option in enumerate(question.options):
            print(f"{idx + 1}. {option}")

    def show_results(self):
        results = self.quiz.get_results()
        print("\nQuiz Completed! 🎉")
        print(f"You scored {results['score']} out of {results['total']} ({results['percentage']:.2f}%)")
        if results['percentage'] >= 80:
            print("Excellent! You are a quiz master! 🌟")
        elif results['percentage'] >= 60:
            print("Good job! You know your stuff! 👍")
        elif results['percentage'] >= 40:
            print("Not bad! Keep learning! 📚")
        else:
            print("Keep practicing! You can do better! 💪")


# Start the quiz application
if __name__ == "__main__":
    QuizUI()
