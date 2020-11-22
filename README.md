# Never Miss a Deal
**Want to know when a product goes on sale.** 

Track ANY product from clothing, electronics, toys and TVs on Takealot, Makro and Game `South Africa`. 
The price tracker app will regularly compares the prices of your favorite stuff on Takealot, Makro and Game and sends you a customized 
notification email to tell you if the prices fell down.

## Requirements
* Gmail Account.
* Google Chrome.


## Here's how it works:
1. Install the required packages.
``` pip Install requests bs4 selenium pandas smtplib```

2. Modify the excel sheet by adding the urls and Tracking Price for an item. The file located in `data/items_details.csv`.

3. Edit the sender and recipient email in mail.json file which exist in the `config` folder.
* Sender Email: To be able to receive an email from the app you need to have a sender email.
* recipient Email: This email will be the receiver.

4. run the following command:

```python
python price_tracker.py
```

