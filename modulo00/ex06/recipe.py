cookbook = {
	"bocadillo" : {
		"ingredients" : ["jamon", "pan", "queso", "tomate"],
		"meal" : "almuerzo",
		"prep_time" : 10
	},
	"tarta" : {
		"ingredients" : ["harina", "azucar", "huevos"],
		"meal" : "postre",
		"prep_time" : 60
	},
	"ensalada" : {
		"ingredients" : ["aguacate", "rucula", "tomates", "espinacas"],
		"meal" : "almuerzo",
		"prep_time" : 15
	}
}

def print_recetas():
	for x in cookbook:
		print(x)

def print_receta(name):
	print(cookbook[name])
	print("Recipe for {}:".format(name))
	print("\tIngredients list: {}".format(cookbook[name]["ingredients"]))
	print("\tTo be eaten for {}.".format(cookbook[name]["meal"]))
	print("\tTakes {} minutes of cooking.".format(cookbook[name]["prep_time"]))

def remove_receta(name):
	cookbook.pop(name)

def create_receta():
	print("Enter a name:")
	name = input()
	cookbook[name] = {
		"ingredients" : [],
		"meal" : "",
		"prep_time" : 0
	}
	print("Enter ingredients:")
	while 1:
		ingredient = input()
		if ingredient == "":
			break
		cookbook[name]["ingredients"].append(ingredient)
	print("Enter a meal type:")
	meal = input()
	cookbook[name]["meal"] = meal
	print("Enter a preparation time:")
	time = input()
	if time.isdigit() == True:
		cookbook[name]["prep_time"] = int(time)

def take_receta():
	print("Please enter a recipe name to get its details:")
	receta = input()
	try:
		cookbook[receta]
	except:
		print("Sorry, this receta does not exist.")
		return -1
	return receta

def main():
	print("Welcome to the Python Cookbook !\nList of available option:\n\t1: Add a recipe\n\t2: Delete a recipe\n\t3: Print a recipe\n\t4: Print the cookbook\n\t5: Quit\n")
	while 1:
		print("Please select an option:")
		index = input()
		if not (index.isdigit() == True \
			and int(index) >= 1 and int(index) <= 5):
			print("Sorry, this option does not exist.")
			continue
		idx = int(index)
		if idx == 1:
			create_receta()
		if idx == 2:
			receta = take_receta()
			if receta == -1:
				continue
			remove_receta()
		if idx == 3:
			receta = take_receta()
			if receta == -1:
				continue
			print_receta(receta)
		if idx == 4:
			print_recetas()
		if idx == 5:
			print("Cookbook closed. Goodbye !")
			exit()

if __name__ == "__main__":
	main()