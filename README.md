Quiz Game
Este es un programa de preguntas y respuestas en Python que permite a los usuarios responder preguntas de un archivo CSV. El programa carga preguntas con una respuesta correcta y varias incorrectas, las muestra en orden aleatorio, permite al usuario elegir la respuesta y luego muestra un puntaje final al completar el cuestionario.

Estructura del Programa
El programa contiene la clase Quiz y se divide en las siguientes secciones principales:

1. Quiz
La clase Quiz gestiona el funcionamiento principal del programa, con métodos para cargar preguntas desde un archivo CSV, obtener la respuesta del usuario, y ejecutar el cuestionario.

2. Métodos principales
__init__(self, file_path: str)
Inicializa el cuestionario cargando preguntas desde un archivo CSV especificado.

load_questions(self, file_path: str) -> List[Dict[str, str]]
Carga las preguntas desde el archivo CSV, verifica que las columnas requeridas existan y organiza las respuestas en un orden aleatorio. Las preguntas se guardan en una lista de diccionarios con las claves "question", "options" (opciones mezcladas), y "correct_answer".

get_user_answer(self, num_options: int) -> int
Solicita al usuario que ingrese su respuesta y verifica que sea un número dentro del rango de opciones. Devuelve la selección como un índice.

run_quiz(self)
Ejecuta el cuestionario mostrando cada pregunta y opciones al usuario, evaluando si la respuesta es correcta e incrementando el puntaje en caso de acierto. Al final, muestra el puntaje total.

Estructura del Archivo CSV
El archivo CSV debe incluir las siguientes columnas:

question: Contiene la pregunta.
correct_answer: Contiene la respuesta correcta.
incorrect_answer_1, incorrect_answer_2, incorrect_answer_3: Contienen respuestas incorrectas.




Quiz Game
Este es un programa de preguntas y respuestas en Python que permite a los usuarios responder preguntas de un archivo CSV. El programa carga preguntas con una respuesta correcta y varias incorrectas, las muestra en orden aleatorio, permite al usuario elegir la respuesta y luego muestra un puntaje final al completar el cuestionario.

Estructura del Programa
El programa contiene la clase Quiz y se divide en las siguientes secciones principales:

1. Quiz
La clase Quiz gestiona el funcionamiento principal del programa, con métodos para cargar preguntas desde un archivo CSV, obtener la respuesta del usuario, y ejecutar el cuestionario.

2. Métodos principales
__init__(self, file_path: str)
Inicializa el cuestionario cargando preguntas desde un archivo CSV especificado.

load_questions(self, file_path: str) -> List[Dict[str, str]]
Carga las preguntas desde el archivo CSV, verifica que las columnas requeridas existan y organiza las respuestas en un orden aleatorio. Las preguntas se guardan en una lista de diccionarios con las claves "question", "options" (opciones mezcladas), y "correct_answer".

get_user_answer(self, num_options: int) -> int
Solicita al usuario que ingrese su respuesta y verifica que sea un número dentro del rango de opciones. Devuelve la selección como un índice.

run_quiz(self)
Ejecuta el cuestionario mostrando cada pregunta y opciones al usuario, evaluando si la respuesta es correcta e incrementando el puntaje en caso de acierto. Al final, muestra el puntaje total.


Estructura del Archivo CSV
El archivo CSV debe incluir las siguientes columnas:

question: Contiene la pregunta.
correct_answer: Contiene la respuesta correcta.
incorrect_answer_1, incorrect_answer_2, incorrect_answer_3: Contienen respuestas incorrectas.
Ejemplo de archivo CSV
csv


Ejecución del Programa
Asegúrate de tener un archivo questions.csv en la ruta especificada en questions_file.
Ejecuta el programa desde la terminal o un entorno de desarrollo ejecutando el archivo .py.
Sigue las instrucciones en pantalla para responder cada pregunta ingresando el número de la opción elegida.
Al finalizar el cuestionario, el programa muestra el puntaje total basado en el número de respuestas correctas.
