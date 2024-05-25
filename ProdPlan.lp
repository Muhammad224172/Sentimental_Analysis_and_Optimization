\ Model ProdPlan
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  2 x_1 + 3 x_2 + 10 x_3 + 4 x_4 + 8 x_5 + 4 x_6 + 10 x_7 + 5 x_8 + I_1
   + I_2 + I_3 + I_4 + I_5 + I_6 + I_7 + I_8
Subject To
 R0: x_1 - I_1 = 50
 R1: x_2 + I_1 - I_2 = 60
 R2: x_3 + I_2 - I_3 = 20
 R3: x_4 + I_3 - I_4 = 30
 R4: x_5 + I_4 - I_5 = 80
 R5: x_6 + I_5 - I_6 = 50
 R6: x_7 + I_6 - I_7 = 25
 R7: x_8 + I_7 - I_8 = 60
 R8: I_8 = 10
Bounds
End
