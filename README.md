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

- **API testy:** 5 passed, 1 skipped (ParaBank API vracia 500 – nahlásené ako BUG)
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

## Nájdené chyby (BUG reporty)

- **Registrácia:** API vracia 500 Internal Server Error
- **Zostatok (overview):** API vracia 500 Internal Server Error

## Použité technológie

- Python 3.11+
- pytest, requests, playwright
- SQLite, DBeaver
- GitHub Actions
- Allure / HTML reporty

## Autor

František Radoš
