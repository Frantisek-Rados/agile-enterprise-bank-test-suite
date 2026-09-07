# Agile Enterprise Bank Test Suite

Komplexný testovací projekt pre bankovú aplikáciu (ParaBank). Simuluje prácu v agilnom tíme a zahŕňa UI, API, databázové, výkonnostné a bezpečnostné testy.

## Obsah

- [Testovací plán](docs/test-plan.md)
- [Licencia](LICENSE)

## Nástroje

- Playwright, Robot Framework (UI)
- Python + pytest + requests (API)
- DBeaver, SQL (databáza)
- k6, JMeter (výkon)
- GitHub Actions (CI/CD)

## Výsledky testov

- **API testy:** 5 passed, 1 skipped
- **UI testy:** Prechádzajú (Playwright + POM)
- **Databázové testy:** Prechádzajú (SQLite)
- **CI/CD:** GitHub Actions – automatické spúšťanie testov

## Spustenie testov

```bash
# Inštalácia závislostí
pip install -r requirements.txt

# Spustenie všetkých testov s reportom
pytest --alluredir=allure-results

# Zobrazenie reportu (ak máš Allure)
allure serve allure-results
```

## Jira bug reporty

Ukážky bug reportov v Jira Cloud:

### 1. Krátke heslo akceptované
**System akceptuje kratke heslo (123) pri registracii**

- **Kroky:** Registrácia s heslom "123"
- **Skutočný výsledok:** Registrácia prebehla úspešne
- **Očakávaný výsledok:** Chybová správa "Heslo musí mať aspoň 6 znakov"
- **Screenshot:** [docs/bug-kratke-heslo-123.png](docs/bug-kratke-heslo-123.png)

### 2. API Overview – 500 Internal Server Error (nepotvrdené)
**API Overview vracia 500 Internal Server Error**

- **Kroky:** Prihlásenie a kliknutie na "Accounts Overview"
- **Skutočný výsledok:** API vrátilo 500 Internal Server Error (pri opakovanom testovaní sa nepotvrdilo)
- **Očakávaný výsledok:** 200 OK a zobrazenie zostatku
- **Stav:** Zatvorené – nepodarilo sa reprodukovať
- **Screenshot:** [docs/jira-ticket-closed.png](docs/jira-ticket-closed.png)

## Použité technológie

- Python 3.11+
- pytest, requests, playwright
- SQLite, DBeaver
- GitHub Actions
- Allure / HTML reporty

## Autor

František Radoš
