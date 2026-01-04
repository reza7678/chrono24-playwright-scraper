# Chrono24 Playwright Scraper

A Python scraper built with Playwright to extract Rolex listings from Chrono24 (JavaScript-rendered website).

## Features
- Uses Playwright (Chromium)
- Handles dynamic content
- Scrolls page to load products
- Exports data to CSV

## Output
- Product name
- Price
- Seller country

## Requirements
- Python 3.9+
- Playwright

## How to Run
```bash
pip install playwright
playwright install chromium
python chrono24.py
