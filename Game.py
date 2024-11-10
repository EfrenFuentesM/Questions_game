import os
import csv
import random
from typing import List, Dict

class Quiz:
    EXPECTED_COLUMNS = ["question", "correct_answer", "incorrect_answer_1", "incorrect_answer_2", "incorrect_answer_3"]

    def __init__(self, file_path: str):
        """Initializes the quiz by loading questions from the specified file."""
        self.questions = self.load_questions(file_path)

    def load_questions(self, file_path: str) -> List[Dict[str, str]]:
        """Loads questions from a CSV file and returns a list of questions with shuffled options."""
        questions = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                if not set(self.EXPECTED_COLUMNS).issubset(reader.fieldnames):
                    raise ValueError("Error: Missing expected columns in the CSV file.")
                
                for row in reader:
                    options = [opt for opt in [row.get("correct_answer"), row.get("incorrect_answer_1"), 
                                               row.get("incorrect_answer_2"), row.get("incorrect_answer_3")] if opt]
                    random.shuffle(options)
                    questions.append({
                        "question": row.get("question", "Question not available"),
                        "options": options,
                        "correct_answer": row.get("correct_answer", "")
                    })
        except FileNotFoundError:
            print("Error: File not found. Please check the file path.")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Unexpected error: {e}")
        return questions

    def get_user_answer(self, num_options: int) -> int:
        """Gets a valid answer from the user and returns it as an index."""
        while True:
            try:
                answer = int(input("Enter the number of your answer: "))
                if 1 <= answer <= num_options:
                    return answer - 1
                else:
                    print("Please enter a valid option number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def run_quiz(self):
        """Runs the quiz, displaying questions, options, and calculating the final score."""
        if not self.questions:
            print("No questions loaded. Exiting quiz.")
            return

        score = 0
        random.shuffle(self.questions)  # Optional: shuffle the order of questions
        total_questions = len(self.questions)

        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i + 1}/{total_questions}: {question['question']}")
            for idx, option in enumerate(question["options"], start=1):
                print(f"{idx}. {option}")

            user_answer_idx = self.get_user_answer(len(question["options"]))
            if question["options"][user_answer_idx] == question["correct_answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was: {question['correct_answer']}")

        print(f"\nQuiz completed! Your final score is {score}/{total_questions}.")

# Define the path to the questions file
questions_file = os.path.expanduser("~/Desktop/Questions_game/questions.csv")

# Run the program
quiz = Quiz(questions_file)
quiz.run_quiz()
