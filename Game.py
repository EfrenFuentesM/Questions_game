import os
import csv
import random

class Quiz:
    def __init__(self, file_path):
        self.questions = self.load_questions(file_path)

    # Function to load questions from a CSV file
    def load_questions(self, file):
        questions = []
        try:
            with open(file, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    options = [row["correct_answer"], row["incorrect_answer_1"], row["incorrect_answer_2"], row["incorrect_answer_3"]]
                    random.shuffle(options)  # Randomize the order of options
                    questions.append({
                        "question": row["question"],
                        "options": options,
                        "correct_answer": row["correct_answer"]
                    })
        except FileNotFoundError:
            print("Error: File not found. Please check the file path.")
        except KeyError:
            print("Error: Missing expected columns in CSV file.")
        return questions

    # Function to execute the quiz
    def run_quiz(self):
        if not self.questions:
            print("No questions loaded. Exiting quiz.")
            return
        
        score = 0
        total_questions = len(self.questions)

        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i + 1}/{total_questions}: {question['question']}")
            for idx, option in enumerate(question["options"], start=1):
                print(f"{idx}. {option}")
            
            # Get user input with validation
            while True:
                try:
                    answer = int(input("Enter the number of your answer: "))
                    if 1 <= answer <= len(question["options"]):
                        break
                    else:
                        print("Please enter a valid option number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            if question["options"][answer - 1] == question["correct_answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was: {question['correct_answer']}")

        print(f"\nQuiz completed! Your final score is {score}/{total_questions}.")

# Define the path to the questions file
questions_file = os.path.expanduser("~/Desktop/questions.csv")

# Run the program
quiz = Quiz(questions_file)
quiz.run_quiz()
