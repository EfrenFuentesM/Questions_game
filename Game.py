import os
import csv
import random
from typing import List, Dict

class Quiz:
    EXPECTED_COLUMNS = ["question", "correct_answer", "incorrect_answer_1", "incorrect_answer_2", "incorrect_answer_3"]

    def __init__(self, file_path: str):
        """Inicializa el quiz cargando las preguntas desde el archivo especificado."""
        self.questions = self.load_questions(file_path)

    def load_questions(self, file_path: str) -> List[Dict[str, str]]:
        """Carga preguntas desde un archivo CSV y devuelve una lista de preguntas con opciones mezcladas."""
        questions = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                if not set(self.EXPECTED_COLUMNS).issubset(reader.fieldnames):
                    raise ValueError("Error: Faltan columnas esperadas en el archivo CSV.")
                
                for row in reader:
                    options = [opt for opt in [row.get("correct_answer"), row.get("incorrect_answer_1"), 
                                               row.get("incorrect_answer_2"), row.get("incorrect_answer_3")] if opt]
                    random.shuffle(options)
                    questions.append({
                        "question": row.get("question", "Pregunta no disponible"),
                        "options": options,
                        "correct_answer": row.get("correct_answer", "")
                    })
        except FileNotFoundError:
            print("Error: Archivo no encontrado. Verifica la ruta del archivo.")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Error inesperado: {e}")
        return questions

    def get_user_answer(self, num_options: int) -> int:
        """Obtiene una respuesta válida del usuario y la devuelve como índice."""
        while True:
            try:
                answer = int(input("Introduce el número de tu respuesta: "))
                if 1 <= answer <= num_options:
                    return answer - 1
                else:
                    print("Por favor, introduce un número de opción válido.")
            except ValueError:
                print("Entrada inválida. Por favor, introduce un número.")

    def run_quiz(self):
        """Ejecuta el quiz, mostrando preguntas, opciones y calculando la puntuación final."""
        if not self.questions:
            print("No se cargaron preguntas. Saliendo del quiz.")
            return

        score = 0
        random.shuffle(self.questions)  # Opcional: barajar el orden de las preguntas
        total_questions = len(self.questions)

        for i, question in enumerate(self.questions):
            print(f"\nPregunta {i + 1}/{total_questions}: {question['question']}")
            for idx, option in enumerate(question["options"], start=1):
                print(f"{idx}. {option}")

            user_answer_idx = self.get_user_answer(len(question["options"]))
            if question["options"][user_answer_idx] == question["correct_answer"]:
                print("¡Correcto!")
                score += 1
            else:
                print(f"Incorrecto. La respuesta correcta era: {question['correct_answer']}")

        print(f"\n¡Quiz completado! Tu puntuación final es {score}/{total_questions}.")

# Definir la ruta al archivo de preguntas
questions_file = os.path.expanduser("~/Desktop/Questions_game/questions.csv")

# Ejecutar el programa
quiz = Quiz(questions_file)
quiz.run_quiz()
