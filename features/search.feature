Feature: Search functionality

  @product
  Scenario Outline: Search for a valid product
    Given I got navigated to home page
    When I enter valid <product> into the search box field
    And I click on search button
    Then Valid <product> should get displayed in search results
    Examples:
      | product |
      | HP      |
      | Apple   |

  @implemented
  Scenario Outline: Search for an invalid product
    Given I got navigated to home page
    When I enter <invalid_product> into the search box field
    And I click on search button
    Then proper message is displayed in search results
    Examples:
      | invalid_product |
      | zart            |
      | zurt            |

  @implemented
  Scenario: Search without entering any product
    Given I got navigated to home page
    When I don't enter anything into search box field
    And I click on search button
    Then proper message is displayed in search results