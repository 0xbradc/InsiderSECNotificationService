## Introduction
This application is a web-scraping tool for pulling the day's SEC insider filings gathered from 
[fivbiz.com](https://finviz.com/insidertrading.ashx?or=10000&tv=1000000&tc=1&o=-sec).
Email notifications are currently being used. The user must have a valid email to send and receive with in order to successfully run the application.

Thank you to the various contributors of [other open source applications](https://github.com/mariostoev/finviz/blob/master/finviz/screener.py) that indirectly aided in the development of this app.



# Getting Started
1. Clone the repository into your preferred directory. 

2. Install necessary dependencies found in the import statements. Some dependencies that may be required are bs4 and schedule. These can be downloaded with the following terminal statements.
    ```
    $ pip3 install bs4
    $ pip3 install schedule
    ```

3. Run the following command in the root directory of the downloaded folder to start the email server.
    ```
    $ python3 main.py
    ```


# Example Response

The email service should be sending an SEC Form 4 Filing Report to the inputted email between 7:30 pm and 8:30 pm local time. Below is an example response.

<img width="389" alt="Screen Shot 2021-07-15 at 7 04 21 AM" src="https://user-images.githubusercontent.com/48145615/125785458-1ce531e4-1a5c-41bd-bc92-ffef1befd356.png">


# Resources
[Date/Time Docs](https://www.programiz.com/python-programming/datetime/current-datetime)

[Sending Emails w/ Python Docs](https://realpython.com/python-send-email/)

[Developed with references from Other Contributors](https://github.com/mariostoev/finviz/blob/master/finviz/screener.py)
