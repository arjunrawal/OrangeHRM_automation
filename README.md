#OrangeHRM Automation Testing with Selenium
This project demonstrates the automation testing of various modules and functionalities in the OrangeHRM application using Python and Selenium.

Key Features Automated:
1.Login Automation: Automates the login process with valid credentials.

2.Dashboard Navigation: Automates navigation from the login screen to the dashboard.

3.PIM (Personal Information Management):

Automates the navigation to the PIM section.

Automates employee form filling (personal details, job, and more).

Handles dynamic form elements like dropdowns and date pickers.

4.Leave Management:

Automates applying for leave, approving leave requests, and managing leave types.

Time & Attendance: Automates the management of time and attendance records.

5.Recruitment:

Automates the process of adding and managing job vacancies.

Handles candidate application form filling.

6.Employee Management: Automates employee record updates, including status changes, and adding/removing employees.

7.Logout Automation: Automates the logout process, ensuring a smooth session termination.

8.Error Handling: Robust error handling to wait for elements and ensure stability during interactions.

#Requirements
Python 3.x

Selenium

ChromeDriver (ensure it's in your system PATH)

#Install dependencies:

bash
Copy
Edit
pip install selenium
Setup
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/OrangeHRM-automation-testing.git
Download ChromeDriver from here and ensure it's accessible in your system PATH.

Running Tests
To run the tests:

bash
Copy
Edit
python -m unittest tests/test_pim.py
Future Improvements
Cross-browser Testing: Add support for other browsers like Firefox, Edge, etc.

Parallel Execution: Speed up testing with parallel execution of tests.

Advanced Reporting: Integrate test reporting tools for detailed results.

