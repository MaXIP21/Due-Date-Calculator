# Due Date Calculator

Some time ago, I was engaged in a project involving the calculation of SLA times. Initially, this task appeared straightforward, but it quickly became complex due to the inclusion of holidays from various nations, different time zones, and diverse work schedules. To address this challenge, I developed a Python module aimed at simplifying the process of calculating due dates. The primary objective was to ensure its simplicity while meticulously crafting unit tests for the code. Leveraging Jenkins, I executed these tests to identify and rectify any potential issues within the codebase.
The class also able to calculate Timedelta from a start date to and end date. 

Now, I'm sharing this code to assist others encountering similar challenges.

The first version was to just calculate the due date 
Class: 
- calculate_due_date.py
Unit tests:
- unit_test_calculate_due_date.py


The fine grained version 
Class:
- datecalculator.py # contains all the functions to calculate due dates. 
Unit tests:
- unit_test_datecaclulator # Contains the unit tests of the class

