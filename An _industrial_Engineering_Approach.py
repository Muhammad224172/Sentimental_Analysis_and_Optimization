# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 07:57:58 2023

@author: MUHAMMAD
"""
###
#The aim of this project is to optimize customer satisfaction under certain conditions 
# our decision variables incluses 
#customer service(with a weight of 5) (x1 and x2)
#product(with a weight of 4)
#price(with a weight of 2)


#consider the following contrains 
#1. we have a maximum budget we can invest into this as 30,000 dollars 
#1)change the a staff will cost 2000 dollars to recuirt a better staff 2) we also have the choice of retraining staff which will cost 5000 dollars 
# considiering the time it will take hence we can take only one choice here 
# 1) product lenses 2) product frames 2) product colors (x3 , x4 , x5)
## 1) we can only decrease price as much as 200 dollars (x6)

#our model will follow a knapsack solution however we will have more contrains to show

from gurobipy import GRB,Model,quicksum #*

def Output(m):  
    # Print the result
    status_code = {1:'LOADED', 2:'OPTIMAL', 3:'INFEASIBLE', 4:'INF_OR_UNBD', 5:'UNBOUNDED'} #this is how a 'dictionary' 
                                                                                            #is defined in Python
    status = m.status
    
    print('The optimization status is ' + status_code[status])
    if status == 2:    
        # Retrieve variables value
        print('Optimal solution:')
        for v in m.getVars():
            print(str(v.varName) + " = " + str(v.x))    
        print('Optimal objective value: ' + str(m.objVal) + "\n")
        

def ModelHardcoded():
    # Create the model
    m = Model('Satisfaction')
    
    # Set parameters
    m.setParam('OutputFlag',True)
    #varaibles 
    upper = 200 #upper price range 
    lower = 90 #lower price range 
    products = 2 #number of product areas we would like to focus on
    customer_service = 2 #areass under customer service we would like to focus on
    
    # Add variables
    marketing_delivery  = m.addVar(name='marketing_deivery', lb=0, ub=GRB.INFINITY, vtype=GRB.BINARY)
    recruiting = m.addVar(name='recruiting', lb=0, ub=GRB.INFINITY, vtype=GRB.BINARY)    
    training   = m.addVar(name='training',   lb=0, ub=GRB.INFINITY, vtype=GRB.BINARY)    
    lenses  = m.addVar(name='lenses',   lb=0, ub=GRB.INFINITY, vtype=GRB.BINARY) 
    color   = m.addVar(name='color',   lb=0, ub=GRB.INFINITY, vtype=GRB.BINARY) 
    frame  = m.addVar(name='frame',   lb=0, ub=GRB.INFINITY, vtype=GRB.BINARY) 
    price  = m.addVar(name='price',   lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS) 
    
    # maximize satisfaction
    m.setObjective(800*recruiting + 730*marketing_delivery + 700*training + 600* lenses + 400*color + 700*frame - 20*price , GRB.MAXIMIZE)
    
    # Constraint on customer service changes 
    m.addConstr(recruiting + training + marketing_delivery <= customer_service, name="Customer services")
    
  
    # Constraint on product
    m.addConstr(lenses + color + frame <= products, name="products")
    
    # Constraint on price
    m.addConstr(price <= upper, name="prices")
    
    m.addConstr(price >= lower, name="prices_1")
    
    
    
    #overall_contrain on values 
    m.addConstr(6000*recruiting + 5000*training + 730*marketing_delivery + 4000*lenses + 3000* color + 5500*frame <= 10000 + 1000*price ,   name="over_all")
        
    # Optimize the model
    m.optimize()
    
    Output(m)
    
    # print the LP file
    m.write('Satisfaction.lp')
    
    # print the sol file
    m.write('Satisfaction.sol')
ModelHardcoded()