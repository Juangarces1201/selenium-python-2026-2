Feature: Login Feature
  Scenario: Ingresar con un nombre único a la lobby
    Given El usuario se encuentra en la pagina de login
    When El usuario ingresa con el nombre "Garces"
    Then El nombre del usuario "Garces" aparece en el dashboard

  
  Scenario: Rechazar un nombre de usuario que contiene espacios
    Given El usuario se encuentra en la pagina de login
    When El usuario ingresa con el nombre "Juan Diego"
    Then Se muestra un mensaje de error por nombre invalido
  

