import pandas as pd
from bs4 import BeautifulSoup

# current timestamp
current_time = pd.Timestamp.now()
# 24 hours ago timestamp
yesterday = current_time - pd.Timedelta('24 hours')

# save html table as dataframe, "df"
url = "http://bazaar.abuse.ch/downloads/misp"
df_list = pd.read_html(url, flavor='bs4')
df = df_list[0]

# filter df for rows less than 24 hours old
df = df[["Name", "Last modified", "Size", "Description"]]
df["Last modified"] = pd.to_datetime(df["Last modified"])
df = df[df["Last modified"] > yesterday]

print(df)

