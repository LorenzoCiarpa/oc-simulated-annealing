from newton_troncato import troncatoMAIN
from auxiliary import function
from problems import starting_point
#from autograd import grad
import autograd.numpy as np
from constants import *
import keyboard

# PASSO 0 #

n_func_eval = 0
n = DIM

# x_0 € D e x_0 = x_0*
x_start = starting_point(n)
x_Star = x_start

#calcolo la funzione in x_0 e x_0*
f_prev = function(x_start, n, eps)
f_Star = f_prev
n_func_eval += 1

print("Valore di funzione ottimo iniziale: ", f_Star, x_Star)

# k = 1
k = 1

# inizializzo T
T = 1 / (k)


# max_iter = 10**6 * 4
max_iter = 10**4 * 2
dic = {}
file = open("Funzione Test PROB 4", "w")

                    
while k < max_iter:
    
    if keyboard.is_pressed('q'):
        print("Hai premuto 'q'. Uscita dal programma.")
        break

# PASSO 1 #        
    x_k = starting_point(n)
    alpha = np.random.uniform(0, 1)

    # nf += 1
    
    #Perchè? limita divergenza fObj?!
    # fObj = function(x_k, n, eps)
    # if fObj > fStar :
    #     k += 1
    #     if k % 10000 == 0: 
    #         print(f"Numero di iterazioni totali: {k}, fObj: {fObj}, fStar: {fStar}")
    #     continue
    
    
# PASSO 2 # 
    numeratore_exp = function(x_k, n, eps) - f_Star
    d = np.exp((-(np.maximum(0.0, numeratore_exp)) / T))
    
    if (alpha > d) :
        # xs = x_k
        # fs = function(xs, n, eps)
        k += 1
        print("Numero di iterazioni totali: ", k)
        continue

# PASSO 3 #
    fObj = function(x_k, n, eps)
    print("Numero di punti generati: ", k)
    print("Valore funzione obiettivo prima di minimizzazione locale: ", fObj)

    file_stampe.write(f"Valore funzione obiettivo prima della minimizzazione locale all'iterazione {k}: {fObj} \n")

    y_k = troncatoMAIN(eps, delta, x_k)
    
    if (y_k > 10).any() :
        print(f"Out of range, y_k: {y_k}")
        break
    if (y_k < -10).any() :
        print(f"Out of range, y_k: {y_k}")
        break
    
# PASSO 4 #
    #print("XK", x_k)
    #print("XK-1", x_k_1)

    fObj = function(y_k, n, eps)
    print("Valore funzione obiettivo dopo minimizzazione locale: ", fObj)
    file_stampe.write(f"Valore funzione obiettivo dopo la minimizzazione locale all'iterazione {k}: {fObj} \n")


    n_func_eval += 1
    if fObj < f_Star :
        x_Star = y_k
        f_Star = function(y_k, n, eps)
        # sp = " x = " + str(x_Star)
        # sf = " f = " + str(f_Star)
        # snf = " nf = " + str(n_func_eval)
        # sni = " k = " + str(k)
        # file.write(sni + "\t\t" + snf + "\t\t" + sf)
        # file.write("\n\n")
    # else :
        # xs = x_k
        # fs = function(x_k, n, eps)
    file_stampe.write(f"f* all'iterazione {k}: {f_Star}\n\n")
    
    
    
    # if fs < fStar :
    #     fStar = fs
    #     xStar = xs
    #     dic[str(xStar)] = fStar
    #     sp = " x = " + str(xStar)
    #     sf = " f = " + str(fStar)
    #     snf = " nf = " + str(nf)
    #     sni = " k = " + str(k)
    #     file.write(sni + "\t\t" + snf + "\t\t" + sf)
    #     file.write("\n\n")
    
    

# PASSO 5 #
    
    T = 1 / (1 + k)
    
    # if T < 10**(-4) : T = 10**(-4)
   
    
# PASSO 6 #
    k += 1
    print("Numero di iterazioni totali: ", k, n_func_eval)

    if k % 10000 == 0:
        print(f_Star)
    
    
# print("\nAlgoritmo terminato per massimo numero di iterazioni, pari a", k)
print("\nAlgoritmo terminato per massimo numero di iterazioni, pari a", max_iter)

file_stampe.write(f"\n\n")
file_stampe.write(f"Algoritmo terminato in {k} iterazioni \n")

file.write("\nAlgoritmo terminato per massimo numero di iterazioni, pari a " + str(max_iter))
file.write("\n\n")

file_stampe.write(f"Il valore di x*: \n")

for i in range(0, n) :
    file_stampe.write(f"x({i+1}) = {x_Star[i]} \n")
    print("\nx(",i+1,") =",x_Star[i], "\n")
    file.write("\nx("+str(i+1)+") = "+str(x_Star[i])+ "\n")
file.close()

print("Il valore ottimo è ", f_Star, " !")
file_stampe.write(f"Il valore della funzione obiettivo in x*: {f_Star} \n")

#print(dic_minimi)
