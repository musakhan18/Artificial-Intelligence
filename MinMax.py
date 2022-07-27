# D for Depth
# I for Index
# T for Turn
# S for Score
# T_D for Target_Depth
import math
def MINIMAX_ALGO(D,I,T,S,T_D):
    # base case : targetDepth reached
    if (D == T_D):  
        return S[I]
    if (T):
        return max(MINIMAX_ALGO(D + 1,I*2,False,S,T_D),MINIMAX_ALGO(D + 1,I*2+1,False,S,T_D))
    else:
        return min(MINIMAX_ALGO(D + 1,I*2,True,S,T_D),MINIMAX_ALGO(D + 1,I*2+1,True,S,T_D))
    
# Driver code
Utility_Values = [5,7,1,-2,8,-4,3,7,-9,2,3,1,-5,8,1,3,2]
Tree_Depth = int(math.log(len(Utility_Values), 2))
print("Tree Depth: ",Tree_Depth)
print("The Optimal Value is : ", end = "")
print(MINIMAX_ALGO(0,0,True,Utility_Values,Tree_Depth))