import random
from items_data import items_list, items_descriptions
from class_data import *

class Player:
    def __init__(self, player_class, max_hp, max_mana, experience_per_level):
        self.player_class = player_class
        self.level = 1
        self.experience = 0
        self.current_class = None
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.max_mana = max_mana
        self.current_mana = player_class.starting_mana if hasattr(player_class, 'starting_mana') else 0
        self.experience_per_level = experience_per_level

    def choose_class(self, game_classes):
        print("Choose your class:")
        for idx, game_class in enumerate(game_classes, start=1):
            print(f"{idx}. {game_class.name}")

        choice = int(input("Enter the number corresponding to your choice: "))
        if 1 <= choice <= len(game_classes):
            self.current_class = game_classes[choice - 1]
            
            # Set current_mana based on starting_mana if the property exists
            if hasattr(self.current_class, 'starting_mana'):
                self.current_mana = self.current_class.starting_mana
            else:
                self.current_mana = 0
            print(f"You have chosen the {self.current_class.name}.")
        else:
            print("Invalid choice. Please try again.")
    
    def handle_level_up(self):
        while self.experience >= self.experience_needed_for_next_level():
            self.level_up()
    
    def level_up(self):
        self.level += 1
        print(f"Congratulations! You have reached Level {self.level}.")
        # Adjust experience if you want to carry over remaining experience to the next level
        self.experience = 0
        # Implement class-specific level-up bonuses or unlock new skills here
        # Example: self.current_class.skills[NewSkillLevel] = NewSkillObject

    def display_status(self):
        print(f"\nPlayer Status:")
        print(f"Current Level: {self.level}")
        print(f"Current HP: {self.current_hp}/{self.max_hp}")
        # Check if the class has mana before attempting to display it
        if hasattr(self.current_class, 'starting_mana'):
            print(f"Current Mana: {self.current_mana}/{self.current_class.starting_mana}")
        print(f"Experience: {self.experience}/{100 * self.level}")
        if self.current_class:
            print(f"Class: {self.current_class.name}")
        else:
            print("Class: None")

    def heal(self, healing_percentage):
        healing_amount = int(self.max_hp * healing_percentage)
        self.current_hp = min(self.current_hp + healing_amount, self.max_hp)
    
    def experience_needed_for_next_level(self):
        return self.experience_per_level * (self.level ** 2)

class Item:
    def __init__(self, name, tag, description, healing_range=(0.1, 0.25)):
        self.name = name
        self.tag = tag
        self.description = description
        self.healing_range = healing_range   

class Monster:
    def __init__(self, name, hp, damage_range, monster_level):
        self.name = name
        self.hp = hp
        self.damage_range = damage_range
        self.monster_level = monster_level

    def perform_attack(self):
        return random.randint(*self.damage_range)
    
class Inventory:
    def __init__(self):
        self.data = {'gold': 0}
        self.data.update({item['name']: 0 for item in items_list})

    def add_gold(self, amount):
        self.data['gold'] += amount

    def add_item(self, item_name, quantity=1):
        if item_name in self.data:
            self.data[item_name] += quantity
        else:
            self.data[item_name] = quantity

    def use_item(self, item_name, quantity=1):
        if item_name in self.data and self.data[item_name] >= quantity:
            self.data[item_name] -= quantity
            return True
        return False

    def get_gold(self):
        return self.data['gold']

    def get_item_quantity(self, item_name):
        return self.data.get(item_name, 0)

    def display_inventory(self):
        print("\nCurrent Inventory:")
        print(f"Gold: {self.data['gold']}")
        for item, count in self.data.items():
            if item != 'gold' and count > 0:
                print(f"{count} {item}")

    def get_data(self):
        return self.data

# Define monsters with varying degrees of hp, damage range, level
monsters = {
    'goblin': {'name': 'Goblin', 'hp': 20, 'damage_range': (5, 10), 'monster_level': 1},
    'skeleton': {'name': 'Skeleton', 'hp': 30, 'damage_range': (8, 12), 'monster_level': 2},
    'orc': {'name': 'Orc', 'hp': 40, 'damage_range': (10, 15), 'monster_level': 3},
    'troll': {'name': 'Troll', 'hp': 60, 'damage_range': (15, 20), 'monster_level': 4},
    'minotaur': {'name': 'Minotaur', 'hp': 80, 'damage_range': (20, 25), 'monster_level': 5},
    'demon': {'name': 'Demon', 'hp': 100, 'damage_range': (25, 30), 'monster_level': 6},
    'dragon': {'name': 'Dragon', 'hp': 120, 'damage_range': (30, 35), 'monster_level': 7},
    'hydra': {'name': 'Hydra', 'hp': 150, 'damage_range': (35, 40), 'monster_level': 8},
    'behemoth': {'name': 'Behemoth', 'hp': 180, 'damage_range': (40, 45), 'monster_level': 9},
    'eldritch_horror': {'name': 'Eldritch Horror', 'hp': 200, 'damage_range': (45, 50), 'monster_level': 10},
}

