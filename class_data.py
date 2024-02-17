class Class:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
class Skills:
    def __init__(self, name, description, level_requirement):
        self.name = name
        self.description = description
        self.level_requirement = level_requirement
        
class Passives:
    def __init__(self, name, description, level_requirement):
        self.name = name
        self.description = description
        self.level_requirement = level_requirement
        
class InnateSkills:
    def __init__(self, name, description):
        self.name = name
        self.description = description        

class_dict = {
    1: Class("Warrior", "Masters of melee combat, skilled in the use of various weapons and armor. They are the frontline defenders."),
    2: Class("Cleric", "Divine healers and supporters, capable of mending wounds and providing powerful blessings to their allies."),
    3: Class("Wizard", "Masters of arcane magic, specializing in the destructive forces of fire, ice, and other elemental powers."),
    4: Class("Rogue", "Stealthy and cunning, rogues excel in sneaking around, disarming traps, and delivering deadly critical strikes."),
    5: Class("Enchanter", "Masters of crowd control and illusion, enchanters manipulate the minds of their enemies and allies alike."),
    6: Class("Druid", "Nature-oriented spellcasters with the ability to heal, shape-shift, and commune with the forces of the wilderness."),
    7: Class("Necromancer", "Masters of death magic, necromancers summon undead minions and wield dark powers to drain life."),
    8: Class("Shadowknight", "Dark knights who combine martial prowess with necromantic abilities, often serving dark deities."),
    9: Class("Monk", "Disciplined warriors who specialize in unarmed combat, evasion, and physical and mental balance."),
    10: Class("Shaman", "Spiritual leaders with a connection to nature and spirits, capable of healing and enhancing their allies."),
    11: Class("Magician", "Summoners of magical creatures and wielders of elemental magic, magicians command powerful summoned beings."),
    12: Class("Bard", "Versatile performers who inspire their allies with music, as well as use magic and weapons to contribute to battles."),
    13: Class("Paladin", "Holy warriors devoted to justice and righteousness, combining martial prowess with divine magic."),
    14: Class("Beastlord", "Masters of nature and animals, beastlords form bonds with powerful animal companions to aid them in battle."),
    15: Class("Ranger", "Skilled outdoorsmen and archers, rangers excel in both ranged combat and survival skills."),
}

## used to duck errors
class DefaultClass:
    def __init__(self):
        self.name = "Default"
        self.starting_hp = 100
        self.starting_mana = 100
        # Add any other default attributes if needed

class WarriorClass:
    def __init__(self):
        self.name = "Warrior"
        self.starting_hp = 150
        self.warrior = Class("Warrior", "Masters of melee combat, skilled in the use of various weapons and armor. They are the frontline defenders.")
        self.skills = {
    2: Skills("Power Strike", "Deliver a powerful strike, dealing extra damage.", 1),
    4: Skills("Cleave", "Perform a sweeping attack, hitting multiple enemies in front of you.", 4),
    7: Skills("Block", "Raise your shield to reduce incoming damage.", 7),
    10: Skills("Reckless Assault", "Launch a series of aggressive strikes, dealing increased damage but reducing your own defense temporarily.", 10),
    13: Skills("Defensive Stance", "Assume a defensive posture, reducing damage taken.", 13),
    16: Skills("Charge", "Dash towards the enemy, stunning and damaging on impact.", 16),
    19: Skills("Bleeding Strike", "Inflict a bleeding effect on the target, causing damage over time.", 19),
    22: Skills("Whirlwind", "Perform a spinning attack, hitting enemies around you.", 22),
    25: Skills("Shield Slam", "Slam your shield into the enemy, briefly stunning them.", 25),
    28: Skills("Mighty Blow", "Unleash a mighty blow, dealing massive damage to a single target.", 28),
    31: Skills("Shield Wall", "Create a defensive shield wall, reducing damage for a duration.", 31),
    34: Skills("Execute", "Deliver a finishing blow to low-health enemies, dealing bonus damage.", 34),
    37: Skills("Rallying Cry", "Boost the morale of allies, granting a temporary bonus to stats.", 37),
    40: Skills("Serrated Sweep", "Execute a powerful sweeping attack, causing bleeding on affected enemies.", 40),
    43: Skills("Blade Storm", "Enter a frenzied state, rapidly striking all nearby enemies with a flurry of powerful slashes.", 43),
    46: Skills("Whirlwind Strike", "Unleash a whirlwind of strikes, hitting all nearby enemies.", 46),
    49: Skills("Warrior's Resolve", "Temporarily increase your resistance to status effects.", 49),
    52: Skills("Thunderous Roar", "Intimidate enemies, reducing their attack and defense.", 52),
    55: Skills("Berserker Rage", "Enter a berserker state, increasing attack speed and damage.", 55),
    58: Skills("Titanic Slam", "Deliver a powerful slam, causing a shockwave and stunning enemies.", 58),
        }
        self.innate_skills = {
            "Taunt": InnateSkills("Taunt", "Taunt your enemies, drawing their attention towards you and away from your allies. Useful for controlling the battlefield."),
            "Defensive Stance": InnateSkills("Defensive Stance", "Assume a defensive stance, reducing incoming damage and increasing your ability to withstand enemy attacks. Ideal for bolstering your defenses in tough situations."),
        }
        self.passives = {
            7: Passives("Counterattack", "Automatically counterattack after a successful block.", 7),
            10: Passives("Riposte", "Counter-attack after successfully blocking an enemy's attack.", 10),
            13: Passives("Dual Wield", "Master the art of dual wielding, allowing you to wield a weapon in each hand.", 13),
            20: Passives("Weapon Expertise", "Gain expertise with your chosen weapon type, increasing damage.", 20),
        }

