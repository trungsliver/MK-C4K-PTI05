import oop

# Test load data dạng dict (file json)
dtb = oop.PlayerDatabase()
print(len(dtb.players_dict))

# Test load data dạng object
dtb.load_data()
print(len(dtb.players_list))

dtb.show_all()
print(dtb.find_player_by_name('Lionel Messi'))