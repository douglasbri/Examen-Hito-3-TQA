# Análisis de caja blanca

## Código y criterio elegido

Se analiza la función del examen, conservada sin cambios en [validar_compra.py](../src/validar_compra.py). El criterio principal es **cobertura de decisiones**: cada `if` debe tomar los resultados verdadero y falso al menos una vez. No se exige cubrir todas las combinaciones posibles de entradas.

```python
def validar_compra(edad, cuenta_activa, saldo, monto):
    if edad < 18:
        return "Compra no permitida: edad"
    if not cuenta_activa:
        return "Compra no permitida: cuenta"
    if saldo >= monto and monto > 0:
        return "Compra aprobada"
    return "Compra rechazada"
```

## Decisiones y condiciones simples

| Decisión | Expresión | Condiciones simples |
|---|---|---|
| D1 | edad < 18 | C1: edad < 18 |
| D2 | not cuenta_activa | C2: not cuenta_activa |
| D3 | saldo >= monto and monto > 0 | C3: saldo >= monto; C4: monto > 0 |

Son 3 decisiones y 4 condiciones simples. La función termina anticipadamente en los retornos de D1 y D2. Python evalúa `and` con cortocircuito: si C3 es falsa, C4 no se evalúa.

## Los tres casos solicitados

| ID | edad | cuenta_activa | saldo | monto | Resultado esperado | D1 | D2 | D3 |
|---|---:|---|---:|---:|---|---|---|---|
| CB-001 | 17 | True | 100 | 50 | Compra no permitida: edad | V | NE | NE |
| CB-002 | 18 | False | 100 | 50 | Compra no permitida: cuenta | F | V | NE |
| CB-003 | 18 | True | 100 | 100 | Compra aprobada | F | F | V |

NE significa no evaluada por retorno anticipado, no falso. CB-001 está justo por debajo de 18; CB-002 y CB-003 usan el límite 18. CB-003 también comprueba saldo igual al monto.

Los tres casos cubren D1 verdadero y falso, D2 verdadero y falso y D3 verdadero: **5 de 6 resultados, 83.33% de cobertura de decisiones**. No se declara cobertura completa con tres casos.

## Mínimo y ajuste necesario

Hay cuatro trayectorias terminales mutuamente excluyentes: rechazo por edad, rechazo por cuenta, aprobación y rechazo final. Cada llamada solo puede recorrer una. Para cubrir D1 verdadero, D2 verdadero, D3 verdadero y D3 falso se requieren **al menos 4 casos**. Los casos anteriores más CB-004 alcanzan ese límite, por lo que cuatro es el mínimo para este código y criterio.

| Ajuste | edad | cuenta_activa | saldo | monto | Resultado esperado | D1 | D2 | D3 |
|---|---:|---|---:|---:|---|---|---|---|
| CB-004 | 18 | True | 50 | 100 | Compra rechazada | F | F | F |

Con CB-004 se cubren **6 de 6 resultados, 100% de decisiones**. La ejecución de los tres casos y del ajuste se comprobó con la función original y un rastreo de sus líneas. Véase [caja_blanca_ejecucion.json](../evidencias/caja_blanca_ejecucion.json).

## Diferencia con cobertura de condiciones

En CB-004, C3 es falsa y C4 no se evalúa. Aunque se alcanza el 100% de decisiones, estos cuatro casos aún no demuestran que C4 pueda evaluarse como falsa.

Una ampliación CB-005 con `(18, True, 0, 0)` devuelve `Compra rechazada`: C3 es verdadera y C4 es falsa. Con los cinco casos se observan verdadero y falso para cada condición simple evaluada. Bajo esta definición y respetando el cortocircuito, cinco es el mínimo para 100% de condiciones: dos casos para los retornos tempranos y tres para las combinaciones evaluables de C3 y C4 necesarias.

CB-005 se aporta como comprobación adicional. No modifica el criterio principal elegido ni el requisito de presentar tres casos y explicar su ajuste.

## Ejecución reproducible

```powershell
python src/verificar_caja_blanca.py
```

La prueba compara los resultados reales con los esperados y registra las decisiones recorridas. Los cinco casos Python se ejecutaron correctamente. El alcance se limita a las entradas seleccionadas; no se afirma validar tipos de datos ni todos los valores posibles.