def initialize_game():
    player_level = 1
    player_experience = 0
    total_experience_gained = 0
    player_command = ""
    is_standing = False
    experience_per_level = 100
    player_conditions = []
    starting_room = 'map_dungeon01_room1'
    current_room = starting_room
    in_combat = False
    current_monster = None
    debug_mode = False
    direction = ""
    total_rooms = 100
    game_map = generate_rooms(player_level, starting_room, total_rooms)

    # Initialize the inventory as an instance of the Inventory class
    inventory_instance = Inventory()
    # Add a default minor healing potion to the inventory
    inventory_instance.add_item('healing potion (minor)')

    while True:
        print("Choose a class:")
        print("1. Warrior")
        print("2. Cleric")
        print("3. Wizard")
        class_choice = input("Enter the number of your chosen class: ")
        class_mapping = {
            '1': WarriorClass(),
            '2': ClericClass(),
            '3': WizardClass(),
            # Add other classes as needed
        }
        selected_class = class_mapping.get(class_choice)
        if selected_class:
            print(f"Selected Class: {selected_class.name}")
            player_class = selected_class

            # Handle the absence of 'starting_mana' attribute
            max_mana = getattr(selected_class, 'starting_mana', 0)

            player = Player(
                player_class=selected_class,
                max_hp=selected_class.starting_hp,
                max_mana=max_mana,
                experience_per_level=experience_per_level
            )
            player.current_class = selected_class
            equipment = initialize_equipment()
            inventory = inventory_instance

            # Return the necessary variables without using the global keyword
            return (
                player, player_class, player_level, player_experience, total_experience_gained,
                player_command, is_standing, experience_per_level,
                player_conditions, current_room, in_combat, current_monster,
                debug_mode, direction, total_rooms, game_map, inventory, equipment
            )
        else:
            print("Invalid class choice. Please try again.")
        
def initialize_equipment():
    # Initialize the equipment with weapon and armor slots
    equipment = {
        'primary': None,
        'secondary': None,
        'head': None,
        'neck': None,
        'chest': None,
        'arms': None,
        'gloves': None,
        'ring1': None,
        'ring2': None,
        'legs': None,
        'feet': None,
    }
    return equipment

def equip_item(equipment, slot, item_type, items_list):
    # Check if the slot is already occupied
    if equipment[slot] is not None:
        unequip_item(equipment, slot)
    
    # Prompt the user for the item to equip
    print(f"Available {slot} {item_type}s:")
    check_inventory(items_list, item_type=item_type)
    item_to_equip = input(f"Enter the {slot} {item_type} you want to equip: ").lower()

    # Check if the selected item is in the items list
    if item_to_equip in items_list and items_list[item_to_equip]['type'] == item_type:
        equipment[slot] = item_to_equip
        print(f"You equipped {item_to_equip} in the {slot} slot.")
    else:
        print(f"Invalid {item_type} selection. Try again.")

def unequip_item(equipment, slot):
    if equipment[slot] is not None:
        unequipped_item = equipment[slot]
        equipment[slot] = None
        print(f"You unequipped {unequipped_item} from the {slot} slot.")
    else:
        print(f"No item equipped in the {slot} slot.")

def display_equipment(equipment):
    print("\nCurrent Equipment:")
    for slot, item in equipment.items():
        print(f"{slot.capitalize()}: {item if item is not None else 'Empty'}")

    while True:
        choice = input("Enter the number corresponding to your choice: ")
        if choice == "1":
            return WarriorClass()
        elif choice == "2":
            return ClericClass()
        elif choice == "3":
            return WizardClass()
        # Add conditions for other classes

        print("Invalid choice. Please enter a valid number.")

# Toggle the debug mode
def toggle_debug_mode():
    global debug_mode
    debug_mode = not debug_mode
    print(f"Debug mode {'enabled' if debug_mode else 'disabled'}.")
    print("DEBUG: Current Room ID:", current_room)  # DEBUG STATEMENT
    if current_room in game_map:
        print("DEBUG: Room Description:", game_map[current_room]["description"])  # DEBUG STATEMENT
    else:
        print(f"DEBUG: Error - Room '{current_room}' not found in the game_map.")  # DEBUG STATEMENT
    print(f"DEBUG: Player's Inventory: {inventory_instance}")  # NEW DEBUG STATEMENT
    print(f"DEBUG: Player's HP: {player.hp}")  # NEW DEBUG STATEMENT
    print(f"DEBUG: Player's Conditions: {player_conditions}")  # NEW DEBUG STATEMENT
    print(f"DEBUG: Current Monster: {current_monster}")  # NEW DEBUG STATEMENT

