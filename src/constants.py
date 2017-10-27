import urllib

"""
Common Db connection parameters
"""

username="stockitadmin"
password="9f2194"
dbprops="@ds125195.mlab.com:25195/stockitdb"

# URI connection parameter
mongo_uri = "mongodb://"+username+":"+urllib.quote(password)+dbprops

#bloomberg URL for stock quote
bloomurl='https://www.bloomberg.com/quote/'
