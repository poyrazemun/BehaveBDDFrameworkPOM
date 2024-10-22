Feature: Register Account functionality

  @done
  Scenario: Register with mandatory fields
    Given I navigate to register page
    When I enter details into mandatory fields
      | first_name | last_name | tel_num   | password |
      | Mali       | Amali     | 123456789 | 12345    |
    And I select privacy policy option
    And I click on continue button
    Then Account is created

  @thisone
  Scenario Outline: Register with a duplicate email address
    Given I navigate to register page
    When I enter details into all fields except email field
      | first_name | last_name | tel_num   | password |
      | Mali       | Amali     | 123456789 | 12345    |
    And I enter <existing_accounts_email> into email field
    And I select privacy policy option
    And I click on continue button
    Then proper warning message informing about duplicate account is displayed
    Examples:
      | existing_accounts_email     |
      | amotooriapril2023@gmail.com |
      | amotooriapril2024@gmail.com |


  @implemented
  Scenario: Register without providing any details
    Given I navigate to register page
    When I dont enter anything into the fields
    And I click on continue button
    Then proper warning messages for every mandatory fields are displayed
