from behave import *


@given(u'I got navigated to home page')
def step_impl(context):
    assert context.hp.verify_navigation_to_home_page(), "Navigation to the home page is failed!"


@when(u'I enter valid {product} into the search box field')
def step_impl(context, product):
    context.hp.type_into_search_box(product)


@when(u'I click on search button')
def step_impl(context):
    context.hp.click_on_search_button()


@then(u'Valid {product} should get displayed in search results')
def step_impl(context, product):
    assert context.sp.verify_valid_product_displayed(product), "Product is not displayed!"


@when(u'I enter {invalid_product} into the search box field')
def step_impl(context, invalid_product):
    context.hp.type_into_search_box(invalid_product)


@then(u'proper message is displayed in search results')
def step_impl(context):
    assert context.sp.verify_proper_message_displayed_for_invalid_product()


@when(u"I don't enter anything into search box field")
def step_impl(context):
    context.hp.type_into_search_box("")
