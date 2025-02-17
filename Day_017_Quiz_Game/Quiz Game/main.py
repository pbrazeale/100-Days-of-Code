from question_model import Question
from data2 import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    text = q["question"]
    answer = q["correct_answer"]
    question = Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
