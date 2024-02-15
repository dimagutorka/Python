"""STRINGS FUNCTIONS"""


def length_of_string(string):
	"""return the length of the string"""
	return len(string)


def sum_of_strings(string_1, string_2):
	"""return sum of two strings"""
	return string_1 + string_2


""""INTEGER FUNCTIONS"""


def square(number):
	"""return a square of a number"""
	return number * number


#func can take any amount of args, sum them and return their sum
def sum_of_integers(*args):
	"""return sum of numbers"""
	return sum(args)


def division_of_numbers (number_1, number_2):
	"""return devided number with its remainder"""
	return number_1 / number_2


"""LISTS"""


def average_number_in_list(lst):
	"""return average value in list"""
	return sum(lst) / len(lst)


def merge_lists(lst_1, lst_2):
	lst_3 = lst_1 + lst_2
	"""returns a list consisting of the other two"""
	return lst_3


"""DICTIONARIES"""


def keys_of_dict (dict):
	"""returns the keys of a dictionary"""
	return dict.keys()


#func adds the first dict in the second one and returns it
def merge_dicts(dict_1, dict_2):
	"""returns a second dict with all the values from the first dict"""
	return dict_2.update(dict_1)


dict_1 = {"name": "Karl"}
dict_2 = {"age": 12}
merge_dicts(dict_1,dict_2)


"""SETS"""


def merge_sets(set1, set2):
	"""returns the first set with all unique values from the second set"""
	return set1.union(set2)


#func checks whether the second set is subset of the first one
def sets_similarity (set1, set2):
	"""returns True if the second set is subset of the first one otherwise returns False"""
	if set2.issubset(set1):
		return True
	return False


set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}


"""OTHER FUNCS"""


def even_number_cheker(number):
	"""returns Even if a number is even otherwise returns Odd"""
	if number % 2 == 0:
		return "Even"
	return "Odd"


def list_with_even_numbers(list):
	even_numbers = []  #creting empty list for storing our even values
	for i in list: #check whether our number is even or not by dividing by two modulo
		if i % 2 == 0: #if it's even, we add it in out new created list
			even_numbers.append(i)
	return even_numbers #returns a list with even numbers



car_1 = Car("Audi", "White")
car_2 = Car("BMW", "Black")
car_3 = Car("Hyundai", "Gray")


