Feature: Buy_flight_ticket
  # Description of buying process in Blazedemo.com
  # E2E = End to End
  Scenario: From Sao Paulo to Rome
    Given access Blazedemo website
    When select origin as "São Paolo"
    And select destiny as "Rome"
    And click in Find Flights
    Then be redirected to flight page
    When select the first flight
    Then be redirected to payment page
    When fill all required fields
    And click in purchase button
    Then be redirected to confirmation page

  Scenario: From Sao Paulo to Rome compact
    Given access Blazedemo website
    When select flight from "São Paolo" to "Rome"
    Then be redirected to flight page
    When select the first flight
    Then be redirected to payment page
    When fill all required fields
    And click in purchase button
    Then be redirected to confirmation page