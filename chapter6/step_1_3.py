from playwright.sync_api import Page
from step_1_2 import run_playwright

def goto_best_goods(page : Page) :
    page.goto("https://snxbest.naver.com/home")
    page.get_by_role("link", name="패션뷰티").click()

if __name__ == "__main__" :
    play,browser,page = run_playwright(slow_mo=1000)
    goto_best_goods(page)
    page.pause()
    browser.close()
    play.stop()