from step_1_2 import run_playwright
from step_1_3 import goto_best_goods
from step_2_1 import select_category, select_options
from step_2_2 import take_screenshot

def fetch_trends_by_filter(category:str=None, option:str=None) :
    play,browser,page = run_playwright(slow_mo=500)
    goto_best_goods(page)
    if category :
        select_category(page,category)
    if option :
        select_options(page,option)
    take_screenshot(page)
    browser.close()
    play.stop()

if __name__ == "__main__" : 
    category, option = "패션뷰티","여성의류"
    fetch_trends_by_filter(category,option)