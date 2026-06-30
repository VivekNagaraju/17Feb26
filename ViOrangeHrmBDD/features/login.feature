# Given - Pre condition steps
# When - Action steps/ Test steps
# Then - Validation steps
# And - extension/ continuation of previous step/ keyword
Feature: Login feature file

  Background: Initial steps to be executed in each scenario
    Given Chrome browser is launched
    When User navigates to Login Page URL

  Scenario: Validate navigation to OrangeHRM Login page
    Then User should see login in current page URL

  Scenario: Validate login to OrangeHRM
    And User enters username
    And User enters password
    And User clicks on login button
    Then User should see dashboard in current page URL

  Scenario: Validate login with parameters
    And User enters username Admin
    And User enters password admin123
    And User clicks on login button
    Then User should see dashboard in current page URL

  Scenario Outline: Validate login in DDT
    And User enters username <username> #placeholder
    And User enters password <password>
    And User clicks on login button
    Then User should see dashboard in current page URL

    Examples:
      | username | password  |
      | admin    | admin123  |
      | admin    | admin1234 |
      | admins   | admin123  |
      | admins   | admin1234 |
