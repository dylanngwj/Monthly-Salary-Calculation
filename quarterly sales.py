monthlypay = float(input("Enter your monthly pay here: "))
salesAmount = float(input("Enter your total sales amount for the quarter: "))

Sales_Threshold_1 = monthlypay * 3.15 *3
Commission_Rate_1 = 5/100
Sales_Threshold_2 = Sales_Threshold_1 + 90000 
Commission_Rate_2 = 10/100
Sales_Threshold_3 = Sales_Threshold_2 + 90000
Commission_Rate_3 = 20/100
Commission_Rate_4 = 30/100
#no Sales_Threshold_4 

commissionEarned = 0
deduction = 0 #penalty if sales target is not met
check = True

if salesAmount < Sales_Threshold_1:
    deduction -= 20/100 * monthlypay

if salesAmount >= Sales_Threshold_1:
    commissionEarned += (Sales_Threshold_1 * Commission_Rate_1) # hitting 3.15X (5%)
    
if salesAmount >= Sales_Threshold_1 and salesAmount < Sales_Threshold_2: # <90,000 (10%)
    commissionEarned += ((salesAmount - Sales_Threshold_1) * Commission_Rate_2)
    
if salesAmount > Sales_Threshold_2: # to cover the 10% * 90,000
    commissionEarned += (Sales_Threshold_2 - Sales_Threshold_1) * Commission_Rate_2

if salesAmount >= Sales_Threshold_2 and salesAmount < Sales_Threshold_3: # between 90,000 and 180,000 (20%)
    commissionEarned += ((salesAmount - Sales_Threshold_2) * Commission_Rate_3)

if salesAmount > Sales_Threshold_3: # to cover the 20% * 90,000
    commissionEarned += (Sales_Threshold_3 - Sales_Threshold_2) * Commission_Rate_3

if salesAmount > Sales_Threshold_3: # >180,000 (30%)
    commissionEarned += ((salesAmount - Sales_Threshold_3) * Commission_Rate_4)

monthlyp = (monthlypay*3 + commissionEarned + deduction*3) / 3

if commissionEarned == 0:
    check = False 

print('Met sales target?', check)
print('Your commission earned is: HKD', commissionEarned)
print ('Your monthly salary is: HKD', monthlyp)

