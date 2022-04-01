from instascrape import * 
from time import sleep
profile = Profile('https://www.instagram.com/riiidhs')
profile.scrape()
print(profile.followers)






