import numpy as np 

# Define Cricketer's name

Cricketer=np.array(["Hardik Pandiya","Virat Kohli","Ms Dhoni","Ravindra jadeja"])

# Define runs
Runs=np.array([
    int(input(f"Enter Runs - {Name} :"))
    for Name in Cricketer
    ])
# Define Balls
print("Enter Balls Of All Players")
Balls=np.array([
    int(input(f"Enter Balls - {ball} :"))
    for ball in Cricketer

])

# Strike Rate
print("====== Strike Rate ======")
for i ,j,k in zip(Runs,Balls,Cricketer):
        strike=(i/j)*100
        print(f"{k} : {round(strike,2)}")

      
# Average Runs
print("====== Average Runs ======")
print(np.mean(Runs))

# Average Balls
print("====== Average Balls =======")
print(np.mean(Balls))

# Highest Runs
print("====== Highest Runs And Balls")
Highest_Run=np.argmax(Runs)
print(f"{Cricketer[Highest_Run]} : {Runs[Highest_Run]} : {Balls[Highest_Run]}")


# Lowest Runs
print("====== Lowest Runs And Balls ======")
Lowest_Run=np.argmin(Runs)
print(f"{Cricketer[Lowest_Run]} : {Runs[Lowest_Run]} : {Balls[Lowest_Run]}")

# Standard Divation

print("======= Standard Divation ========")
print(np.std(Runs))

# Highest To Lowest Runs
print("======= Ranking Accoring To Runs =======")
sort_run=np.argsort(Runs)[::-1]
for i in sort_run:
    if Runs[i]>=50:
        print(f"{Cricketer[i]} : {Runs[i]} : {Balls[i]} = Excellient")
    elif Runs[i]>=30 & Runs[i]<50:
        print(f"{Cricketer[i]} : {Runs[i]} : {Balls[i]} = Good")
    elif Runs[i]<30:
        print(f"{Cricketer[i]} : {Runs[i]} : {Balls[i]} = Needs Improvement")


# Final Report
print("========== Final Report ==========")
Total_player=len(Cricketer)
print("\n Total Players : ",Total_player)
Total_Run=np.sum(Runs)
print("\n Total Runs :",Total_Run)
print("\n Average :",np.mean(Runs))
Hightest_Strike=np.max(strike)
print("\n Highest Strike Rate :",Hightest_Strike)
print("\n====== Highest Runs And Balls")
Highest_Run=np.argmax(Runs)
print(f"{Cricketer[Highest_Run]} : {Runs[Highest_Run]} : {Balls[Highest_Run]}")
print("\n====== Lowest Runs And Balls ======")
Lowest_Run=np.argmin(Runs)
print(f"{Cricketer[Lowest_Run]} : {Runs[Lowest_Run]} : {Balls[Lowest_Run]}")
