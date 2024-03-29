"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

class Pluralizer:
	@staticmethod
	def pluralize(singular):
		plural = Pluralizer.__aberrant_plural_map.get(singular)

		if plural is None:
			root = singular

			try:
				if singular[-1] == "y" and singular[-2] not in Pluralizer.__vowels:
					root = singular[:-1]
					suffix = "ies"
				elif singular[-1] == "s":
					if singular[-2] in Pluralizer.__vowels:
						if singular[-3:] == "ius":
							root = singular[:-2]
							suffix = "i"
						else:
							root = singular[:-1]
							suffix = "ses"
					else:
						suffix = "es"
				elif singular[-2:] in ("ch", "sh"):
					suffix = "es"
				else:
					suffix = "s"
			except IndexError:
				suffix = "s"

			plural = root + suffix

		return plural

	__aberrant_plural_map = {
		"appendix": "appendices",
		"barracks": "barracks",
		"cactus": "cacti",
		"child": "children",
		"criterion": "criteria",
		"deer": "deer",
		"echo": "echoes",
		"elf": "elves",
		"embargo": "embargoes",
		"focus": "foci",
		"fungus": "fungi",
		"goose": "geese",
		"hero": "heroes",
		"hoof": "hooves",
		"index": "indices",
		"knife": "knives",
		"leaf": "leaves",
		"life": "lives",
		"man": "men",
		"mouse": "mice",
		"nucleus": "nuclei",
		"person": "people",
		"phenomenon": "phenomena",
		"potato": "potatoes",
		"self": "selves",
		"syllabus": "syllabi",
		"tomato": "tomatoes",
		"torpedo": "torpedoes",
		"veto": "vetoes",
		"woman": "women",
		}

	__vowels = set("aeiou")