# Get the player's action during combat
def get_player_action(monster_name):
    action = input(f"Enter 'attack' to attack the {monster_name}, or 'flee' to run away: ").lower()
    return action

# Handle combat between the player and a monster
def combat(player_hp, current_monster, inventory_instance, player_level, player_experience):
    global in_combat

    def get_player_action(monster_name):
        action = input(f"Enter 'attack' to attack the {monster_name}, or 'flee' to run away: ").lower()
        return action

    def perform_player_attack():
        return random.randint(10, 20)

    def perform_monster_attack(monster):
        return random.randint(*monster['damage_range'])

    initial_monster_hp = current_monster['hp']  # Fix: Access 'hp' key in the dictionary

    while player_hp > 0 and current_monster['hp'] > 0:
        action = get_player_action(current_monster['name'])

        if action == 'attack':
            # Player attacks the monster
            damage_to_monster = perform_player_attack()
            current_monster['hp'] -= damage_to_monster
            print(f"You attack the {current_monster['name']} for {damage_to_monster} damage!")

            if current_monster['hp'] > 0:
                # Monster counter-attacks
                damage_to_player = perform_monster_attack(current_monster)
                player_hp -= damage_to_player
                print(f"The {current_monster['name']} attacks you for {damage_to_player} damage!")

        elif action == 'flee':
            flee_success = random.random() < 0.6
            if flee_success:
                print(f"\nYou barely escape from the {current_monster['name']}!")
                in_combat = False  # Successfully fleeing ends combat
                break
            else:
                print(f"\nYou failed to flee! The {current_monster['name']} gets an attack off.")
                # Handle counter-attack when fleeing fails
                damage_to_player = perform_monster_attack(current_monster)
                player_hp -= damage_to_player
                print(f"The {current_monster['name']} attacks you for {damage_to_player} damage!")

        else:
            print("Invalid command. Try again.")

    if player_hp <= 0:
        print("You have been defeated. Game Over.")

    elif current_monster['hp'] <= 0:
        print(f"You have defeated the {current_monster['name']}!")
        experience_gained = max(0, int(initial_monster_hp * 0.7))
        gold_percentage = random.uniform(0.1, 0.25)
        gold_gained = max(0, int(initial_monster_hp * gold_percentage))

        # Update player's experience
        player_experience += experience_gained

        # Ensure the 'gold' key exists in the Inventory data before accessing it
        if isinstance(inventory_instance, dict):
            if 'gold' not in inventory_instance:
                inventory_instance['gold'] = 0
            else:
                inventory_instance['gold'] += gold_gained
        elif isinstance(inventory_instance, Inventory):
            if 'gold' not in inventory_instance.get_data():
                inventory_instance.add_gold(0)
            else:
                inventory_instance.add_gold(gold_gained)

        print(f"You gained {experience_gained} experience!")
        current_monster = spawn_monster(player_level)

    in_combat = False  # Exit combat after finishing the loop
    return player_hp, player_experience, inventory_instance, player_level

def spawn_monster(player_level):
    if random.random() < 0.5:
        eligible_monsters = [monster_name for monster_name, monster_info in monsters.items() if
                             isinstance(player_level, int) and player_level <= monster_info['monster_level'] <= player_level + 1]

        if eligible_monsters:
            monster_name = random.choice(eligible_monsters)
            monster_info = monsters[monster_name]
            return Monster(name=monster_info['name'], hp=monster_info['hp'], damage_range=monster_info['damage_range'],
                           monster_level=monster_info['monster_level'])
    return None

# Get the player's command input
def get_player_command():
    player_command = input("Enter a command: ").lower()
    return player_command

# Move the player to the next room based on the chosen direction
def move_player(current_room, direction, exits, player):
    global in_combat

    if direction in exits:
        next_room = exits[direction]

        if next_room in game_map:
            current_room = next_room
            current_monster = spawn_monster(player.level)

            if current_monster:
                in_combat = True  # Enter combat if there's a monster
                print(f"A wild {current_monster.name} appears!")  # Access 'name' attribute
            else:
                in_combat = False  # No monster in the room

            return current_room, current_monster
        else:
            print("Invalid direction. Try again.")
            return current_room, None
    else:
        print("Invalid direction. Try again.")
        return current_room, None

