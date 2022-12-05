from EntitiesTable import EntitiesTable, Player, Mob

entities_table = EntitiesTable()

p1 = Player("p1")
print('Summoned new Player')
entities_table.add_entity(p1)

print("Set the time to 15000")
print('Your game mode has been updated to God Mode Mode')
print("Changing to fimbulwinter weather")
print("Set game difficulty to story")
print('Given [Leviathan] * 1 to p1')
entities_table.kill_entity(p1.name)
print('Killed ' + p1.name)
end1 = Mob("end1")
print("Summoned new Dark Elf Lords")
entities_table.add_entity(end1)

entities_table.kill_entity(end1.name)
print('Killed ' + end1.name)
