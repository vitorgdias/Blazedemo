from selenium import webdriver


# Beginning
def before_all(context):
    # Declare Selenium and set up as a driver
    context.driver = webdriver.Chrome('C:/Users/Vitor/Desktop/Vitor/Cursos/Python2023/Blazedemo/driver/114/chromedriver.exe')
    context.driver.maximize_window()
    print('Step A - Before All')


def after_all(context):
    # Turn off Selenium
    context.driver.quit()
    print('Step Z - After All')
