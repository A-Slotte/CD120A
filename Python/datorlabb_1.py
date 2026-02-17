import numpy as np
import math as math
import matplotlib.pyplot as plt

# Uppgifter Talföljder
# Fråga 1:

def fråga1():
    s_1 = np.array([]) 
    tot = 0
    for i in range(1, 16):
        s_i = 1/i
        s_1 = np.append(s_1, s_i)
        tot += s_i
    return tot

# Fråga 2:
# a)
def exp_coeffs():
    s_2a = np.array([])
    for i in range(1, 16):
        s_2a = np.append(s_2a, exp(i))
    return s_2a

def exp(k):
    return 1/math.factorial(k)

# b)
def fib():
    s_2b = np.array([])
    for i in range(0, 15):
        if(i <= 1):
            s_2b = np.append(s_2b, i)
        else:
            s_i = s_2b[i - 1] + s_2b[i - 2]
            s_2b = np.append(s_2b, s_i)
    return s_2b

# c)
def sin_coeffs(n):
    s_coeffs = np.array([])
    for i in range(0,n):
       s_coeffs = np.append(s_coeffs, sin_sum(i))
    return s_coeffs

def sin_sum(k):
    if(k%2 != 0):
        a = (-1)**((k-1)//2) / math.factorial(k)
    else:
        a = 0
    return a

# Uppgifter Polynomer
# Fråga 3:
# Beräkna polynom

def eval_poly(x_int, coeffs_arr):
    x_arr = np.array([])
    for i in range(0, len(coeffs_arr)):
        x_arr = np.append(x_arr, x_int**i)
    p = x_arr * coeffs_arr
    a = np.sum(p)
    return a

def approx_e_exp(x_int, tol, return_mode):
    coeffs = np.array([])
    deg = -1
    p_val = 0
    e_exp = np.exp(x_int) - 10**-4
    while abs(p_val - e_exp) > tol: 
        deg += 1
        coeffs = np.append(coeffs, exp(deg))
        p_val = eval_poly(x_int, coeffs)
    if return_mode == "value_only":
        return p_val
    else:
        return p_val, deg

def approx_sin(x_int, tol, return_mode):
    coeffs_sin = np.array([])
    deg = -1
    p_val = 0
    a = np.sin(x_int)
    while abs(p_val - a) > tol:
        deg += 1
        coeffs_sin = np.append(coeffs_sin, sin_sum(deg))
        p_val = eval_poly(x_int, coeffs_sin)
    if return_mode == "value_only":
        return p_val
    else:
        return p_val, deg

def plotGraf():
    my_appval = np.array([])
    e_val = np.array([])
    my_sin= np.array([])
    sin_val = np.array([])

    points = np.linspace(-np.pi, np.pi, 100)
    for i in points:
        my_appval = np.append(my_appval, approx_e_exp(i, 10**-4, "value_only"))
        e_val = np.append(e_val, np.exp(i))
        my_sin = np.append(my_sin, approx_sin(i, 10**-4, "value_only"))
        sin_val = np.append(sin_val, np.sin(i))
    #graf 1
    plt.figure()
    plt.scatter(points, my_appval)
    plt.plot(points, e_val, 'r')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Min approximation(blå) och numpys(röd)")
    plt.grid(True)
    #graf 2
    plt.figure()
    plt.scatter(points, my_sin)
    plt.plot(points, sin_val, 'r')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Min approximation(blå) och numpys(röd)")
    plt.grid(True)
    plt.show()

def mult_coeffs(coeffs_p, coeffs_q):
    len_p = len(coeffs_p)
    len_q = len(coeffs_q)
    # deg(pq) = deg(q) + deg(p). -1 pga indexering.
    len_r = len_p + len_q - 1
    coeffs_r = np.array([])
    coeffs_r = np.append(coeffs_r, np.zeros(len_r))

    for i in range(len_q):
        for j in range(len_p):
            coeffs_r[i+j] += coeffs_p[j] * coeffs_q[i]
    return coeffs_r

def bygg_polynom(coeffs):
    poly = np.array([])
    for i in range(0, len(coeffs)):
        a = coeffs[i]
        if (a < 0):
            poly = np.append(poly, f"{coeffs[i]}x**{i}")
        else:
            poly = np.append(poly, f"+{coeffs[i]}x**{i}")
    s = "".join(poly)
    s = s.strip("+")
    return s

def run():
    # Fråga 1:
    print("================Fråga 1================"+"\n"+f"s = {fråga1()}")
    # Fråga 2:
    print("================Fråga 2================"+"\n"+"Exp-koefficienterna:"+"\n"
          f"{exp_coeffs()}")
    # Fråga 2b:
    print("Fibbonaci följden"+"\n"+f"{fib()}")
    # Fråga 2c:
    print("Sinus koefficienterna"+"\n"+f"{sin_coeffs(16)}")
    # Fråga 3a:
    print("================Fråga 3================"+"\n"+"Graden för att approximera e^2 med fel mindre än 10^-4:"+"\n")
    x = 2
    tol = 10**-4
    values = approx_e_exp(x, tol, "grad")
    print(f"Grad: {values[1]}")
    print(f"Min funktion: {values[0]}")
    print(f"Numpy: {np.exp(2)}")
    # Fråga 3b:
    print("Graden för att approximera sin(5pi/3) med fel mindre än 10^-4")
    x = np.pi*5/3
    values = approx_sin(x, tol, "grad")
    print(f"Grad: {values[1]}")
    print(f"Min funktion: {values[0]}")
    print(f"Numpy: {np.sin((5*np.pi)/3)}")
    
    # Fråga 4:
    print("================Fråga 4================")
    # Kontroll med numpoys polynomial paket
    p = np.polynomial.Polynomial([1.0, -2.0, 0.5, 0.0, 0.2])
    q = np.polynomial.Polynomial([2.0, 5.0])
    r = p * q
    print(f"Numpy polynom {r}")
    # Min kod.
    p_arr = np.array(([1.0, -2.0, 0.5, 0.0, 0.2]))
    q_arr = np.array(([2.0, 5.0]))
    # Multiplicera koefficienterna av två polynom
    coeffs = mult_coeffs(p_arr, q_arr)
    # bygg_polynom, lägger till x till koeficcienterna.
    print(f"Polynom: {bygg_polynom(coeffs)}")
    # Plotta grafer
    plotGraf()

run()

    



