# Publicación y acceso del docente

Repositorio de destino: https://github.com/douglasbri/Examen-Hito-3-TQA

Se comprobó en el navegador que el repositorio era público y estaba vacío al iniciar la preparación. La sesión del navegador no estaba iniciada en GitHub. No se publicó contenido, no se enviaron invitaciones y no se crearon Issues ni Projects durante las pruebas.

## Usar Git desde terminal

La carpeta incluye los archivos de la entrega. Abrir una terminal dentro de esta carpeta. Si todavía no tiene repositorio local, ejecutar:

```powershell
git init -b main
git config user.name "Douglas Brian Aliaga Quisbert"
git config user.email "TU_CORREO_ASOCIADO_A_GITHUB"
git remote add origin https://github.com/douglasbri/Examen-Hito-3-TQA.git
git add README.md docs src evidencias bugs entregable gestion .gitignore
git commit -m "Documenta pruebas SauceDemo, defectos y cobertura de caja blanca"
git push -u origin main
```

Reemplazar el marcador del correo por el propio correo asociado a GitHub o por el correo noreply que GitHub muestre en Settings > Emails. No usar el correo del docente para los commits. Si origin ya existe, comprobarlo con `git remote -v` antes de agregarlo de nuevo. Si el repositorio ya tiene historial remoto, clonarlo y copiar los archivos de la entrega sobre esa copia, sin forzar la subida ni sobrescribir trabajo existente. Los comandos son una guía: no se afirma haber ejecutado la publicación.

## Invitar al docente

En el repositorio, abrir Settings > Collaborators > Add people. Buscar `doc.reynel.sanchez.ch@unifranz.edu.bo`, comprobar la cuenta y enviar la invitación. El docente REYNEL SANCHEZ CHUQUIMIA debe aceptarla. En un repositorio personal el colaborador tiene capacidad de escritura; el repositorio público ya puede consultarse mediante el enlace.

## Issues y Project

Usar gestion/issues_propuestos.md como texto base. Crear un Issue por tarea y por defecto, enlazar sus evidencias y añadirlos a un Project con las columnas To Do, In Progress, In Review y Done. gestion/tablero_propuesto.csv contiene los estados locales propuestos, sin afirmar que el tablero remoto ya exista. Los bugs siguen abiertos hasta que se corrijan y se verifique la corrección.

## Revisión final

Comprobar que el PDF se abre, que los enlaces relativos del README muestran sus archivos, que las capturas se ven en GitHub, que los Issues y el Project existen realmente y que la invitación está aceptada. Entregar el enlace del repositorio y el PDF según las indicaciones de Moodle.
