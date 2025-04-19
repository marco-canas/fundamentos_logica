"""
Módulo para verificar equivalencia lógica entre proposiciones en SymPy

Este archivo proporciona una función para comparar dos proposiciones lógicas
y determinar si son equivalentes, mostrando su tabla de verdad.

Autor: Marco Julio Cañas Campillo
Fecha: 19 de Abril de 2025
"""

from sympy import symbols, simplify_logic
from sympy.logic.boolalg import truth_table, And, Or, Not, Implies, Equivalent

def equivalencia_logica(propo_1_sympy, propo_2_sympy):
    """
    Determina la equivalencia lógica entre dos proposiciones compuestas.
    Muestra la tabla de verdad de p ↔ q e indica si son equivalentes.

    Args:
        propo_1_sympy: Expresión lógica 1 en notación SymPy funcional Or(p,q)
        propo_2_sympy: Expresión lógica 2 en notación SymPy

    Returns:
        None (imprime resultados en consola)
    
    Ejemplo de uso:
        >>> p, q = symbols('p q')
        >>> prop1 = Implies(p, q)
        >>> prop2 = Or(Not(p), q)
        >>> equivalencia_logica(prop1, prop2)
    """
    # Definir símbolos básicos
    p, q = symbols('p q')
    
    # Crear expresión de equivalencia
    equivalencia = Equivalent(propo_1_sympy, propo_2_sympy)
    
    # Simplificar para verificar equivalencia
    simplificada = simplify_logic(equivalencia)
    
    # Generar y mostrar tabla de verdad
    print("\n" + "="*50)
    print("Análisis de Equivalencia Lógica")
    print("="*50)
    
    print(f"\nProposición 1: {propo_1_sympy}")
    print(f"Proposición 2: {propo_2_sympy}\n")
    
    print(f"Tabla de Verdad para la equivalencia ({propo_1_sympy} ↔ {propo_2_sympy}):")
    print("-"*70)
    print("|  p  |  q  | Proposición 1 | Proposición 2 | Equivalente |")
    print("-"*70)
    
    # Generar todas las combinaciones posibles de valores de verdad
    for p_val in [True, False]:
        for q_val in [True, False]:
            # Evaluar las proposiciones con los valores actuales
            val_prop1 = propo_1_sympy.subs({p: p_val, q: q_val})
            val_prop2 = propo_2_sympy.subs({p: p_val, q: q_val})
            result = equivalencia.subs({p: p_val, q: q_val})
            
            print(f"| {str(p_val):^4}| {str(q_val):^4}| {str(val_prop1):^13}| {str(val_prop2):^13}| {str(result):^11}|")
    
    print("-"*70 + "\n")
    
    # Mostrar conclusión
    if simplificada:
        print("RESULTADO: Las proposiciones SON LÓGICAMENTE EQUIVALENTES")
        print(f"Demostración: {equivalencia} ≡ {simplificada}")
    else:
        print("RESULTADO: Las proposiciones NO SON EQUIVALENTES")

if __name__ == "__main__":
    # Ejemplo demostrativo al ejecutar el archivo directamente
    print("DEMOSTRACIÓN AUTOMÁTICA DE EQUIVALENCIA LÓGICA")
    print("Ejemplo: p → q ≡ ¬p ∨ q (Ley del condicional)\n")
    
    p, q = symbols('p q')
    prop1 = Implies(p, q)
    prop2 = Or(Not(p), q)
    
    equivalencia_logica(prop1, prop2)