from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/887997899143774218/zvzXrhEu0vEB7F_f-EXYko_ICHPA6MqAoApbqKb_Fh4zCDcbl4v3JTEkacp10gkQFskc", username="New Webhook Username")

embed = DiscordEmbed(
    title="Embed Title", description="Your Embed Description", color='03b2f8'
)
embed.set_author(
    name="Author Name",
    url="https://github.com/lovvskillz",
    icon_url="https://avatars0.githubusercontent.com/u/14542790",
)
embed.set_footer(text="Embed Footer Text")
embed.set_timestamp()
# Set `inline=False` for the embed field to occupy the whole line
embed.add_embed_field(name="Field 1", value="Lorem ipsum", inline=False)
embed.add_embed_field(name="Field 2", value="dolor sit", inline=False)
embed.add_embed_field(name="Field 3", value="amet consetetur")
embed.add_embed_field(name="Field 4", value="sadipscing elitr")

webhook.add_embed(embed)
response = webhook.execute()