from behave import given, when, then
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# Always need to import environment to run behave
from features import environment


# Method to be executed before Feature, to run all steps forward
def before_feature(context, feature):
    if 'Buy_flight_ticket' in feature.tag:
        context.execute_steps(
            # Can be included other actions
        )


@given(u'access Blazedemo website')
def step_impl(context):
    context.driver.get('https://www.blazedemo.com')
    print('Step 1 - Access successful')


@when(u'select origin as "{origin}"')
def step_impl(context, origin):
    # Set up the list with all origin cities
    origin_list = context.driver.find_element(By.NAME, 'fromPort')
    # Create an object to allow the list options selection
    origin_object = Select(origin_list)
    # Select the element in the list
    origin_object.select_by_visible_text(origin)
    # origin_object.select_by_value(origin) - Is possible to use this sentence to get the city name
    print('Step 2 - Selected the origin city')


@when(u'select destiny as "{destiny}"')
def step_impl(context, destiny):
    # Set up the list with all origin cities
    destiny_list = context.driver.find_element(By.NAME, 'toPort')
    # Create an object to allow the list options selection
    destiny_object = Select(destiny_list)
    # Select the element in the list
    destiny_object.select_by_visible_text(destiny)
    print('Step 3 - Selected the destiny city')


@when(u'click in Find Flights')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()   # Don't have ID, but have a tag and name, so is used CSS Selector
    print('Step 4 - Clicked in search button')


@then(u'be redirected to flight page')
def step_impl(context):
    # assert context.driver.find_element(By.TAG_NAME, 'h3').text() == 'Flights from São Paolo to Rome: '
    assert context.driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/h3[1]').text() == 'Flights from São Paolo to Rome: '
    print('Step 5 - Redirected to flight selection page')


@when(u'select the first flight')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-small').click()
    print('Step 6 - Selected the first flight')


@then(u'be redirected to payment page')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//p[contains(text(),'Please submit the form below to purchase the flight.')]").text == 'Please submit the form below to purchase the flight.'
    print('Step 7 - Redirected to the payment page')


@when(u'fill all required fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'inputName').send_keys('Name')
    print('Step 8 - Fill all required data')


@when(u'click in purchase button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn;btn-primary').click()
    print('Step 9 - Clicked in purchase button')


@then(u'be redirected to confirmation page')
def step_impl(context):
    assert context.driver.find_element(By.TAG_NAME, 'h1').text() == 'Thank you for your purchase today!'
    print('Step 10 - Redirected to confirmation page')


@when(u'select flight from "São Paolo" to "Rome"')
def step_impl(context):
    print('Step 2c - Selected the origin and destiny cities')
