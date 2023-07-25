from selenium import webdriver


# Beginning
def before_all(context):
    # Declare Selenium and set up as a driver
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)
    print('Step A - Before All')


def after_all(context):
    # Turn off Selenium
    context.driver.quit()
    print('Step Z - After All')