def get_healing_range(item_name, items_list):
    item = next((i for i in items_list if i.get('name') == item_name and 'healing_range' in i), None)
    if item and 'healing_range' in item:
        return item['healing_range']
    else:
        return (0.1, 0.25)  # Default healing range for minor potions
    
def check_inventory(inventory_instance):
    
    if isinstance(inventory_instance, Inventory):
        # Access the 'data' attribute of the Inventory class
        gold = inventory_instance.get_gold()
        items = [f"{count} {item}" if item != 'gold' else f"{count} gold" for item, count in inventory_instance.get_data().items() if count > 0 and item != 'gold']
        items_str = ', '.join(items) if items else "Your pouch is empty. No items to display."
        print(f"Gold: {gold if gold > 0 else '0'}")
        print(f"Items: {items_str}")

def use_item(inventory_instance, player_hp, max_hp, items_list, equipment):
    print("Use which item?")
    check_inventory(inventory_instance)  # Display the list of currently held items
    item_to_use = input("Enter the item you want to use: ").lower()  # Convert input to lowercase

    # Check if the user input is a substring of any item in the inventory
    matching_items = [item for item in inventory_instance.get_data() if item_to_use in item.lower()]

    if matching_items:
        # Take the first matching item (you may want to handle multiple matches differently)
        item_to_use = matching_items[0]

        # Check if the used item is an armor piece or weapon
        if item_to_use in ['head', 'chest', 'legs', 'arms', 'gloves', 'ring1', 'ring2', 'neck', 'feet']:
            # Equip the armor
            equip_item(equipment, item_to_use, items_list[item_to_use]['type'], items_list)
        elif item_to_use in ['primary', 'secondary']:
            # Equip the weapon
            equip_item(equipment, item_to_use, items_list[item_to_use]['type'], items_list)
        elif item_to_use in inventory_instance.get_data() and inventory_instance.get_data()[item_to_use] > 0:
            # Handle non-armor items
            healing_range = get_healing_range(item_to_use, items_list)
            healing_amount = int(random.uniform(healing_range[0], healing_range[1]) * max_hp)
            player_hp += healing_amount
            print(f"You used a {item_to_use} and restored {healing_amount} HP.")

            # Update the inventory
            inventory_instance.add_item(item_to_use, -1)

            # Display the updated inventory
            check_inventory(inventory_instance)

            # Ensure the player's HP doesn't exceed the maximum (e.g., 100)
            player_hp = min(player_hp, max_hp)
        else:
            print("Invalid item or no more of that item. Try again.")
    else:
        print("Invalid item. Try again.")

    return player_hp, item_to_use, inventory_instance

## def hiddengive(inventory_instance):
    for item in items_list:
        item_name = item['name']
        if item_name in inventory_instance:
            inventory_instance[item_name] += 1
        else:
            inventory_instance[item_name] = 1
    print("Developer command 'hiddengive' executed. Player received one of each item.")

# Calculate the experience needed for the next level using the formula: experience_per_level * level^2
def experience_needed_for_next_level(current_level):
    return experience_per_level * (current_level ** 2)

def has_usable_item(inventory_instance):
    if isinstance(inventory_instance, dict):
        return bool(inventory_instance and any(count > 0 for count in inventory_instance.values()))
    elif isinstance(inventory_instance, Inventory):
        return bool(inventory_instance.get_data() and any(count > 0 for count in inventory_instance.get_data().values()))
    else:
        print(f"Invalid inventory_instance type: {type(inventory_instance)}")
        return False

def process_player_command(player_command, current_room, current_monster, player, inventory_instance, player_conditions, items_list, equipment):
    global in_combat
    global player_experience

    if player_command.startswith("move"):
        direction = player_command.split(" ", 1)[1]
        return move_player(current_room, direction, game_map[current_room]['exits'], player)

    elif player_command == "toggle debug":
        toggle_debug_mode()

    elif player_command == "status":
        player.display_status()

    elif player_command == "inspect":
        print("Inspecting the room...")
        print(game_map[current_room]['description'])

    elif player_command == "inventory":
        check_inventory(inventory_instance)

    elif player_command == "equipment":
        display_equipment(equipment)

    elif player_command.startswith("use item"):
        return use_item(inventory_instance, player.current_hp, player.max_hp, items_list, equipment)

    elif current_monster and in_combat:
        # Handle actions during combat
        return combat(player.current_hp, current_monster, inventory_instance, player.level)

   ## elif player_command == "hiddengive":
        hiddengive(inventory_instance)

    else:
        print("Invalid command. Try again.")

    return player.current_hp, player_command, current_monster, player_conditions, inventory_instance

