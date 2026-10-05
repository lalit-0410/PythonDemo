import numpy as np
import pandas as pd

data = {
    "Name": ["Lalit", "Rahul", "Amit", "Priya", "Neha", "Ravi"],
    "Python": [85, 72, 10, 65, 88, 55],
    "Java": [78, 80, 92, 70, 85, 60],
    "DBMS": [90, 75, 18, 68, 91, 58],
    "AI": [88, 70, 25, 72, 89, 62]
}
scorecard=pd.DataFrame(data)
# print(scorecard)

#save data
scorecard.to_csv('Result.csv', index=False)

#read data from csv
load_data=pd.read_csv('Result.csv')

#print(load_data)

#calculate avg and total marks

scorecard['Total']=np.sum(scorecard[["Python", "Java", "DBMS", "AI"]],axis=1)
# print(scorecard)
scorecard['Average']=scorecard['Total']/4
#print(scorecard)

#highest scorer
high=scorecard.sort_values('Total',ascending=False).head(1) 
#print(high)

#lowest scorer
lower=scorecard.sort_values('Total').head(1)
#print(lower)

#class average
class_avg=np.sum(scorecard['Average']/len(scorecard))
#print(class_avg)

scorecard["Status"] = scorecard["Average"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)
# print(scorecard)

#pass and fail
pass_stu = scorecard[scorecard["Status"] == "Pass"]
# print(pass_stu)

fail_stu = scorecard[scorecard["Status"] == "Fail"]
# print(fail_stu)

#subject vise avg
subject_avg=scorecard[["Python", "Java", "DBMS", "AI"]].mean()
# print(subject_avg)

#top 3
top3=scorecard.sort_values('Total',ascending=False).head(3)
# print(top3)



#FINAL REPORT
print("\n" + "=" * 50)
print("             FINAL SCORECARD REPORT")
print("=" * 50)

print("\n1. STUDENT SCORECARD")
print(scorecard.to_string(index=False))

print("\n2. SUBJECT-WISE AVERAGE")
subject_avg = scorecard[["Python", "Java", "DBMS", "AI"]].mean().round(2)
print(subject_avg)

print("\n3. CLASS STATISTICS")
print("Class Average :", round(scorecard["Average"].mean(), 2))
print("Highest Total :", scorecard["Total"].max())
print("Lowest Total  :", scorecard["Total"].min())

print("\n4. RESULT SUMMARY")
print("Total Students :", len(scorecard))
print("Passed         :", (scorecard["Status"] == "Pass").sum())
print("Failed         :", (scorecard["Status"] == "Fail").sum())

print("\n5. PASSED STUDENTS")
print(scorecard[scorecard["Status"] == "Pass"][["Name", "Total", "Average", "Status"]].to_string(index=False))

print("\n6. FAILED STUDENTS")
print(scorecard[scorecard["Status"] == "Fail"][["Name", "Total", "Average", "Status"]].to_string(index=False))

print("\n" + "=" * 50)
print("              REPORT COMPLETED")
print("=" * 50)

