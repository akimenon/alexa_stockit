# alexa_stockit
An alexa app which can be used to check NASDAQ stock prices, create personalized portfolios and check performance of portfolios. This app is still WIP but it has different flavor & concept to pull & store stock data

   1) Real time stock prices: Couldn't find any good free API(s) to pull real-time stock quotes. Hence, built a webscrapper to       scrap bloomberg for real time stock prices
   
   2) NoSQL MongoDB (cloud): portfolios/wishlist to be created will be stored in cloud. 
   
   3) Stock prices can be pulled based on TICKER symbols, but a user may not necessarily know a ticker symbol. Hence built a         function to pull TICKER price based on the company name. It used complex regex to match the org name. Eg: say 'Amazon'         will pull ticker symbol of 'Amazon.com'
   
   There are further plans to expand the functionalities. More to come soon. 
   
   :::::::::::Testing::::::::::::::::::::
   
   locally tested in AWS lambda. To be tested in amazon echo device. 
