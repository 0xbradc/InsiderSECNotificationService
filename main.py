# Script for Pulling SEC Insider Filings with Certain parameters
# By Brad Campbell
# June 2021

import email_service
import grab_response
from datetime import date
import time
import schedule

def send_report():
    message = grab_response.format_response()
    email_service.email_response(message)
    print("Report sent for " + date.today().strftime("%b %d, %Y") + ".")

# Scheduled for 7:30 PM
schedule.every().day.at("19:30").do(send_report)

def main():
    schedule.run_pending()
    # Sleep for an hour
    time.sleep(3599)
    main()

if __name__ == "__main__":
    main()
