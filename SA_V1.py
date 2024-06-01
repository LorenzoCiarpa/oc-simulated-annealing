from newton_troncato import troncatoMAIN
from auxiliary import function
from problems import starting_point
#from autograd import grad
import autograd.numpy as np
from constants import *
import keyboard

# PASSO 0 #

nf = 0
n = DIM

# x_0 € D e x_0 = x_0*
xs = starting_point(n)
xStar = xs

#calcolo la funzione in x_0 e x_0*
f = function(xs, n, eps)
fs = f
fStar = f
nf += 1

print("Valore di funzione ottimo iniziale: ", fs, xs)

# k = 1
k = 1

# inizializzo T
T = 1 / (1 + k)


# max_iter = 10**6 * 4
max_iter = 10**5 * 2
dic = {}
file = open("Funzione Test PROB 4", "w")

                    
while k < max_iter:
    
    if keyboard.is_pressed('q'):
        print("Hai premuto 'q'. Uscita dal programma.")
        break

# PASSO 1 #        
    x_k = starting_point(n)
    alpha = np.random.random()

    # nf += 1
    
    #Perchè? limita divergenza fObj?!
    fObj = function(x_k, n, eps)
    if fObj > fStar :
        k += 1
        if k % 10000 == 0: 
            print(f"Numero di iterazioni totali: {k}, fObj: {fObj}, fStar: {fStar}")
        continue
    
    
# PASSO 2 # 
    #a = 0
    #b = 0
    numeratore_exp = function(x_k, n, eps) - fStar
    d = np.exp(-(np.maximum(0.0, numeratore_exp)) / T)
    
    """
    if function(x_k, n) - f_min > 10**2 :
        d = np.exp(-(np.maximum(0.0, numeratore_exp)) / T)
        a += 1
    else :
        d = 0.1
        b += 1
    """    
    
    #print(function(x_k, n),   m   f_min, function(x_k, n) - f_min)
    #print(alpha, d)
    #print(np.exp(np.maximum(0.0, function(x_k, n) - f_min)))
    if (alpha > d) :
        xs = x_k
        fs = function(x_k, n, eps)
        k += 1
        print("Numero di iterazioni totali: ", k)
        continue

# PASSO 3 #
    print("Numero di punti generati: ", k)
    print("Valore funzione obiettivo prima di minimizzazione locale: ", fObj)
    y_k = troncatoMAIN(eps, delta, x_k)
    
    #print("y_k", y_k)

    #Perchè vincolare y_k?
    # if (y_k - 500 > 0).any() :
    #     print("Out of range")
    #     continue
    # if (y_k  < 0).any() :
    #     print("Out of range")
    #     continue


    if (y_k > 10).any() :
        print("Out of range")
        break
    if (y_k < -10).any() :
        print("Out of range")
        break
    
# PASSO 4 #
    #print("XK", x_k)
    #print("XK-1", x_k_1)

    fObj = function(y_k, n, eps)
    print("Valore funzione obiettivo dopo minimizzazione locale: ", fObj)

    nf += 1
    if fObj < fStar :
        xs = y_k
        fs = function(y_k, n, eps)
        sp = " x = " + str(xs)
        sf = " f = " + str(fs)
        snf = " nf = " + str(nf)
        sni = " k = " + str(k)
        file.write(sni + "\t\t" + snf + "\t\t" + sf)
        file.write("\n\n")
    else :
        xs = x_k
        fs = function(x_k, n, eps)
    
    
    if fs < fStar :
        fStar = fs
        xStar = xs
        dic[str(xStar)] = fStar
        sp = " x = " + str(xStar)
        sf = " f = " + str(fStar)
        snf = " nf = " + str(nf)
        sni = " k = " + str(k)
        file.write(sni + "\t\t" + snf + "\t\t" + sf)
        file.write("\n\n")
    
    

# PASSO 5 #
    """
    if k < max_iter*0.33 :
        T = 15/16
    if k < max_iter*0.66 and k >= max_iter*0.33 :
        T = (15/16)**100
    if k < max_iter*1 and k >= max_iter*0.66 :
        T = (15/16)**200
    """
    
    T = 1 / (1 + k)
    
    if T < 10**(-2) : T = 10**(-2)
   
    
# PASSO 6 #
    #print(x_k)
    k += 1
    #f = function(xs, n)
    print("Numero di iterazioni totali: ", k, nf)
    
    #f_min = function(xs, n)
    
print("\nAlgoritmo terminato per massimo numero di iterazioni, pari a", max_iter)
file.write("\nAlgoritmo terminato per massimo numero di iterazioni, pari a " + str(max_iter))
file.write("\n\n")
for i in range(0, n) :
    print("\nx(",i+1,") =",xStar[i], "\n")
    file.write("\nx("+str(i+1)+") = "+str(xStar[i])+ "\n")
file.close()
#for i in range(0, n) :
    #print  ("\nx(",i+1,") =",x_k_1[i], "\n")
print("Il valore ottimo è ", fStar, " !")

#print(dic_minimi)
