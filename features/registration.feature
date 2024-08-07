Feature: Registration Feature
  @run_this_scenario
  Scenario Outline: Validate The Registration Feature
    Given I Enter The qa.automation.com
    When I enter the name as "<name>"
    And I enter the phone as "<phone>"
    And I Enter the email as "<email>"
    And I enter the country as "<country>"
    And I enter the city as "<city>"
    And I enter the username as "<username>"
    And I enter the password as "<password>"
    And I click on the sub,it button
    Examples:
    | name    | phone          | email   | country | city | username | password |
    | Monther | 00962795727257 | m@m.com | Jordan  | Amman | mmskbh  | mmskbh123 |
    | mohammad | 00962795727257 | m@m.com | Jordan  | Amman | mmskbh  | mmskbh123 |


