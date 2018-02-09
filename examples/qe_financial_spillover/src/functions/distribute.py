import random
from bisect import bisect

""" Helper functions to assign funds to countries """

def distribute_funds_equally(n_funds, list_countries):
    """
	param: n_funds integer
		total number of funds to be assigned to a country
	param: list_countries list of strings
		contains the countries
	returns: list
		evenly distributed list of countries
	"""
    funds = []
    for fund in range(n_funds):
        for i in range(len(list_countries)):
            funds.append(list_countries[i])

    return funds[:n_funds]
	
def weighted_choice(choices):
        """
		param: choices list of tuples
			tuple with (Country, chance of getting country)
			
		returns: string
			chosen country 
		from https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
		"""
        values, weights = zip(*choices)
        total = 0
        cum_weights = []
        for w in weights:
            total += w
            cum_weights.append(total)
        x = random.random() * total
        i = bisect(cum_weights, x)
        return values[i]

def split_equal(parts, value):
    """

    :param parts: number of parts the value will be split into
    :param value:  the value that needs to be divided by parts
    :return: list with equal distributed parts
    """


    value = float(value)
    return [1 * value / parts for i in range(1, parts + 1)]


# Print for testing
# print weighted_choice([("Germany", 85), ("SA", 15)])
# print distribute_funds_equally(4, [250])
# print split_equal(3, 465)

