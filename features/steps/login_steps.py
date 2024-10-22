from behave import *
from datetime import datetime


@given(u'I navigated to login page')
def step_impl(context):
    context.hp.click_on_my_account()
    context.hp.click_on_login_option()


@when(u'I enter valid {email_address} and valid {password} into the fields')
def step_impl(context, email_address, password):
    context.lp.enter_email(email_address)
    context.lp.enter_password(password)


@when(u'I click on Login button')
def step_impl(context):
    context.lp.click_login_button()


@then(u'I should get logged in')
def step_impl(context):
    assert context.map.verify_login_is_successful(), "Login is failed"


@when(u'I enter {invalid_email_address} and valid {password} into the fields')
def step_impl(context, invalid_email_address, password):
    context.lp.enter_email(invalid_email_address)
    context.lp.enter_password(password)


@then(u'I should get a proper warning message')
def step_impl(context):
    assert context.lp.verify_login_is_failed(), "Failed login attempt is FAILED!"


@when(u'I enter valid {email_address} and {invalid_password} into the fields')
def step_impl(context, email_address, invalid_password):
    context.lp.enter_email(email_address)
    context.lp.enter_password(invalid_password)


@when(u'I enter {invalid_email_address} and {invalid_password} into the fields')
def step_impl(context, invalid_email_address, invalid_password):
    context.lp.enter_email(invalid_email_address)
    context.lp.enter_password(invalid_password)


@when(u"I don't enter any credentials into the fields")
def step_impl(context):
    context.lp.enter_email("")
    context.lp.enter_password("")
