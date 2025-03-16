# Recurso 1 para el aprendizaje y la enseñanza de los cinco operadores lógicos 
from sympy import symbols, And, Or, Not, Implies, Equivalent # Operadores lógicos con Sympy con notación fuuncional
from sympy.logic.boolalg import truth_table
import ipywidgets as widgets
from IPython.display import display

# Definición interactiva de proposiciones
p, q = symbols('p q')
expresion = And(p, q)  # (p ∧ q)

# Widget para explorar operadores, menu de opciones  
@widgets.interact(operador=['Or', 'Not', 'And', 'Implies', 'Equivalent'])

def explicar_operador(operador):
    ejemplos = {
        'Or': Or(p, q),
        'Not': Not(p),
        'And': And(p, q),
        'Implies': Implies(p, q),
        'Equivalent': Equivalent(p, q)
    }
    
    print(f"Tabla de verdad para {operador}:")
    
    # Mostrar tabla de verdad
    tabla = list(truth_table(ejemplos[operador], [p, q]))
    
    # Imprimir la tabla
    for fila in tabla:
        print(fila)
