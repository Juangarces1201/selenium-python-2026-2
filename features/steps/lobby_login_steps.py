from behave import given, when, then
from selenium import webdriver
from pages.lobby_login_page import LobbyLoginPage
from pages.lobby_dashboard_page import LobbyDashboardPage
from selenium.webdriver.common.by import By

@given('El usuario se encuentra en la pagina de login')
def step_given_user_on_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://lobby-global.vercel.app/")
    context.lobby_login_page = LobbyLoginPage(context.driver)

@when('El usuario ingresa con el nombre "{username}"')
def step_when_user_logs_in(context,username):
    context.lobby_login_page.login(username)
    context.lobby_dashboard_page = LobbyDashboardPage(context.driver)

@then('El nombre del usuario "{username}" aparece en el dashboard')
def step_then_user_login(context,username):
    assert context.lobby_dashboard_page.find_username(username) is True


@then('Se muestra un mensaje de error por nombre invalido')
def step_then_invalid_username(context):
    error_message = context.lobby_login_page.get_error_message()

    assert error_message == (
        "Usa entre 3 y 20 caracteres: letras sin tildes, "
        "números, guion o guion bajo."
    ), f"Mensaje de error inesperado: {error_message}"

    