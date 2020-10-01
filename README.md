### Document Size
Automating Doc Size analysis:

### Set up:
Download repo, you can exclude the jupyter notebook. You may need to follow the QuickStart setup in Google Sheets API here in order to generate auth:
https://developers.google.com/sheets/api/quickstart/python.

Dependencies, python3, pip, beautifulsoup4, google-api-python-client, google-auth-httplib2, google_auth_oauthlib:
```python3 install pip```
```python3 -m pip install bs4```
```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```

### Run program
1. Open spread sheet and change URL to one that you are interested in investigating the doc size of:
https://docs.google.com/spreadsheets/d/1eVV4O_HcU_BiETm3AyHIPgmXO9FMdBGGwwf6k-T31fc/edit#gid=0

2. In your working directory run ```python3 quickstart.py```

3. Should update the data and graphs in the sheet and in your terminal see an output like:
```
Url Loaded
Successfully Parsed Document
Doc Size - 813729
Head Size - 10315 <head><link href="/conten
Body Size - 803372 <body class="no-spriteshe
Scripts Total Size - 557107
Sheet successfully Updated
```
