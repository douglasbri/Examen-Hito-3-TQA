# Examen Hito 3 de Testing y Quality Assurance

**Estudiante:** Douglas Brian Aliaga Quisbert.  
**Docente:** REYNEL SANCHEZ CHUQUIMIA.  
**Aplicación:** [SauceDemo](https://www.saucedemo.com/).  
**Fecha de pruebas:** 20 de octubre de 2026, America/La_Paz.

Se diseñaron y ejecutaron cinco casos funcionales: **5 PASS, 0 FAIL, 0 BLOCKED y 0 NOT RUN**. En exploraciones adicionales con error_user se encontraron dos defectos reproducibles, confirmados en dos sesiones cada uno y comparados con standard_user. Los defectos de exploración no se suman al denominador de los cinco casos principales.

Las acciones del navegador y del código Python las ejecutó Codex por autorización de Douglas. Los datos del checkout son sintéticos y las credenciales corresponden a las cuentas públicas de demostración. Los resultados son observaciones de esa ejecución, no una certificación de todo el sitio ni una declaración de que el estudiante realizó manualmente cada acción.

## Contenido

- [Informe consolidado en PDF](entregable/informe_hito3.pdf).
- [Diseño y ejecución de caja negra](docs/casos_caja_negra.md), con los campos de la plantilla de la materia.
- [Análisis de caja blanca](docs/analisis_caja_blanca.md): 3 casos, 83.33% de decisiones; ajuste de un cuarto caso para 100%.
- [Gherkin](docs/escenarios_gherkin.md) y [archivo feature](docs/login.feature).
- [Defectos reproducibles](bugs/bugs_encontrados.md).
- [Capturas](evidencias/capturas/) y [bitácora](evidencias/registro_ejecucion.json).
- [Código original](src/validar_compra.py) y [comprobación ejecutable](src/verificar_caja_blanca.py).
- [Guía de publicación, acceso del docente y tablero](gestion/guia_publicacion.md).

## Reproducir caja blanca

```powershell
python src/verificar_caja_blanca.py
```

Solo utiliza la biblioteca estándar de Python. La ejecución genera evidencias/caja_blanca_ejecucion.json. Los escenarios Gherkin describen el comportamiento y no constituyen por sí mismos una suite automatizada.

## Estado de GitHub

Los archivos están preparados para el repositorio de destino. Las pruebas no publicaron cambios, no crearon Issues ni un Project y no enviaron la invitación al docente. Los textos y estados propuestos se incluyen en gestion/ para completar esas actividades desde una sesión autorizada en GitHub.
