import numpy as np

# Creating Student Name 
Students=np.array(["Lucky","Sumit","Sohan","Surjeet","Sunjay"])

# Creating Marks Of Students
Marks=np.array([
    [67,87,55],
    [78,76,65],
    [55,65,77],
    [90,96,66],
    [56,66,78]
])

print("Students Name :\n")
print(Students,"\n")

print("Student Marks :\n")
print(Marks,"\n")


# Sum Of All Students Marks
Total_Marks=np.sum(Marks,axis=1)
print("Total Marks : ",Total_Marks)

# Percentage Of All Students Marks

Percentage=(Total_Marks*100)/300
print("Percentage : ",Percentage)


# Statitics

print("Average Number :",np.mean(Percentage))
print("Minimun number : ",np.min(Percentage))
print("Maximum Number : ",np.max(Percentage))
print("Median Number : ",np.median(Percentage))

# Filtering Students 

print("--- Students Number Above 80% ---")
High_score=Students[Percentage>80]
print(High_score)


print("--- Students Number Is Above 60% ---")
Medium_Score=Students[(Percentage>60)&(Percentage<=80)]
print(Medium_Score)

print("--- Students Number Is Above 33% ---")
Low_score=Students[(Percentage>40)&(Percentage<=60)]
print(Low_score)

print("--- Students Number Is Below 33% ---")
Failed_Score=Students[(Percentage<33)]
print(Failed_Score)


# Topper Students 
Topper_index=np.argmax(Percentage)
print(f"Topper Students :{Students[Topper_index]} - Marks :{Percentage[Topper_index]}")



# Ranking Students 

Ranking_Students=np.argsort(Percentage)[::-1]
for rank,idx in enumerate(Ranking_Students,start=1):
    print(f"Rank {rank} :{Students[idx]} - {Percentage[idx]} ")

# Students Scoring Above Student

Average=np.sort(Percentage)
print("--- Student Above Average ---")
print(Students[Percentage>Average],"\n")


# Grade Assignemnet 
Grade=np.where(
    Percentage>90,'A+',
        np.where(
            (Percentage>60)&(Percentage<=90),'A',
            np.where(
                (Percentage>40)&(Percentage<=60),'B',
                np.where(
                    (Percentage>33)&(Percentage<=40),'C','F'
                    
                )
            )
    )
)


for s,g,m in zip(Students,Grade,Percentage):
    print(f"{s} : {m} - {g}")
    






