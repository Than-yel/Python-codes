# Using Object Oriented Programming
# Multiple Choice Question Game

"""
Multiple Choice game using Object Oriented Programming in Python (For Educative Purposes)

This script defines a simple console-based multiple-choice quiz game.
It includes two main classes:
- Question: Represents a single multiple-choice question.
- Game: Manages a list of questions, interacts with the user, checks answers, and keeps score.

The game allows users to:
- View each question with its answer options.
- Input their chosen option (A/B/C/D).
- Receive feedback on whether their answer was correct or not.
- View their total score at the end of the game.
"""
# Define a class to represent a single multiple-choice question
class Question:
    def __init__(self, question, options, answer):
        # Initialize the question text, answer options (as a dictionary), and the correct answer
        self.question = question
        self.options = options
        self.answer = answer

    def display(self):
        # Display the question and its answer options
        print(self.question)
        for option, value in self.options.items():
            print(f"{option}: {value}")

    def check_answer(self, user_answer):
        # Check if the user's answer matches the correct answer (case-insensitive)
        return user_answer.upper() == self.answer


# Define a class to represent the quiz game
class Game:
    def __init__(self):
        # Initialize an empty list to store questions and set the initial score to 0
        self.questions = []
        self.score = 0

    def add_question(self, question):
        # Add a question object to the list of questions
        self.questions.append(question)

    def play(self):
        # Loop through each question and play the game
        for question in self.questions:
            question.display()  # Show the question and options to the user
            user_answer = input("Choose the correct option (A/B/C/D): ")  # Get user's answer

            if question.check_answer(user_answer):  # Check if the answer is correct
                print("Correct answer!")
                self.score += 1  # Increment score for correct answer
            else:
                # Show correct answer if user was wrong
                print(f"Incorrect answer. The correct answer is {question.answer}.")
        
        # Display final score after all questions have been answered
        print(f"\nGame over! Your final score is {self.score}/{len(self.questions)}.")


# Create multiple Question objects with their options and correct answers
question1 = Question(
    "What was the name of the hurricane that caused widespread destruction in Florida, USA in September 2022?",
    {"A": "Hurricane Ian", "B": "Hurricane Irma", "C": "Hurricane Katrina", "D": "Hurricane Harvey"},
    "A"
)

question2 = Question(
    "Which tech company launched the satellite-based internet service, Starlink, in Nigeria in 2022?",
    {"A": "SpaceX", "B": "Google", "C": "Amazon", "D": "Microsoft"},
    "A"
)

question3 = Question(
    "Who became the President of Nigeria in May 2023?",
    {"A": "Bola Tinubu", "B": "Atiku Abubakar", "C": "Peter Obi", "D": "Rabiu Kwankwaso"},
    "A"
)

question4 = Question(
    "Which team won the 2022 FIFA World Cup in Qatar?",
    {"A": "Argentina", "B": "Brazil", "C": "France", "D": "Germany"},
    "A"
)

question5 = Question(
    "What is the name of the African fintech company that acquired a majority stake in Mobile Money, a mobile financial services company, in 2022?",
    {"A": "Flutterwave", "B": "Paystack", "C": "Chipper Cash", "D": "Interswitch"},
    "A"
)


# Create a Game instance
game = Game()

# Add all the questions to the game
game.add_question(question1)
game.add_question(question2)
game.add_question(question3)
game.add_question(question4)
game.add_question(question5)

# Start the game
game.play()
