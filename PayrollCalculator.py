currency = '$'
space = " ";
EmployeeName = str(input('Employee’s name : '))
WorkedHours = float(input('Number of hours worked in a week : '))
HourlyPayRate = float(input('Hourly pay rate : '))

FederalTax = float(input('Federal tax withholding rate : '))
Federal = f"{float(FederalTax) * 1:.1%}"

StateTax = float(input('State tax withholding rate : '))
State = f"{float(StateTax) * 1:.1%}"

Gross = WorkedHours * HourlyPayRate
ResultFederal = Gross * FederalTax
ResultState = Gross * StateTax
Total = ResultState + ResultFederal
NetPay = Gross - Total

print('Employee Name: ' + EmployeeName)
print('Hours Worked: ', WorkedHours)
print('Pay Rate: ' + currency, HourlyPayRate)
print('Gross Pay: ', currency, round(Gross, 2))
print('Deductions: ')
print(space * 3 + 'Federal withholding (', Federal, '): ', currency, round(ResultFederal, 2))
print(space * 3 + 'State withholding (', State, '):', currency, round(ResultState, 2))
print(space * 3 + 'Total Deduction: ', currency, round(Total, 2))
print("Net Pay: ", currency, round(NetPay, 2))
