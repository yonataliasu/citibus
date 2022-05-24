from pulp import *
import csv
#sets
Routes=['NW3','WFE1','NF1','TN1','NTOP1','STOP1','STOP4','MaskedRaider3','NW1','DoubleT1','RedRaider4','NTOP2','T1','NW2','MaskedRaider1','TN2','NF2','NTOP4',
           'WFE2','DoubleT3','RedRaider1','RedRaider2','MaskedRaider5','NTOP3','T2','STOP3','DoubleT2','DoubleT4','RedRaider3','MaskedRaider2','MaskedRaider4','T3','DoubleT5','RedRaider5']

Drivers= ['FT1', 'FT2', 'FT3', 'FT4', 'FT5', 'FT6', 'FT7', 'FT8', 'FT9', 'FT10', 'FT11', 'FT12', 'FT13', 'FT14', 'FT15', 'FT16', 'FT17', 'FT18', 'FT19', 'FT20', 'FT21', 'FT22', 'FT23', 'FT24']
print(len(Routes))
print(len(Drivers))      

#Dictionary of Max amount that each driver can drive

Drivers_max_hours={'FT1':37.5,
       'FT2':37.5,
       'FT3':37.5,
       'FT4':37.5,
       'FT5':37.5,
       'FT6':37.5,
       'FT7':37.5,
       'FT8':37.5,
       'FT9':37.5,
       'FT10':37.5,
       'FT11':37.5,
       'FT12':37.5,
       'FT13':37.5,
       'FT14':37.5,
       'FT15':37.5,
       'FT16':37.5,
       'FT17':37.5,
       'FT18':37.5,
       'FT19':37.5,
       'FT20':37.5,
       'FT21':37.5,
       'FT22':37.5,
       'FT23':37.5,
       'FT24':37.5}

#Dictionary of time each route will cover
route_time={'NW3':36.05,
        'WFE1':35.95,
        'NF1':33.05,
        'TN1':32.85,
        'NTOP1':32.7,
        'STOP1':31,
        'STOP4':31,
        'MaskedRaider3':30.8,
        'NW1':30.75,
        'DoubleT1':30,
        'RedRaider4':30,
        'NTOP2':29.5,
        'T1':28.55,
        'NW2':27.9,
        'MaskedRaider1':27.85,
        'TN2':27.85,
        'NF2':27.75,
        'NTOP4':27.7,
        'WFE2':26.8,
        'DoubleT3':25,
        'RedRaider1':25,
        'RedRaider2':25,
        'MaskedRaider5':24.9,
        'NTOP3':24.5,
        'T2':23.85,
        'STOP3':23,
        'DoubleT2':22.7,
        'DoubleT4':22.7,
        'RedRaider3':22.7,
        'MaskedRaider2':21.95,
        'MaskedRaider4':21.95,
        'T3':11.85,
        'DoubleT5':10,
        'RedRaider5':10}



       
        
#Set Problem Variable
prob = LpProblem("Transportation",LpMinimize)

routes_drivers=[(i,j) for i in Routes for j in Drivers]

#Decision Variable

amount_vars=LpVariable.dicts("RouteOperator",(Routes,Drivers),0)
print(amount_vars)
#Objective Function
prob += lpSum(amount_vars[i][j] for (i,j)in routes_drivers)

#Constraints
for j in Drivers:
    prob+= lpSum(amount_vars[i][j] for i in Routes) <=Drivers_max_hours[j]
    prob+= lpSum(amount_vars[i][j] for i in Routes) >=36
for i in Routes:
    prob+= lpSum(amount_vars[i][j] for  j in Drivers) ==route_time[i]

prob.solve()
print("Status:",LpStatus[prob.status])

for v in prob.variables():
    if v.varValue>0:
        print(v.name,v.varValue)

        
print(value(prob.objective))        
    

print(value(prob.objective))


with open('excelpython24ft.csv','w') as f:
    for v in prob.variables():
        if v.varValue>0:
            f.write(",Length of Hours\n")
            f.write(str(v.name) + "," + str(v.varValue) + "\n")
    

