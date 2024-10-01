from selene import browser

def test_form():
    #browser.element("#firstName").hover()
    browser.open('/')
    browser.element('#firstName')
    browser.element("#firstName").click()
    browser.element("#firstName").type("Иван")
    browser.element('#lastName').click()
    browser.element('#lastName').type("Иванов")
    # userEmail
    # gender-radio-2
    # userNumber

    browser.element("#dateOfBirthInput").click()
    browser.element("#dateOfBirth > div.react-datepicker__tab-loop > div.react-datepicker-popper > "
                    "div > div > div.react-datepicker__month-container > div.react-datepicker__header > "
                    "div.react-datepicker__header__dropdown.react-datepicker__header__dropdown--select >"
                    " div.react-datepicker__year-dropdown-container.react-datepicker__year-dropdown-container--select").click()
    #browser.element("// *[ @ id = ""dateOfBirth""] / div[2] / div[2] / div / div / div[2] / div[1] / div[2] / div[2] / select").click()
   # browser.element("// *[ @ id = ""dateOfBirth""] / div[2] / div[2] / div / div / div[2] / div[2] / div[3] / div[3]").click()

    browser.element("#firstName").press_enter()

    browser.close()