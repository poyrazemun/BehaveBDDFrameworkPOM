from behave import *
import utilities.util


@given(u'I navigate to register page')
def step_impl(context):
    context.hp.click_on_my_account()
    context.hp.click_on_register_option()


@when(u'I enter details into mandatory fields')
def step_impl(context):
    for row in context.table:
        new_email = utilities.util.email_generator()
        context.rp.fill_out_the_mandatory_fields(row["first_name"], row["last_name"], new_email, row["tel_num"],
                                                 row["password"])


@when(u'I select privacy policy option')
def step_impl(context):
    context.rp.click_on_privacy_policy_option_checkbox()


@when(u'I click on continue button')
def step_impl(context):
    context.rp.click_on_continue_button()


@then(u'Account is created')
def step_impl(context):
    assert context.asp.verify_account_creation, "Account is not created!"


@when(u'I enter details into all fields except email field')
def step_impl(context):
    for row in context.table:
        context.rp.fill_out_the_mandatory_fields(row["first_name"], row["last_name"], tel_num=["tel_num"],
                                                 password=["password"])


@when(u'I enter {existing_accounts_email} into email field')
def step_impl(context, existing_accounts_email):
    context.rp.enter_email(existing_accounts_email)


@then(u'proper warning message informing about duplicate account is displayed')
def step_impl(context):
    assert context.rp.verify_warning_displayed_for_duplicate_email()


@when(u'I dont enter anything into the fields')
def step_impl(context):
    context.rp.fill_out_the_mandatory_fields()


@then(u'proper warning messages for every mandatory fields are displayed')
def step_impl(context):
    assert context.rp.verify_messages_for_every_mandatory_field_is_displayed()
