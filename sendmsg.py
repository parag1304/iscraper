
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed


# def sendmsg(follower, following, Bio):
#   webhook = DiscordWebhook(url='https://discord.com/api/webhooks/887997899143774218/zvzXrhEu0vEB7F_f-EXYko_ICHPA6MqAoApbqKb_Fh4zCDcbl4v3JTEkacp10gkQFskc')
#   embed = DiscordEmbed(title='Instgram Bot', description="", color='03b2f8')
#   embed.add_embed_field(name='Follower', value=follower)
#   embed.add_embed_field(name='Following', value=following)
#   embed.add_embed_field(name='Bio', value=Bio)
#   webhook.add_embed(embed)

#   response = webhook.execute()

def sendmsg(information):
  webhook = DiscordWebhook(url='https://discord.com/api/webhooks/887997899143774218/zvzXrhEu0vEB7F_f-EXYko_ICHPA6MqAoApbqKb_Fh4zCDcbl4v3JTEkacp10gkQFskc')
  embed = DiscordEmbed(title='Instgram Bot', description="", color='03b2f8')
  follower = information[0]
  following = information[1]
  bio = information[2]
  embed.add_embed_field(name='Follower', value=follower, inline = False)
  embed.add_embed_field(name='Following', value=following, inline = False)
  embed.add_embed_field(name='Bio', value=bio, inline = False)
  webhook.add_embed(embed)

  response = webhook.execute()


def convertTuple(tup):
    st = ' '.join(map(str, tup))
    return st