from EntitiesTable import EntitiesTable, Player, Mob

entities_table = EntitiesTable()

player1 = Player("player1")
print('Summoned new Player')
entities_table.add_entity(player1)

player2 = Player("player2")
print('Summoned new Player')
entities_table.add_entity(player2)

player3 = Player("player3")
print('Summoned new Player')
entities_table.add_entity(player3)

mob1 = Mob("mob1")
print("Summoned new Exploding Nightmares")
entities_table.add_entity(mob1)

entities_table.kill_entity(player2.name)
print('Killed ' + player2.name)
players = entities_table.get_all_players()
for player in players:
	print('Given [Talon Bow] * 23 to ' + player.name)
player2 = Player("player2")
print('Summoned new Player')
entities_table.add_entity(player2)

print('Teleported player2 to 921, 21, 333')
