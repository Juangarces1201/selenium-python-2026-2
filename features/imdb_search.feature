
Feature: Buscar peliculas en IMDb

  Scenario: Buscar Pulp Fiction y verificar su calificacion
    Given El usuario se encuentra en IMDb
    When El usuario busca la pelicula "Pulp Fiction"
    And El usuario abre el primer resultado
    Then Se muestra la calificacion de la pelicula
