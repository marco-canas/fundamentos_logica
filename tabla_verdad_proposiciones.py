import pandas as pd
import itertools

def tabla_verdad(proposicion='p y q -> r'):
    # Generar todas las combinaciones posibles de valores de verdad
    valores = [True, False]
    combinaciones = list(itertools.product(valores, repeat=3))
    
    # Crear DataFrame con las combinaciones
    df = pd.DataFrame(combinaciones, columns=['p', 'q', 'r'])
    
    # Calcular la proposición compuesta
    if proposicion == 'p y q -> r':
        # p ∧ q → r
        df['p y q'] = df['p'] & df['q']
        df['p y q -> r'] = ~df['p y q'] | df['r']
    # Aquí se pueden agregar más casos para otras proposiciones
    
    return df

# Ejemplo de uso
if __name__ == '__main__':
    # Mostrar tabla con estilo para el video
    df = tabla_verdad()
    # Resaltar solo las filas donde la proposición es falsa
    def highlight_false(val):
        color = '#ffcccc' if val == False else ''
        return f'background-color: {color}'
    
    styled_df = df.style.applymap(highlight_false, subset=['p y q -> r'])
    print(styled_df)
