from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

def fill_input(element_id, value):
    input = driver.find_element_by_id(element_id)
    input.send_keys(value)

def fill_select(element_id, value):
    select = Select(driver.find_element_by_id(element_id))
    select.select_by_value(value)

def validate_input(element_id) -> bool:
    ok_class = "form-ok"
    element = driver.find_element_by_id(element_id)
    driver.execute_script("$('#" + element_id + "').focusout()")
    time.sleep(1)
    element_parent = element.find_element_by_xpath('..')
    element_parent_classes = element_parent.get_attribute('class')
    return ok_class in element_parent_classes

def expect_error(expected_error) -> bool:
    alertbox = driver.find_elements_by_class_name(alert_box_class)[0]
    items = alertbox.find_elements_by_tag_name("li")
    for item in items:
        if expected_error == item.text:
            return True
    return False

if __name__ == "__main__":
    url = "http://automationpractice.com/"

    expected_error = "firstname is required"

    test_email = "test12332323@test.com"
    test_surname = "nowak"
    test_password = "password"
    test_state = "1"
    test_birth_day = "1"
    test_birth_month = "1"
    test_birth_year = "1989"
    test_address = "Warszawska 9"
    test_city = "Boston"
    test_postcode = "00000"
    test_mobile = "507567483"
    test_alias = "My address"

    sign_in_href_text = "Sign in"
    create_account_input_id = "email_create"
    create_account_button_id = "SubmitCreate"
    register_account_button_id = "submitAccount"
    male_gender_element_for = "id_gender1"
    firstname_input_id = "customer_firstname"
    surname_input_id = "customer_lastname"
    email_input_id = "email"
    password_input_id = "passwd"
    day_select_id = "days"
    month_select_id = "months"
    year_select_id = "years"
    address_address_input_id = "address1"
    address_city_input_id = "city"
    address_postcode_input_id = "postcode"
    address_state_select_id = "id_state"
    address_mobile_id = "phone_mobile"
    address_alias_id = "alias"
    alert_box_class = "alert-danger"

    chrome_options = set_chrome_options()
    driver = webdriver.Chrome(options=chrome_options)
    # poczatek testu
    driver.get(url)

    # 1. Kliknij "Sign in"
    driver.find_element_by_link_text(sign_in_href_text).click()
    time.sleep(3)

    # 2. Wpisz e-mail
    fill_input(create_account_input_id, test_email)
    time.sleep(1)

    # 3. Kliknij przycisk "Create account"
    driver.find_element_by_id(create_account_button_id).click()
    time.sleep(8)

    # 4. Wybierz płeć
    driver.find_element_by_xpath('//label[@for="' + male_gender_element_for + '"]').click()
    time.sleep(1)

    # 5. Wpisz nazwisko
    fill_input(surname_input_id, test_surname)
    time.sleep(1)

    # 6. Sprawdź poprawność e-maila
    assert validate_input(email_input_id) == True

    # 7. Wpisz hasło
    fill_input(password_input_id, test_password)
    time.sleep(1)

    # 8. Wybierz datę urodzenia
    fill_select(day_select_id, test_birth_day)
    fill_select(month_select_id, test_birth_month)
    fill_select(year_select_id, test_birth_year)
    time.sleep(1)

    # 9. Sprawdź pole "First name"
    assert validate_input(firstname_input_id) == False

    # 10. Sprawdź pole "Last name"
    assert validate_input(surname_input_id) == True

    # 11. Wpisz adres
    fill_input(address_address_input_id, test_address)
    time.sleep(1)

    # 12. Wpisz miasto
    fill_input(address_city_input_id, test_city)
    time.sleep(1)

    # 13. Wpisz kod pocztowy
    fill_input(address_postcode_input_id, test_postcode)
    time.sleep(1)

    # 14. Wybierz stan
    fill_select(address_state_select_id, test_state)
    time.sleep(1)

    # 15. Wpisz nr telefonu komórkowego
    fill_input(address_mobile_id, test_mobile)
    time.sleep(1)

    # 16. Wpisz alias adresu
    fill_input(address_alias_id, test_alias)
    time.sleep(1)

    # 17. Kliknij register
    driver.find_element_by_id(register_account_button_id).click()
    time.sleep(8)

    # 18. Uzytkownik otrzymuje komunikat "firstname is required" i konto nie zostaje załozone
    assert expect_error(expected_error) == False
    # koniec testu
    print("Test zakonczony powodzeniem")
    driver.close()
