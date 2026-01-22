import json 
from pathlib import Path
from playwright.sync_api import Page
from step_1_1 import OUT_DIR
from step_1_2 import run_playwright
from step_1_3 import goto_best_goods

OUT_2_2 = OUT_DIR / f"{Path(__file__).stem}.json"

def take_screenshot(page:Page, count:int=15) :
    selector = "li[class*='productCardResponsive_product_card']"
    page.wait_for_selector(selector, timeout=10000)
    locs = page.locator(selector).all()
    imgs_path = []
    for idx, loc in enumerate(locs[:count]) :
        path = OUT_DIR / f"{Path(__file__).stem}_{idx+1:03}.png"
        loc.screenshot(path=path)
        imgs_path.append(path.as_posix())
    with open(OUT_2_2,"w",encoding="utf-8") as fp :
        json.dump(imgs_path,fp,indent=2,ensure_ascii=False)

if __name__ == "__main__" :
    play,browser,page = run_playwright(slow_mo=1000)
    goto_best_goods(page)
    page.pause()
    take_screenshot(page)
    browser.close()
    play.stop()