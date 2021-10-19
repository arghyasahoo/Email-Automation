# Email Automation

This script fetches all emails from past 1 day and stores them in a text file. Use `cron` to make this executable everyday and Wallah!! all your mails are fetched and stored.


## Usage
1. Clone this repo.
2. This script fetches username and password from environment variables, so save usermame and password of you email address in `.bashrc`

```
export mail_username='<your_username>'
export mail_password='<your_password>'
```

> If you want to name variables differently, make sure to change them in the source as well.

3. Run the script, and it should fetch all emails from the today and store them in a file in current directory.


## Tweaks and Upgrades
- Add this script to **cron** and execute it daily to get automatic updates for all your emails without, any manual interaction
- Change the `since_date` and `before_date` to get emails of any other duration
- Feel free to update the script in any other way possible


## Future of this project
Some kind of auto notification system will be implemented to automatically notify the user about new mails everyday.

