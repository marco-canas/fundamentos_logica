from sympy import symbols, Equivalent

def verificar_equivalencia(propo1, propo2):
    """
    Verifica si dos proposiciones lógicas son equivalentes.

    Args:
        propo1: Una proposición lógica en formato sympy. ~ para negar >> para implicación, & para conjunción, | para disyunción.
        propo2: Otra proposición lógica en formato sympy.

    Returns:
        bool: True si las proposiciones son equivalentes, False en caso contrario.
    """
    return bool(Equivalent(propo1, propo2))

# Ejemplo de uso
if __name__ == "__main__":
    # Definir variables lógicas
    p, q = symbols('p q')
    
    # Proposiciones de ejemplo
    proposicion1 = ~((p >> q) & (q >> p))
    proposicion2 = (p | q) & ~(p & q)
    
    # Verificar equivalencia
    resultado = verificar_equivalencia(proposicion1, proposicion2)
    print(f"¿Son equivalentes? {resultado}")