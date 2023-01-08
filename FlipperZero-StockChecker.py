import bs4, requests, smtplib, time
#===================================
def main():
    appPassword = input('enter google email application password: ')    # asks user for their email *application* password
    while(True):
        # download HTML and raise error if one occurs
        res = requests.get('https://shop.flipperzero.one/')
        res.raise_for_status()

        # parsing HTML using BeautifulSoup4
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        schema_text = soup.select('#shopify-section-161367529272a863ec > script:nth-child(4)')

        # buy_button = soup.select('#shopify-section-161367529272a863ec > script:nth-child(4)')
        schema_text = str(schema_text[0].text).strip()

        # prints start execution time and status
        print('Start func exec time: ' + time.ctime())

        # connect to SMTP & send email __if__ product no longer sold out
        if 'http://schema.org/OutOfStock' not in schema_text:
            conn = smtplib.SMTP('smtp.gmail.com', 587)
            conn.ehlo()
            conn.starttls()
            conn.login('<sender email address>', appPassword)
            conn.sendmail('<sender email address>', '<recipient email address>', 'Subject: FLIPPER ZERO Stock Change Alert\n\n\
                The bot has noticed a change in the website\'s HTML indicating the product is back in stock.\n\
                Check Flipper website: https://shop.flipperzero.one')
            conn.quit()

            # prints email is sent and end execution time
            print('Email sent.')
            print('End exec time: ' + time.ctime())
            print('//=========================')
            return

        # prints email is not sent and end execution time
        print('Email not sent.')
        print('//=========================')

        # wait 5 minutes
        time.sleep(300)
    return
#===================================
main()