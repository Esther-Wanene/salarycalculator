basic_pay = float(input("Please enter basic pay: "))
benefits = float(input("Please enter housing allowance: "))
insurance = float(input("Amount of insurance premiums paid by the company: "))

# Insurance relief is equivalent to 15%
# taxable pay is equal to (basic pay + allowance) - (15% of insurance premiums)
gross_pay = basic_pay + benefits
print("Gross pay", gross_pay)
taxable_pay = (basic_pay + benefits) - (.15 * insurance)

# tax relief
tax_relief = 1408

# calculate PAYE
def payee(money):
    # defined fixed tax for each level
    tax_for_level_1 = 12298 * 0.1
    tax_for_level_2 = 11587 * 0.15
    tax_for_level_3 = 11587 * 0.20
    tax_for_level_4 = 11587 * 0.25

    # define amount to deduct after each level
    deduct_for_level_1 = 12298
    deduct_for_level_2 = 12298 + 11587
    deduct_for_level_3 = 12298 + 11587 + 11587
    deduct_for_level_4 = 12298 + 11587 + 11587 + 11587
    # calculate tax for level 1 Up to 12,298
    if money <= 12298:
        tax1 = money * 0.1
        return tax1
    # Calculate tax for level 2 (12,299 - 23,885)
    elif money >= 12299 and money<= 28335:
        bal = money - deduct_for_level_1
        tax2 = tax_for_level_1 + (bal * 0.15)
        return tax2
    # calculate tax for level 3 (23,886 - 35,472)
    elif money >=23886 and money <=35472:
        bal2 = money - deduct_for_level_2
        tax3 = tax_for_level_1 + tax_for_level_2 + (bal2 * 0.20)
        return tax3
    # calculate tax for level 4 (35,473 - 47,059)
    elif money >= 35473 and money <= 47059:
        bal3 = money - deduct_for_level_3
        tax4 = tax_for_level_1 + tax_for_level_2 + tax_for_level_3 + (bal3 * 0.25)
        return tax4
    # calculate tax for level 5 (Above 47,059)
    else:
        bal4 = money - deduct_for_level_4
        tax5 = tax_for_level_1 + tax_for_level_2 + tax_for_level_3 + tax_for_level_4 + (bal4 * 0.3)
        return tax5

# calculate amount to be deducted for NHIF
def nhif_deductions(deduct_from):
    if deduct_from <= 5999:
        return 150
    elif deduct_from >= 6000 and deduct_from <= 7999:
        return 300
    elif deduct_from >=8000 and deduct_from <=11999:
        return 400
    elif deduct_from >=12000 and deduct_from <=14999:
        return 500
    elif deduct_from >= 15000 and deduct_from <= 19999:
        return 600
    elif deduct_from >= 20000 and deduct_from <= 24999:
        return 750
    elif deduct_from >= 25000 and deduct_from <= 29999:
        return 850
    elif deduct_from >= 30000 and deduct_from <= 34999:
        return 900
    elif deduct_from >= 35000 and deduct_from <= 39999:
        return 950
    elif deduct_from >= 40000 and deduct_from <= 44999:
        return 1000
    elif deduct_from >= 45000 and deduct_from <= 49999:
        return 1100
    elif deduct_from >= 50000 and deduct_from <= 59999:
        return 1200
    elif deduct_from >= 60000 and deduct_from <= 69999:
        return 1300
    elif deduct_from >= 70000 and deduct_from <= 79999:
        return 1400
    elif deduct_from >= 80000 and deduct_from <= 89999:
        return 1500
    elif deduct_from >= 90000 and deduct_from <= 99999:
        return 1600
    elif deduct_from > 100000:
        return 1700
    else:
        return "please enter a correct value"


# calculate amount to be deducted for NSSF
# I did not get a predefined formulae on how to calculate NSSF rate.
# I just used 360 because that is what I got from most people.
nssf = 360

# let's calculate the total deductions
total_deductions = (payee(taxable_pay)-tax_relief) + nhif_deductions(taxable_pay) + nssf


print("Total Deductions", total_deductions)
print("Taxable pay", taxable_pay)
# to get payee subtract a tax relief of 1408
print("PAYEE: ", payee(taxable_pay) - tax_relief)
print("NHIF DEDUCTIONS: ", nhif_deductions(taxable_pay))
print("NSSF DEDUCTIONS: ", nssf)
# Net taxable income= Gross taxable income - Deductions
print("Net Pay", gross_pay - total_deductions)


