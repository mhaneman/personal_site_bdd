from playwright.sync_api import sync_playwright, Locator, Page, expect
from pytest_bdd import given, when, then, scenarios, parsers

scenarios("../features/homepage.feature")  

@given('the user was on the homepage')
def step_the_user_was_on_the_homepage(page: Page):
    page.goto('https://mthaneman.xyz')


@when(parsers.parse('the user "{action}" on "{icon}" social link'))
def the_user_on_social_link(action, icon, page: Page):
    _social = page.locator(".socials").get_by_label(icon)
    do_action_on_element(action, _social)


@when(parsers.parse('the user opened article titled "{name}"'))
def the_user_opened_article_titled(name, page: Page):
    article = page.locator("article").filter(has_text=name)
    article.scroll_into_view_if_needed()
    article.get_by_role('link', name='Continue Reading').click()


@when(parsers.parse('the user "{action}" on "{item}" header link'))
def the_user_on_header_link(action, item, page: Page):
    _header_item = page.locator("header").get_by_text(item)
    do_action_on_element(action, _header_item)


@then(parsers.parse('the user is redirected to "{url}"'))
def the_user_is_redirected_to(url, page):
    # check url
    pass


def do_action_on_element(action: str, _element: Locator):
    match action.upper():
        case "CLICK" | "CLICKED":
            _element.click()
        case "DOUBLE CLICK" | "DOUBLE CLICKED":
            _element.dblclick()
        case "HOVER" | "HOVERED":
            _element.hover()
        case _:
            pass

