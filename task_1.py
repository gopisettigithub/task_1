class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question_num):
        question = self.questions[question_num]['question']
        options = self.questions[question_num]['options']
        print(f"\nQuestion {question_num + 1}: {question}")
        for idx, option in enumerate(options):
            print(f"{idx + 1}. {option}")

    def check_answer(self, question_num, user_answer):
        correct_answer = self.questions[question_num]['answer']
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")

    def play_quiz(self):
        num_questions = len(self.questions)
        for i in range(num_questions):
            self.display_question(i)
            user_input = input("Enter your answer (1, 2, 3, etc.): ")
            self.check_answer(i, user_input)
        print(f"\nYour final score is: {self.score}/{num_questions}")


if __name__ == "__main__":
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin"],
            "answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5"],
            "answer": "4"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Shakespeare", "Hemingway", "Tolstoy"],
            "answer": "Shakespeare"
        }
    ]
    quiz = Quiz(questions)
    quiz.play_quiz()

