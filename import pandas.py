import pandas as pd
sd = pd.read_excel('Employee Sample Data - Copy.xlsx')
x = pd.DataFrame(sd)

x.fillna({"Exit Date": "In Company"}, inplace = True)
x.fillna({"City": "Unknown"}, inplace = True)
x.fillna({"Country": "Unknown"}, inplace = True)
x.fillna({"Job Title": "NO ENTRY"}, inplace = True)
x.fillna({"Age": 0}, inplace = True)
x.fillna({"Ethiniciy": "Uknown"}, inplace = True)

print(x.head(5))

m = x["Annual Salary"].mean()
x.fillna({"Annual Salary": m}, inplace= True)


x["Age"].loc[3] = 32
x["Exit Date"].loc[4] = "12/4/2020"
x["Bonus %"].loc[1] = 13/100
x["Annual Salary"].loc[4] = 100000
x["City"].loc[0] = "California"


i = 1
temp1 = x["Annual Salary"].loc[0]
k = 0
while i < len(x["Annual Salary"]):
    temp2 = x["Annual Salary"].loc[i]
    if temp2 > temp1:
        temp1 = temp2
        k = i
    i += 1

print(x.loc[k])

G_Dep = x.groupby('Department')
AVG_A = G_Dep['Age'].mean()
AVG_S = G_Dep['Annual Salary'].mean()
print("Average Age: \n" , AVG_A) 

print("Avergae Salary: \n" , AVG_S)


G_Dep_Eth = x.groupby(['Department', 'Ethnicity'])
Max = G_Dep_Eth['Age'].max()
Min = G_Dep_Eth['Age'].min()
Med_S = G_Dep_Eth['Annual Salary'].median()

print("Maximum Age: \n" , Max)
print("Minimum Age: \n", Min)
print("Median Salary: \n" , Med_S)

x.to_excel("Modified_Employee_Data1.xlsx")




