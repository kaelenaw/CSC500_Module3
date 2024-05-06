# get input from user for item 1 of meal
item_name = input('Enter food item name: \n')
item_price = float(input('Enter item price: \n'))
item_quantity = int(input('Enter item quantity: \n'))
item_total = item_quantity * item_price

# get input from user for item 2 of meal
print()
item2_name = input('Enter second food item name: \n')
item2_price = float(input('Enter item price: \n'))
item2_quantity = int(input('Enter item quantity: \n'))
item2_total = item2_quantity * item2_price

# print receipt of items with quantities and item totals, then creates a Sub Total
print()
print('RECEIPT')
print(item_quantity, item_name, '@ $' + '{:.2f}'.format(item_price), '= $' + '{:.2f}'.format(item_total))
print(item2_quantity, item2_name, '@ $' + '{:.2f}'.format(item2_price), '= $' + '{:.2f}'.format(item2_total))
sub_total = item_total + item2_total
print('Sub Total: $' + '{:.2f}'.format(sub_total) + '\n')

# adds gratuity and taxes
tip = sub_total * 0.18
tax = sub_total * 0.07
print('18% gratuity: $' + '{:.2f}'.format((tip)))
print('7% sales tax: $' + '{:.2f}'.format((tax)))
print('Total: $' + '{:.2f}'.format((sub_total + tip + tax)))