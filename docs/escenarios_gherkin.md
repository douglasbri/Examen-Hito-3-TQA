# Escenarios Gherkin

Actividad adicional: un escenario exitoso y otro de error, relacionados con TC-001 y TC-002. Son especificaciones BDD; no se presenta una automatización Cucumber ni se afirma haber ejecutado un archivo feature. Los comportamientos correspondientes sí se comprobaron en el navegador.

```gherkin
Feature: Inicio de sesión en SauceDemo
  Como usuario del sitio de demostración
  Quiero validar mis credenciales
  Para acceder al catálogo solo cuando sean correctas

  Scenario: Acceso con credenciales válidas
    Given que estoy en https://www.saucedemo.com/ sin una sesión activa
    When ingreso el usuario "standard_user" y la contraseña "secret_sauce"
    And pulso el botón "Login"
    Then accedo a la página "/inventory.html"
    And veo el título "Products"

  Scenario: Rechazo de contraseña incorrecta
    Given que estoy en https://www.saucedemo.com/ sin una sesión activa
    When ingreso el usuario "standard_user" y la contraseña "incorrecta_2026"
    And pulso el botón "Login"
    Then permanezco en la página de inicio de sesión
    And veo el mensaje "Epic sadface: Username and password do not match any user in this service"
```