class ClericClass:
    def __init__(self):
        self.name = "Cleric"
        self.starting_hp = 100
        self.starting_mana = 75
        self.cleric = Class("Cleric", "Divine healers and supporters, capable of mending wounds and providing powerful blessings to their allies.")
        self.skills = {
    2: Skills("Healing Light", "Channel a beam of healing light to restore a moderate amount of health to the target.", 1),
    4: Skills("Divine Shield", "Invoke a protective shield, reducing incoming damage for a short duration.", 4),
    7: Skills("Blessing of Fortitude", "Bless allies with increased stamina, temporarily boosting their maximum health.", 7),
    10: Skills("Sacred Cleanse", "Purify the target, removing harmful debuffs and conditions.", 10),
    13: Skills("Resurrection I", "Revive fallen allies with 0% of lost experience.", 13),
    16: Skills("Divine Intervention", "Intercede on behalf of an ally, redirecting damage to yourself for a short duration.", 16),
    19: Skills("Holy Smite", "Smite enemies with divine power, dealing damage and inflicting holy vulnerability.", 19),
    22: Skills("Renewal", "Restore vitality to the target, gradually replenishing health over time.", 22),
    25: Skills("Divine Vigor", "Infuse allies with divine vigor, increasing their movement and attack speed.", 25),
    28: Skills("Resurrection II", "Revive fallen allies with 25% of lost experience.", 28),
    31: Skills("Divine Wrath", "Unleash a burst of divine energy, damaging enemies in an area.", 31),
    34: Skills("Holy Resilience", "Grant allies increased resistance to incoming damage and status effects.", 34),
    37: Skills("Martyr's Sacrifice", "Take on the damage intended for an ally, sacrificing your health to protect them.", 37),
    40: Skills("Divine Renewal", "Renew the life force of all allies, instantly restoring a significant amount of health.", 40),
    43: Skills("Resurrection III", "Revive fallen allies with 50% of lost experience.", 43),
    46: Skills("Celestial Judgment", "Call down a celestial judgment, damaging and incapacitating enemies in the area.", 46),
    49: Skills("Guardian's Embrace", "Surround a target with a protective aura, nullifying harmful effects and damage.", 49),
    52: Skills("Atonement", "Cleanse the area of negative energy, removing debuffs and restoring health to allies.", 52),
    55: Skills("Eternal Blessing", "Invoke an eternal blessing, providing continuous healing and protection to all allies.", 55),
    58: Skills("Resurrection IV", "Revive fallen allies with 100% of lost experience.", 58),
}
        self.innate_skills = {
            "Healing Touch": InnateSkills("Healing Touch", "Channel a healing touch, restoring a small amount of health to the target."),
        }
class WizardClass:
    def __init__(self):
        self.name = "Wizard"
        self.starting_hp = 75
        self.starting_mana = 100
        self.wizard = Class("Wizard", "Masters of arcane magic, specializing in the destructive forces of fire, ice, and other elemental powers.")
        self.skills = {
    2: Skills("Magic Missle", "Launch an array of arcane missiles at your targets, dealing damage.", 1),
    4: Skills("Mystic Shield", "Summon a mystical shield, reducing incoming damage for a short duration.", 4),
    7: Skills("Elemental Attunement", "Attune to an elemental affinity, enhancing your spells of that element.", 7),
    10: Skills("Arcane Rift", "Create a rift in the fabric of reality, damaging enemies in the target area and distorting space.", 10),
    13: Skills("Mana Surge", "Channel a surge of mana, temporarily boosting mana return.", 13),
    16: Skills("Frost Nova", "Release a burst of frost energy, freezing and damaging nearby enemies.", 16),
    19: Skills("Flamestrike", "Summon a pillar of flames, scorching enemies in the target area.", 19),
    22: Skills("Aetherial Shift", "Shift into the aetherial plane, becoming immune to physical damage for a brief moment.", 22),
    25: Skills("Arcane Mastery", "Tap into arcane mastery, reducing spellcasting cooldowns and resource costs.", 25),
    28: Skills("Meteor Shower", "Summon a shower of meteors, causing widespread destruction in the area.", 28),
    31: Skills("Chain Lightning", "Unleash a chain of lightning bolts, jumping between multiple enemies.", 31),
    34: Skills("Time Warp", "Manipulate time to briefly slow down the movement and actions of enemies.", 34),
    37: Skills("Inferno", "Summon an inferno, engulfing the target area in intense fire.", 37),
    40: Skills("Teleportation Circle", "Create a magical circle, allowing instant teleportation to a designated location.", 40),
    43: Skills("Arcane Explosion", "Trigger a powerful explosion of arcane energy, damaging all nearby foes.", 43),
    46: Skills("Ice Vortex", "Summon a swirling vortex of ice, freezing and pulling in enemies.", 46),
    49: Skills("Mirror Image", "Create illusory duplicates of yourself, confusing and diverting enemy attacks.", 49),
    52: Skills("Nova Barrier", "Generate a protective barrier, absorbing incoming damage for a duration.", 52),
    55: Skills("Astral Projection", "Project your essence into the astral plane, becoming invulnerable for a short time.", 55),
    58: Skills("Arcane Cataclysm", "Channel an overwhelming surge of arcane energy, creating a cataclysmic explosion that obliterates everything in its radius, including the caster.", 58),
        }
        self.innate_skills = {
            "Elemental Attunement": InnateSkills("Elemental Attunement", "Attune to an elemental affinity, enhancing your spells of that element."),
            "Blink": InnateSkills("Blink", "Swiftly teleport a short distance, evading attacks and repositioning."),
            "Arcane Bolt": InnateSkills("Arcane Bolt", "Unleash a quick and precise bolt of arcane energy, dealing minor damage to the target.")
        }