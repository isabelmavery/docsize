### Document Size
Automating Doc Size analysis:

### Set up:
Download the files in python folder. May need to follow the QuickStart setup in Google Sheets API here in order for it to run correctly:
https://developers.google.com/sheets/api/quickstart/python.

Dependencies, python3, pip, beautifulsoup4:
```python3 install pip```
```python3 -m pip install bs4```

### Run program
1. Open spread sheet and change URL to one that you are interested in investigating the doc size of:
https://docs.google.com/spreadsheets/d/1eVV4O_HcU_BiETm3AyHIPgmXO9FMdBGGwwf6k-T31fc/edit#gid=0&range=A3:B32

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
