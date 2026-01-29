from playwright.sync_api import Browser,Page,Playwright, sync_playwright

def run_playwright(slow_mo : float = None) -> tuple[Playwright,Browser,Page] :
    play : Playwright = sync_playwright().start()
    browser : Browser = play.chromium.launch(args=["--start-maximized"],headless=False,slow_mo=slow_mo)
    page : Page = browser.new_page(no_viewport=True)
    page.add_locator_handler(page.get_by_role("button",name="하루동안 보지않기"),handler=lambda loc:loc.click(),times=1)
    return play,browser,page

if __name__ == "__main__" :
    play,browser,page = run_playwright()
    page.goto("https://www.naver.com/")
    page.pause()
    browser.close()
    play.stop()