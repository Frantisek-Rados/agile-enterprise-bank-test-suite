*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}         https://parabank.parasoft.com/parabank/register.htm
${FIRSTNAME}   Jan
${LASTNAME}    Novak
${STREET}      Hlavna 123
${CITY}        Kosice
${STATE}       SK
${ZIP}         04001
${PHONE}       0900123456
${SSN}         123-45-6789
${USERNAME}    jan_novak
${PASSWORD}    Test123!

*** Test Cases ***
Registracia noveho pouzivatela
    Open Browser    ${URL}    chrome
    Sleep           3s
    # Skúsime vyplniť formulár bez čakania na text
    Input Text      id=customer.firstName    ${FIRSTNAME}
    Input Text      id=customer.lastName     ${LASTNAME}
    Input Text      id=customer.address.street    ${STREET}
    Input Text      id=customer.address.city      ${CITY}
    Input Text      id=customer.address.state     ${STATE}
    Input Text      id=customer.address.zipCode   ${ZIP}
    Input Text      id=customer.phoneNumber       ${PHONE}
    Input Text      id=customer.ssn               ${SSN}
    Input Text      id=customer.username          ${USERNAME}
    Input Text      id=customer.password          ${PASSWORD}
    Input Text      id=repeatedPassword           ${PASSWORD}
    Click Button    xpath=//input[@value='Register']
    Sleep           3s
    # Overíme, či sme na správnej stránke (kontrola URL)
    ${current_url}=    Get Location
    Should Contain    ${current_url}    register
    Close Browser