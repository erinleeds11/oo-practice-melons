############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = None
        self.is_seedless = None
        self.name = name

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas", 2003, "orange", True, False, "Casaba")
    cas.add_pairing("mint")
    cas.add_pairing("strawberries")
    all_melon_types.append(cas)

    cren = MelonType("cren", 1996, "green", True, False, "Crenshaw")
    cren.add_pairing("proscuitto")
    all_melon_types.append(cren)

    yw = MelonType("yw", 2013, "yellow", True, True, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")
        print()

def make_melon_type_lookup(melon_types):

    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}
    for melon in melon_types:
        key = melon.code
        value = melon
        melon_dict[key] = value

    return melon_dict

    ############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, field, person):

        self.melon_type = melon_type
        self.shape_rating =shape_rating
        self.color_rating = color_rating
        self.field = field
        self.person = person

    def is_sellable(self):

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)
    melons = []

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'],10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    melons.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7,
        melon_8, melon_9])

    return melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            can_harvest = "(CAN BE SOLD)"
        else:
            can_harvest = "(NOT SELLABLE)"
        print(f"Harvested by {melon.person} from Field {melon.field} {can_harvest}")



def using_file(filename):
    melon_objects = []
    file = open(filename)
    for line in file:
        line = line.rstrip()
        words = line.split(" ")
        print(words)
        melon = Melon(words[5], words[1], words[3], words[11], words[8])
    melon_objects.append(melon)
    for melon in melon_objects:
        print(melon)

using_file("harvest-log.txt")







