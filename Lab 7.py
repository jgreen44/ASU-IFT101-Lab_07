#   Filename:           Lab 7
#   Created by:         jasongreen
#   Date:               Thursday, February 14, 2019
#   Time of Creation:   11:21
#   ---

names = ["Kelly", "Jason", "Alice", "Debra", "Gordon"]
ID = [1, 2, 3, 4, 5]
pay_type = ["H", "S", "S", "H", "H"]
pay_rate = [12, 700, 720, 13, 12]
hours_worked = [32, 40, 40, 19, 23]
gross_pay = []

# with open("salary.txt", "w") as salary_file:
#     header = "{:^20}{:^20}{:^20}{:^20}{:^20}".format("Names", "ID", "Pay Type", "Pay Rate", "Hours Worked")
#     print(header, file=salary_file)
#     for i in range(len(names)):
#         records = "{:^20}{:^20}{:^20}{:^20}{:^20}".format(names[i], ID[i], pay_type[i], pay_rate[i], hours_worked[i])
#         print(records, file=salary_file)

for i in range(len(names)):
    if pay_type[i] == "H":
        gross_pay.append(pay_rate[i] * hours_worked[i])
    elif pay_type[i] == "S":
        gross_pay.append(pay_rate[i])

with open("salary.txt", "w") as salary_file:
    header = "{:^20}{:^20}{:^20}{:^20}{:^20}{:^20}".format("Names", "ID", "Pay Type",
                                                           "Pay Rate", "Hours Worked", "Gross Pay")
    print(header, file=salary_file)
    for i in range(len(names)):
        records = "{:^20}{:^20}{:^20}{:^20}{:^20}{:^20}".format(names[i], ID[i], pay_type[i],
                                                                pay_rate[i], hours_worked[i], gross_pay[i])
        print(records, file=salary_file)
