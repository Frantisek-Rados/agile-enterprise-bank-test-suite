# Bug reporty – ParaBank

Zoznam chýb nájdených počas testovania.

---

## 1. Krátke heslo akceptované

- **Popis:** Systém akceptuje heslo "123" (príliš krátke) počas registrácie.
- **Kroky na reprodukciu:**
  1. Otvor registračný formulár.
  2. Vyplň všetky polia.
  3. Do poľa "Password" zadaj "123".
  4. Do poľa "Confirm Password" zadaj "123".
  5. Klikni na "Register".
- **Očakávaný výsledok:** Chybová správa "Heslo musí mať aspoň 6 znakov".
- **Skutočný výsledok:** Registrácia prebehne úspešne.
- **Závažnosť:** Stredná
- **Nástroj:** Playwright
- **Stav:** Nahlásené

---

## 2. API Overview vracia 500 Internal Server Error

- **Popis:** Po prihlásení vracia endpoint `/parabank/overview.htm` chybu 500.
- **Kroky na reprodukciu:**
  1. Prihlás sa do aplikácie.
  2. Prejdi na stránku "Accounts Overview".
- **Očakávaný výsledok:** 200 OK a zobrazenie zostatku.
- **Skutočný výsledok:** 500 Internal Server Error.
- **Závažnosť:** Vysoká
- **Nástroj:** JMeter, k6
- **Stav:** Nahlásené