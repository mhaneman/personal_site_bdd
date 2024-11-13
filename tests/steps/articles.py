from playwright.sync_api import sync_playwright, Locator, Page, expect
from pytest_bdd import given, when, then, scenarios, parsers

scenarios("../features/articles.feature")  

@then(parsers.parse('the article has the following criteria'))
def the_article_has_the_following_criteria(criteria, page: Page):
    pass