import requests

"""
# Use Get Function
web = get('https://water.taiwanstat.com/') 

# Change UTF-8
web.encoding = 'utf-8'

# Print Out
print(web.text)
"""
"""
# web2 
web =requests.get('https://data.kcg.gov.tw/12345')
if web.status_code == 404:
    print("404 Error!!")
"""

# Set Num
Params = {
    'name':'oxxo',
    'age':'18'
}

# Add Num
web = requests.get('https://script.google.com/macros/s/AKfycbw5PnzwybI_VoZaHz65TpA5DYuLkxIF-HUGjJ6jRTOje0E6bVo/exec',
                   params = Params)

print(web.text)