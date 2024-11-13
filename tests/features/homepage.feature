Feature: Homepage
  Background:
    Given the user was on the homepage

  Scenario Outline: Social Links
    When the user "clicked" on "<icon>" social link
    Then the user is redirected to "<url>"
    Examples:
      | icon      | url                                                     |
      | github    | https://github.com/mhaneman                             |
      | gitlab    | https://gitlab.com/mhaneman                             |
      | linkedin  | https://www.linkedin.com/in/michael-haneman-1062461a4/  |

  Scenario Outline: Header Navigation
    When the user "clicked" on "<item>" header link

    Examples:
      | item      |
      | Articles  |
      | About     |
      | Projects  | 