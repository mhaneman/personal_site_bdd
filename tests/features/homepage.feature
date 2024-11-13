Feature: Homepage
  Background:
    Given the user was on the homepage

  Scenario Outline: The user navigated to the Social Media Links 
    When the user "clicked" on "<icon>" social link
    Then the user is redirected to "<url>"
    Examples:
      | icon      | url                                                     |
      | github    | https://github.com/mhaneman                             |
      | gitlab    | https://gitlab.com/mhaneman                             |
      | linkedin  | https://www.linkedin.com/in/michael-haneman-1062461a4/  |

  Scenario Outline: The user went to all header links
    When the user "clicked" on "<item>" header link
    Then the user is redirected to "<url>"

    Examples:
      | item      | url                                 |
      | Articles  | https://www.mthaneman.xyz/articles/ |
      | About     | https://www.mthaneman.xyz/about/    |
      | Projects  | https://www.mthaneman.xyz/projects/ |