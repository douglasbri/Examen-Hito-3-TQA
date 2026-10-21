# Casos de caja negra y ejecución

Se conservan los campos de diseño y ejecución de la plantilla de la materia. El diseño previo está en [diseno_previo.md](diseno_previo.md). Los resultados se registraron después de ejecutar las acciones.

**Resumen:** 5 ejecutados, 5 PASS, 0 FAIL, 0 BLOCKED y 0 NOT RUN. Las exploraciones de defectos se contabilizan por separado.

## TC-001 Inicio de sesión con credenciales válidas

### Parte 1 Diseño del caso

- **Prioridad:** Alta. **Tipo:** Funcional positiva.
- **Módulo:** Login. **Ambiente:** Windows; navegador integrado de Codex; sitio público de demostración SauceDemo. Versión del sitio y del navegador no expuesta en la interfaz consultada.
- **Objetivo:** Verificar que un usuario habilitado accede al catálogo.
- **Estado inicial:** Abrir https://www.saucedemo.com/ sin una sesión activa.
- **Usuario y permisos:** standard_user, usuario de demostración habilitado
- **Configuración:** Conexión a Internet; campos de login vacíos.
- **Datos y valores:** Username: standard_user. Password: secret_sauce.
- **Origen:** Credenciales públicas indicadas en la pantalla de SauceDemo.
- **Observación de datos:** La contraseña pertenece al sitio de demostración.

| Paso | Acción | Dato | Resultado esperado | Resultado observado al ejecutar | Estado |
|---|---|---|---|---|---|
| 1 | Abrir la página de login. | https://www.saucedemo.com/ | Mostrar Username, Password y Login. | Formulario de acceso visible. | PASS |
| 2 | Ingresar las credenciales válidas. | standard_user / secret_sauce | Campos completos y contraseña enmascarada. | Se ingresaron los datos indicados. | PASS |
| 3 | Pulsar Login. | Credenciales completas | Abrir el catálogo Products. | Abrió /inventory.html con Products y seis productos en el estado accesible de la página. | PASS |

**Resultado esperado final:** Acceso al catálogo Products sin mensaje de error.

### Parte 2 Ejecución

- **Ejecutado por:** Codex, asistente de Douglas Brian Aliaga Quisbert, por autorización del estudiante.
- **Fecha y hora de captura final:** 20/10/2026 21:12:38 (America/La_Paz).
- **Versión:** No expuesta por el sitio.
- **Estado:** **PASS**.
- **Resultado obtenido:** Se accedió al catálogo y se mostraron los productos.
- **Comparación:** coincide con el resultado esperado.
- **Tipo de evidencia:** captura y bitácora de ejecución.
- **Referencia del defecto:** N/A; no hubo desviación en este caso.
- **Observaciones:** El número de productos se comprobó en el estado accesible del catálogo; la captura muestra la parte visible de la página.

- [TC-001_login_valido.png](../evidencias/capturas/TC-001_login_valido.png)


## TC-002 Rechazo de contraseña incorrecta

### Parte 1 Diseño del caso

- **Prioridad:** Alta. **Tipo:** Funcional negativa.
- **Módulo:** Login. **Ambiente:** Windows; navegador integrado de Codex; sitio público de demostración SauceDemo. Versión del sitio y del navegador no expuesta en la interfaz consultada.
- **Objetivo:** Verificar que una contraseña incorrecta no permite acceder.
- **Estado inicial:** Cerrar sesión con Open Menu > Logout y abrir la página de login.
- **Usuario y permisos:** standard_user con contraseña incorrecta
- **Configuración:** Sin sesión activa y formulario de login disponible.
- **Datos y valores:** Username: standard_user. Password: incorrecta_2026.
- **Origen:** Usuario público de SauceDemo y contraseña inválida preparada para esta prueba.
- **Observación de datos:** El mensaje de rechazo es el comportamiento esperado y representa PASS.

| Paso | Acción | Dato | Resultado esperado | Resultado observado al ejecutar | Estado |
|---|---|---|---|---|---|
| 1 | Cerrar la sesión anterior. | Open Menu > Logout | Volver al formulario de login. | Se mostró el formulario sin sesión. | PASS |
| 2 | Ingresar usuario válido y contraseña incorrecta. | standard_user / incorrecta_2026 | Permitir enviar las credenciales para validarlas. | Se ingresaron los datos del caso. | PASS |
| 3 | Pulsar Login. | Credenciales inválidas | Permanecer en login y avisar que las credenciales no coinciden. | Permaneció en / y mostró Epic sadface: Username and password do not match any user in this service. | PASS |

**Resultado esperado final:** Denegar el acceso con un mensaje de credenciales incorrectas.

