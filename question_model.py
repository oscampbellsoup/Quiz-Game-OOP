# Define Question class to transfer dictionary parameters to objects in a new list
class Question:
# Initialize question attributes using two parameters: question and answer
    def __init__(self, q_text, q_answer):
# Self statements to access the question and answer attributes
        self.text = q_text
        self.answer = q_answer


