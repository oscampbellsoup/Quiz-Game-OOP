from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Define list of question objects to be used by Question and Quizbrain classes
question_bank = []
# For Loop through number of questions in question_data and add them to question_bank
for i in question_data:
# Define parameter for question (text)
    question_text = i["text"]
# Define parameter for answer
    question_answer = i["answer"]
# Define new question object using two defined parameters
    new_question = Question(question_text, question_answer)
# Add object to question bank list
    question_bank.append(new_question)
# Create instance of quiz giving QuizBrain question bank parameter to use
quiz = QuizBrain(question_bank)
# While Loop through entire list of questions from question bank
while quiz.still_has_questions():
    quiz.next_question()
# Final print statements
print("You have completed the quiz!")
print(f"Your final score is: {quiz.quiz_score}/{quiz.question_number}")
