

# [Plan de la secuencia de proyectos ABPP para fundamentos de Lógica (2025-2)](https://www.youtube.com/watch?v=5iFvjAP2ilE)  

Propongo una serie de **situaciones problemáticas** que se pueden articular con los cuatro proyectos del curso de **Fundamentos de Lógica**, y que hacen evidente la utilidad de los **operadores lógicos** en el **control de un bombillo con uno o dos suiches**.

---

# Situaciones problemáticas de control de un bombillo

# 1. Negación (¬p)

**Situación:**
En una casa se quiere que el bombillo **esté encendido solamente cuando el interruptor esté apagado**.

* Si el interruptor está en posición **0 (apagado)**, el bombillo debe **encenderse**.
* Si el interruptor está en posición **1 (encendido)**, el bombillo debe **apagarse**.

**Interpretación lógica:**
Bombillo = ¬S (no del estado del interruptor).
**Aplicación:** se relaciona con el comportamiento de un **inversor NOT** en lógica digital.

---

# 2. Conjunción (p ∧ q)

**Situación:**
Dos compañeros de cuarto desean que el bombillo del estudio **solo se encienda si ambos suiches están encendidos**.

* Si los dos suiches (S1 y S2) están en posición **1**, el bombillo enciende.
* En cualquier otro caso, se apaga.

**Interpretación lógica:**
Bombillo = S1 ∧ S2.
**Aplicación:** corresponde a una conexión de **serie** en circuitos eléctricos o a una compuerta **AND** en lógica digital.

---

## 🔹 3. Disyunción inclusiva (p ∨ q)

**Situación:**
En un corredor, se coloca un bombillo que puede encenderse desde **dos extremos diferentes**. Se desea que el bombillo **se encienda si al menos uno de los suiches está encendido**.

* Si cualquiera de S1 o S2 es 1, el bombillo enciende.

**Interpretación lógica:**
Bombillo = S1 ∨ S2.
**Aplicación:** conexión en **paralelo** en electricidad o compuerta **OR** en lógica digital.

---

## 🔹 4. Disyunción exclusiva (p ⊕ q)

**Situación:**
En un dormitorio, se necesita que el bombillo pueda encenderse desde la puerta o desde la cama, pero que **cambiar cualquiera de los dos suiches altere el estado del bombillo**.

* Si ambos están en el mismo estado (0,0 o 1,1), el bombillo está apagado.
* Si están en estados diferentes (0,1 o 1,0), el bombillo enciende.

**Interpretación lógica:**
Bombillo = S1 ⊕ S2.
**Aplicación:** circuito de **conmutadores de escalera** o compuerta **XOR**.

---

# 5. Implicación (p → q)

**Situación:**
En un taller, un bombillo de advertencia debe encenderse **solo si se acciona el interruptor principal, pero no debe encenderse si este está apagado**.

* Si el interruptor principal (S1) está encendido, el bombillo depende del estado del interruptor secundario (S2).
* Si S1 = 0, el bombillo nunca enciende.

**Interpretación lógica:**
Bombillo = S1 → S2.
**Aplicación:** sistema de **seguridad**, donde un control maestro habilita o no el encendido.

---

## 🔹 6. Equivalencia (p ↔ q)

**Situación:**
Un bombillo de pasillo debe encenderse **solo cuando ambos interruptores estén en la misma posición** (ambos apagados o ambos encendidos).

* Si S1 = S2, el bombillo enciende.
* Si S1 ≠ S2, el bombillo se apaga.

**Interpretación lógica:**
Bombillo = S1 ↔ S2.
**Aplicación:** compuerta **XNOR** o control sincronizado de dos estados.

---

# Secuencia de proyectos por mes

* **Proyecto 1 (Agosto):** los estudiantes, partiendo de una situación problemática real, fabrican maquetas con interruptores y bombillos reales para representar cada caso.
* **Proyecto 2 (Septiembre):** los mismos casos se llevan a esquemas pictóricos de **circuitos eléctricos** (serie, paralelo, conmutadores). Este se realiza con el simulador Crocodile Clips
* **Proyecto 3: (Octubre)** traducción a **compuertas lógicas simbólicas** (AND, OR, NOT, XOR, XNOR, etc.). Este se realiza con el simulador Crocodile Clips
* **Proyecto 4:(Noviembre)** implementación en **GeoGebra o Excel** usando tablas de verdad dinámicas y gráficos de encendido/apagado.

---

# Cómo elegir el proyecto por mes. 

1. El proyecto se realiza induvidual o en parejas.
2. Debe elegir un solo operador lógico por proyecto y no debe haber dos equipos con el mismo operador lógico elegido. Por favor, publicar en https://github.com/marco-canas/fundamentos_logica/discussions/new?category=announcements.

# Compromiso del profesor con todo el grupo para el 18 de Noviembre  


Quedo comprometido a mandarles mañana un [video donde muestre los tres elementos que todos debemos mostrar con cada uno de los proyectos](https://www.youtube.com/watch?v=5iFvjAP2ilE). Los elementos son: 1. Situación real problema, 2. El circuito lógico electrico que la resuelve y 3. La tabla de verdad de la proposición lógica asociada al problema. 
