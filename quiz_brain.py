# Define QuizBrain class to store quiz attribtues (question number, transfer question bank object list to this class, and quiz score)
class QuizBrain:
# 
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.quiz_score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            guess = (input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")).lower()
            if guess == 'true':
                break
            elif guess == 'false':
                break
            else:
                print("Invalid input. Please type 'True' or 'False'.")
                continue
        self.check_answer(guess, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, guess, correct_answer):
        if guess == correct_answer.lower():
            self.quiz_score += 1
            print("You got it right!")
            print(f"The correct answer was: {correct_answer}.")
            print(f"Your current score is {self.quiz_score}/{self.question_number}.")
            print("\n" * 2)
        elif guess != correct_answer.lower():
            print("That's wrong")
            print(f"The correct answer was: {correct_answer}.")
            print(f"Your current score is {self.quiz_score}/{self.question_number}.")
            print("\n" * 2)
