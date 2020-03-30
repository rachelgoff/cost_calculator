toppings_cost_table = {
	'': 0.00,
	'pepperoni': 1.00,
	'mushroom': 0.50,
	'olive': 0.50,
	'anchovy': 2.00,
	'ham': 1.50
}

drinks_cost_table = {
	'small': 2.00,
	'medium': 3.00,
	'large': 3.50,
	'tub': 3.75
}

wings_cost_table = {
	'10': 5.00,
	'20': 9.00,
	'40': 17.50,
	'100': 48.00
}

tax = 0.0625

# get total pizza cost
def get_pizza_cost(*toppings):
	plain_pizza_cost = 13.00
	add_ons_cost = 0.00
	for items in toppings:
		for item in items:
			add_ons_cost = add_ons_cost + toppings_cost_table[item]
	return (plain_pizza_cost + add_ons_cost)

# get total drinks cost
def get_drinks_cost(*drinks):
	drinks_cost = 0.00
	for items in drinks:
		for item in items:
			drinks_cost = drinks_cost + drinks_cost_table[item]
	return drinks_cost

#get wings cost
def get_wings_cost(*wings):
	wings_cost = 0.00
	for items in wings:
		for item in items:
			wings_cost = wings_cost + wings_cost_table[str(item)]
	return wings_cost

#get total cost with tax and coupon calculation
def cost_caculator(*args, **kwargs):
	pizza_cost = 0.00
	drinks_cost = 0.00
	wings_cost = 0.00
	total_cost = 0.00
	coupon_rate = 0.00

	for item in args:
		pizza_cost = get_pizza_cost(item)
		print(pizza_cost) # Verify pizza cost. You can remove from the final code.

	for key, value in kwargs.items():
		if key == 'drinks':
			drinks_cost = get_drinks_cost(value)
			print(drinks_cost) # Verify drinks cost. You can remove from the final code.
		elif key == 'wings':
			wings_cost = get_wings_cost(value)
			print(wings_cost) # Verify wings cost. You can remove from the final code.
		elif key == 'coupon':
			coupon_rate = value

		total_cost = round((pizza_cost + drinks_cost + wings_cost) * (1 + tax) * (1 - coupon_rate), 2)
	
	print(total_cost) # Test the output. You can remove this line from the final code.
	return(total_cost)

cost_caculator([],["ham", "anchovy"], drinks=["tub", "tub"], wings=[10, 20], coupon=0.1) # Give an example to test the output. You can remove this line from the final code.

