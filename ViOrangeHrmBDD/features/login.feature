# Given - Pre condition steps
# When - Action steps/ Test steps
# Then - Validation steps
# And - extension/ continuation of previous step/ keyword

Feature: Login feature file

  Scenario: Validate navigation to OrangeHRM Login page
    Given Chrome browser is launched
    When User navigates to Login Page URL
    Then User should see login in current page URL

  Scenario: Validate login to OrangeHRM
    Given Chrome browser is launched
    When User navigates to Login Page URL
    And User enters username
    And User enters password
    And User clicks on login button
    Then User should see dashboard in current page URL
    
