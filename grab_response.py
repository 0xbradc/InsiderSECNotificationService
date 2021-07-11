# Grabs HTML Content, Parses through the Code, and Formats Information from Today

import urllib.request
from bs4 import BeautifulSoup
import ssl
from datetime import date

# Get html from page
def pull_response():
    # Ordered by SEC filing date and transactions over $1 million
    url = "https://finviz.com/insidertrading.ashx?or=10000&tv=1000000&tc=1&o=-sec"
    hdr = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) "
        "Chrome/23.0.1271.64 Safari/537.11"
    }
    req = urllib.request.Request(url, headers=hdr)
    con = ssl._create_unverified_context()
    with urllib.request.urlopen(req, context=con) as response:
        html = response.read().decode("utf-8")

    # Parse html and locate table we are interested in
    parsed = BeautifulSoup(html, "html.parser")
    filters_table = None
    for td in parsed.find_all("td"):
        tbl = td.find_parent("table")
        if tbl != None:
            filters_table = tbl
    # Ensures the correct table was found
    if filters_table is None:
        raise Exception("Could not locate filter parameters")

    # Delete all div tags as they are not needed
    for div in filters_table.find_all("div"):
        div.decompose()
    
    # Populate array with correct information
    td_list = filters_table.find_all("td")
    filter_dict = []
    today = date.today()

    for i in range(10, len(td_list), 10):
        # Checks if trade is from today
        month_day = today.strftime("%b %d")

        if month_day == td_list[i+9].get_text().strip()[0:len(month_day)]:
            current = {
                "Ticker": td_list[i].get_text().strip(),
                "Owner": td_list[i+1].get_text().strip(),
                "Relationship": td_list[i+2].get_text().strip(),
                "Date": td_list[i+3].get_text().strip(),
                "Transaction": td_list[i+4].get_text().strip(),
                "Cost": td_list[i+5].get_text().strip(),
                "# of Shares": td_list[i+6].get_text().strip(),
                "Value": td_list[i+7].get_text().strip(),
                "# of Shares Total": td_list[i+8].get_text().strip(),
                "SEC": td_list[i+9].get_text().strip()
            }
            filter_dict.append(current)
        else:
            break

    return filter_dict



def format_response():
    response = pull_response()
    if response == []:
        return None

    formatted_response = ""
    
    for elem in response:
        formatted_response += "\n"
        formatted_response += "_________________________\n\n"
        formatted_response += "Ticker: " + elem["Ticker"] + "\n"
        formatted_response += "Owner: " + elem["Owner"] + "\n"
        formatted_response += "Relationship: " + elem["Relationship"] + "\n"
        formatted_response += "Date of Transaction: " + elem["Date"] + "\n"
        formatted_response += "Transaction Type: " + elem["Transaction"] + "\n"
        formatted_response += "# of Shares: " + elem["# of Shares"] + "\n"
        formatted_response += "Value (in USD): $ " + elem["Value"] + "\n"
        formatted_response += "# of Shares Total: " + elem["# of Shares Total"] + "\n"
        formatted_response += "SEC Form 4 Filing: " + elem["SEC"] + "\n"
        formatted_response += "_________________________\n"
    formatted_response += "\n"

    return formatted_response
