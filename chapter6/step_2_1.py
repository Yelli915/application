from playwright.sync_api import Page
from step_1_2 import run_playwright
from step_1_3 import goto_best_goods

def select_category(page:Page, category:str=None) :
    page.get_by_role("button").filter(has_text=category).first.click()
    
def select_options(page:Page, option:str=None) :
    page.get_by_text(option).first.click()

if __name__ == "__main__" :
    play,browser,page = run_playwright(slow_mo=1000)
    goto_best_goods(page)
    select_category(page, "여성의류")
    page.wait_for_timeout(1000)
    select_options(page, "스커트")
    page.pause()
    browser.close()
    play.stop()