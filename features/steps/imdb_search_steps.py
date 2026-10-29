
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.imdb_search_page import IMDbSearchPage
from pages.imdb_movie_page import IMDbMoviePage


@given('El usuario se encuentra en IMDb')
def step_open_imdb(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com/")

    WebDriverWait(context.driver, 30).until(
        lambda driver: driver.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    print("URL:", context.driver.current_url)
    print("Título:", context.driver.title)
    print("Contenido:", context.driver.find_element("tag name", "body").text[:500])

    context.imdb_search_page = IMDbSearchPage(context.driver)


@when('El usuario busca la pelicula "{title}"')
def step_search_movie(context, title):
    context.imdb_search_page.search(title)


@when('El usuario abre el primer resultado')
def step_open_first_result(context):
    context.imdb_search_page.open_first_result()
    context.imdb_movie_page = IMDbMoviePage(context.driver)


@then('Se muestra la calificacion de la pelicula')
def step_verify_rating(context):
    rating = context.imdb_movie_page.get_rating()
    assert rating, "No se encontró la calificación de la película"
    print(f"Calificación de IMDb: {rating}")


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
