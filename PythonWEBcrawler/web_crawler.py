import requests

"""
# Use Get Function
web = get('https://water.taiwanstat.com/') 

# Change UTF-8
web.encoding = 'utf-8'

# Print Out
print(web.text)
"""

# web2 
web =requests.get('https://data.kcg.gov.tw/12345')
if web.status_code == 404:
    print("404 Error!!")
