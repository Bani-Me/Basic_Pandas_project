import pandas as pd
sd = pd.read_excel('Employee Sample Data - Copy.xlsx')
x = pd.DataFrame(sd)

x.fillna({"Exit Date": "In Company"}, inplace = True)
x.fillna({"City": "Unknown"}, inplace = True)
x.fillna({"Country": "Unknown"}, inplace = True)
x.fillna({"Job Title": "NO ENTRY"}, inplace = True)


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
print(x.head(19))