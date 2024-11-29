import allure

def screenshot_page(page, name):
    png_bytes = page.screenshot()
    allure.attach(
        png_bytes,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )