from lxml import html
import requests
from time import sleep


# Function that returns SMS code from online free phone
# returns 0000 if it doesnt manage to read proper code

def getsmscode():

    sleep(30)

    sms_code = ['0000']

    page = requests.get('https://www.receivesms.org/us-number/3456/')
    tree = html.fromstring(page.content)

    for i in range(1, 10):

        try:

            sms_text = tree.xpath('/html/body/section/div/div/div/div[4]/div[' + str(i * 3) + ']/text()')
            time_received = tree.xpath('/html/body/section/div/div/div/div[4]/div[' + str(i * 3 - 1) + ']/div/text()')

            if sms_text == [
                'Sent from your Twilio trial account - Welcome to Phone Verify! Please use security code ',
                ' to proceed.'] and time_received[0].endswith('sec ago'):
                sms_code = tree.xpath(
                    '/html/body/section/div/div/div/div[4]/div[' + str(i * 3) + ']/span/b/text()')
                break

        except:
            continue

    return sms_code