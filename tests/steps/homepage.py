from playwright.sync_api import sync_playwright, Locator
import pytest
from pytest_bdd import given, when, then, scenarios, parsers

# scenarios("../features/homepage.feature")
scenarios("../features/articles.feature")    

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()


@given('the user was on the homepage')
def step_the_user_was_on_the_homepage(page):
    page.goto('https://mthaneman.xyz')

@when(parsers.parse('the user "{action}" on "{icon}" social link'))
def the_user_on_social_link(action, icon, page):
    _social = page.locator(".socials").get_by_label(icon)
    do_action_on_element(action, _social)

@when(parsers.parse('the user opened article titled "{name}"'))
def the_user_opened_article_titled(name, page):
    article = page.locator("article").filter(has_text=name)
    article.scroll_into_view_if_needed()
    article.get_by_role('link', name='Continue Reading').click()

@when(parsers.parse('the user "{action}" on "{item}" header link'))
def the_user_on_header_link(action, item, page):
    _header_item = page.locator("header").get_by_text(item)
    do_action_on_element(action, _header_item)

@then(parsers.parse('the user is redirected to "{url}"'))
def the_user_is_redirected_to(url, page):
    # check url
    pass

@then(parsers.parse('the article has the following criteria'))
def the_article_has_the_following_criteria(criteria, page):
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

