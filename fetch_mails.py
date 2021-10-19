import imaplib as imap
import email as e
import datetime as dt
import os

# credentials
username = os.getenv("mail_username")
password = os.getenv("mail_password")
host = "imap.gmail.com"

os.system('clear')


def setup_con():
    # setup connection
    print("[~] Connecting to the Mail Server")
    mail = imap.IMAP4_SSL(host)
    print("[+] Connected")
    return mail


def login(mail):
    # login to the main
    print("[~] Logging in...")
    mail.login(username, password)
    print("[+] Logged in")


def fetch_mail(mail):

    # select inbox
    status, messages = mail.select('INBOX')
    before_date = dt.datetime.now()
    since_date = (before_date - dt.timedelta(1))
    
    since_date = since_date.strftime('%d-%b-%Y')
    before_date = before_date.strftime('%d-%b-%Y')

    (retcode, messages) = mail.search(None, f'(since {since_date} before {before_date})')
    if retcode == 'OK':
        msg = messages[0].decode().split(' ')[::-1]

        with open(f"new_emails_{since_date}-{before_date}.txt", 'w') as mailbox:
            for num in msg:
                typ, data = mail.fetch(num,'(RFC822)')
                email = e.message_from_string(data[0][1].decode())
                
                Date = email["date"]
                From = email["from"]
                Subject = email["subject"]

                msg = ""
                for part in email.walk():
                    if part.get_content_type() == "text/plain":
                        msg += part.get_payload()
                # print("\n\n\n=============================================\n\n\n")
                content = "-"*25 + "\n" + "Date: " + Date + '\n' + "From: " + From + '\n' + "Subject: " + Subject + "\n" + "-"*25 + '\n\n' + "Message: \n" + msg

                # the line below keeps the emails still unread after reading them, if you want them to be seen, comment the line below
                typ, data = mail.store(num,'-FLAGS','\\Seen')

                mailbox.write(content)
                mailbox.write('\n\n')
                mailbox.write('='*75)
                mailbox.write('\n')
                mailbox.write('='*75)
                mailbox.write('\n\n')




# Driver Code
def main():
    mail = setup_con()
    login(mail)
    fetch_mail(mail)


main()
