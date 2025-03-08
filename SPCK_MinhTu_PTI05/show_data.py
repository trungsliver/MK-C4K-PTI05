import main

# Test load data dạng dict (file json)
dtb = accDatabase()
print(len(dtb.acc_dict))

# Test load data dạng object
dtb.load_data()
print(len(dtb.acc_list))


# Sắp xếp
sort1 = dtb.sort_item_by_rating()
sort2 = dtb.sort_item_by_title()

print(sort1)
print(sort2)