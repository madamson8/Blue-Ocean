class MapGenerator:

    # MAP GENERATOR FOLLOWS SPECIFIC RULES LAYED OUT HERE
    # EACH ROOM HAS 1 SPAWN POINT. THIS ROOM SHOULD BE DEVOID OF ENEMIES, AND IS RANDOMLY SELECTED AT THE BEGINNING OF MAP GENERATION.
    # AS SUCH, MAP_SIZE IS REQUIRED TO BE >= 1.
    # THE MAP WILL GENERATE IN A MAZE LIKE STRUCTURE, UNLESS LINEAR PROGRESSION IS SPECIFIED. EACH ROOM SHOULD HAVE BLANK AVAILABLE SPACES FOR MONSTER_ID WHICH CAN BE PASSED
    # AND SAVED LATER. THIS WILL ALLOW THE MAIN CLASS TO HAVE CONTROL OVER MONSTER GENERATION, TRAP GENERATION, ETC.

    def __init__(self, map_size, is_linear):
        self.map_size = map_size
        self.is_linear = is_linear

    def generate_map(self):
        pass

    def write_map(self, path):
        pass