This Code uses Selenium for Automation and Beautiful Soup for web_Scraping

Libraries Used:
1.selenium
2.requests
3.bs4 (Beautiful Soup)
4.openpyxl ( Access Excel and perform Read/Write operations )

Methodology:
# Fetchs the ISIN number of each company from the excel sheet.
# Sends request to the website to access.
# For loop which:
    Automates the access to google chrome
    Searches the ISIN number of each company on the website
    Web-scraping to get the details required
    Writing the information into the excel file and saving it.
# Continues this process for rest of the list.