### Parte 2 Ejecución

- **Ejecutado por:** Codex, asistente de Douglas Brian Aliaga Quisbert, por autorización del estudiante.
- **Fecha y hora de captura final:** 20/10/2026 21:12:51 (America/La_Paz).
- **Versión:** No expuesta por el sitio.
- **Estado:** **PASS**.
- **Resultado obtenido:** Acceso denegado y mensaje esperado visible.
- **Comparación:** coincide con el resultado esperado.
- **Tipo de evidencia:** captura y bitácora de ejecución.
- **Referencia del defecto:** N/A; no hubo desviación en este caso.
- **Observaciones:** No se registra un bug porque el rechazo coincide con el resultado esperado.

- [TC-002_login_invalido.png](../evidencias/capturas/TC-002_login_invalido.png)


## TC-003 Agregar una mochila al carrito

### Parte 1 Diseño del caso

- **Prioridad:** Alta. **Tipo:** Funcional positiva.
- **Módulo:** Catálogo y carrito. **Ambiente:** Windows; navegador integrado de Codex; sitio público de demostración SauceDemo. Versión del sitio y del navegador no expuesta en la interfaz consultada.
- **Objetivo:** Verificar que agregar un producto actualiza la insignia y el contenido del carrito.
- **Estado inicial:** Iniciar sesión con standard_user y disponer de carrito vacío.
- **Usuario y permisos:** standard_user autenticado
- **Configuración:** Catálogo Products disponible; Sauce Labs Backpack sin agregar.
- **Datos y valores:** Producto: Sauce Labs Backpack. Cantidad: 1. Precio visible: USD 29.99.
- **Origen:** Producto y precio del catálogo observado antes de agregarlo.
- **Observación de datos:** El caso utiliza un único producto para comprobar identidad, cantidad y precio.

| Paso | Acción | Dato | Resultado esperado | Resultado observado al ejecutar | Estado |
|---|---|---|---|---|---|
| 1 | Pulsar Add to cart de Sauce Labs Backpack. | Sauce Labs Backpack | Cambiar a Remove y mostrar una insignia 1. | El botón cambió a Remove y Cart indicó 1 item. | PASS |
| 2 | Abrir el carrito. | Botón Cart | Mostrar el producto añadido. | Abrió /cart.html con Sauce Labs Backpack. | PASS |
| 3 | Revisar cantidad, precio e insignia. | 1 unidad; USD 29.99 | Un único producto, cantidad 1, precio 29.99 e insignia 1. | Se observaron los cuatro valores esperados. | PASS |

**Resultado esperado final:** El carrito conserva exactamente una mochila y sus datos correctos.

### Parte 2 Ejecución

- **Ejecutado por:** Codex, asistente de Douglas Brian Aliaga Quisbert, por autorización del estudiante.
- **Fecha y hora de captura final:** 20/10/2026 21:13:02 (America/La_Paz).
- **Versión:** No expuesta por el sitio.
- **Estado:** **PASS**.
- **Resultado obtenido:** Mochila, cantidad 1, precio USD 29.99 e insignia 1 correctos.
- **Comparación:** coincide con el resultado esperado.
- **Tipo de evidencia:** captura y bitácora de ejecución.
- **Referencia del defecto:** N/A; no hubo desviación en este caso.
- **Observaciones:** El carrito preparado se utilizó como precondición del siguiente caso; los pasos permiten recrearlo de forma independiente.

- [TC-003_carrito.png](../evidencias/capturas/TC-003_carrito.png)


## TC-004 Validación del nombre obligatorio en checkout

### Parte 1 Diseño del caso

- **Prioridad:** Alta. **Tipo:** Funcional negativa.
- **Módulo:** Checkout. **Ambiente:** Windows; navegador integrado de Codex; sitio público de demostración SauceDemo. Versión del sitio y del navegador no expuesta en la interfaz consultada.
- **Objetivo:** Comprobar que el checkout no avanza cuando falta First Name.
- **Estado inicial:** standard_user autenticado, mochila en carrito y Checkout abierto.
- **Usuario y permisos:** standard_user autenticado
- **Configuración:** Formulario Checkout: Your Information; todos los campos vacíos.
- **Datos y valores:** First Name: vacío. Last Name: vacío. Zip/Postal Code: vacío.
- **Origen:** Valores vacíos preparados para probar la primera validación obligatoria.
- **Observación de datos:** Este caso comprueba First Name; no afirma cubrir todas las combinaciones de campos vacíos.

