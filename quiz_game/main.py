from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    question = Question(question_data[i]["question"],question_data[i]["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("\nyou completed the quiz")
print(f"Here is the final score {quiz.score}/{quiz.question_number}")