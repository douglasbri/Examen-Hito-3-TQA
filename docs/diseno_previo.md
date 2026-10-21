# Diseño previo a la ejecución

Autor académico: Douglas Brian Aliaga Quisbert.
Docente: REYNEL SANCHEZ CHUQUIMIA.
Ejecución: asistente Codex, por autorización de Douglas, sobre SauceDemo.
La hora de cada ejecución se registrará en America/La_Paz.

| ID | Objetivo | Precondiciones y datos | Pasos | Resultado esperado |
|---|---|---|---|---|
| TC-001 | Acceder con credenciales válidas | Sesión cerrada; standard_user / secret_sauce | Ingresar credenciales; pulsar Login | Catálogo Products visible |
| TC-002 | Rechazar contraseña incorrecta | Sesión cerrada; standard_user / incorrecta_2026 | Ingresar credenciales; pulsar Login | Permanecer en login con aviso de credenciales no coincidentes |
| TC-003 | Agregar un producto al carrito | standard_user autenticado; carrito vacío; Sauce Labs Backpack | Pulsar Add to cart del producto; abrir carrito | Insignia 1, un producto Sauce Labs Backpack, cantidad 1 y precio $29.99 |
| TC-004 | Validar nombres obligatorios antes de continuar | standard_user; mochila en carrito; checkout de datos personales | Dejar First Name, Last Name y Zip/Postal Code vacíos; pulsar Continue | Aviso First Name is required y permanencia en el formulario |
| TC-005 | Completar compra de demostración | standard_user; mochila en carrito; formulario checkout; datos sintéticos Prueba / TQA / 00000 | Completar formulario; Continue; revisar resumen; Finish | Artículo correcto, subtotal $29.99, impuesto $2.40, total $32.39 y confirmación de pedido |

Exploración EX-001: error_user; probar clasificación por precio ascendente. Antes de interactuar se espera orden numérico creciente y ausencia de errores.
Exploración EX-002: repetir cualquier fallo observado en una sesión nueva con idénticos datos para confirmar reproducibilidad.

Ampliación previa a su ejecución EX-003: con error_user y carrito vacío, agregar Sauce Labs Backpack y pulsar Remove desde el catálogo. Se espera eliminar el artículo, vaciar la insignia y restaurar Add to cart. Si falla, repetir en otra sesión y comparar con standard_user.

No hay resultados registrados todavía. Un rechazo de credenciales inválidas o de campos vacíos es PASS si coincide con el resultado esperado.
