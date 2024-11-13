Feature: Articles
    Background:
        Given the user was on the homepage
        When the user "clicked" on "articles" header link


    Scenario Outline: The user read and article
        When the user opened article titled "<name>"
        Then the saw the page had the title "<name>"
        And  the user saw a visible footer
        Examples:
            | name                                      |
            | LearnOpenGL Setup with VKPKG for Linux    |