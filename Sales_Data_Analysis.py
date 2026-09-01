import numpy as np

# Define Months

Months=np.array(["January","February","March","April","May","June","July","August","September","October","November","December"])

# define Sales

Sales=np.array([20000,30000,15000,50000,60000,45000,90000,95000,77000,98000,54000,87000])

# print Months

print("--- Sales Months ---")
print(Months)

# Print Sales

print("--- Sales ---")
print(Sales)


# Stataics

print("Average Sales :" ,np.mean(Sales))
print("Maximum Sales :",np.max(Sales))
print("Minimum Sales :",np.min(Sales))
print("standard Deviation :",round(np.std(Sales),2))


# Highest Month Sales

Highest_Saleidx=np.argmax(Sales)
print("--- Highest Sales ---")

Highest_month=Months[Highest_Saleidx]

Highest_Sales=Sales[Highest_Saleidx]
print(f"{Highest_month} : {Highest_Sales}")

# Lowest Month Sales
Lowest_Saleidx=np.argmin(Sales)

print("--- Lowest Sales ---")
Lowest_month=Months[Lowest_Saleidx]

Lowest_Sales=Sales[Lowest_Saleidx]
print(f"{Lowest_month} : {Lowest_Sales} \n")

# Sales Above Average
Average=np.mean(Sales)
Above_average=Sales>Average
for sale,month in zip(Months[Above_average],Sales[Above_average]):
    print(f"{month} : {sale}")
    

# Monthly Report 
print("\n --- Monthly Report ---")

for month,sale in zip(Months,Sales):
    print(f"{month} : {sale}")

# Growth Analysis

Growth=np.diff(Sales)
for i in range(len(Growth)):

    if Growth[i]>0:
        print(f"{Months[i]} -> {Months[i+1]} : {Growth[i]}")
        print("Profit !")

    elif Growth[i]<0:
        print(f"{Months[i]} -> {Months[i+1]} : {Growth[i]}")
        print("Loss !")



