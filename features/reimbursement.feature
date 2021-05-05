Feature: Different Users Can Manage Reimbursement Requests

    Scenario: User Can Log In
      Given The User is on the log in page
      When The User enters a correct Id
      And The User Clicks submit
      Then The User will be on the home page

    Scenario: Supervisor Can Log In
      Given The User is on the log in page
      When The supervisor enters a correct Id
      And The User Clicks submit
      Then The User will be on the home page

    Scenario: Department Head Can Log In
      Given The User is on the log in page
      When The Department Head enters a correct Id
      And The User Clicks submit
      Then The User will be on the home page

    Scenario: Benefits Coordinator Can Log In
      Given The User is on the log in page
      When The Benefits Coordinator enters a correct Id
      And The User Clicks submit
      Then The User will be on the home page

    Scenario: User can submit reimbursement request
      Given The User is logged in
      And The User is on the home page
      When The User clicks on Start New
      And The User Enters All of the required info
      Then The User is Redirected to the home page

    Scenario: Supervisor can approve request
      Given The Supervisor is logged in
      And The User is on the home page
      And A request is pending
      When The User clicks the Accept button
      Then The request is approved by the user

    Scenario: Department Head can approve request
      Given The Department Head is logged in
      And The User is on the home page
      And A request is pending
      When The User clicks the Accept button
      Then The request is approved by the user

    Scenario: Benefits Coordinator can approve request
      Given The Benefits Coordinator is logged in
      And The User is on the home page
      And A request is pending
      When The User clicks the Accept button
      Then The request is approved by the user

    Scenario: Supervisor can deny request
      Given The Supervisor is logged in
      And The User is on the home page
      And A request is pending
      When The User clicks the Deny button
      Then The request is denied by the user

    Scenario: Supervisor can request more info
      Given The Supervisor is logged in
      And The User is on the home page
      And A request is pending
      When The User clicks the request more info button
      Then The request is forwarded to the user
