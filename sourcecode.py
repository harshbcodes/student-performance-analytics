import numpy as np
import pandas as pd


df = pd.read_csv("students.csv")
print("------------------------------------------------------------------")
print(df.shape)
print("------------------------------------------------------------------")
print(df.info())


display(df.head())
print("-----------------------------------------------------------")
display(df.tail())

df["Total_Marks"] = df["Python_Marks"] + df["AI_Marks"] + df["Maths_Marks"]
df["Average_Marks"] = df["Total_Marks"] / 3
print(df[["Name", "Total_Marks", "Average_Marks"]])
df.head()
#Calculate total marks and average marks for each student.


print("Highest Average:", df["Average_Marks"].max())
print("Lowest Average:", df["Average_Marks"].min())
print("Class Average:", df["Average_Marks"].mean())


def grade(Marks):
    if(Marks)>=90:
        return 'A'
    elif(Marks)>=70:
        return 'B'
    elif(Marks)>=50:
        return 'C'
    else:
        return 'F'   

#Assign grades based on a clearly defined grading rule.  reusable functions

df["Grade"] = df["Average_Marks"].apply(grade)
print(df[["Student_ID","Average_Marks","Grade"]])
#Assign grades based on a clearly defined grading rule.

def check(Grade):
    if(Grade)=='F':
        return "Fail"
    else:
        return "Pass"

 #Identify pass/fail students using a clearly defined condition. reusable functions

df["Result"] = df["Grade"].apply(check)
print(df[["Student_ID","Average_Marks","Grade","Result"]])

count_pass = (df["Result"]=='Pass').sum()
count_fail = (df["Result"]=='Fail').sum()
print("Passed students-",count_pass)
print("Failed students-",count_fail)
# Identify pass/fail students using a clearly defined condition.


Total = count_pass + count_fail
pass_percentage = (count_pass/Total)*100
fail_percentage = (count_fail/Total)*100
print("Pass percentage(%)-",pass_percentage)
print("Fail percentage(%)-",fail_percentage)
# Identify pass/fail students using a clearly defined condition.


Python_Average = df["Python_Marks"].mean()
AI_Average = df["AI_Marks"].mean()
Maths_Average = df["Maths_Marks"].mean()
print("Python_Average-",Python_Average)
print("AI_Average-",AI_Average)
print("Maths_Average-",Maths_Average)
#Generate subject-wise performance analysis.

def getmax(m1,m2,m3):
    return np.max([m1,m2,m3])
def getmin(m1,m2,m3):
    return np.min([m1,m2,m3])

highest_avg = getmax(Python_Average,AI_Average,Maths_Average)
lowest_avg = getmin(Python_Average,AI_Average,Maths_Average)

print("Highest_avg-",highest_avg)
print("Lowest_avg-",lowest_avg)

pm = df["Python_Marks"].to_numpy()  
Python_max = pm.max()
Python_min = pm.min()
am = df["AI_Marks"].to_numpy()  
AI_max = am.max()
AI_min = am.min()
mm = df["Maths_Marks"].to_numpy()  
Maths_max = mm.max()
Maths_min = mm.min()


pmm = pm.max()

print("Python Highest Marks, Python Lowest Marks = ",Python_max,Python_min)
print("AI Highest Marks, AI Lowest Marks = ",AI_max,AI_min)
print("Maths Highest Marks, Maths Lowest Marks = ",Maths_max,Maths_min)


# Find highest, lowest and average performance using numpy.


Python_Topper = df.loc[df["Python_Marks"] == Python_max, "Name"]
AI_Topper = df.loc[df["AI_Marks"] == AI_max, "Name"]
Maths_Topper = df.loc[df["Maths_Marks"] == Maths_max, "Name"]



print("Python Topper-",Python_Topper)
print("AI Topper-",AI_Topper)
print("Maths Topper-",Maths_Topper)
#Generate subject-wise performance analysis.

Class_Topper = df.loc[df["Average_Marks"].max() == df["Average_Marks"], "Name"]

print("Class Topper-", Class_Topper)

#Identify top-performing students.

Avg_Attendance = df["Attendance_Percent"].mean()
print("Avg_Attendance-",Avg_Attendance)
print("-------------------------------------------------------------------------")
print("is_Attendance_Defaulter")
df["Attendance_defaulter"] = df["Attendance_Percent"] <= 75
print(df[["Name","Attendance_defaulter"]])

AIML_maxavgMark = df[df["Department"] == 'AIML']["Average_Marks"].max()
CSE_maxavgMark = df[df["Department"] == 'CSE']["Average_Marks"].max()
print("AIML maximum average marks-",AIML_maxavgMark)
print("CSE maximum average marks-",CSE_maxavgMark)





