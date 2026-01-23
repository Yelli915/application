import json
from pathlib import Path
from playwright.sync_api import Page
from step_1_1 import OUT_DIR
from step_1_2 import run_playwright

OUT_1_3 = OUT_DIR / f"{Path(__file__).stem}.json"

# def goto_market_cap(page:Page)