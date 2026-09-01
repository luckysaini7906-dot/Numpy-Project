import numpy as np


# Creating Student Name Array
Students=np.array(["Lucky","Satyam","Rahul","Vivek","Vansh"])


# Total Classes & Attended Classes

Total_class=int(input("Enter Total Class :"))
Attandence=np.array([
    int(input(f"Class Attended By : {Student} :"))
    for Student in Students
])


# Precentage
Percentage=(Attandence*100)/Total_class

print("===== Attandance Report =====")

for s,a,p in zip(Students,Attandence,Percentage):
    print(f"{s} : {a}/{Total_class} : {p:.2f}%")



# Average Attandance

Average=np.mean(Attandence)
print("====== Average Attandance ======")
print(round(Average,2))

# Highest Attandance

Highest=np.argmax(Percentage)
print("===== Highest Attandance ======")
print(Students[Highest] ," : ",Percentage[Highest] )


# Lowest Attandance

Lowest=np.argmin(Percentage)
print("====== Lowest Attandance ======")
print(f"{Students[Lowest]} : {Percentage[Lowest]}")

# Defaulters Students

Defaulter=Students[Percentage<75]

print(" Students Which Is Below 75% :")
if len(Defaulter)>0:
    print("Defaulter")
else:
    print("Not Defaulter")


# Statistics
print("Maximum Attandense :",round(np.max(Percentage),2),"%")
print("Minimum Attandance :",round(np.min(Percentage),2),"%")
print("Standard Deviation :",round(np.std(Percentage),2))

