import numpy as np
from autograd import grad

from constants import *


# prob1

# def dim() :
#     return DIM
    
# def functionProblem(x, n) :
#     #c = 10**2
#     f = (10**(5)*x[0]**2) + x[1]**2 - (x[0]**2 + x[1]**2)**2 + (10**(-5)*(x[0]**2 + x[1]**2)**4) 
#     #for i in range(0, n - 1) :
#         #f = f + c*(x[i + 1] - (x[i]**2))**2 + (1 - x[i])**2
#     #print("funzione", f)
#     return f

# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-20, 20))
#         pto_init[i + 1] = float(np.random.uniform(-20, 20))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init

# problem 2
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-2.5, 2.5))
#         pto_init[i + 1] = float(np.random.uniform(-1.5, 1.5))
#     return pto_init
    
# def functionProblem(x, n) :
#     f = 0
#     f = (4 - 2.1*(x[0]**2) + (x[0]**4)/3)*(x[0]**2) + x[0]*x[1] + ((-4 + 4*x[1]**2)*(x[1]**2))
#     return f


#prob 3
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(0, 500))
#         pto_init[i + 1] = float(np.random.uniform(0, 500))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init
    
# def functionProblem(x, n) :
#     #c = 10**2
#     f = -x[0]*x[1]*(72 - 2*x[0] - 2*x[1])
#     #for i in range(0, n - 1) :
#         #f = f + c*(x[i + 1] - (x[i]**2))**2 + (1 - x[i])**2
#     #print("funzione", f)
#     return f


#prob4

# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-500, 500))
#         pto_init[i + 1] = float(np.random.uniform(-500, 500))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init
    
# def functionProblem(x, n) :
#     #c = 10**2
#     f = 100*(x[1]-(x[0]**2))**2 + 6*(6.4*(x[1]-0.5)**2 - x[0] - 0.6)**2
#     #for i in range(0, n - 1) :
#         #f = f + c*(x[i + 1] - (x[i]**2))**2 + (1 - x[i])**2
#     #print("funzione", f)
#     return f



#prob5
    
# def starting_point(n) :
#     pto_init = np.zeros(n)
#     for i in range(0, n, 2) :
#         pto_init[i] = float(np.random.uniform(-10, 10))
#         pto_init[i + 1] = float(np.random.uniform(-10, 10))
#     #print(pto_init, type(pto_init), pto_init[0])
#     return pto_init
    
# def functionProblem(x, n) :
#     #c = 10**2
#     f = (x[0] - 13 + ((5-x[1])*x[1] - 2)*x[1])**2 +  (x[0]-29 + ((x[1] + 1)*x[1] - 14)*x[1])**2
#     #for i in range(0, n - 1) :
#         #f = f + c*(x[i + 1] - (x[i]**2))**2 + (1 - x[i])**2
#     #print("funzione", f)
#     return f

#prob 6

def dim() :
    return 4
    
def starting_point(n) :
    pto_init = np.zeros(n)
    for i in range(0, n, 2) :
        pto_init[i] = float(np.random.uniform(-10, 10))
    #print(pto_init)
    return pto_init
    
def functionProblem(x, n) :
    f = (100*(x[0]**2 - x[1])**2) + ((x[0] - 1)**2) + ((x[2] - 1)**2) + (90*(x[2]**2 - x[3])**2) + (10.1*((x[1] - 1)**2 + (x[3] - 1)**2)) + (19.8*(x[1] - 1)*(x[3] - 1))
    #print("funzione", f)
    return f