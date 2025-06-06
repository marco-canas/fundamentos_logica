"""
Script para generar la tabla de verdad de la disyunción lógica (OR)

Este programa muestra todas las combinaciones posibles de valores booleanos
(True, False) y el resultado de aplicar el operador OR entre ellos.

La salida se muestra en formato de tabla alineada para mejor legibilidad.
"""

def generar_tabla_verdad():
    """
    Genera e imprime la tabla de verdad para la disyunción lógica (OR)
    
    Returns:
        None: Solo imprime la tabla en la consola
    """
    # Encabezado de la tabla
    print("|  p  |  q  | p OR q |")
    print("|-----|-----|--------|")
    
    # Generar todas las combinaciones posibles de True/False
    for p in [True, False]:
        for q in [True, False]:
            # Calcular el resultado de la disyunción
            resultado = p or q
            # Imprimir fila con formato alineado
            print(f"| {str(p):^4} | {str(q):^4} | {str(resultado):^7} |")

if __name__ == "__main__":
    print("Tabla de verdad de la disyunción lógica (OR)\n")
    generar_tabla_verdad()
    print("\nLeyenda:")
    print("- p: Primer operando")
    print("- q: Segundo operando")
    print("- p OR q: Resultado de la disyunción lógica")
