from igramscraper.instagram import Instagram

from sendmsg import sendmsg


insta = Instagram()


insta.with_credentials('', '')
insta.login()

acoount = insta.get_account('')

print(acoount.biography())
Id = acoount.identifier()
following = acoount.follows_count()
follower = acoount.followed_by_count()
bio = acoount.biography()



sendmsg('', Id, following, follower, bio)
