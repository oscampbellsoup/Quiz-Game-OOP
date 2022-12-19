# Define QuizBrain class to store quiz attribtues (question number, transfer question bank object list to this class, and quiz score)
class QuizBrain:
# Initialize QuizBrain attributes
# __init__ function holds new parameter as a differently named variable
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.quiz_score = 0
# Define next question method
    def next_question(self):
# Define current question object using transferred list attribute and question number
        current_question = self.question_list[self.question_number]
# Add 1 to question number when question is asked
        self.question_number += 1
# while True Loop through inputs until valid guess is inputted
        while True:
            guess = (input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")).lower()
            if guess == 'true':
                break
            elif guess == 'false':
                break
            else:
                print("Invalid input. Please type 'True' or 'False'.")
                continue
# Self statement to pass guess and current_question.answer parameters through check answer method
# Call object that uses transferred question list and call answer attribute when defining second parameter
        self.check_answer(guess, current_question.answer)
# Define still has questions method
    def still_has_questions(self):
# Return boolean value to determine if more questions need to be asked
        return self.question_number < len(self.question_list)
# Define check answer method
# __init__ function holds guess parameter and new parameter as a differently named variable
    def check_answer(self, guess, correct_answer):
# Compare guess and correct answer
        if guess == correct_answer.lower():
# Add 1 to quiz score for correct guess
            self.quiz_score += 1
            print("You got it right!")
# Call parameter to be used in print statement        
            print(f"The correct answer was: {correct_answer}.")
# Call quiz score and number attributes to be used in print statement
            print(f"Your current score is {self.quiz_score}/{self.question_number}.")
            print("\n" * 2)
        elif guess != correct_answer.lower():
            print("That's wrong")
            print(f"The correct answer was: {correct_answer}.")
            print(f"Your current score is {self.quiz_score}/{self.question_number}.")
            print("\n" * 2)