| Paso | Acción | Dato | Resultado esperado | Resultado observado al ejecutar | Estado |
|---|---|---|---|---|---|
| 1 | Abrir Checkout desde el carrito. | Una mochila en carrito | Mostrar Checkout: Your Information. | Abrió /checkout-step-one.html. | PASS |
| 2 | Conservar los tres campos vacíos. | Sin nombre, apellido ni código postal | Formulario listo para comprobar el campo obligatorio. | Los tres campos permanecieron vacíos. | PASS |
| 3 | Pulsar Continue. | Formulario vacío | Mostrar Error: First Name is required y no avanzar. | Mostró exactamente el mensaje esperado y permaneció en checkout-step-one.html. | PASS |

**Resultado esperado final:** Mostrar el aviso del nombre obligatorio sin avanzar al resumen.

### Parte 2 Ejecución

- **Ejecutado por:** Codex, asistente de Douglas Brian Aliaga Quisbert, por autorización del estudiante.
- **Fecha y hora de captura final:** 20/10/2026 21:13:16 (America/La_Paz).
- **Versión:** No expuesta por el sitio.
- **Estado:** **PASS**.
- **Resultado obtenido:** El formulario rechazó el avance con Error: First Name is required.
- **Comparación:** coincide con el resultado esperado.
- **Tipo de evidencia:** captura y bitácora de ejecución.
- **Referencia del defecto:** N/A; no hubo desviación en este caso.
- **Observaciones:** El aviso observado es una validación correcta y representa PASS.

- [TC-004_nombre_obligatorio.png](../evidencias/capturas/TC-004_nombre_obligatorio.png)


## TC-005 Completar una compra de demostración

### Parte 1 Diseño del caso

- **Prioridad:** Alta. **Tipo:** Funcional positiva.
- **Módulo:** Checkout. **Ambiente:** Windows; navegador integrado de Codex; sitio público de demostración SauceDemo. Versión del sitio y del navegador no expuesta en la interfaz consultada.
- **Objetivo:** Comprobar el resumen, el cálculo monetario y la confirmación del pedido.
- **Estado inicial:** standard_user autenticado; una mochila en carrito; formulario de checkout abierto.
- **Usuario y permisos:** standard_user autenticado
- **Configuración:** Sauce Labs Backpack, una unidad. No hay otros artículos.
- **Datos y valores:** First Name: Prueba. Last Name: TQA. Zip/Postal Code: 00000. Subtotal esperado: USD 29.99. Impuesto esperado: USD 2.40. Total esperado: USD 32.39.
- **Origen:** Datos personales sintéticos preparados para el caso; precio observado en catálogo.
- **Observación de datos:** Solo se realiza una compra del sitio de demostración; no se ingresan datos de pago reales.

| Paso | Acción | Dato | Resultado esperado | Resultado observado al ejecutar | Estado |
|---|---|---|---|---|---|
| 1 | Completar el formulario. | Prueba / TQA / 00000 | Aceptar los tres valores. | Los campos recibieron los valores indicados. | PASS |
| 2 | Pulsar Continue. | Formulario completo | Mostrar Checkout: Overview con la mochila. | Se mostró el resumen con una mochila. | PASS |
| 3 | Verificar los importes. | 29.99 + 2.40 = 32.39 | Subtotal USD 29.99, impuesto USD 2.40 y total USD 32.39. | Los tres importes coincidieron. | PASS |
| 4 | Pulsar Finish. | Resumen comprobado | Mostrar Checkout: Complete! y Thank you for your order!; carrito vacío. | Se mostraron ambos textos y Cart quedó vacío. | PASS |

**Resultado esperado final:** Pedido de demostración confirmado y valores monetarios correctos.

### Parte 2 Ejecución

- **Ejecutado por:** Codex, asistente de Douglas Brian Aliaga Quisbert, por autorización del estudiante.
- **Fecha y hora de captura final:** 20/10/2026 21:13:25 (America/La_Paz).
- **Versión:** No expuesta por el sitio.
- **Estado:** **PASS**.
- **Resultado obtenido:** Compra confirmada con total USD 32.39 y carrito vacío.
- **Comparación:** coincide con el resultado esperado.
- **Tipo de evidencia:** captura y bitácora de ejecución.
- **Referencia del defecto:** N/A; no hubo desviación en este caso.
- **Observaciones:** Se repitió el flujo para capturar los importes situados más abajo en la pantalla. La captura de importes corresponde a esa repetición; ambos pedidos de demostración finalizaron correctamente.

- [TC-005_resumen_compra.png](../evidencias/capturas/TC-005_resumen_compra.png)
- [TC-005_compra_completa.png](../evidencias/capturas/TC-005_compra_completa.png)
- [TC-005_importes_verificados.png](../evidencias/capturas/TC-005_importes_verificados.png)
- [TC-005_confirmacion_repeticion.png](../evidencias/capturas/TC-005_confirmacion_repeticion.png)
