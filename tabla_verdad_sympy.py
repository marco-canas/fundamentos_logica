import pandas as pd
import itertools
from sympy import symbols, And, Or, Not, Implies, Equivalent
from sympy.logic.boolalg import Boolean

def tabla_verdad_sympy(expresion):
    """
    Genera tabla de verdad para una expresión lógica de SymPy
    
    Args:
        expresion: Expresión lógica de SymPy (ej: Implies(And(p, q), r))
    
    Returns:
        DataFrame con todas las combinaciones y resultado de la expresión
    """
    # Obtener variables ordenadas alfabéticamente
    variables = sorted(list(expresion.free_symbols), key=lambda x: str(x))
    n = len(variables)
    
    # Generar todas las combinaciones de valores de verdad
    combinaciones = list(itertools.product([True, False], repeat=n))
    
    # Crear DataFrame
    df = pd.DataFrame(combinaciones, columns=[str(v) for v in variables])
    
    # Evaluar expresión para cada combinación
    resultados = []
    for vals in combinaciones:
        sustitucion = dict(zip(variables, vals))
        resultados.append(bool(expresion.subs(sustitucion)))
    
    df['Resultado'] = resultados
    return df

def mostrar_tabla(expresion):
    """
    Muestra la tabla de verdad con resaltado para valores False
    """
    df = tabla_verdad_sympy(expresion)
    
    def highlight_false(val):
        return 'background-color: #ffcccc' if val == False else ''
    
    styled = df.style.map(highlight_false, subset=['Resultado'])
    return styled

# Ejemplo de uso
if __name__ == '__main__':
    # Definir variables
    p, q, r = symbols('p q r')
    
    # Crear expresión: (p ∧ q) → r
    expresion = Implies(And(p, q), r)
    
    # Mostrar tabla
    print(mostrar_tabla(expresion))
