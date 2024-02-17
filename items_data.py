
def get_healing_range(item_name):
    item = next((i for i in items_list if i.get('name') == item_name and 'healing_range' in i), None)
    if item and 'healing_range' in item:
        return item['healing_range']
    else:
        return (0.1, 0.25)  # Default healing range for minor potions

items_list = [
        {'name': 'sword', 'tag': 'wearable'},
        {'name': 'shield', 'tag': 'wearable'},
        {'name': 'potion', 'tag': 'usable'},
        {'name': 'rusty dagger', 'tag': 'wearable'},
        {'name': 'tattered cloth armor', 'tag': 'wearable'},
        {'name': 'healing potion (minor)', 'tag': 'usable', 'healing_range': (0.1, 0.25)},
        {'name': 'healing potion (major)', 'tag': 'usable', 'healing_range': (0.5, 0.75)},
        {'name': 'goblin tooth necklace', 'tag': 'wearable'},
        {'name': 'copper coins', 'tag': 'usable'},
        {'name': 'small mana crystal', 'tag': 'usable'},
        {'name': 'moldy bread', 'tag': 'usable'},
        {'name': 'goblin ear trophy', 'tag': 'wearable'},
        {'name': 'rat tail whip', 'tag': 'wearable'},
        {'name': 'scroll of magic missile', 'tag': 'usable'},
    ]

# Detailed physical descriptions for magical items
items_descriptions = {
            'Wand of Illumination': 'A slender wand crafted from enchanted willow wood, its surface adorned with intricate silver runes that shimmer softly.',
            'Cloak of Invisibility': 'A velvety cloak woven from the silk of elusive shadow moths, granting its wearer a mystifying ability to blend into the surroundings.',
            'Ring of Teleportation': 'A golden ring encrusted with a mysterious azure gemstone, pulsating with ethereal energies that whisper tales of distant realms.',
            'Potion of Strength': 'A crystal vial filled with a swirling concoction of liquid courage, distilled from the laughter of mountain giants and the essence of ancient oaks.',
            'Crystal Ball of Clairvoyance': 'A flawless crystal sphere that captures the essence of the cosmos within its depths, revealing glimpses of events both past and future.',
            'Amulet of Healing': 'An ornate amulet forged from the tears of healing springs, its intricate design depicting mythical creatures intertwining in a dance of restoration.',
            'Sword of Flames': 'A magnificent sword with a blade forged from the heart of an otherworldly fire, its hilt adorned with phoenix feathers that flicker with eternal flames.',
            'Boots of Speed': 'Ethereal boots crafted from the wind itself, allowing the wearer to move with the swiftness of a zephyr and dance through the air.',
            'Staff of Thunder': 'A majestic staff hewn from ancient thunderstruck oak, its core pulsating with the power of storm giants and echoing with distant thunderclaps.',
            'Shield of Protection': 'A formidable shield crafted from the scales of benevolent dragons, each scale a testament to the guardian spirit woven into its protective enchantment.'
    }