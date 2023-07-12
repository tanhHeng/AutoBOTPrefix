import re

def team_add_bot(server):
    server.execute("team add bot")
    server.execute('team modify bot prefix {"text":"[BOT]","color":"aqua"}')
    server.execute('team modify bot displayName {"text":"bot"}')

def on_server_startup(server):
    team_add_bot(server)

def on_load(server, prev_module):
    if server.is_server_startup:
        team_add_bot(server)

def on_player_joined(server, player, info):
    ip = re.match(r"\w+\[([\S]+)]", info.content)
    if ip and ip.groups()[0] == "local":
        server.execute("execute as %s run team join bot"%player)

def on_info(server, info):
    if not info.is_player:
        player = re.match(r"\[BOT](\w+) left the game", info.content)
        if player:
            server.execute("team leave %s"%(player.groups()[0]))