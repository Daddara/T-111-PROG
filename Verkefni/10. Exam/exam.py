class Question():
    
    def __init__(self, question="", answer=""):
        self.question = question
        self.answer = answer
        
    def set_question(self):
        return str(self.question)
    
    def set_answer(self):
        return str(self.answer)
    
    def __str__(self):
        return '{} \n{}'.format(self.question, self.answer)

        
    def __repr__(self):
        pass
    
class ChoiceQuestion(Question):
    
    def __init__():
        pass
    
    
    def add_choice():
        pass
    
    def __repr__(self):
        pass
    
class Exam(Question):

    def __init__():
        pass
    
    def add_question():
        pass
    
    def add_choice_question():
        pass
    
    def present_exam():
        pass




# #def answer_question(a_question):
#     print(a_question)
#     response = input("Your answer: ")
#     print(a_question.check_answer(response))

# Main
q = Question()
q.set_question("Who is the inventor of Python?")
q.set_answer("Guido van Rossum")

#answer_question(q)
#print(repr(q))


# q = ChoiceQuestion()
# q.set_question("In what year was the Python language first released?")
# q.add_choice("1991", True)
# q.add_choice("1995", False)
# q.add_choice("1998", False)
# q.add_choice("2000", False)

# answer_question(q)
# print(repr(q))


# exam = Exam()
# exam.add_question("Who is the inventor of Python?", "Guido van Rossum")
# exam.add_question("What does OOP stand for?", "Object-oriented programming")

# question1_str = "In what year was the Python language first released?"
# choices1_list = [("1991", True), ("1995", False), ("1998", False), ("2000", False)]
# exam.add_choice_question(question1_str, choices1_list)

# question2_str = "Which of the following is a built-in type in Pyhon?"
# choices2_list = [("array", False), ("record", False), ("dict", True), ("bug", False)]
# exam.add_choice_question(question2_str, choices2_list)

# exam.present_exam()
# print("Your score is {} point(s) out of {} point(s)".format(exam.get_points(), exam.get_num_questions()))
