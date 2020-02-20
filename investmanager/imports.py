import csv
from . import models

opfile  =  'C:/Users/Inoxevious Greats/market/investmanager/Loan.csv'
   

def get_data(csv_file):
    header  =  []
    lbfile  =  open(opfile, "rt")
    reader  =  csv.reader(lbfile)
    rownum  =  0
    for row in reader:
        if rownum  ==  0:
            header.append(row)
            rownum += 1
        else:
            the_row  =  models.loans(loan_amount=row[0], funded_amount=row[1], term=row[2], int_rate=row[3], installment=row[4],
                                grade=row[5], sub_grade=row[6], emp_title=[7], emp_length=row[8], home_owner=row[9],
                                annual_inc=row[10], verification_status=row[11], loan_status=row[12], purpose=row[13],
                                title=row[14], zip=row[15], state=row[16], dti=row[17], open_acc=row[18], revol_bal=row[19],
                                revolv_util=row[20], total_acct=row[21], application_type=row[22], total_cur_bal=row[23],
                                acc_open_past_24=row[24], avg_cur_bal=row[25], bc_open_to_buy=row[26], tot_hi_cred=row[27],
                                total_bal_ex_mort=row[28], total_bc_limit=row[29], total_il_high_cred=row[30])
            the_row.save()

