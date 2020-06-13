# Bot's token
token = "NzIxMTQ5ODU1MDQ4OTI1MjU0.XuQgHg.Ml1Faj90z1SEe0dmZy_xRd6GsGE"

# Whether the bot is for testing, if true, stats and errors will not be posted
testing = True

# PUBSUB channel for Redis
ipc_channel = ""

# Number of shards for each cluster
shards_per_cluster = 4

# Additional shards to launch
additional_shards = 0

# The default prefix for commands
default_prefix = "="

# The server to send tickets to, no confirmation messages if set
default_server = None

# Status of the bot
activity = f"DM to Contact Staff | {default_prefix}help"

# The main bot owner
owner = 694367588464984095

# Bot owners that have access to owner commands
owners = [694367588464984095]

# Bot admins that have access to admin commands
admins = [694367588464984095]

# Cogs to load on startup
initial_extensions = [
    "cogs.admin",
    "cogs.communication",
    "cogs.configuration",
    "cogs.core",
    "cogs.direct_message",
    "cogs.error_handler",
    "cogs.events",
    "cogs.general",
    "cogs.miscellaneous",
    "cogs.modmail_channel",
    "cogs.owner",
    "cogs.premium",
    "cogs.snippet",
]

# Channels to send logs
join_channel = 721162089393160212
event_channel = 721162089393160212
admin_channel = 721162089393160212

# The colour used in embeds
primary_colour = 0x1E90FF
user_colour = 0x00FF00
mod_colour = 0xFF4500
error_colour = 0xFF0000

# Version of bot
__version__ = "2.0.0"
