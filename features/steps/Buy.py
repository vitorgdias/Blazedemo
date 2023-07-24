from behave import given, when, then


@given(u'access Blazedemo website')
def step_impl(context):
    print('Step 1 - Access successful')


@when(u'select origin as "São Paolo"')
def step_impl(context):
    print('Step 2 - Selected the origin city')


@when(u'select destiny as "Rome"')
def step_impl(context):
    print('Step 3 - Selected the destiny city')


@when(u'click in Find Flights')
def step_impl(context):
    print('Step 4 - Clicked in search button')


@then(u'be redirected to flight page')
def step_impl(context):
    print('Step 5 - Redirected to flight selection page')


@when(u'select the first flight')
def step_impl(context):
    print('Step 6 - Selected the first flight')


@then(u'be redirected to payment page')
def step_impl(context):
    print('Step 7 - Redirected to the payment page')


@when(u'fill all required fields')
def step_impl(context):
    print('Step 8 - Fill all required data')


@when(u'click in purchase button')
def step_impl(context):
    print('Step 9 - Clicked in purchase button')


@then(u'be redirected to confirmation page')
def step_impl(context):
    print('Step 10 - Redirected to confirmation page')


@when(u'select flight from "São Paolo" to "Rome"')
def step_impl(context):
    print('Step 2c - Selected the origin and destiny cities')
