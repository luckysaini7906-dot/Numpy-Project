import numpy as np

# Define Tempreature Of 15 Day's in Degree Celcuis

Tempreature=np.array([24,32,33,35,40,45,44,20,25,22,46,42,34,29,39])


print("Tempreature Data :")
print(Tempreature)

# Statical Analysis

print("--- Statistics ---")
print("Average Tempreature :",np.mean(Tempreature))
print("Maximum Tempreature :",np.max(Tempreature))
print("Minimum Tempreature :",np.min(Tempreature))
print("Standard Deviation :",np.std(Tempreature))

# Conditional Filtering

Hot_days=Tempreature[Tempreature>35]
print("Hot Day's :",Hot_days)

Cold_days=Tempreature[Tempreature<30]
print("Cold Day's :",Cold_days)

Pleasant_days=Tempreature[(Tempreature>=30)&(Tempreature<=35)]
print("Pleasent Day's (30-35 Degree Celcius) :",Pleasant_days)


# percentile Analysis

p25=np.percentile(Tempreature,25)
p50=np.percentile(Tempreature,50)
p75=np.percentile(Tempreature,75)
p90=np.percentile(Tempreature,90)


print("25th Percentile :",p25)
print("50th Percentile (Median Percentile) :",p50)
print("75th Percentile :",p75)
print("90th Percentile :",p90)

# Extra Analysis
Above_avg=Tempreature[Tempreature>np.mean(Tempreature)]
print("Tempreature Above Average :",Above_avg)


print("Number Of Hot Days :")
print(np.sum(Tempreature>35))
print("Number OF Cold Days :")
print(np.sum(Tempreature<30))



