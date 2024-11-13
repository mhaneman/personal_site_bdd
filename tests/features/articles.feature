Feature: Articles
    Background:
        Given the user was on the homepage
        When the user "clicked" on "articles" header link

    Scenario Outline: The user reads and article
        When the user opened article titled "<name>"
        Then the article has the following criteria
            | Title | <name> |
        Examples:
            | name                                      |
            | LearnOpenGL Setup with VKPKG for Linux    |