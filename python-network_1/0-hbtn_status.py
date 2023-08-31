"""The module must fetch the url request"""
import requests
"""To import resquest"""

"""Define the url"""
url = https://alu-intranet.hbtn.io/status

"""Send http get resquest"""
response = requests.get(url)

"""Check if response is successful"""
if response.status_code == 200:
    """Show response in tabulation"""
    lines = response.text.split('\n')
    
    """To print lines"""
    for line in lines:
        print("\t{}".format(line))

    """If the response fails to fecth"""
else:
    print("Did not fect URL. Status code: {}".format(response.status_code))