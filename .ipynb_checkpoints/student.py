class Student():
    def __init__(self, first_name, last_name, score):
        self.first_name = first_name
        self.last_name = last_name
        self.score = score

    def display_student(self):
        return("Nom : {0} \nPrenom : {1} \nNote : {2} \n------".format(self.last_name, self.first_name, self.score))

    def change_student_score(self):
        new_score_choice = str(input('Voulez-vous changer la note de {0} ?(Y/N)'.format(self.first_name)))
        if(new_score_choice.lower() == 'y'):
            new_score = int(input("Quelle est la note de {0} ?".format(self.first_name)))
            self.score = new_score
            print('Changement de la note effectué.')