# Procedurally generate rooms with random exits
def generate_rooms(player_level, starting_room, total_rooms):
    # Define the game_map
    game_map = {}
    room_descriptions = [
        'You find yourself in a dimly lit room with stone walls.',
        'This room has a low ceiling, and you hear water dripping somewhere.',
        'A large cavernous space with echoes of your footsteps.',
        'The air is thick with ancient dust, and cobwebs hang in the corners.',
        'A mysterious glow emanates from strange runes etched on the walls.',
        'You stumble upon a hidden passage, revealing a secret chamber.',
        'The ground is uneven, and you sense a faint draft from a hidden exit.',
        'A musty odor fills the air, and you notice discarded bones on the floor.',
        'You enter a room adorned with faded tapestries, telling tales of old battles.',
        'The ceiling is so high that your torchlight barely reaches the top.',
    ]

    # Generate a list of eligible monsters based on player's level
    eligible_monsters = [monster_name for monster_name, monster_info in monsters.items() if
                        isinstance(player_level, int) and player_level <= monster_info['monster_level'] <= player_level + 1]
    
    for i in range(1, total_rooms):
        room_id = f'map_dungeon01_room{i}'
        exits = {
            'north': f'map_dungeon01_room{i + 1}' if i < total_rooms - 1 else None,
            'south': f'map_dungeon01_room{i - 1}' if i > 1 else None,
            'east': f'map_dungeon01_room{i + 10}' if i + 10 < total_rooms else None,
            'west': f'map_dungeon01_room{i - 10}' if i - 10 >= 1 else None,
        }
        exits = {direction: room for direction, room in exits.items() if room}
        random.shuffle(list(exits.keys()))

        game_map[room_id] = {
            'description': random.choice(room_descriptions),
            'exits': exits if exits else {'north': 'exit'},
            'monster': random.choice(eligible_monsters) if random.random() < 1.0 else None
        }

    return game_map  # Move the return statement outside the loop

(
    player, player_class, player_level, player_experience, total_experience_gained,
    player_command, is_standing, experience_per_level,
    player_conditions, current_room, in_combat, current_monster,
    debug_mode, direction, total_rooms, game_map, inventory_instance, equipment
) = initialize_game()

# Display available commands based on the player's situation
while True:
    if isinstance(game_map, dict) and current_room in game_map:
        room_info = game_map[current_room]
        exits = room_info.get("exits", {})
    else:
        exits = {}

    available_commands = [f"move {direction}" for direction in exits.keys()] + ["status", "inspect", "inventory", "equipment"]

    if has_usable_item(inventory_instance):
        available_commands.append("use item")

    if debug_mode:
        available_commands.append("toggle debug")  # Allow toggling debug mode in debug mode

    print("Available commands:", ", ".join(available_commands))

    player_command = get_player_command()

    result = process_player_command(player_command, current_room, current_monster, player, inventory_instance, player_conditions, items_list, equipment)

    if result:
        if isinstance(result, tuple):
            player_conditions = None  # Set player_conditions to a default value
            if len(result) == 2:
                player_hp, item_to_use = result  # Update inventory
                inventory_instance = Inventory()
            elif len(result) == 3:
                player_hp, item_to_use, inventory_instance = result  # Update inventory
            elif len(result) == 4:
                player_hp, player_command, current_monster, player_conditions = result
                inventory_instance = result[-1]  # Update inventory from the last element of the tuple
            else:
                # Handle other cases if needed
                pass
    if player_command.startswith("move"):
        direction = player_command.split(" ", 1)[1]
        if direction in exits:
            current_room = exits[direction]
            current_monster = monsters[game_map[current_room].get("monster")]

            if current_monster and not in_combat:
                in_combat = True  # Enter the combat loop for the encounter
                print(f"A wild {current_monster['name']} appears!")  # Print the appearance of the monster
            else:
                print(game_map[current_room]['description'])

            if debug_mode:
                print("DEBUG: Moved to Room ID:", current_room)  # Debug statement
                print("DEBUG: Room Descrip  tion:", game_map[current_room]["description"])  # Debug statement
                print("DEBUG: Current Monster in Room:", current_monster)  # Debug statement

            if in_combat:
                player.current_hp, player.experience, inventory_instance, player.level = combat(player.current_hp, current_monster, inventory_instance, player.level, player.experience)
                current_monster = None  # Reset the current_monster variable after combat
                in_combat = False  # Reset the in_combat flag after combat

        else:
            print("Invalid direction. Try again.")