from . import models as mod

# co-relation betwn loan amount vs credit grade

class GradeVs:
    def __init__(self, a, b, c, d, e):
        self.grade_a = a
        self.grade_b = b
        self.grade_c = c
        self.grade_d = d
        self.grade_e = e


def avg_helper(my_list):
    return sum(my_list)/len(my_list)

def percent_remover(percent):
    interest = percent.split('%')
    return float(interest[0])

def grade_avg(data):

    loan_a, loan_b, loan_c, loan_d, loan_e = [], [], [], [], []
    interest_a, interest_b, interest_c, interest_d, interest_e = [], [], [], [], []
    vs = []
    for row in data:
        # list of loan amount and anuual income
        vs.append((row.loan_amount, row.annual_inc))
        if row.grade == 'A':
            loan_a.append(row.loan_amount)
            interest_a.append(percent_remover(row.int_rate))

        elif row.grade == 'B':
            loan_b.append(row.loan_amount)
            interest_b.append(percent_remover(row.int_rate))

        elif row.grade == 'C':
            loan_c.append(row.loan_amount)
            interest_c.append(percent_remover(row.int_rate))

        elif row.grade == 'D':
            loan_d.append(row.loan_amount)
            interest_d.append(percent_remover(row.int_rate))

        elif row.grade == 'E':
            loan_e.append(row.loan_amount)
            interest_e.append(percent_remover(row.int_rate))

    la_data = GradeVs((avg_helper(loan_a), len(loan_a)), (avg_helper(loan_b), len(loan_b)), (avg_helper(loan_c), len(loan_c)),
                     (avg_helper(loan_d), len(loan_d)), (avg_helper(loan_e), len(loan_e)))
    int_data = GradeVs((avg_helper(interest_a), len(interest_a)),(avg_helper(interest_b), len(interest_b)), 
                       (avg_helper(interest_c), len(interest_c)), (avg_helper(interest_d), len(interest_d)), 
                       (avg_helper(interest_e), len(interest_e)))
    
    return la_data, int_data, vs