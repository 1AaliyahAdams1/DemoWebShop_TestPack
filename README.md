# Phase 3 UI Automation Assessment
**Application:** Demo Web Shop — https://demowebshop.tricentis.com
**Stack:** Python · Playwright · Pytest

---

## Project Structure
```
/
├── conftest.py              # Fixtures and credential helpers
├── requirements.txt
├── README.md
├── data/
│   ├── locators.py          # All XPath/CSS selectors
│   └── test_data.py         # All static test data
├── pages/
│   ├── base_page.py         # Shared WaitClick/WaitFill helpers
│   ├── register_page.py
│   ├── login_page.py
│   └── checkout_page.py
└── tests/
    ├── test_register.py     # Part 1
    ├── test_login.py        # Part 2
    └── test_checkout.py     # Part 3
```

---

## Setup
```bash
pip install -r requirements.txt
playwright install chromium
```

## Run
```bash
# Run all tests
pytest tests/ -v OR
python -m pytest tests/ -v


# Run a single test
pytest tests/test_register.py -v 
```

---

## Assumptions

- Assumed only 1 Digital SLR Camera needs to be checked out with no additional product requirements
- Assumed the following fields do not need to be filled in during registration: Fax and Address Line 2
- Assumed the card expiry year just needs to be a future valid year — updated to 2030 as the provided dummy data year (2022) was expired
- Assumed billing address only needs to be filled in once per user — if saved details are detected, the form is skipped automatically

---

## Tradeoffs

- Each test runs independently — if no credentials exist, `ensureCredentials()` automatically registers a new user before running, so tests do not need to run in a specific order
- A fresh browser context is created per test to prevent page state carrying over between tests
- Only billing address is filled in during checkout — shipping and payment method steps use the default pre-selected options
- Locators and test data are separated into a `data/` folder so selectors and values have a single source of truth
- Shared helper methods (`WaitClick`, `WaitFill`) live in `BasePage` and are inherited by all page objects to avoid duplication

---

## Improvements Given More Time

- Add negative testing for all 3 test cases (invalid email, wrong password, empty fields)
- Handle a non-empty cart before checkout — currently the test assumes the cart is empty when it starts
- Add screenshot capture on test failure via a pytest fixture hook
- Add a pytest-html report generated automatically on each run