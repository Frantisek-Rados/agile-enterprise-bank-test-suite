# Testovací plán – Banková aplikácia (ParaBank)

## 1. Cieľ projektu
Otestovať kompletný bankový proces – od registrácie po správu platieb a notifikácií.

---

## 2. Rozsah testovania

- **UI testy** – responzivita, vzhľad, funkcionalita tlačidiel
- **API testy** – backend operácie (registrácia, prihlásenie, platby)
- **Databázové testy** – overenie uložených dát
- **Výkonnostné testy** – odozva pri registrácii a platbách
- **Bezpečnostné testy** – HTTPS, citlivé údaje v URL
- **Regresné testy** – overenie, že oprava neporušila inú funkcionalitu

---

## 3. Testované oblasti

### 3.1. Hlavná stránka
- Responzivita (mobil, tablet, desktop)
- Kontrola tlačidiel (prekliky)
- Vzhľad a dizajn (farba, veľkosť, odsadenie)
- Právne vyhlásenia (Ochrana osobných údajov)
- Pravopis a gramatika

### 3.2. Registračný proces
- Povinné polia (chybové hlásenia)
- Sila hesla (kontrola znakov, dĺžky)
- Validácia údajov (email, telefón, adresa)
- Rýchlosť odozvy pri registrácii
- Presmerovanie po registrácii
- Funkčnosť menu nového klienta

### 3.3. Notifikácie
- **SMS notifikácie**
  - Autorizácia platieb
  - Výpis bankového účtu
  - Upozornenie na nezrealizovanú / zrealizovanú platbu
  - Upozornenie na podozrivé prihlásenie
- **Email notifikácie**
  - Potvrdenie registrácie
  - Upozornenia o platbách
  - Bezpečnostné upozornenia

### 3.4. Platobné príkazy
- Bežný prevod (overenie sumy, zostatku)
- Trvalý príkaz (nastavenie, úprava, zrušenie)
- SIPO príkaz (kontrola údajov)

---

## 4. Nástroje

| Oblasť | Nástroj |
|--------|---------|
| UI testy | Playwright, Robot Framework |
| API testy | Python + `requests` + pytest |
| Databáza | DBeaver, SQL |
| Výkon | k6, JMeter |
| CI/CD | GitHub Actions |
| Reporting | pytest-html, ExtentReports |

---

## 5. Výstupy

- Testovacie prípady (`docs/test-cases.md`)
- Bug reporty (`docs/bug-reports.md`)
- Finálny report (`docs/sprint-report.md`)
- Automatizované testy v repozitári
