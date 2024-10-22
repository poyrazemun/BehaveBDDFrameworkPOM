Feature: Login Functionality

  @para
  Scenario Outline: Login with valid credentials
    Given I navigated to login page
    When I enter valid <email_address> and valid <password> into the fields
    And I click on Login button
    Then I should get logged in
    Examples:
      | email_address               | password |
      | amotooriapril2023@gmail.com | 12345    |
      | amotooriapril2024@gmail.com | 12345    |


  Scenario Outline: Login with invalid email and valid password
    Given I navigated to login page
    When I enter <invalid_email_address> and valid <password> into the fields
    And I click on Login button
    Then I should get a proper warning message
    Examples:
      | invalid_email_address       | password |
      | zartzurtkartkurt1@gmail.com | 12345    |
      | zartzurtkartkurt2@gmail.com | 12345    |

  @implemented
  Scenario Outline: Login with valid email and invalid password
    Given I navigated to login page
    When I enter valid <email_address> and <invalid_password> into the fields
    And I click on Login button
    Then I should get a proper warning message
    Examples:
      | email_address               | invalid_password |
      | amotooriapril2023@gmail.com | 563556456sd56a   |
      | amotooriapril2024@gmail.com | 664565566565     |

  @implemented
  Scenario Outline: Login with invalid credentials
    Given I navigated to login page
    When I enter <invalid_email_address> and <invalid_password> into the fields
    And I click on Login button
    Then I should get a proper warning message
    Examples:
      | invalid_email_address       | invalid_password |
      | zartzurtkartkurt1@gmail.com | safasfsafas      |
      | zartzurtkartkurt1@gmail.com | dsasaffafassaf   |

  @smoke
  Scenario: Login without entering any credentials
    Given I navigated to login page
    When I don't enter any credentials into the fields
    And I click on Login button
    Then I should get a proper warning message
