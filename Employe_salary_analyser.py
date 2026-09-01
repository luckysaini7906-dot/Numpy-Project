# Comcepts Of Enmploye Salary Analyser 

# 1 : Average Salary
# 2 : Highest Salary
# 3 : Lowest Salary
# 4 : Salary Above Average
# 5 : Hr Department Employes
# 6 : Salary Increment (10%)
# 7 : Employe Ranking 
# 8 : Standard Deviation



# Start Coding Of employe Salary Analyser

import numpy as np

# Define Employes
Employes=np.array(["Rohit","Mohit","Sohan","Lucky","Sumit","Himanshu"])

# Define Departments
Departments=np.array(["HR","IT","IT","HR","Finance","IT"])


# Define Salary
Salary=np.array([45000,60000,66000,70000,39000,55000])


# Average Salary
print("\n--- Average Salary ---")
Average=np.mean(Salary)
print("Average Salary :", Average)


# Highest Salary

print("\n--- Highest Salary ---")
Highest_salary=np.argmax(Salary)
print(f"{Employes[Highest_salary]} : {Salary[Highest_salary]}")


# Lowest Salary

print("\n--- Lowest Salary ---")
Lowest_Salary=np.argmin(Salary)
print(f"{Employes[Lowest_Salary]} : {Salary[Lowest_Salary]}\n")



# Salary Above Average
print("\n--- Salary Above Average ---")
Above_avg=np.sort(Salary)[::-1]
Above_avg_data=Salary>Average
for emp,sal in zip(Employes[Above_avg_data],Salary[Above_avg_data]):
    print(f"{emp} : {sal}")

# Hr Department Employes

print("\n--- HR Department Employes ---")
Department_data=Departments=="HR"
for emp,sal,dep in zip(Employes[Department_data],Salary[Department_data],Departments[Department_data]):
    print(f"{emp} : {sal} : {dep}")


# Salary Increment (10%)
print("\n--- Salary Increment ---")
for emp,sal in zip(Employes,Salary):
    Increment_Salary=sal+((sal*10)/100)
    # for emp,sal in zip(Employes,Increment_Salary):
    print(f"{emp} : {Increment_Salary}")


# Employes Ranking
print("\n--- Employes Ranking ---")
for dep,emp,sal in zip(Departments,Employes,Salary):
    if dep=="HR":
        print(f"{emp} : {dep} : {sal} : Ranking - A")
    elif dep=="IT":
        print(f"{emp} : {dep} : {sal} : Ranking - B")
    else:
        print(f"{emp} : {dep} : {sal} : Ranking - C")

# Standard Deviation
print("\n--- Standarded Deviation ---")
Standard_dev=np.std(Salary)
print(round(Standard_dev,2))

print("\nThanks For Using Employes Salary Analysis System \n")
