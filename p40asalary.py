BASIC=8000
DA=BASIC*52/100
HRA=BASIC*10/100
MA=BASIC*10/100
ITC=BASIC*5/100
VA=BASIC*10/100
GROSSALARY=BASIC+DA+HRA+MA+ITC+VA
PF=GROSSALARY*12/100
NETSALARY=GROSSALARY-PF
print("The Gross Salary =>",GROSSALARY)
print("The Net Salary =>",NETSALARY)