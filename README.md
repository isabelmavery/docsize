### Document Size
Automating Doc Size Analysis

### Set up:
Download the repo, you can exclude the jupyter notebook (this was attempt one). You may need to follow the QuickStart setup in Google Sheets API here in order to generate auth:
https://developers.google.com/sheets/api/quickstart/python.

Dependencies, python3, pip, beautifulsoup4, google-api-python-client, google-auth-httplib2, google_auth_oauthlib:

```python3 install pip```

```python3 -m pip install bs4```

```python3 -m pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```

https://www.python.org/downloads/

### Running and Viewing Analysis:
Google Sheet with Analysis: https://docs.google.com/spreadsheets/d/1eVV4O_HcU_BiETm3AyHIPgmXO9FMdBGGwwf6k-T31fc/edit#gid=0

1. Open the spread sheet above and change the **URL** to a fanatics page, for example: 

"https://www.fanatics.com/nfl/atlanta-falcons/o-3527+t-69931287+z-91230-2469337799"

2. In your working directory run ```python3 quickstart.py```

3. This should update the data and graphs in the google sheet, linked above. In your terminal you will see an output like:
```
Url Loaded
Successfully Parsed Document
Doc Size - 813729
Head Size - 10315 <head><link href="/conten
Body Size - 803372 <body class="no-spriteshe
Scripts Total Size - 557107
Sheet successfully Updated
```
