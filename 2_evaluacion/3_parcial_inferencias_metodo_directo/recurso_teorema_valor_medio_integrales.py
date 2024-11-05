# 
import numpy as np 
import matplotlib.pyplot as plt   
from ipywidgets import interact  
from scipy.integrate import quad

def trazo_region_rectangular(c = 0):
    plt.figure(figsize = (6,4)) 
    plt.title('Trazo del rectángulo de área igual al área bajo la curva de f') 
    plt.xlabel('x')
    plt.ylabel('y') 
    # trazo de la región bajo la función identidad 
    paso = 0.1
    a,b = 0,1
    dominio = np.arange(a, b + paso, paso) 
    f = lambda x: x
    y = f(dominio) 
    plt.plot(dominio, y)
    resultado, error = quad(f, a, b)
    plt.fill_between(dominio, y, label = f'el área bajo f es {resultado}') 
    #  trazo del rectángulo de área igual al área bajo la curva de f 
    rectangulo_y = f(c)*np.ones_like(dominio) 
    plt.fill_between(dominio, rectangulo_y, color = 'red', label = f'Área del rectángulo es: {f(c)*(b-a)}') 
    plt.xticks(np.arange(0, 1 + paso, paso)) 
    plt.yticks(np.arange(0, 1 +  paso, paso)) 

    plt.grid(alpha = 0.3)
    plt.legend()
    plt.show()  
    

interact(trazo_region_rectangular, c = (0, 1, 0.1))