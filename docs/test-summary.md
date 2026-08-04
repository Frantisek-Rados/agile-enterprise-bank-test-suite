# Zhrnutie testov – ParaBank

Tento dokument obsahuje prehľad všetkých testov, ktoré sme vytvorili pre bankovú aplikáciu ParaBank.

---

## 🧪 1. UI testy (Playwright + POM)

### 1.1 Responzivita (`test_responsive.py`)
- **Cieľ:** Overiť, či sa stránka správne zobrazuje na mobile, tablete a desktope.
- **Výsledok:** ✅ PASS

### 1.2 Registrácia (`test_registration.py`)
- **Cieľ:** Overiť, či sa nový používateľ vie úspešne zaregistrovať.
- **Výsledok:** ✅ PASS

### 1.3 Negatívne testy registrácie (`test_registration_negative.py`)
- **Cieľ:** Overiť, či systém odmietne neplatné heslo.
- **Výsledky:**
  - Prázdne heslo: ✅ PASS
  - Krátke heslo (123): ❌ BUG – systém ho akceptuje

### 1.4 Prevod medzi účtami (`test_transfer.py`)
- **Cieľ:** Overiť, či používateľ vie poslať peniaze medzi svojimi účtami.
- **Výsledok:** ✅ PASS

### 1.5 Jednorazová platba (`test_bill_pay.py`)
- **Cieľ:** Overiť, či používateľ vie zaplatiť faktúru.
- **Výsledok:** ✅ PASS

### 1.6 Trvalý príkaz (`test_recurring_payment.py`)
- **Cieľ:** Overiť, či používateľ vie nastaviť pravidelnú platbu.
- **Výsledok:** ✅ PASS

### 1.7 SIPO príkaz (`test_sipo_payment.py`)
- **Cieľ:** Overiť, či používateľ vie uhradiť viacero platieb naraz.
- **Výsledok:** ✅ PASS

---

## 📊 Prehľad výsledkov

| Test | Typ | Výsledok |
|------|-----|----------|
| Responzivita | UI | ✅ PASS |
| Registrácia | UI | ✅ PASS |
| Prázdne heslo | UI | ✅ PASS |
| Krátke heslo | UI | ❌ BUG |
| Prevod medzi účtami | UI | ✅ PASS |
| Jednorazová platba | UI | ✅ PASS |
| Trvalý príkaz | UI | ✅ PASS |
| SIPO príkaz | UI | ✅ PASS |