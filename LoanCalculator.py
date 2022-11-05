def LoanCalculator():
    LoanAmount = float(input("Loan Amount:"))
    NumOfYears = float(input("Number of Years:"))
    AnnualRate = float(5.0)
    print("\nInterest Rate\t" + "Monthly Payment\t" + "\tTotal Payment")
    while AnnualRate <= 8.0:
        MonthlyRate = float(AnnualRate / 1200)
        MonthlyPayment = float(LoanAmount * MonthlyRate / (1 - 1 / pow(1 + MonthlyRate, NumOfYears * 12)))
        TotalPayment = format(MonthlyPayment * NumOfYears * 12, ".2f")

        print(format(AnnualRate, ".3f"), end="%\t\t\t")
        print(format(MonthlyPayment, ".2f"), end="\t\t\t\t")
        print(TotalPayment, end="\n")
        AnnualRate += 1.0 / 8


LoanCalculator()
