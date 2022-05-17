class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        for i in self.question_list:
            current_question = self.question_list[self.question_number]
            user_answer = input(f"Q{self.question_number + 1}: {current_question.text} (True/False): ")
            self.question_number += 1
            self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        if self.still_has_questions():
            print(f"Your current score is {self.score} out of {self.question_number}\n")
        if not self.still_has_questions():
            print(f"\nYour final score is {self.score}")
