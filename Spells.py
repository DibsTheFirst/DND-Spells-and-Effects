####################################################################################################
# Welcome to the D&D Command Line Interface (CLI)! The purpose of this program is to help DMs      #
# by putting all the information that you regularly need only ONE click away with no loading time! #
####################################################################################################

from Dice import *
from prettytable import PrettyTable
from cmd2 import Cmd, with_argparser, with_category
from cmd2.argparse_completer import *
import shlex
from Info import *
import json

print_rolls = True
list_of_items = []


class Spells(Cmd):
    intro = 'Hello! Please type the name of a spell or effect (all lowercase, underscore in place of space). ' \
            'Type help or ? to list all available commands, or help "command" for its full description.'
    prompt = 'Spell/Effect: '

    # Creates a list with the name of all the items in the item.json file
    with open('data/items.json') as json_file:
        data = json.load(json_file)
        for item in data['item']:
            list_of_items.append(str.lower(item['name']))

    # Creates a completer for the "item" command
    item_parser = ACArgumentParser()
    item_parser.add_argument('item', choices=list_of_items, type=str)

    def __init__(self):
        Cmd.__init__(self)
        hidden_cmds = {'edit', 'alias', 'help', 'history', 'load', 'macro', 'py',
                       'pyscript', 'set', 'shell', 'shortcuts', 'test_all_cmds'}

        self.hidden_commands += hidden_cmds

    @with_category('Other')
    def do_quit(self, arg):
        """Exit the application"""
        print('Goodbye!')
        exit()

    @with_category('Other')
    def do_clear(self, arg):
        """Clears the screen of text by printing 100 empty lines"""
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
              '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    @with_category('Other')
    def do_print_rolls(self, arg):
        """Turned on by default. Turning it off results in only the end sum of die rolls being shown."""
        global print_rolls
        print_rolls = not print_rolls

    @with_category('Other')
    def do_print_all_spells(self, arg):
        """Prints a table which includes all spells. Mostly used for debugging."""
        all_spell_helper()

    @with_category('Other')
    def do_test_all_cmds(self, arg):
        """Hidden command used for debugging."""
        cmds = Cmd.get_visible_commands(self)
        for cmd in cmds:
            Cmd.onecmd(self, cmd)

    @with_category('Utility')
    def do_d4(self, arg):
        """Roll given argument number of d4s"""
        if arg:
            arg = shlex.split(arg)
            if len(arg) == 1 and str.isdigit(arg[0]):
                print(' =', roll_d4(int(arg[0]), print_rolls))
            else:
                print('Invalid Argument')
        else:
            print(d4())

    @with_category('Utility')
    def do_d6(self, arg):
        """Roll given argument number of d6s"""
        if arg:
            arg = shlex.split(arg)
            if len(arg) == 1 and str.isdigit(arg[0]):
                print(' =', roll_d6(int(arg[0]), print_rolls))
            else:
                print('Invalid Argument')
        else:
            print(d6())

    @with_category('Utility')
    def do_d8(self, arg):
        """Roll given argument number of d8s"""
        if arg:
            arg = shlex.split(arg)
            if len(arg) == 1 and str.isdigit(arg[0]):
                print(' =', roll_d8(int(arg[0]), print_rolls))
            else:
                print('Invalid Argument')
        else:
            print(d8())

    @with_category('Utility')
    def do_d10(self, arg):
        """Roll given argument number of d10s"""
        if arg:
            arg = shlex.split(arg)
            if len(arg) == 1 and str.isdigit(arg[0]):
                print(' =', roll_d10(int(arg[0]), print_rolls))
            else:
                print('Invalid Argument')
        else:
            print(d10())

    @with_category('Utility')
    def do_d12(self, arg):
        """Roll given argument number of d12s"""
        if arg:
            arg = shlex.split(arg)
            if len(arg) == 1 and str.isdigit(arg[0]):
                print(' =', roll_d12(int(arg[0]), print_rolls))
            else:
                print('Invalid Argument')
        else:
            print(d12())

    @with_category('Utility')
    def do_d20(self, arg):
        """Roll given argument number of d20s"""
        if arg:
            arg = shlex.split(arg)
            if len(arg) == 1 and str.isdigit(arg[0]):
                print(' =', roll_d20(int(arg[0]), print_rolls))
            else:
                print('Invalid Argument')
        else:
            print(d20())

    @with_category('Utility')
    def do_d100(self, arg):
        """Roll given argument number of d100s"""
        if arg:
            arg = shlex.split(arg)
            if len(arg) == 1 and str.isdigit(arg[0]):
                print(' =', roll_d100(int(arg[0]), print_rolls))
            else:
                print('Invalid Argument')
        else:
            print(d100())

    @with_category('Utility')
    def do_wild_magic(self, arg):
        """Rolls on the wild magic table, can also be used to look up a roll. Optional input: Number from 1 - 100"""
        if arg:
            nr = check_arg_range_100(arg)
            print(wild_magic_table[nr - 1])
        else:
            print(wild_magic_table[d100() - 1])

    @with_category('Utility')
    @with_argparser(item_parser)
    def do_item(self, arg):
        """Takes the name of any item (as a string) as argument and prints that item's information."""
        items = open('data/items.json')
        arg = vars(arg)
        # arg = check_arg_string(arg)
        item_dict = json.load(items)
        items.close()
        for item in item_dict['item']:
            if item['name'].lower() == str.lower(arg['item']):
                print_item(item)

    @with_category('Utility')
    def do_create_character(self, arg):
        """Rolls 4d6 and removes the lowest roll. Does it once for every stat(6 times)."""
        for i in range(6):
            roll_4d6_remove_lowest()

    '''
    @with_category('Utility')
    def do_generate_dungeon(self, arg):
        dungeonGenerator.placeRandomRooms(4, 8, stepSize=1, margin=3, attempts=500)
    '''

    @with_category('Encounters')
    def do_encounter_arctic(self, arg):
        """Returns a random encounter suitable to an arctic region. Requires input: Players' level (1 - 20)"""
        if arg:
            nr = check_arg_range_20(arg)
            if nr <= 4:
                print(arctic_low[d100()])
            elif nr <= 10:
                print(arctic_mid[d100()])
            elif nr <= 16:
                print(arctic_high[d100()])
            elif nr <= 20:
                print(arctic_epic[d100()])
            else:
                pass
        else:
            print("This feature requires the players' level as input (1 - 20).")

    @with_category('Encounters')
    def do_encounter_coastal(self, arg):
        """Returns a random encounter suitable to a coastal region. Requires input: Players' level (1 - 20)"""
        if arg:
            nr = check_arg_range_20(arg)
            if nr <= 4:
                print(coastal_low[d100()])
            elif nr <= 10:
                print(coastal_mid[d100()])
            elif nr <= 16:
                print(coastal_high[d100()])
            elif nr <= 20:
                print(coastal_epic[d100()])
            else:
                pass
        else:
            print("This feature requires the players' level as input (1 - 20).")

    @with_category('Encounters')
    def do_encounter_desert(self, arg):
        """Returns a random encounter suitable to a desert region. Requires input: Players' level (1 - 20)"""
        encounter_helper(arg, 'Desert')

    @with_category('Encounters')
    def do_encounter_forest(self, arg):
        """Returns a random encounter suitable to a forest region. Requires input: Players' level (1 - 20)"""
        encounter_helper(arg, 'Forest')

    @with_category('Encounters')
    def do_encounter_grassland(self, arg):
        """Returns a random encounter suitable to a grassland region. Requires input: Players' level (1 - 20)"""
        encounter_helper(arg, 'Grassland')

    @with_category('Encounters')
    def do_encounter_hill(self, arg):
        """Returns a random encounter suitable to a hill region. Requires input: Players' level (1 - 20)"""
        encounter_helper(arg, 'Hill')

    @with_category('Encounters')
    def do_encounter_mountain(self, arg):
        """Returns a random encounter suitable to a mountain region. Requires input: Players' level (1 - 20)"""
        encounter_helper(arg, 'Mountain')

    @with_category('Encounters')
    def do_encounter_swamp(self, arg):
        """Returns a random encounter suitable to a swamp region. Requires input: Players' level (1 - 20)"""
        encounter_helper(arg, 'Swamp')

    @with_category('Encounters')
    def do_encounter_underdark(self, arg):
        """Returns a random encounter suitable to the Underdark. Requires input: Players' level (1 - 20)"""
        encounter_helper(arg, 'Underdark')

    @with_category('Encounters')
    def do_encounter_underwater(self, arg):
        """Returns a random encounter suitable to an underwater region. Requires input: Players' level (1 - 20)"""
        encounter_helper(arg, 'Underwater')

    @with_category('Encounters')
    def do_encounter_urban(self, arg):
        """Returns a random encounter suitable to an urban area. Requires input: Players' level (1 - 20)"""
        encounter_helper(arg, 'Urban')

    @with_category('Game Rules')
    def do_condition_blinded(self, arg):
        print(blinded)

    @with_category('Game Rules')
    def do_condition_deafened(self, arg):
        print(deafened)

    @with_category('Game Rules')
    def do_condition_exhaustion(self, arg):
        exhaustion()

    @with_category('Game Rules')
    def do_condition_frightened(self, arg):
        print(frightned)

    @with_category('Game Rules')
    def do_condition_grappled(self, arg):
        print(grappled)

    @with_category('Game Rules')
    def do_condition_incapacitated(self, arg):
        print(incapacitated)

    @with_category('Game Rules')
    def do_condition_invisible(self, arg):
        print(invisible)

    @with_category('Game Rules')
    def do_condition_paralyzed(self, arg):
        print(paralyzed)

    @with_category('Game Rules')
    def do_condition_petrified(self, arg):
        print(petrified)

    @with_category('Game Rules')
    def do_condition_poisoned(self, arg):
        print(poisoned)

    @with_category('Game Rules')
    def do_condition_prone(self, arg):
        print(prone)

    @with_category('Game Rules')
    def do_condition_restrained(self, arg):
        print(restrained)

    @with_category('Game Rules')
    def do_condition_stunned(self, arg):
        print(stunned)

    @with_category('Game Rules')
    def do_condition_unconscious(self, arg):
        print(unconscious)

    @with_category('Potions')
    def do_minor(self, arg):
        """Roll given argument number of minor healing potions(2d4+2)"""
        if arg:
            if len(arg) == 1 and str.isdigit(arg[0]):
                for i in range(int(arg)):
                    total = roll_d4(2, print_rolls)
                    print(' + 2 =', total + 2)
            else:
                print('Invalid Argument(s)')
        else:
            total = roll_d4(2, print_rolls)
            print(' + 2 =', total + 2)

    @with_category('Potions')
    def do_greater(self, arg):
        """Roll given argument number of greater healing potions(4d4+4)"""
        if arg:
            if len(arg) == 1 and str.isdigit(arg[0]):
                for i in range(int(arg)):
                    total = roll_d4(4, print_rolls)
                    print(' + 4 =', total + 4)
            else:
                print('Invalid Argument(s)')
        else:
            total = roll_d4(4, print_rolls)
            print(' + 4 =', total + 4)

    @with_category('Potions')
    def do_superior(self, arg):
        """Roll given argument number of superior healing potions(8d4+8)"""
        if arg:
            if len(arg) == 1 and str.isdigit(arg[0]):
                for i in range(int(arg)):
                    total = roll_d4(8, print_rolls)
                    print(' + 8 =', total + 8)
            else:
                print('Invalid Argument(s)')
        else:
            total = roll_d4(8, print_rolls)
            print(' + 8 =', total + 8)

    @with_category('Potions')
    def do_supreme(self, arg):
        """Roll given argument number of supreme healing potions(10d4+20)"""
        if arg:
            if len(arg) == 1 and str.isdigit(arg[0]):
                for i in range(int(arg)):
                    total = roll_d4(10, print_rolls)
                    print(' + 20 =', total + 20)
            else:
                print('Invalid Argument(s)')
        else:
            total = roll_d4(10, print_rolls)
            print(' + 20 =', total + 20)

    @with_category('Spells')
    def do_fireball(self, arg):
        """A bright streak flashes from your pointing finger to a point you choose within range and then blossoms with a low roar into an explosion of flame.
Each creature in a 20-foot-radius sphere centered on that point must make a Dexterity saving throw.
A target takes 8d6 fire damage on a failed save, or half as much damage on a successful one.
The fire spreads around corners. It ignites flammable objects in the area that aren't being worn or carried.
At Higher Levels. When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 for each slot level above 3rd.
Material components: A tiny ball of bat guano and sulfur."""
        print_description('3rd', 'Fireball', '1 Action', 'Instantaneous', '150ft/20ft radius', 'DEX Save', 'Fire',
                          'V, S, M', 'Evocation')
        global print_rolls
        die_rolls = 8
        minimum_spell_level = 3
        cast_d6(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_abi_dalzims_horrid_wilting(self, arg):
        """You draw the moisture from every creature in a 30-foot cube centered on a point you choose within range.
Each creature in that area must make a Constitution saving throw.
Constructs and undead aren’t affected, and plants and water elementals make this saving throw with disadvantage.
A creature takes 12d8 necrotic damage on a failed save, or half as much damage on a successful one.
Nonmagical plants in the area that aren’t creatures, such as trees and shrubs, wither and die instantly.
Material component: A bit of sponge."""
        print_description('8th', "Abi-Dalzim's Horrid Wilting", '1 Action', 'Instantaneous', '150ft/30ft cube',
                          'CON Save', 'Necrotic', 'V, S, M', 'Necromancy')
        global print_rolls
        die_rolls = 12
        minimum_spell_level = 8
        cast_d8(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_absorb_elements(self, arg):
        """The spell captures some of the incoming energy, lessening its effect on you and storing it for your next melee attack.
You have resistance to the triggering damage type until the start of your next turn.
Also, the first time you hit with a melee attack on your next turn, the target takes an extra 1d6 damage of the triggering type, and the spell ends.
At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the extra damage increases by 1d6 for each slot level above 1st."""
        print_description('1st', 'Absorb Elements', '1 Reaction', '1 Round', 'Self', 'None', 'Elemental', 'S',
                          'Abjuration')
        global print_rolls
        die_rolls = 1
        minimum_spell_level = 1
        cast_d6(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_acid_arrow(self, arg):
        """A shimmering green arrow streaks toward a target within range and bursts in a spray of acid.
Make a ranged spell attack against the target. On a hit, the target takes 4d4 acid damage immediately and 2d4 acid damage at the end of its next turn.
On a miss, the arrow splashes the target with acid for half as much of the initial damage and no damage at the end of its next turn.
At Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, the damage (both initial and later) increases by 1d4 for each slot level above 2nd.
Material components: Powdered rhubarb leaf and an adder’s stomach."""
        print_description('2nd', 'Acid Arrow', '1 Action', 'Instantaneous', '90ft', 'Ranged Spell Attack', 'Acid',
                          'V, S, M', 'Evocation')
        global print_rolls
        die_rolls = 4
        minimum_spell_level = 2
        print('Current turn: ', end='')
        cast_d4(die_rolls, minimum_spell_level, arg, print_rolls)
        print('End of next turn: ', end='')
        cast_d4(2, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_acid_splash(self, arg):
        """You hurl a bubble of acid. Choose one or two creatures you can see within range.
If you choose two, they must be within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage.
This spell’s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6)."""
        print_description('Cantrip', 'Acid Splash', '1 Action', 'Instantaneous', '60ft', 'DEX Save', 'Acid',
                          'V, S', 'Abjuration')
        global print_rolls
        die_rolls = 1
        minimum_spell_level = 1
        cast_d6(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_aganazzars_scorcher(self, arg):
        """A line of roaring flame 30 feet long and 5 feet wide emanates from you in a direction you choose.
Each creature in the line must make a Dexterity saving throw.
A creature takes 3d8 fire damage on a failed save, or half as much damage on a successful one.
At Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for each slot level above 2nd.
Material component: A red dragon scale"""
        print_description('2nd', 'Aganazzar’s Scorcher', '1 Action', 'Instantaneous', '30ft/30ft line', 'DEX Save',
                          'Fire', 'V, S, M', 'Evocation')
        global print_rolls
        die_rolls = 3
        minimum_spell_level = 2
        cast_d8(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_aid(self, arg):
        """Your spell bolsters your allies with toughness and resolve. Choose up to three creatures within range.
Each target's hit point maximum and current hit points increase by 5 for the duration.
At Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, a target's hit points increase by an additional 5 for each slot level above 2nd.
Material component: A tiny strip of white cloth."""
        print_description('2nd', 'Aid', '1 Action', '8 Hours', '30ft/3 Creatures', 'None', '+5 To Max HP',
                          'V, S, M', 'Abjuration')

    @with_category('Spells')
    def do_alarm(self, arg):
        """You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot cube.
Until the spell ends, an alarm alerts you whenever a Tiny or larger creature touches or enters the warded area.
When you cast the spell, you can designate creatures that won't set off the alarm. You also choose whether the alarm is mental or audible.
A mental alarm alerts you with a ping in your mind if you are within 1 mile of the warded area. This ping awakens you if you are sleeping.
An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet.
Material component: A tiny bell and a piece of fine silver wire."""
        print_description('1st', 'Alarm', '1 Minute/Ritual', '8 Hours', '30ft/20ft cube', 'None', 'Detection',
                          'V, S, M', 'Abjuration')

    @with_category('Spells')
    def do_alter_self(self, arg):
        """You assume a different form. When you cast the spell, choose one of the following options, the effects of which last for the duration of the spell.
While the spell lasts, you can end one option as an action to gain the benefits of a different one.

Aquatic Adaptation. You adapt your body to an aquatic environment, sprouting gills and growing webbing between your fingers.
You can breathe underwater and gain a swimming speed equal to your walking speed.

Change Appearance. You transform your appearance.
You decide what you look like, including your height, weight, facial features, sound of your voice, hair length, coloration, and distinguishing characteristics, if any.
You can make yourself appear as a member of another race, though none of your statistics change.
You also can't appear as a creature of a different size than you, and your basic shape stays the same; if you're bipedal, you can't use this spell to become quadrupedal, for instance.
At any time for the duration of the spell, you can use your action to change your appearance in this way again.

Natural Weapons. You grow claws, fangs, spines, horns, or a different natural weapon of your choice.
Your unarmed strikes deal 1d6 bludgeoning, piercing, or slashing damage, as appropriate to the natural weapon you chose, and you are proficient with your unarmed strikes.
Finally, the natural weapon is magic and you have a +1 bonus to the attack and damage rolls you make using it."""
        print_description('2nd', 'Alter Self', '1 Action', '1 Hour [C]', 'Self', 'None', 'Shapechanging',
                          'V, S', 'Transmutation')

    @with_category('Spells')
    def do_animal_friendship(self, arg):
        """This spell lets you convince a beast that you mean it no harm. Choose a beast that you can see within range.
It must see and hear you. If the beast's Intelligence is 4 or higher, the spell fails.
Otherwise, the beast must succeed on a Wisdom saving throw or be charmed by you for the spell's duration.
If you or one of your companions harms the target, the spell ends.
At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, you can affect one additional beast level above 1st.
Material component: A morsel of food."""
        print_description('1st', 'Animal Friendship', '1 Action', '24 Hours', '30ft', 'WIS Save', 'Charmed',
                          'V, S, M', 'Enchantment')
        print(d20(), '+ wisdom save modifier')

    @with_category('Spells')
    def do_animal_messenger(self, arg):
        """By means of this spell, you use an animal to deliver a message.
Choose a Tiny beast you can see within range, such as a squirrel, a blue jay, or a bat.
You specify a location, which you must have visited, and a recipient who matches a general description,
such as "a man or woman dressed in the uniform of the town guard" or "a red-haired dwarf wearing a pointed hat."
You also speak a message of up to twenty-five words.
The target beast travels for the duration of the spell toward the specified location,
covering about 50 miles per 24 hours for a flying messenger, or 25 miles for other animals.

When the messenger arrives, it delivers your message to the creature that you described, replicating the sound of your voice.
The messenger speaks only to a creature matching the description you gave.
If the messenger doesn't reach its destination before the spell ends, the message is lost, and the beast makes its way back to where you cast this spell.

At Higher Levels. If you cast this spell using a spell slot of 3rd level or higher, the duration of the spell increases by 48 hours for each slot level above 2nd.
Material component: A morsel of food."""
        print_description('2nd', 'Animal Messenger', '1 Action/Ritual', '24 Hours', '30ft', 'None', 'Communication',
                          'V, S, M', 'Enchantment')

    @with_category('Spells')
    def do_animal_shapes(self, arg):
        """Your magic turns others into beasts. Choose any number of willing creatures that you can see within range.
You transform each target into the form of a Large or smaller beast with a challenge rating of 4 or lower.
On subsequent turns, you can use your action to transform affected creatures into new forms.

The transformation lasts for the duration for each target, or until the target drops to 0 hit points or dies.
You can choose a different form for each target. A target's game statistics are replaced by the statistics of the chosen beast,
though the target retains its alignment and Intelligence, Wisdom, and Charisma scores.
The target assumes the hit points of its new form, and when it reverts to its normal form,
it returns to the number of hit points it had before it transformed.
If it reverts as a result of dropping to 0 hit points, any excess damage carries over to its normal form.
As long as the excess damage doesn't reduce the creature's normal form to 0 hit points, it isn't knocked unconscious.
The creature is limited in the actions it can perform by the nature of its new form, and it can't speak or cast spells.

The target's gear melds into the new form. The target can't activate, wield, or otherwise benefit from any of its equipment."""
        print_description('8th', 'Animal Shapes', '1 Action', '24 Hours [C]', '30ft/Willing Creatures', 'None',
                          'Shapechanging',
                          'V, S', 'Transmutation')

    @with_category('Spells')
    def do_animate_dead(self, arg):
        """This spell creates an undead servant. Choose a pile of bones or a corpse of a Medium or Small humanoid within range.
Your spell imbues the target with a foul mimicry of life, raising it as an undead creature.
The target becomes a skeleton if you chose bones or a zombie if you chose a corpse (the GM has the creature's game statistics).

On each of your turns, you can use a bonus action to mentally command any creature you made with this spell
if the creature is within 60 feet of you (if you control multiple creatures, you can command any or all of them at the same time,
issuing the same command to each one).
You decide what action the creature will take and where it will move during its next turn,
or you can issue a general command, such as to guard a particular chamber or corridor.
If you issue no commands, the creature only defends itself against hostile creatures.
Once given an order, the creature continues to follow it until its task is complete.

The creature is under your control for 24 hours, after which it stops obeying any command you've given it.
To maintain control of the creature for another 24 hours, you must cast this spell on the creature again before the current 24-hour period ends.
This use of the spell reasserts your control over up to four creatures you have animated with this spell, rather than animating a new one.

At Higher Levels. When you cast this spell using a spell slot of 4th level or higher, you animate or reassert control
over two additional undead creatures for each slot level above 3rd. Each of the creatures must come from a different corpse or pile of bones.
Material Component: A drop of blood, a piece of flesh, and a pinch of bone dust."""
        print_description('3rd', 'Animate Dead', '1 Minute', 'Instantaneous', '10ft', 'None', 'Creation',
                          'V, S, M', 'Necromancy')

    @with_category('Spells')
    def do_animate_objects(self, arg):
        """Objects come to life at your command.
Choose up to ten nonmagical objects within range that are not being worn or carried.
Medium targets count as two objects, Large targets count as four objects, Huge targets count as eight objects.
You can't animate any object larger than Huge.
Each target animates and becomes a creature under your control until the spell ends or until reduced to 0 hit points.

As a bonus action, you can mentally command any creature you made with this spell if the creature is within 500 feet of you
(if you control multiple creatures, you can command any or all of them at the same time, issuing the same command to each one).
You decide what action the creature will take and where it will move during its next turn,
or you can issue a general command, such as to guard a particular chamber or corridor.
If you issue no commands, the creature only defends itself against hostile creatures.
Once given an order, the creature continues to follow it until its task is complete.

An animated object is a construct with AC, hit points, attacks, Strength, and Dexterity determined by its size.
Its Constitution is 10 and its Intelligence and Wisdom are 3, and its Charisma is 1.
Its speed is 30 feet; if the object lacks legs or other appendages it can use for locomotion,
it instead has a flying speed of 30 feet and can hover.
If the object is securely attached to a surface or a larger object, such as a chain bolted to a wall, its speed is 0.
It has blindsight with a radius of 30 feet and is blind beyond that distance.
When the animated object drops to 0 hit points, it reverts to its original object form, and any remaining damage carries over to its original object form.

If you command an object to attack, it can make a single melee attack against a creature within 5 feet of it.
It makes a slam attack with an attack bonus and bludgeoning damage determined by its size.
The GM might rule that a specific object inflicts slashing or piercing damage based on its form.

At Higher Levels. If you cast this spell using a spell slot of 6th level or higher, you can animate two additional objects for each slot level above 5th."""
        print_description('5th', 'Animate Objects', '1 Action', '1 Minute [C]', '120ft', 'None', 'Creation',
                          'V, S', 'Transmutation')
        table = PrettyTable()
        table.field_names = ['SIZE', 'HP', 'AC', 'STR', 'DEX', 'ATTACK']
        table.add_row(['Tiny', '20', '18', '4', '18', '+8 to hit, 1d4 + 4 damage'])
        table.add_row(['Small', '25', '16', '6', '14', '+6 to hit, 1d8 + 2 damage'])
        table.add_row(['Medium', '40', '13', '10', '12', '+5 to hit, 2d6 + 1 damage'])
        table.add_row(['Large', '50', '10', '14', '10', '+6 to hit, 2d10 + 2 damage'])
        table.add_row(['Huge', '80', '10', '18', '6', '+8 to hit, 2d12 + 4 damage'])
        print(table)

    @with_category('Spells')
    def do_antilife_shell(self, arg):
        """A shimmering barrier extends out from you in a 10-foot radius and moves with you,
remaining centered on you and hedging out creatures other than undead and constructs.
The barrier lasts for the duration.

The barrier prevents an affected creature from passing or reaching through.
An affected creature can cast spells or make attacks with ranged or reach weapons through the barrier.

If you move so that an affected creature is forced to pass through the barrier, the spell ends."""
        print_description('5th', 'Antilife Shell', '1 Action', '1 Hour [C]', 'Self/10ft Sphere', 'None', 'Control',
                          'V, S', 'Abjuration')

    @with_category('Spells')
    def do_antimagic_field(self, arg):
        """A 10-foot-radius invisible sphere of antimagic surrounds you.
This area is divorced from the magical energy that suffuses the multiverse.
Within the sphere, spells can't be cast, summoned creatures disappear, and even magic items become mundane.
Until the spell ends, the sphere moves with you, centered on you.

Spells and other magical effects, except those created by an artifact or a deity, are suppressed in the sphere
and can't protrude into it. A slot expended to cast a suppressed spell is consumed.
While an effect is suppressed, it doesn't function, but the time it spends suppressed counts against its duration.

Targeted Effects. Spells and other magical effects, such as magic missile and charm person,
that target a creature or an object in the sphere have no effect on that target.

Areas of Magic. The area of another spell or magical effect, such as fireball, can't extend into the sphere.
If the sphere overlaps an area of magic, the part of the area that is covered by the sphere is suppressed.
For example, the flames created by a wall of fire are suppressed within the sphere,
creating a gap in the wall if the overlap is large enough.

Spells. Any active spell or other magical effect on a creature or an object in the sphere is suppressed while the creature or object is in it.

Magic Items. The properties and powers of magic items are suppressed in the sphere. For example, a longsword, +1 in the sphere functions as a nonmagical longsword.

A magic weapon's properties and powers are suppressed if it is used against a target in the sphere or wielded by an attacker in the sphere.
If a magic weapon or a piece of magic ammunition fully leaves the sphere (for example, if you fire a magic arrow or
throw a magic spear at a target outside the sphere), the magic of the item ceases to be suppressed as soon as it exits.

Magical Travel. Teleportation and planar travel fail to work in the sphere, whether the sphere is the destination or
the departure point for such magical travel. A portal to another location, world, or plane of existence, as well as an
opening to an extradimensional space such as that created by the rope trick spell, temporarily closes while in the sphere.

Creatures and Objects. A creature or object summoned or created by magic temporarily winks out of existence in the sphere.
Such a creature instantly reappears once the space the creature occupied is no longer within the sphere.

Dispel Magic. Spells and magical effects such as dispel magic have no effect on the sphere. Likewise,
the spheres created by different antimagic field spells don't nullify each other.

Material Components: A pinch of powdered iron or iron filings."""
        print_description('8th', 'Antimagic Field', '1 Action', '1 Hour [C]', 'Self/10ft Sphere ', 'None', 'Control',
                          'V, S, M', 'Abjuration')

    @with_category('Spells')
    def do_antipathy_sympathy(self, arg):
        """This spell attracts or repels creatures of your choice. You target something within range,
either a Huge or smaller object or creature or an area that is no larger than a 200-foot cube.
Then specify a kind of intelligent creature, such as red dragons, goblins, or vampires.
You invest the target with an aura that either attracts or repels the specified creatures for the duration.
Choose antipathy or sympathy as the aura's effect.

Antipathy. The enchantment causes creatures of the kind you designated to feel an intense urge to leave the area and avoid the target.
When such a creature can see the target or comes within 60 feet of it, the creature must succeed on a Wisdom saving throw or become frightened.
The creature remains frightened while it can see the target or is within 60 feet of it.
While frightened by the target, the creature must use its movement to move to the nearest safe spot from which it can't see the target.
If the creature moves more than 60 feet from the target and can't see it, the creature is no longer frightened,
but the creature becomes frightened again if it regains sight of the target or moves within 60 feet of it.

Sympathy. The enchantment causes the specified creatures to feel an intense urge to approach the target while within 60 feet of it or able to see it.
When such a creature can see the target or comes within 60 feet of it, the creature must succeed on a Wisdom saving throw
or use its movement on each of its turns to enter the area or move within reach of the target.
When the creature has done so, it can't willingly move away from the target.

If the target damages or otherwise harms an affected creature, the affected creature can make a Wisdom saving throw to end the effect, as described below.

Ending the Effect. If an affected creature ends its turn while not within 60 feet of the target or able to see it,
the creature makes a Wisdom saving throw. On a successful save, the creature is no longer affected by the target and
recognizes the feeling of repugnance or attraction as magical. In addition, a creature affected by the spell is allowed
another Wisdom saving throw every 24 hours while the spell persists.

A creature that successfully saves against this effect is immune to it for 1 minute, after which time it can be affected again.

Material Components: Either a lump of alum soaked in vinegar for the antipathy effect or a drop of honey for the sympathy effect."""
        print_description('8th', 'Antipathy/Sympathy', '1 Hour', '10 Days', '60ft/200ft Cube', 'WIS Save', 'Frightened',
                          'V, S, M', 'Enchantment')
        print('Wisdom Save:', d20())

    @with_category('Spells')
    def do_arcane_eye(self, arg):
        """You create an invisible, magical eye within range that hovers in the air for the duration.

You mentally receive visual information from the eye, which has normal vision and darkvision out to 30 feet.
The eye can look in every direction.

As an action, you can move the eye up to 30 feet in any direction. There is no limit to how far away from you the eye
can move, but it can't enter another plane of existence. A solid barrier blocks the eye's movement,
but the eye can pass through an opening as small as 1 inch in diameter.

Material Component: A bit of bat fur."""
        print_description('4th', 'Arcane Eye', '1 Action', '1 Hour [C]', '30ft', 'None', 'Detection',
                          'V, S, M', 'Divination')

    @with_category('Spells')
    def do_arcane_gate(self, arg):
        """You create linked teleportation portals that remain open for the duration.
Choose two points on the ground that you can see, one point within 10 feet of you and one point within 500 feet of you.
A circular portal, 10 feet in diameter, opens over each point. If the portal would open in the space occupied by a creature, the spell fails, and the casting is lost.

The portals are two-dimensional glowing rings filled with mist, hovering inches from the ground and perpendicular to it at the points you choose.
A ring is visible only from one side (your choice), which is the side that functions as a portal.

Any creature or object entering the portal exits from the other portal as if the two were adjacent to each other;
passing through a portal from the nonportal side has no effect. The mist that fills each portal is opaque and blocks vision through it.
On your turn, you can rotate the rings as a bonus action so that the active side faces in a different direction."""
        print_description('6th', 'Arcane Gate', '1 Action', '10 Minutes [C]', '500ft', 'None', 'Teleportation',
                          'V, S', 'Conjuration')

    @with_category('Spells')
    def do_arcane_hand(self, arg):
        """You create a Large hand of shimmering, translucent force in an unoccupied space that you can see within range.
The hand lasts for the spell's duration, and it moves at your command, mimicking the movements of your own hand.

The hand is an object that has AC 20 and hit points equal to your hit point maximum. If it drops to 0 hit points, the spell ends.
It has a Strength of 26 (+8) and a Dexterity of 10 (+0). The hand doesn't fill its space.
When you cast the spell and as a bonus action on your subsequent turns, you can move the hand up to 60 feet and then cause one of the following effects with it.

Clenched Fist. The hand strikes one creature or object within 5 feet of it. Make a melee spell attack for the hand using your game statistics. On a hit, the target takes 4d8 force damage.

Forceful Hand. The hand attempts to push a creature within 5 feet of it in a direction you choose. Make a check with the hand's Strength contested by the Strength (Athletics) check of the target. If the target is Medium or smaller, you have advantage on the check. If you succeed, the hand pushes the target up to 5 feet plus a number of feet equal to five times your spellcasting ability modifier. The hand moves with the target to remain within 5 feet of it.

Grasping Hand. The hand attempts to grapple a Huge or smaller creature within 5 feet of it. You use the hand's Strength score to resolve the grapple. If the target is Medium or smaller, you have advantage on the check. While the hand is grappling the target, you can use a bonus action to have the hand crush it. When you do so, the target takes bludgeoning damage equal to 2d6 + your spellcasting ability modifier.

Interposing Hand. The hand interposes itself between you and a creature you choose until you give the hand a different command. The hand moves to stay between you and the target, providing you with half cover against the target. The target can't move through the hand's space if its Strength score is less than or equal to the hand's Strength score. If its Strength score is higher than the hand's Strength score, the target can move toward you through the hand's space, but that space is difficult terrain for the target.

At Higher Levels. When you cast this spell using a spell slot of 6th level or higher, the damage from the clenched fist option increases by 2d8 and the damage from the grasping hand increases by 2d6 for each slot level above 5th.

Material Components: An eggshell and a snakeskin glove."""
        print_description('5th', 'Arcane Hand', '1 Action', '1 Minute [C]', '120ft', 'None', 'Force/Control',
                          'V, S, M', 'Evocation')
        global print_rolls
        die_rolls = 4
        minimum_spell_level = 5
        print('Clenched Fist: ', end='')
        cast_d8(die_rolls, minimum_spell_level, arg, print_rolls, 2)
        print('Grasping Hand: ', end='')
        cast_d6(die_rolls, minimum_spell_level, arg, print_rolls, 2)

    @with_category('Spells')
    def do_arcane_lock(self, arg):
        """You touch a closed door, window, gate, chest, or other entryway, and it becomes locked for the duration. You and the creatures you designate when you cast this spell can open the object normally. You can also set a password that, when spoken within 5 feet of the object, suppresses this spell for 1 minute. Otherwise, it is impassable until it is broken or the spell is dispelled or suppressed. Casting knock on the object suppresses arcane lock for 10 minutes.

While affected by this spell, the object is more difficult to break or force open; the DC to break it or pick any locks on it increases by 10.

Material Component: Gold dust worth at least 25 gp, which the spell consumes."""
        print_description('2nd', 'Arcane Lock', '1 Action', 'Until Dispelled', 'Touch', 'None', 'Utility',
                          'V, S, M', 'Abjuration')

    @with_category('Spells')
    def do_arcane_weapon(self, arg):
        """You channel arcane energy into one simple or martial weapon you’re holding, and choose one damage type: acid, cold, fire, lightning, poison, or thunder. Until the spell ends, you deal an extra 1d6 damage of the chosen type to any target you hit with the weapon. If the weapon isn’t magical, it becomes a magic weapon for the spell’s duration.

As a bonus action, you can change the damage type, choosing from the options above.

At Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, you can maintain your concentration on the spell for up to 8 hours."""
        print_description('1st', 'Arcane Weapon', '1 Bonus Action', '1 Hour [C]', 'Self', 'None', 'Elemental/Buff',
                          'V, S', 'Transmutation')

    @with_category('Spells')
    def do_arcanists_magic_aura(self, arg):
        """You place an illusion on a creature or an object you touch so that divination spells reveal false information about it. The target can be a willing creature or an object that isn't being carried or worn by another creature.
When you cast the spell, choose one or both of the following effects. The effect lasts for the duration. If you cast this spell on the same creature or object every day for 30 days, placing the same effect on it each time, the illusion lasts until it is dispelled.

False Aura. You change the way the target appears to spells and magical effects, such as detect magic, that detect magical auras. You can make a nonmagical object appear magical, a magical object appear nonmagical, or change the object's magical aura so that it appears to belong to a specific school of magic that you choose. When you use this effect on an object, you can make the false magic apparent to any creature that handles the item.

Mask. You change the way the target appears to spells and magical effects that detect creature types, such as a paladin's Divine Sense or the trigger of a symbol spell. You choose a creature type and other spells and magical effects treat the target as if it were a creature of that type or of that alignment.

Material Component: A small square of silk."""
        print_description('2nd', "Arcanist's Magic Aura", '1 Action', '24 Hours', 'Touch', 'None', 'Deception',
                          'V, S, M', 'Illusion')

    @with_category('Spells')
    def do_armor_of_agathys(self, arg):
        """A protective magical force surrounds you, manifesting as a spectral frost that covers you and your gear. You gain 5 temporary hit points for the duration. If a creature hits you with a melee attack while you have these hit points, the creature takes 5 cold damage.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, both the temporary hit points and the cold damage increase by 5 for each slot.

Material Component: A cup of water."""
        print_description('1st', 'Armor of Agathys', '1 Action', '1 Hour', 'Self', 'None', 'Cold',
                          'V, S, M', 'Abjuration')

    @with_category('Spells')
    def do_arms_of_hadar(self, arg):
        """You invoke the power of Hadar, the Dark Hunger. Tendrils of dark energy erupt from you and batter all creatures within 10 feet of you. Each creature in that area must make a Strength saving throw. On a failed save, a target takes 2d6 necrotic damage and can’t take reactions until its next turn. On a successful save, the creature takes half damage, but suffers no other effect.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st."""
        print_description('1st', 'Arms of Hadar', '1 Action', 'Instantaneous', 'Self/10ft Sphere', 'STR Save',
                          'Necrotic',
                          'V, S', 'Conjuration')
        global print_rolls
        die_rolls = 2
        minimum_spell_level = 1
        cast_d6(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_astral_projection(self, arg):
        """You and up to eight willing creatures within range project your astral bodies into the Astral Plane (the spell fails and the casting is wasted if you are already on that plane). The material body you leave behind is unconscious and in a state of suspended animation; it doesn't need food or air and doesn't age.

Your astral body resembles your mortal form in almost every way, replicating your game statistics and possessions. The principal difference is the addition of a silvery cord that extends from between your shoulder blades and trails behind you, fading to invisibility after 1 foot. This cord is your tether to your material body. As long as the tether remains intact, you can find your way home. If the cord is cut--something that can happen only when an effect specifically states that it does--your soul and body are separated, killing you instantly.

Your astral form can freely travel through the Astral Plane and can pass through portals there leading to any other plane. If you enter a new plane or return to the plane you were on when casting this spell, your body and possessions are transported along the silver cord, allowing you to re-enter your body as you enter the new plane. Your astral form is a separate incarnation. Any damage or other effects that apply to it have no effect on your physical body, nor do they persist when you return to it.

The spell ends for you and your companions when you use your action to dismiss it. When the spell ends, the affected creature returns to its physical body, and it awakens.

The spell might also end early for you or one of your companions. A successful dispel magic spell used against an astral or physical body ends the spell for that creature. If a creature's original body or its astral form drops to 0 hit points, the spell ends for that creature. If the spell ends and the silver cord is intact, the cord pulls the creature's astral form back to its body, ending its state of suspended animation.

If you are returned to your body prematurely, your companions remain in their astral forms and must find their own way back to their bodies, usually by dropping to 0 hit points.

Material Component: For each creature you affect with this spell, you must provide one jacinth worth at least 1,000 gp and one ornately carved bar of silver worth at least 100 gp, all of which the spell consumes"""
        print_description('9th', 'Astral Projection', '1 Hour', 'Special', '10ft', 'None', 'Teleportation',
                          'V, S, M', 'Necromancy')

    @with_category('Spells')
    def do_augury(self, arg):
        """By casting gem-inlaid sticks, rolling dragon bones, laying out ornate cards, or employing some other divining tool, you receive an omen from an otherworldly entity about the results of a specific course of action that you plan to take within the next 30 minutes. The DM chooses from the following possible omens:

Weal, for good results
Woe, for bad results
Weal and woe, for both good and bad results
Nothing, for results that aren't especially good or bad

The spell doesn't take into account any possible circumstances that might change the outcome, such as the casting of additional spells or the loss or gain of a companion.

If you cast the spell two or more times before completing your next long rest, there is a cumulative 25 percent chance for each casting after the first that you get a random reading. The DM makes this roll in secret.

Material Components: Specially marked sticks, bones, or similar tokens worth at least 25 gp."""
        print_description('2nd', 'Augury', '1 Minute [R]', 'Instantaneous', 'Self', 'None', 'Foreknowledge',
                          'V, S, M', 'Divination')

    @with_category('Spells')
    def do_aura_of_life(self, arg):
        """Life-preserving energy radiates from you in an aura with a 30-foot radius.  Until the spell ends, the aura moves with you, centered on you. Each nonhostile creature in the aura (including you) has resistance to necrotic damage, and its hit point maximum can’t be reduced. In addition, a nonhostile, living creature regains 1 hit point when it starts its turn in the aura with 0 hit points."""
        print_description('4th', 'Aura of Life', '1 Action', '10 Minutes [C]', 'Self/30ft Sphere', 'None', 'Healing',
                          'V', 'Abjuration')

    @with_category('Spells')
    def do_aura_of_purity(self, arg):
        """Purifying energy radiates from you in an aura with a 30-foot radius. Until the spell ends, the aura moves with you, centered on you. Each nonhostile creature in the aura (including you) can’t become diseased, has resistance to poison damage, and has advantage on saving throws against effects that cause any of the following conditions: blinded, charmed, deafened, frightened, paralyzed, poisoned, and stunned."""
        print_description('4th', 'Aura of Purity', '1 Action', '10 Minutes [C]', 'Self/30ft Sphere', 'None', 'Buff',
                          'V', 'Abjuration')

    @with_category('Spells')
    def do_aura_of_vitality(self, arg):
        """Healing energy radiates from you in an aura with a 30-foot radius. Until the spell ends, the aura moves with you, centered on you. You can use a bonus action to cause one creature in the aura (including you) to regain 2d6 hit points."""
        print_description('3rd', 'Aura of Vitality', '1 Action', '1 Minute [C]', 'Self/30ft Sphere', 'None', 'Healing',
                          'V', 'Evocation')
        global print_rolls
        self.do_d6('2')

    @with_category('Spells')
    def do_awaken(self, arg):
        """After spending the casting time tracing magical pathways within a precious gemstone, you touch a Huge or smaller beast or plant. The target must have either no Intelligence score or an Intelligence of 3 or less. The target gains an Intelligence of 10. The target also gains the ability to speak one language you know. If the target is a plant, it gains the ability to move its limbs, roots, vines, creepers, and so forth, and it gains senses similar to a human's. Your GM chooses statistics appropriate for the awakened plant, such as the statistics for the awakened shrub or the awakened tree.

The awakened beast or plant is charmed by you for 30 days or until you or your companions do anything harmful to it. When the charmed condition ends, the awakened creature chooses whether to remain friendly to you, based on how you treated it while it was charmed.

Stats: https://www.dndbeyond.com/monsters/awakened-shrub - https://www.dndbeyond.com/monsters/awakened-tree

Material Component: An agate worth at least 1,000 gp, which the spell consumes"""
        print_description('5th', 'Awaken', '8 Hours', 'Instantaneous', 'Touch', 'None', 'Charmed',
                          'V, S, M', 'Transmutation')

    @with_category('Spells')
    def do_bane(self, arg):
        """Up to three creatures of your choice that you can see within range must make Charisma saving throws. Whenever a target that fails this saving throw makes an attack roll or a saving throw before the spell ends, the target must roll a d4 and subtract the number rolled from the attack roll or saving throw.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st.

Material Component: A drop of blood."""
        print_description('1st', 'Bane', '1 Action', '1 Minute [C]', '30ft', 'CHA Save', 'Debuff',
                          'V, S, M', 'Enchantment')
        print('Charisma save:', d20())

    @with_category('Spells')
    def do_banishing_smite(self, arg):
        """The next time you hit a creature with a weapon attack before this spell ends, your weapon crackles with force, and the attack deals an extra 5d10 force damage to the target.

Additionally, if this attack reduces the target to 50 hit points of fewer, you banish it. If the target is native to a different plane of existence than the on you’re on, the target disappears, returning to its home plane. If the target is native to the plane you’re on, the creature vanishes into a harmless demiplane. While there, the target is incapacitated. It remains there until the spell ends, at which point the target reappears in the space it left or in the nearest unoccupied space if that space is occupied."""
        print_description('5th', 'Banishing Smite', '1 Bonus Action', '1 Minute [C]', 'Self', 'None', 'Force',
                          'V', 'Abjuration')
        self.do_d10('5')

    @with_category('Spells')
    def do_banishment(self, arg):
        """You attempt to send one creature that you can see within range to another plane of existence. The target must succeed on a Charisma saving throw or be banished.

If the target is native to the plane of existence you're on, you banish the target to a harmless demiplane. While there, the target is incapacitated. The target remains there until the spell ends, at which point the target reappears in the space it left or in the nearest unoccupied space if that space is occupied.

If the target is native to a different plane of existence than the one you're on, the target is banished with a faint popping noise, returning to its home plane. If the spell ends before 1 minute has passed, the target reappears in the space it left or in the nearest unoccupied space if that space is occupied. Otherwise, the target doesn't return.

At Higher Levels. When you cast this spell using a spell slot of 5th level or higher, you can target one additional creature for each slot level above 4th.

Material Component: An item distasteful to the target"""
        print_description('4th', 'Banishment', '1 Action', '1 Minute [C]', '60ft', 'CHA Save', 'Banishment',
                          'V, S, M', 'Abjuration')
        print('Charisma Save:', d20())

    @with_category('Spells')
    def do_barkskin(self, arg):
        """You touch a willing creature. Until the spell ends, the target's skin has a rough, bark-like appearance, and the target's AC can't be less than 16, regardless of what kind of armor it is wearing.

Material Component: A handful of oak bark."""
        print_description('2nd', 'Barkskin', '1 Action', '1 Hour [C]', 'Touch', 'None', 'Buff',
                          'V, S, M', 'Transmutation')

    @with_category('Spells')
    def do_beacon_of_hope(self, arg):
        """This spell bestows hope and vitality. Choose any number of creatures within range. For the duration, each target has advantage on Wisdom saving throws and death saving throws, and regains the maximum number of hit points possible from any healing."""
        print_description('3rd', 'Beacon of Hope', '1 Action', '1 Minute [C]', '30ft', 'None', 'Buff',
                          'V, S', 'Abjuration')

    @with_category('Spells')
    def do_beast_bond(self, arg):
        """You establish a telepathic link with one beast you touch that is friendly to you or charmed by you. The spell fails if the beast’s Intelligence is 4 or higher. Until the spell ends, the link is active while you and the beast are within line of sight of each other. Through the link, the beast can understand your telepathic messages to it, and it can telepathically communicate simple emotions and concepts back to you. While the link is active, the beast gains advantage on attack rolls against any creature within 5 feet of you that you can see.

    Material Component: A bit of fur wrapped in a cloth"""
        print_description('1st', 'Beast Bond', '1 Action', '10 Minutes [C]', 'Touch', 'None', 'Buff',
                          'V, S, M', 'Divination')

    @with_category('Spells')
    def do_beast_sense(self, arg):
        """You touch a willing beast. For the duration of the spell, you can use your action to see through the beast’s eyes and hear what it hears, and continue to do so until you use your action to return to your normal senses."""
        print_description('2nd', 'Beast Sense', '1 Action [R]', '1 Hour [C]', 'Touch', 'None', 'Detection',
                          'S', 'Divination')

    @with_category('Spells')
    def do_bestow_curse(self, arg):
        """
You touch a creature, and that creature must succeed on a Wisdom saving throw or become cursed for the duration of the spell. When you cast this spell, choose the nature of the curse from the following options:

Choose one ability score. While cursed, the target has disadvantage on ability checks and saving throws made with that ability score.
While cursed, the target has disadvantage on attack rolls against you.
While cursed, the target must make a Wisdom saving throw at the start of each of its turns. If it fails, it wastes its action that turn doing nothing.
While the target is cursed, your attacks and spells deal an extra 1d8 necrotic damage to the target.

A remove curse spell ends this effect. At the DM's option, you may choose an alternative curse effect, but it should be no more powerful than those described above. The DM has final say on such a curse's effect.

At Higher Levels. If you cast this spell using a spell slot of 4th level or higher, the duration is concentration, up to 10 minutes. If you use a spell slot of 5th level or higher, the duration is 8 hours. If you use a spell slot of 7th level or higher, the duration is 24 hours. If you use a 9th level spell slot, the spell lasts until it is dispelled. Using a spell slot of 5th level or higher grants a duration that doesn't require concentration."""
        print_description('3rd', 'Bestow Curse', '1 Action', '1 Minute [C]', 'Touch', 'WIS Save', 'Debuff',
                          'V, S', 'Necromancy')
        print('Wisdom Save:', d20())

    @with_category('Spells')
    def do_bigbys_hand(self, arg):
        """*shamooone* You create a Large hand of shimmering, translucent force in an unoccupied space that you can see within range.
The hand lasts for the spell's duration, and it moves at your command, mimicking the movements of your own hand.

The hand is an object that has AC 20 and hit points equal to your hit point maximum. If it drops to 0 hit points, the spell ends.
It has a Strength of 26 (+8) and a Dexterity of 10 (+0). The hand doesn't fill its space.
When you cast the spell and as a bonus action on your subsequent turns, you can move the hand up to 60 feet and then cause one of the following effects with it.

Clenched Fist. The hand strikes one creature or object within 5 feet of it. Make a melee spell attack for the hand using your game statistics. On a hit, the target takes 4d8 force damage.

Forceful Hand. The hand attempts to push a creature within 5 feet of it in a direction you choose. Make a check with the hand's Strength contested by the Strength (Athletics) check of the target. If the target is Medium or smaller, you have advantage on the check. If you succeed, the hand pushes the target up to 5 feet plus a number of feet equal to five times your spellcasting ability modifier. The hand moves with the target to remain within 5 feet of it.

Grasping Hand. The hand attempts to grapple a Huge or smaller creature within 5 feet of it. You use the hand's Strength score to resolve the grapple. If the target is Medium or smaller, you have advantage on the check. While the hand is grappling the target, you can use a bonus action to have the hand crush it. When you do so, the target takes bludgeoning damage equal to 2d6 + your spellcasting ability modifier.

Interposing Hand. The hand interposes itself between you and a creature you choose until you give the hand a different command. The hand moves to stay between you and the target, providing you with half cover against the target. The target can't move through the hand's space if its Strength score is less than or equal to the hand's Strength score. If its Strength score is higher than the hand's Strength score, the target can move toward you through the hand's space, but that space is difficult terrain for the target.

At Higher Levels. When you cast this spell using a spell slot of 6th level or higher, the damage from the clenched fist option increases by 2d8 and the damage from the grasping hand increases by 2d6 for each slot level above 5th.

Material Components: An eggshell and a snakeskin glove."""
        print_description('5th', "Bigby's Hand", '1 Action', '1 Minute [C]', '120ft', 'None', 'Force/Control',
                          'V, S, M', 'Evocation')
        global print_rolls
        die_rolls = 4
        minimum_spell_level = 5
        print('Clenched Fist: ', end='')
        cast_d8(die_rolls, minimum_spell_level, arg, print_rolls, 2)
        print('Grasping Hand: ', end='')
        cast_d6(die_rolls, minimum_spell_level, arg, print_rolls, 2)

    @with_category('Spells')
    def do_black_tentacles(self, arg):
        """Squirming, ebony tentacles fill a 20-foot square on ground that you can see within range. For the duration, these tentacles turn the ground in the area into difficult terrain.

When a creature enters the affected area for the first time on a turn or starts its turn there, the creature must succeed on a Dexterity saving throw or take 3d6 bludgeoning damage and be restrained by the tentacles until the spell ends. A creature that starts its turn in the area and is already restrained by the tentacles takes 3d6 bludgeoning damage.

A creature restrained by the tentacles can use its action to make a Strength or Dexterity check (its choice) against your spell save DC. On a success, it frees itself.

Material Component: A piece of tentacle from a giant octopus or a giant squid."""
        print_description('4th', 'Black Tentacles', '1 Action', '1 Minute [C]', '90ft', 'DEX Save', 'Restrained',
                          'V, S, M', 'Conjuration')

    @with_category('Spells')
    def do_blade_barrier(self, arg):
        """You create a vertical wall of whirling, razor-sharp blades made of magical energy. The wall appears within range and lasts for the duration. You can make a straight wall up to 100 feet long, 20 feet high, and 5 feet thick, or a ringed wall up to 60 feet in diameter, 20 feet high, and 5 feet thick. The wall provides three-quarters cover to creatures behind it, and its space is difficult terrain.

When a creature enters the wall's area for the first time on a turn or starts its turn there, the creature must make a Dexterity saving throw. On a failed save, the creature takes 6d10 slashing damage. On a successful save, the creature takes half as much damage."""
        print_description('6th', 'Blade Barrier', '1 Action', '10 Minutes [C]', '90ft', 'DEX Save', 'Slashing',
                          'V, S', 'Evocation')
        self.do_d10('6')

    @with_category('Spells')
    def do_blade_ward(self, arg):
        """You extend your hand and trace a sigil of warding in the air. Until the end of your next turn, you have resistance against bludgeoning, piercing, and slashing damage dealt by weapon attacks."""
        print_description('Cantrip', 'Blade Ward', '1 Action', '1 Round', 'Self', 'None', 'Warding',
                          'V, S', 'Abjuration')

    @with_category('Spells')
    def do_bless(self, arg):
        """You bless up to three creatures of your choice within range. Whenever a target makes an attack roll or a saving throw before the spell ends, the target can roll a d4 and add the number rolled to the attack roll or saving throw.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st.

Material Component: A sprinkling of holy water."""
        print_description('1st', 'Bless', '1 Action', '1 Minute [C]', '30ft', 'None', 'Buff',
                          'V, S, M', 'Enchantment')

    @with_category('Spells')
    def do_blight(self, arg):
        """Necromantic energy washes over a creature of your choice that you can see within range, draining moisture and vitality from it. The target must make a Constitution saving throw. The target takes 8d8 necrotic damage on a failed save, or half as much damage on a successful one. This spell has no effect on undead or constructs.

If you target a plant creature or a magical plant, it makes the saving throw with disadvantage, and the spell deals maximum damage to it.

If you target a nonmagical plant that isn't a creature, such as a tree or shrub, it doesn't make a saving throw; it simply withers and dies.

At Higher Levels. When you cast this spell using a spell slot of 5th level or higher, the damage increases by 1d8 for each slot level above 4th."""
        print_description('4th', 'Blight', '1 Action', 'Instantaneous', '30ft', 'CON Save', 'Necrotic',
                          'V, S', 'Necromancy')
        global print_rolls
        die_rolls = 8
        minimum_spell_level = 4
        cast_d8(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_blinding_smite(self, arg):
        """The next time you hit a creature with a melee weapon attack during this spell’s duration, you weapon flares with a bright light, and the attack deals an extra 3d8 radiant damage to the target. Additionally, the target must succeed on a Constitution saving throw or be blinded until the spell ends.

A creature blinded by this spell makes another Constitution saving throw at the end of each of its turns. On a successful save, it is no longer blinded."""
        print_description('3rd', 'Blinding Smite', '1 Bonus Action', '1 Minute [C]', 'Self', 'CON Save',
                          'Radiant/Blind', 'V', 'Evocation')
        self.do_d8('3')

    @with_category('Spells')
    def do_blindness_deafness(self, arg):
        """You can blind or deafen a foe. Choose one creature that you can see within range to make a Constitution saving throw. If it fails, the target is either blinded or deafened (your choice) for the duration. At the end of each of its turns, the target can make a Constitution saving throw. On a success, the spell ends.

At Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, you can target one additional creature for each slot level above 2nd."""
        print_description('2nd', 'Blindness/Deafness', '1 Action', '1 Minute', '30ft', 'CON Save', 'Blinded/Deafened',
                          'V', 'Necromancy')
        print('Constitution Save:', d20())

    @with_category('Spells')
    def do_blink(self, arg):
        """Roll a d20 at the end of each of your turns for the duration of the spell. On a roll of 11 or higher, you vanish from your current plane of existence and appear in the Ethereal Plane (the spell fails and the casting is wasted if you were already on that plane). At the start of your next turn, and when the spell ends if you are on the Ethereal Plane, you return to an unoccupied space of your choice that you can see within 10 feet of the space you vanished from. If no unoccupied space is available within that range, you appear in the nearest unoccupied space (chosen at random if more than one space is equally near). You can dismiss this spell as an action.

While on the Ethereal Plane, you can see and hear the plane you originated from, which is cast in shades of gray, and you can't see anything there more than 60 feet away. You can only affect and be affected by other creatures on the Ethereal Plane. Creatures that aren't there can't perceive you or interact with you, unless they have the ability to do so."""
        print_description('3rd', 'Blink', '1 Action', '1 Minute', 'Self', 'None', 'Utility',
                          'V, S', 'Transmutation')
        d20()

    @with_category('Spells')
    def do_blur(self, arg):
        """Your body becomes blurred, shifting and wavering to all who can see you. For the duration, any creature has disadvantage on attack rolls against you. An attacker is immune to this effect if it doesn't rely on sight, as with blindsight, or can see through illusions, as with truesight."""
        print_description('2nd', 'Blur', '1 Action', '1 Minute [C]', 'Self', 'None', 'Deception/Warding',
                          'V', 'Illusion')

    @with_category('Spells')
    def do_bones_of_the_earth(self, arg):
        """You cause up to six pillars of stone to burst from places on the ground that you can see within range. Each pillar is a cylinder that has a diameter of 5 feet and a height of up to 30 feet. The ground where a pillar appears must be wide enough for its diameter, and you can target the ground under a creature if that creature is Medium or smaller. Each pillar has AC 5 and 30 hit points. When reduced to 0 hit points, a pillar crumbles into rubble, which creates an area of difficult terrain with a 10-foot radius that lasts until the rubble is cleared. Each 5-foot-diameter portion of the area requires at least 1 minute to clear by hand.

If a pillar is created under a creature, that creature must succeed on a Dexterity saving throw or be lifted by the pillar. A creature can choose to fail the save.

If a pillar is prevented from reaching its full height because of a ceiling or other obstacle, a creature on the pillar takes 6d6 bludgeoning damage and is restrained, pinched between the pillar and the obstacle. The restrained creature can use an action to make a Strength or Dexterity check (the creature’s choice) against the spell’s save DC. On a success, the creature is no longer restrained and must either move off the pillar or fall off it.

At Higher Levels. When you cast this spell using a spell slot of 7th level or higher, you can create two additional pillars for each slot level above 6th."""
        print_description('6th', 'Bones of the Earth', '1 Action', 'Instantaneous', '120ft/30ft Cylinder', 'DEX Save',
                          'Bludgeoning', 'V, S', 'Transmutation')
        self.do_d6('6')

    @with_category('Spells')
    def do_booming_blade(self, arg):
        """As part of the action used to cast this spell, you must make a melee attack with a weapon against one creature within the spell’s range, otherwise the spell fails. On a hit, the target suffers the attack’s normal effects, and it becomes sheathed in booming energy until the start of your next turn. If the target willingly moves before then, it immediately takes 1d8 thunder damage, and the spell ends.

This spell’s damage increases when you reach higher levels. At 5th level, the melee attack deals an extra 1d8 thunder damage to the target, and the damage the target takes for moving increases to 2d8. Both damage rolls increase by 1d8 at 11th level and 17th level.

Material Component: A weapon"""
        print_description('Cantrip', 'Booming Blade', '1 Action', '1 Round', '5ft', 'Melee Attack', 'Thunder',
                          'V, M', 'Evocation')
        global print_rolls
        die_rolls = 1
        minimum_spell_level = 1
        cast_d8(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_branding_smite(self, arg):
        """The next time you hit a creature with a weapon attack before this spell ends, the weapon gleams with astral radiance as you strike. The attack deals an extra 2d6 radiant damage to the target, which becomes visible if it is invisible, and the target sheds dim light in a 5-foot radius and can’t become invisible until the spell ends.

At Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, the extra damage increases by 1d6 for each slot level above 2nd."""
        print_description('2nd', 'Branding Smite', '1 Bonus Action', '1 Minute [C]', 'Self', 'None', 'Radiant',
                          'V', 'Evocation')
        global print_rolls
        die_rolls = 2
        minimum_spell_level = 2
        cast_d6(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_burning_hands(self, arg):
        """As you hold your hands with thumbs touching and fingers spread, a thin sheet of flames shoots forth from your outstretched fingertips. Each creature in a 15-foot cone must make a Dexterity saving throw. A creature takes 3d6 fire damage on a failed save, or half as much damage on a successful one.

The fire ignites any flammable objects in the area that aren't being worn or carried.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st."""
        print_description('1st', 'Burning Hands', '1 Action', 'Instantaneous', 'Self/15ft Cone', 'DEX Save', 'Fire',
                          'V, S', 'Evocation')
        global print_rolls
        die_rolls = 3
        minimum_spell_level = 1
        cast_d6(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_call_lightning(self, arg):
        """A storm cloud appears in the shape of a cylinder that is 10 feet tall with a 60-foot radius, centered on a point you can see within range directly above you. The spell fails if you can't see a point in the air where the storm cloud could appear (for example, if you are in a room that can't accommodate the cloud).

When you cast the spell, choose a point you can see under the cloud. A bolt of lightning flashes down from the cloud to that point. Each creature within 5 feet of that point must make a Dexterity saving throw. A creature takes 3d10 lightning damage on a failed save, or half as much damage on a successful one. On each of your turns until the spell ends, you can use your action to call down lightning in this way again, targeting the same point or a different one.
If you are outdoors in stormy conditions when you cast this spell, the spell gives you control over the existing storm instead of creating a new one. Under such conditions, the spell's damage increases by 1d10.

At Higher Levels. When you cast this spell using a spell slot of 4th or higher level, the damage increases by 1d10 for each slot level above 3rd."""
        print_description('3rd', 'Call Lightning', '1 Action', '10 Minutes [C]', '120ft/60ft Cone', 'DEX Save',
                          'Lightning', 'V, S', 'Conjuration')
        global print_rolls
        die_rolls = 3
        minimum_spell_level = 3
        print('Normal Conditions: ', end='')
        cast_d10(die_rolls, minimum_spell_level, arg, print_rolls)
        print('Stormy Conditions: ', end='')
        cast_d10(4, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_calm_emotions(self, arg):
        """You attempt to suppress strong emotions in a group of people. Each humanoid in a 20-foot-radius sphere centered on a point you choose within range must make a Charisma saving throw; a creature can choose to fail this saving throw if it wishes. If a creature fails its saving throw, choose one of the following two effects.

You can suppress any effect causing a target to be charmed or frightened. When this spell ends, any suppressed effect resumes, provided that its duration has not expired in the meantime.

Alternatively, you can make a target indifferent about creatures of your choice that it is hostile toward. This indifference ends if the target is attacked or harmed by a spell or if it witnesses any of its friends being harmed. When the spell ends, the creature becomes hostile again, unless the GM rules otherwise."""
        print_description('2nd', 'Calm Emotions', '1 Action', '1 Minute [C]', '60ft/20ft Sphere', 'CHA Save', 'Charmed',
                          'V, S', 'Enchantment')

    @with_category('Spells')
    def do_catapult(self, arg):
        """Choose one object weighing 1 to 5 pounds within range that isn’t being worn or carried. The object flies in a straight line up to 90 feet in a direction you choose before falling to the ground, stopping early if it impacts against a solid surface. If the object would strike a creature, that creature must make a Dexterity saving throw. On a failed save, the object strikes the target and stops moving. When the object strikes something, the object and what it strikes each take 3d8 bludgeoning damage.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the maximum weight of objects that you can target with this spell increases by 5 pounds, and the damage increases by 1d8, for each slot level above 1st."""
        print_description('1st', 'Catapult', '1 Action', 'Instantaneous', '60ft', 'DEX Save', 'Bludgeoning',
                          'S', 'Transmutation')
        global print_rolls
        die_rolls = 3
        minimum_spell_level = 1
        cast_d8(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_catnap(self, arg):
        """You make a calming gesture, and up to three willing creatures of your choice that you can see within range fall unconscious for the spell’s duration. The spell ends on a target early if it takes damage or someone uses an action to shake or slap it awake. If a target remains unconscious for the full duration, that target gains the benefit of a short rest, and it can’t be affected by this spell again until it finishes a long rest.

At Higher Levels. When you cast this spell using a spell slot of 4th level or higher, you can target one additional willing creature for each slot level above 3rd.

Material Component: A pinch of sand"""
        print_description('3rd', 'Catnap', '1 Action', '10 Minutes', '30ft', 'None', 'Buff',
                          'S, M', 'Enchantment')

    @with_category('Spells')
    def do_cause_fear(self, arg):
        """You awaken the sense of mortality in one creature you can see within range. A construct or an undead is immune to this effect. The target must succeed on a Wisdom saving throw or become frightened of you until the spell ends. The frightened target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st. The creatures must be within 30 feet of each other when you target them."""
        print_description('1st', '', 'Cause Fear', '1 Minute [C]', '60ft', 'WIS Save', 'Frightened',
                          'V', 'Necromancy')

    @with_category('Spells')
    def do_ceremony(self, arg):
        """You perform a special religious ceremony that is infused with magic. When you cast the spell, choose one of the following rites, the target of which must be within 10 feet of you throughout the casting.

Atonement. You touch one willing creature whose alignment has changed, and you make a DC 20 Wisdom (Insight) check. On a successful check, you restore the target to its original alignment.

Bless Water. You touch one vial of water and cause it to become holy water.

Coming of Age. You touch one humanoid who is a young adult. For the next 24 hours, whenever the target makes an ability check, it can roll a d4 and add the number rolled to the ability check. A creature can benefit from this rite only once.

Dedication. You touch one humanoid who wishes to be dedicated to your god’s service. For the next 24 hours, whenever the target makes a saving throw, it can roll a d4 and add the number rolled to the save. A creature can benefit from this rite only once.

Funeral Rite. You touch one corpse, and for the next 7 days, the target can’t become undead by any means short of a wish spell.

Wedding. You touch adult humanoids willing to be bonded together in marriage. For the next 7 days, each target gains a +2 bonus to AC while they are within 30 feet of each other. A creature can benefit from this rite again only if widowed.

Material Component: 25 gp worth of powdered silver, which the spell consumes."""
        print_description('1st', 'Ceremony', '1 Hour [R]', 'Instantaneous', 'Touch', 'None', 'Buff',
                          'V, S, M', 'Abjuration')

    @with_category('Spells')
    def do_chain_lightning(self, arg):
        """You create a bolt of lightning that arcs toward a target of your choice that you can see within range. Three bolts then leap from that target to as many as three other targets, each of which must be within 30 feet of the first target. A target can be a creature or an object and can be targeted by only one of the bolts.

A target must make a Dexterity saving throw. The target takes 10d8 lightning damage on a failed save, or half as much damage on a successful one.

At Higher Levels. When you cast this spell using a spell slot of 7th level or higher, one additional bolt leaps from the first target to another target for each slot level above 6th.

Material Components: A bit of fur; a piece of amber, glass, or a crystal rod; and three silver pins."""
        print_description('6th', 'Chain Lightning', '1 Action', 'Instantaneous', '150ft', 'DEX Save', 'Lightning',
                          'V, S, M', 'Evocation')
        self.do_d8('10')

    @with_category('Spells')
    def do_chaos_bolt(self, arg):
        """You hurl an undulating, warbling mass of chaotic energy at one creature in range. Make a ranged spell attack against the target. On a hit, the target takes 2d8 + 1d6 damage. Choose one of the d8s. The number rolled on that die determines the attack’s damage type, as shown below.

If you roll the same number on both d8s, the chaotic energy leaps from the target to a different creature of your choice within 30 feet of it. Make a new attack roll against the new target, and make a new damage roll, which could cause the chaotic energy to leap again.

A creature can be targeted only once by each casting of this spell.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, each target takes 1d6 extra damage of the type rolled for each slot level above 1st."""
        print_description('1st', 'Chaos Bolt', '1 Action', 'Instantaneous', '120ft', 'Ranged Attack', 'Elemental',
                          'V, S', 'Evocation')
        table = PrettyTable()
        table.add_column('d8', ['1', '2', '3', '4', '5', '6', '7', '8'])
        table.add_column('Damage Type', ['Acid', 'Cold', 'Fire', 'Force', 'Lightning', 'Poison', 'Psychic', 'Thunder'])
        print(table)
        global print_rolls
        print('d6: ', end='')
        die_rolls = 1
        minimum_spell_level = 1
        cast_d6(die_rolls, minimum_spell_level, arg, print_rolls)
        print('d8: ', end='')
        self.do_d8('2')

    @with_category('Spells')
    def do_charm_monster(self, arg):
        """You attempt to charm a creature you can see within range. It must make a Wisdom saving throw, and it does so with advantage if you or your companions are fighting it. If it fails the saving throw, it is charmed by you until the spell ends or until you or your companions do anything harmful to it. The charmed creature is friendly to you. When the spell ends, the creature knows it was charmed by you.

At Higher Levels. When you cast this spell using a spell slot of 5th level or higher, you can target one additional creature for each slot level above 4th. The creatures must be within 30 feet of each other when you target them."""
        print_description('4th', 'Charm Monster', '1 Action', '1 Hour', '30ft', 'WIS Save', 'Charmed',
                          'V, S', 'Enchantment')

    @with_category('Spells')
    def do_charm_person(self, arg):
        """You attempt to charm a humanoid you can see within range. It must make a Wisdom saving throw, and does so with advantage if you or your companions are fighting it. If it fails the saving throw, it is charmed by you until the spell ends or until you or your companions do anything harmful to it. The charmed creature regards you as a friendly acquaintance. When the spell ends, the creature knows it was charmed by you.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature for each slot level above 1st. The creatures must be within 30 feet of each other when you target them."""
        print_description('1st', 'Charm Person', '1 Action', '1 Hour', '30ft', 'WIS Save', 'Charmed',
                          'V, S', 'Enchantment')

    @with_category('Spells')
    def do_chill_touch(self, arg):
        """You create a ghostly, skeletal hand in the space of a creature within range. Make a ranged spell attack against the creature to assail it with the chill of the grave. On a hit, the target takes 1d8 necrotic damage, and it can't regain hit points until the start of your next turn. Until then, the hand clings to the target.

If you hit an undead target, it also has disadvantage on attack rolls against you until the end of your next turn.

This spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."""
        print_description('Cantrip', 'Chill Touch', '1 Action', '1 Round', '120ft', 'Ranged Attack', 'Necrotic',
                          'V, S', 'Necromancy')
        global print_rolls
        die_rolls = 1
        minimum_spell_level = 1
        cast_d8(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_chromatic_orb(self, arg):
        """You hurl a 4-inch-diameter sphere of energy at a creature that you can see within range. You choose acid, cold, fire, lightning, poison, or thunder for the type of orb you create, and then make a ranged spell attack against the target. If the attack hits, the creature takes 3d8 damage of the type you chose.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st.

Material Component: A diamond worth at least 50 gp."""
        print_description('1st', 'Chromatic Orb', '1 Action', 'Instantaneous', '90ft', 'Ranged Attack', 'Elemental',
                          'V, S, M', 'Evocation')
        global print_rolls
        die_rolls = 3
        minimum_spell_level = 1
        cast_d8(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_circle_of_death(self, arg):
        """A sphere of negative energy ripples out in a 60-foot- radius sphere from a point within range. Each creature in that area must make a Constitution saving throw. A target takes 8d6 necrotic damage on a failed save, or half as much damage on a successful one.

At Higher Levels. When you cast this spell using a spell slot of 7th level or higher, the damage increases by 2d6 for each slot level above 6th.

Material Component: The powder of a crushed black pearl worth at least 500 gp."""
        print_description('6th', 'Circle of Death', '1 Action', 'Instantaneous', '150ft/60ft Sphere', 'CON Save',
                          'Necrotic', 'V, S, M', 'Necromancy')
        global print_rolls
        die_rolls = 8
        minimum_spell_level = 6
        cast_d6(die_rolls, minimum_spell_level, arg, print_rolls, 2)

    @with_category('Spells')
    def do_circle_of_power(self, arg):
        """Divine energy radiates from you, distorting and diffusing magical energy within 30 feet of you. Until the spell ends, the sphere moves with you, centered on you. For the duration, each friendly creature in the area (including you) has advantage on saving throws against spells and other magical effects.

Additionally, when an affected creature succeeds on a saving throw made against a spell or magical effect that allows it to make a saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throws."""
        print_description('5th', 'Circle of Power', '1 Action', '10 Minutes [C]', 'Self/30ft Sphere', 'None', 'Buff',
                          'V', 'Abjuration')

    @with_category('Spells')
    def do_clairvoyance(self, arg):
        """You create an invisible sensor within range in a location familiar to you (a place you have visited or seen before) or in an obvious location that is unfamiliar to you (such as behind a door, around a corner, or in a grove of trees). The sensor remains in place for the duration, and it can't be attacked or otherwise interacted with.

When you cast the spell, you choose seeing or hearing. You can use the chosen sense through the sensor as if you were in its space. As your action, you can switch between seeing and hearing.

A creature that can see the sensor (such as a creature benefiting from see invisibility or truesight) sees a luminous, intangible orb about the size of your fist.

Material Component: A focus worth at least 100 gp, either a jeweled horn for hearing or a glass eye for seeing."""
        print_description('3rd', 'Clairvoyance', '10 Minutes', '10 Minutes [C]', '1 Mile', 'None', 'Detection',
                          'V, S, M', 'Divination')

    @with_category('Spells')
    def do_clone(self, arg):
        """This spell grows an inert duplicate of a living, Medium creature as a safeguard against death. This clone forms inside a sealed vessel and grows to full size and maturity after 120 days; you can also choose to have the clone be a younger version of the same creature. It remains inert and endures indefinitely, as long as its vessel remains undisturbed.

At any time after the clone matures, if the original creature dies, its soul transfers to the clone, provided that the soul is free and willing to return. The clone is physically identical to the original and has the same personality, memories, and abilities, but none of the original's equipment. The original creature's physical remains, if they still exist, become inert and can't thereafter be restored to life, since the creature's soul is elsewhere.

Material Components: A diamond worth at least 1,000 gp and at least 1 cubic inch of flesh of the creature that is to be cloned, which the spell consumes, and a vessel worth at least 2,000 gp that has a sealable lid and is large enough to hold a Medium creature, such as a huge urn, coffin, mud- filled cyst in the ground, or crystal container filled with salt water."""
        print_description('8th', 'Clone', '1 Hour', 'Instantaneous', 'Touch', 'None', 'Utility',
                          'V, S, M', 'Necromancy')

    @with_category('Spells')
    def do_cloud_of_daggers(self, arg):
        """You fill the air with spinning daggers in a cube 5 feet on each side, centered on a point you choose within range. A creature takes 4d4 slashing damage when it enters the spell’s area for the first time on a turn or starts its turn there.

At Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 2d4 for each slot level above 2nd.

Material Component: A silver of glass."""
        print_description('2nd', 'Cloud of Daggers', '1 Action', '1 Minute [C]', '60ft/5ft Cube', 'None', 'Slashing',
                          'V, S, M', 'Conjuration')
        global print_rolls
        die_rolls = 4
        minimum_spell_level = 2
        cast_d4(die_rolls, minimum_spell_level, arg, print_rolls, 2)

    @with_category('Spells')
    def do_cloudkill(self, arg):
        """You create a 20-foot-radius sphere of poisonous, yellow-green fog centered on a point you choose within range. The fog spreads around corners. It lasts for the duration or until strong wind disperses the fog, ending the spell. Its area is heavily obscured.

When a creature enters the spell's area for the first time on a turn or starts its turn there, that creature must make a Constitution saving throw. The creature takes 5d8 poison damage on a failed save, or half as much damage on a successful one. Creatures are affected even if they hold their breath or don't need to breathe.

The fog moves 10 feet away from you at the start of each of your turns, rolling along the surface of the ground. The vapors, being heavier than air, sink to the lowest level of the land, even pouring down openings.

At Higher Levels. When you cast this spell using a spell slot of 6th level or higher, the damage increases by 1d8 for each slot level above 5th."""
        print_description('5th', 'Cloudkill', '1 Action', '10 Minutes [C]', '120ft/20ft Sphere', 'CON Save', 'Poison',
                          'V, S', 'Conjuration')
        global print_rolls
        die_rolls = 5
        minimum_spell_level = 5
        cast_d8(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_color_spray(self, arg):
        """A dazzling array of flashing, colored light springs from your hand. Roll 6d10; the total is how many hit points of creatures this spell can affect. Creatures in a 15-foot cone originating from you are affected in ascending order of their current hit points (ignoring unconscious creatures and creatures that can't see).

Starting with the creature that has the lowest current hit points, each creature affected by this spell is blinded until the end of your next turn. Subtract each creature's hit points from the total before moving on to the creature with the next lowest hit points. A creature's hit points must be equal to or less than the remaining total for that creature to be affected.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, roll an additional 2d10 for each slot level above 1st.

Material Component: A pinch of powder or sand that is colored red, yellow, and blue."""
        print_description('1st', 'Color Spray', '1 Action', '1 Round', 'Self, 15ft Cone', 'None', 'Blinded',
                          'V, S, M', 'Illusion')
        global print_rolls
        die_rolls = 6
        minimum_spell_level = 1
        cast_d10(die_rolls, minimum_spell_level, arg, print_rolls, 2)

    @with_category('Spells')
    def do_command(self, arg):
        """You speak a one-word command to a creature you can see within range. The target must succeed on a Wisdom saving throw or follow the command on its next turn. The spell has no effect if the target is undead, if it doesn't understand your language, or if your command is directly harmful to it.

Some typical commands and their effects follow. You might issue a command other than one described here. If you do so, the GM determines how the target behaves. If the target can't follow your command, the spell ends.

Approach. The target moves toward you by the shortest and most direct route, ending its turn if it moves within 5 feet of you.

Drop. The target drops whatever it is holding and then ends its turn.

Flee. The target spends its turn moving away from you by the fastest available means.

Grovel. The target falls prone and then ends its turn.

Halt. The target doesn't move and takes no actions. A flying creature stays aloft, provided that it is able to do so. If it must move to stay aloft, it flies the minimum distance needed to remain in the air.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, you can affect one additional creature for each slot level above 1st. The creatures must be within 30 feet of each other when you target them."""
        print_description('1st', 'Command', '1 Action', '1 Round', '60ft', 'WIS Save', 'Prone',
                          'V', 'Enchantment')

    @with_category('Spells')
    def do_commune(self, arg):
        """You contact your deity or a divine proxy and ask up to three questions that can be answered with a yes or no. You must ask your questions before the spell ends. You receive a correct answer for each question.

Divine beings aren't necessarily omniscient, so you might receive "unclear" as an answer if a question pertains to information that lies beyond the deity's knowledge. In a case where a one-word answer could be misleading or contrary to the deity's interests, the GM might offer a short phrase as an answer instead.

If you cast the spell two or more times before finishing your next long rest, there is a cumulative 25 percent chance for each casting after the first that you get no answer. The GM makes this roll in secret.

Material Component: Incense and a vial of holy or unholy water."""
        print_description('5th', 'Commune', '1 Minute [R]', '1 Minute', 'Self', 'None', 'Foreknowledge',
                          'V, S, M', 'Divination')

    @with_category('Spells')
    def do_commune_with_nature(self, arg):
        """You briefly become one with nature and gain knowledge of the surrounding territory. In the outdoors, the spell gives you knowledge of the land within 3 miles of you. In caves and other natural underground settings, the radius is limited to 300 feet. The spell doesn't function where nature has been replaced by construction, such as in dungeons and towns.

You instantly gain knowledge of up to three facts of your choice about any of the following subjects as they relate to the area:

terrain and bodies of water
prevalent plants, minerals, animals, or peoples
powerful celestials, fey, fiends, elementals, or undead
influence from other planes of existence
buildings

For example, you could determine the location of powerful undead in the area, the location of major sources of safe drinking water, and the location of any nearby towns."""
        print_description('5th', 'Commune with Nature', '1 Minute [R]', 'Instantaneous', 'Self', 'None', 'Environment',
                          'V, S', 'Divination')

    @with_category('Spells')
    def do_compelled_duel(self, arg):
        """You attempt to compel a creature into a duel. One creature that you can see within range must make a Wisdom saving throw. On a failed save, the creature is drawn to you, compelled by your divine demand. For the duration, it has disadvantage on attack rolls against creatures other than you, and must make a Wisdom saving throw each time it attempts to move to a space that is more than 30 feet away from you; if it succeeds on this saving throw, this spell doesn’t restrict the target’s movement for that turn.

The spell ends if you attack any other creature, if you cast a spell that targets a hostile creature other than the target, if a creature friendly to you damages the target or casts a harmful spell on it, or if you end your turn more than 30 feet away from the target."""
        print_description('1st', 'Compelled Duel', '1 Bonus Action', '1 Minute [C]', '30ft', 'WIS Save', 'Control',
                          'V', 'Enchantment')

    @with_category('Spells')
    def do_comprehend_languages(self, arg):
        """For the duration, you understand the literal meaning of any spoken language that you hear. You also understand any written language that you see, but you must be touching the surface on which the words are written. It takes about 1 minute to read one page of text.

This spell doesn't decode secret messages in a text or a glyph, such as an arcane sigil, that isn't part of a written language.

Material Components: A pinch of soot and salt."""
        print_description('1st', 'Comprehend Languages', '1 Action [R]', '1 Hour', 'Self', 'None', 'Social',
                          'V, S, M', 'Divination')

    @with_category('Spells')
    def do_compulsion(self, arg):
        """Creatures of your choice that you can see within range and that can hear you must make a Wisdom saving throw. A target automatically succeeds on this saving throw if it can't be charmed. On a failed save, a target is affected by this spell. Until the spell ends, you can use a bonus action on each of your turns to designate a direction that is horizontal to you.

Each affected target must use as much of its movement as possible to move in that direction on its next turn. It can take its action before it moves. After moving in this way, it can make another Wisdom saving throw to try to end the effect.

A target isn't compelled to move into an obviously deadly hazard, such as a fire or pit, but it will provoke opportunity attacks to move in the designated direction."""
        print_description('4th', 'Compulsion', '1 Action', '1 Minute [C]', '30ft', 'WIS Save', 'Charmed',
                          'V, S', 'Enchantment')

    @with_category('Spells')
    def do_cone_of_cold(self, arg):
        """A blast of cold air erupts from your hands. Each creature in a 60-foot cone must make a Constitution saving throw. A creature takes 8d8 cold damage on a failed save, or half as much damage on a successful one.

A creature killed by this spell becomes a frozen statue until it thaws.

At Higher Levels. When you cast this spell using a spell slot of 6th level or higher, the damage increases by 1d8 for each slot level above 5th.

Material Component: A small crystal or glass cone."""
        print_description('5th', 'Cone of Cold', '1 Action', 'Instantaneous', 'Self/60ft Cone', 'CON Save', 'Cold',
                          'V, S, M', 'Evocation')
        global print_rolls
        die_rolls = 8
        minimum_spell_level = 5
        cast_d8(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_confusion(self, arg):
        """This spell assaults and twists creatures' minds, spawning delusions and provoking uncontrolled action. Each creature in a 10-foot-radius sphere centered on a point you choose within range must succeed on a Wisdom saving throw when you cast this spell or be affected by it.

An affected target can't take reactions and must roll a d10 at the start of each of its turns to determine its behavior for that turn.

At the end of each of its turns, an affected target can make a Wisdom saving throw. If it succeeds, this effect ends for that target.

At Higher Levels. When you cast this spell using a spell slot of 5th level or higher, the radius of the sphere increases by 5 feet for each slot level above 4th.

Material Component: Three nut shells."""
        print_description('4th', 'Confusion', '1 Action', '1 Minute [C]', '90ft/10ft Sphere', 'WIS Save', 'Control',
                          'V, S, M', 'Enchantment')
        global print_rolls
        table = PrettyTable()
        table.add_column('d10', ['1', '2-6', '7-8', '9-10'])
        b1 = "The creature uses all its movement to move in a random direction. \nTo determine the direction, roll a d8 and assign a direction to each die face. \nThe creature doesn't take an action this turn."
        b2 = "The creature doesn't move or take actions this turn."
        b3 = "The creature uses its action to make a melee attack against a randomly determined creature within its reach. \nIf there is no creature within its reach, the creature does nothing this turn."
        b4 = 'The creature can act and move normally.'
        table.add_column('Behaviour', [b1, b2, b3, b4])
        print(table)
        print(d10())

    @with_category('Spells')
    def do_conjure_animals(self, arg):
        """You summon fey spirits that take the form of beasts and appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears:

One beast of challenge rating 2 or lower
Two beasts of challenge rating 1 or lower
Four beasts of challenge rating 1/2 or lower
Eight beasts of challenge rating 1/4 or lower

Each beast is also considered fey, and it disappears when it drops to 0 hit points or when the spell ends.

The summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which has its own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions.

The GM has the creatures' statistics. Sample creatures can be found below.

At Higher Levels. When you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 5th-level slot, three times as many with a 7th-level slot, and four times as many with a 9th-level slot."""
        print_description('3rd', 'Conjure Animals', '1 Action', '1 Hour [C]', '60ft', 'None', 'Summoning',
                          'V, S', 'Conjuration')
        print('For a list of all fey creatures, use the "fey_creatures" command!')

    @with_category('Spells')
    def do_conjure_barrage(self, arg):
        """You throw a nonmagical weapon or fire a piece of nonmagical ammunition into the air to create a cone of identical weapons that shoot forward and then disappear. Each creature in a 60-foot cone must succeed on a Dexterity saving throw. A creature takes 3d8 damage on a failed save, or half as much damage on a successful one. The damage type is the same as that of the weapon or ammunition used as a component.

    Material Component: One piece of ammunition or a thrown weapon."""
        print_description('3rd', 'Conjure Barrage', '1 Action', 'Instantaneous', 'Self/60ft Cone', 'Dex Save',
                          'DAMAGE/EFFECT', 'V, S, M', 'Conjuration')
        self.do_d8('3')

    @with_category('Spells')
    def do_conjure_celestial(self, arg):
        """You summon a celestial of challenge rating 4 or lower, which appears in an unoccupied space that you can see within range. The celestial disappears when it drops to 0 hit points or when the spell ends.

The celestial is friendly to you and your companions for the duration. Roll initiative for the celestial, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you), as long as they don't violate its alignment. If you don't issue any commands to the celestial, it defends itself from hostile creatures but otherwise takes no actions.

For a list of celestial units, is the "celestials" command

At Higher Levels. When you cast this spell using a 9th-level spell slot, you summon a celestial of challenge rating 5 or lower."""
        print_description('7th', 'Conjure Celestial', '1 Minute', '1 Hour [C]', '90ft', 'None', 'Summoning',
                          'V, S', 'Conjuration')

    @with_category('Spells')
    def do_conjure_elemental(self, arg):
        """You call forth an elemental servant. Choose an area of air, earth, fire, or water that fills a 10-foot cube within range. An elemental of challenge rating 5 or lower appropriate to the area you chose appears in an unoccupied space within 10 feet of it. For example, a fire elemental emerges from a bonfire, and an earth elemental rises up from the ground. The elemental disappears when it drops to 0 hit points or when the spell ends.

The elemental is friendly to you and your companions for the duration. Roll initiative for the elemental, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you). If you don't issue any commands to the elemental, it defends itself from hostile creatures but otherwise takes no actions.

If your concentration is broken, the elemental doesn't disappear. Instead, you lose control of the elemental, it becomes hostile toward you and your companions, and it might attack. An uncontrolled elemental can't be dismissed by you, and it disappears 1 hour after you summoned it.

The GM has the elemental's statistics. Sample elementals can be found below.

At Higher Levels. When you cast this spell using a spell slot of 6th level or higher, the challenge rating increases by 1 for each slot level above 5th.

Material Components: Burning incense for air, soft clay for earth, sulfur and phosphorus for fire, or water and sand for water"""
        print_description('5th', 'Conjure Elemental', '1 Minute', '1 Hour [C]', '90ft', 'None', 'Summoning',
                          'V, S, M', 'Conjuration')

    @with_category('Spells')
    def do_conjure_fey(self, arg):
        """You summon a fey creature of challenge rating 6 or lower, or a fey spirit that takes the form of a beast of challenge rating 6 or lower. It appears in an unoccupied space that you can see within range. The fey creature disappears when it drops to 0 hit points or when the spell ends.

The fey creature is friendly to you and your companions for the duration. Roll initiative for the creature, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you), as long as they don't violate its alignment. If you don't issue any commands to the fey creature, it defends itself from hostile creatures but otherwise takes no actions.

If your concentration is broken, the fey creature doesn't disappear. Instead, you lose control of the fey creature, it becomes hostile toward you and your companions, and it might attack. An uncontrolled fey creature can't be dismissed by you, and it disappears 1 hour after you summoned it.

The GM has the fey creature's statistics. Some sample creatures are listed below.

At Higher Levels. When you cast this spell using a spell slot of 7th level or higher, the challenge rating increases by 1 for each slot level above 6th."""
        print_description('6th', 'Conjure Fey', '1 Minute', '1 Hour [C]', '90ft', 'None', 'Summoning',
                          'V, S', 'Conjuration')

    @with_category('Spells')
    def do_conjure_minor_elemental(self, arg):
        """You summon elementals that appear in unoccupied spaces that you can see within range. You choose one the following options for what appears:

One elemental of challenge rating 2 or lower
Two elementals of challenge rating 1 or lower
Four elementals of challenge rating 1/2 or lower
Eight elementals of challenge rating 1/4 or lower.

An elemental summoned by this spell disappears when it drops to 0 hit points or when the spell ends.

The summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which has its own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions.

The GM has the creatures' statistics.

At Higher Levels. When you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 6th-level slot and three times as many with an 8th-level slot."""
        print_description('4th', 'Conjure Minor Elemental', '1 Minute', '1 Hour [C]', '90ft', 'None',
                          'Summoning', 'V, S', 'Conjuration')

    @with_category('Spells')
    def do_conjure_volley(self, arg):
        """You fire a piece of nonmagical ammunition from a ranged weapon or throw a nonmagical weapon into the air and choose a point within range. Hundreds of duplicates of the ammunition or weapon fall in a volley from above and then disappear. Each creature in a 40-foot-radius. 20-foot-high cylinder centered on that point must make a Dexterity saving throw. A creature takes 8d8 damage on a failed save, or half as much damage on a successful one. The damage type is the same as that of the ammunition or weapon.

Material Component: One piece of ammunition or one thrown weapon."""
        print_description('5TH', 'Conjure Volley', '1 Action', 'Instantaneous', '150ft/40ft Cylinder', 'Dex Save',
                          'Additional', 'V, S, M', 'Conjuration')

    @with_category('Spells')
    def do_conjure_woodland_beings(self, arg):
        """You summon fey creatures that appear in unoccupied spaces that you can see within range. Choose one of the following options for what appears:

One fey creature of challenge rating 2 or lower
Two fey creatures of challenge rating 1 or lower
Four fey creatures of challenge rating 1/2 or lower
Eight fey creatures of challenge rating 1/4 or lower

A summoned creature disappears when it drops to 0 hit points or when the spell ends.

The summoned creatures are friendly to you and your companions. Roll initiative for the summoned creatures as a group, which have their own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions.

The GM has the creatures' statistics. You can see some sample creatures below.

At Higher Levels. When you cast this spell using certain higher-level spell slots, you choose one of the summoning options above, and more creatures appear: twice as many with a 6th-level slot and three times as many with an 8th-level slot.

Material Component: One holly berry per creature summoned"""
        print_description('4th', 'Conjure Woodland Beings', '1 Action', '1 Hour [C]', 'None', 'None',
                          'Summoning', 'V, S, M', 'Conjuration')

    @with_category('Spells')
    def do_contact_other_plane(self, arg):
        """You mentally contact a demigod, the spirit of a long- dead sage, or some other mysterious entity from another plane. Contacting this extraplanar intelligence can strain or even break your mind. When you cast this spell, make a DC 15 Intelligence saving throw. On a failure, you take 6d6 psychic damage and are insane until you finish a long rest. While insane, you can't take actions, can't understand what other creatures say, can't read, and speak only in gibberish. A greater restoration spell cast on you ends this effect.

On a successful save, you can ask the entity up to five questions. You must ask your questions before the spell ends. The GM answers each question with one word, such as "yes," "no," "maybe," "never," "irrelevant," or "unclear" (if the entity doesn't know the answer to the question). If a one-word answer would be misleading, the GM might instead offer a short phrase as an answer."""
        print_description('5th', 'Contact Other Plane', '1 Minute [R]', '1 Minute', 'Self', 'None', 'Communication',
                          'V', 'Divination')
        self.do_d6('6')

    @with_category('Spells')
    def do_contagion(self, arg):
        """Your touch inflicts disease. Make a melee spell attack against a creature within your reach. On a hit, the target is poisoned.

At the end of each of the poisoned target's turns, the target must make a Constitution saving throw. If the target succeeds on three of these saves, it is no longer poisoned, and the spell ends. If the target fails three of these saves, the target is no longer poisoned, but choose one of the diseases below. The target is subjected to the chosen disease for the spell's duration.

Since this spell induces a natural disease in its target, any effect that removes a disease or otherwise ameliorates a disease's effects apply to it.

Blinding Sickness. Pain grips the creature's mind, and its eyes turn milky white. The creature has disadvantage on Wisdom checks and Wisdom saving throws and is blinded.

Filth Fever. A raging fever sweeps through the creature's body. The creature has disadvantage on Strength checks, Strength saving throws, and attack rolls that use Strength.

Flesh Rot. The creature's flesh decays. The creature has disadvantage on Charisma checks and vulnerability to all damage.

Mindfire. The creature's mind becomes feverish. The creature has disadvantage on Intelligence checks and Intelligence saving throws, and the creature behaves as if under the effects of the confusion spell during combat.

Seizure. The creature is overcome with shaking. The creature has disadvantage on Dexterity checks, Dexterity saving throws, and attack rolls that use Dexterity.

Slimy Doom. The creature begins to bleed uncontrollably. The creature has disadvantage on Constitution checks and Constitution saving throws. In addition, whenever the creature takes damage, it is stunned until the end of its next turn."""
        print_description('5th', 'Contagion', '1 Action', '7 Days', 'Touch', 'CON Save', 'Blinded',
                          'V, S', 'Necromancy')

    @with_category('Spells')
    def do_contingency(self, arg):
        """Choose a spell of 5th level or lower that you can cast, that has a casting time of 1 action, and that can target you. You cast that spell--called the contingent spell--as part of casting contingency, expending spell slots for both, but the contingent spell doesn't come into effect. Instead, it takes effect when a certain circumstance occurs. You describe that circumstance when you cast the two spells. For example, a contingency cast with water breathing might stipulate that water breathing comes into effect when you are engulfed in water or a similar liquid.

The contingent spell takes effect immediately after the circumstance is met for the first time, whether or not you want it to, and then contingency ends.

The contingent spell takes effect only on you, even if it can normally target others. You can use only one contingency spell at a time.

If you cast this spell again, the effect of another contingency spell on you ends. Also, contingency ends on you if its material component is ever not on your person.

Material Components: A statuette of yourself carved from ivory and decorated with gems worth at least 1,500 gp"""
        print_description('6th', 'Contingency', '10 Minutes', '10 Days', 'Self', 'None', 'Utility',
                          'V, S, M', 'Evocation')

    @with_category('Spells')
    def do_continual_flame(self, arg):
        """A flame, equivalent in brightness to a torch, springs forth from an object that you touch. The effect looks like a regular flame, but it creates no heat and doesn't use oxygen. A continual flame can be covered or hidden but not smothered or quenched.

Material Component: Ruby dust worth 50 gp, which the spell consumes."""
        print_description('2nd', 'Continual Flame', '1 Action', 'Until Dispelled', 'Touch', 'None', 'Creation',
                          'V, S, M', 'Evocation')

    ###############################################################################################################
    # With 400 spells to go, I realised I had to make some changes if I'm to ever finish typing them all in.      #
    # As a result, all spells from this point on uses the "spell_helper" function to print the information table. #
    # The spell helper uses the information from the allSpells.json file.                                         #
    # Since there are many projects on github that use the same data folder with the same jsons in it and none    #
    # of them claim to have made it I don't know who to give credit to. Just know that I didn't make it myself.   #
    ###############################################################################################################

    @with_category('Spells')
    def do_control_flames(self, arg):
        """You choose nonmagical flame that you can see within range and that fits within a 5-foot cube. You affect it in one of the following ways:

You instantaneously expand the flame 5 feet in one direction, provided that wood or other fuel is present in the new location.

You instantaneously extinguish the flames within the cube.

You double or halve the area of bright light and dim light cast by the flame, change its color, or both. The change lasts for 1 hour.

You cause simple shapes—such as the vague form of a creature, an inanimate object, or a location—to appear within the flames and animate as you like. The shapes last for 1 hour.

If you cast this spell multiple times, you can have up to three of its non-instantaneous effects active at a time, and you can dismiss such an effect as an action."""
        spell_helper('Control Flames')

    @with_category('Spells')
    def do_control_water(self, arg):
        """Until the spell ends, you control any freestanding water inside an area you choose that is a cube up to 100 feet on a side. You can choose from any of the following effects when you cast this spell. As an action on your turn, you can repeat the same effect or choose a different one.

Flood. You cause the water level of all standing water in the area to rise by as much as 20 feet. If the area includes a shore, the flooding water spills over onto dry land.

If you choose an area in a large body of water, you instead create a 20-foot tall wave that travels from one side of the area to the other and then crashes down. Any Huge or smaller vehicles in the wave's path are carried with it to the other side. Any Huge or smaller vehicles struck by the wave have a 25 percent chance of capsizing.

The water level remains elevated until the spell ends or you choose a different effect. If this effect produced a wave, the wave repeats on the start of your next turn while the flood effect lasts.

Part Water. You cause water in the area to move apart and create a trench. The trench extends across the spell's area, and the separated water forms a wall to either side. The trench remains until the spell ends or you choose a different effect. The water then slowly fills in the trench over the course of the next round until the normal water level is restored.

Redirect Flow. You cause flowing water in the area to move in a direction you choose, even if the water has to flow over obstacles, up walls, or in other unlikely directions. The water in the area moves as you direct it, but once it moves beyond the spell's area, it resumes its flow based on the terrain conditions. The water continues to move in the direction you chose until the spell ends or you choose a different effect.

Whirlpool. This effect requires a body of water at least 50 feet square and 25 feet deep. You cause a whirlpool to form in the center of the area. The whirlpool forms a vortex that is 5 feet wide at the base, up to 50 feet wide at the top, and 25 feet tall. Any creature or object in the water and within 25 feet of the vortex is pulled 10 feet toward it. A creature can swim away from the vortex by making a Strength (Athletics) check against your spell save DC.

When a creature enters the vortex for the first time on a turn or starts its turn there, it must make a Strength saving throw. On a failed save, the creature takes 2d8 bludgeoning damage and is caught in the vortex until the spell ends. On a successful save, the creature takes half damage, and isn't caught in the vortex. A creature caught in the vortex can use its action to try to swim away from the vortex as described above, but has disadvantage on the Strength (Athletics) check to do so.

The first time each turn that an object enters the vortex, the object takes 2d8 bludgeoning damage; this damage occurs each round it remains in the vortex.

Material Components: A drop of water and a pinch of dust."""
        spell_helper('Control Water')
        self.do_d8('2')

    @with_category('Spells')
    def do_control_weather(self, arg):
        """You take control of the weather within 5 miles of you for the duration. You must be outdoors to cast this spell. Moving to a place where you don’t have a clear path to the sky ends the spell early.

When you cast the spell, you change the current weather conditions, which are determined by the DM based on the climate and season. You can change precipitation, temperature, and wind. It takes 1d4 × 10 minutes for the new conditions to take effect. Once they do so, you can change the conditions again. When the spell ends, the weather gradually returns to normal.

When you change the weather conditions, find a current condition on the following tables and change its stage by one, up or down. When changing the wind, you can change its direction.

Material Components: Burning incense and bits of earth and wood mixed in water."""
        spell_helper('Control Weather')
        table = PrettyTable()
        print('Temperature')
        table.add_column('Stage', ['1', '2', '3', '4', '5', '6'])
        table.add_column('Condition', ['Unbearable Heat', 'Hot', 'Warm', 'Cool', 'Cold', 'Arctic Cold'])
        print(table)
        table = PrettyTable()
        print('Wind')
        table.add_column('Stage', ['1', '2', '3', '4', '5'])
        table.add_column('Condition', ['Calm', 'Moderate Wind', 'Strong Wind', 'Gale', 'Storm'])
        print(table)
        table = PrettyTable()
        print('Precipitation')
        table.add_column('Stage', ['1', '2', '3', '4', '5'])
        table.add_column('Condition', ['Clear', 'Light Clouds', 'Overcast or ground fog', 'Rain, hail or snow',
                                       'Torrential rain, driving hail, or blizzard'])
        print(table)

    @with_category('Spells')
    def do_control_winds(self, arg):
        """You take control of the air in a 100-foot cube that you can see within range. Choose one of the following effects when you cast the spell. The effect lasts for the spell’s duration, unless you use your action on a later turn to switch to a different effect. You can also use your action to temporarily halt the effect or to restart one you’ve halted.

Gusts. A wind picks up within the cube, continually blowing in a horizontal direction you designate. You choose the intensity of the wind: calm, moderate, or strong. If the wind is moderate or strong, ranged weapon attacks that enter or leave the cube or pass through it have disadvantage on their attack rolls. If the wind is strong, any creature moving against the wind must spend 1 extra foot of movement for each foot moved.

Downdraft. You cause a sustained blast of strong wind to blow downward from the top of the cube. Ranged weapon attacks that pass through the cube or that are made against targets within it have disadvantage on their attack rolls. A creature must make a Strength saving throw if it flies into the cube for the first time on a turn or starts its turn there flying. On a failed save, the creature is knocked prone.

Updraft. You cause a sustained updraft within the cube, rising upward from the cube’s bottom side. Creatures that end a fall within the cube take only half damage from the fall. When a creature in the cube makes a vertical jump, the creature can jump up to 10 feet higher than normal."""
        spell_helper('Control Winds')

    @with_category('Spells')
    def do_cordon_of_arrows(self, arg):
        """You plant four pieces of nonmagical ammunition – arrows or crossbow bolts – in the ground within range and lay magic upon them to protect an area. Until the spell ends, whenever a creature other than you comes within 30 feet of the ammunition for the first time on a turn or ends its turn there, one piece of ammunition flies up to strike it. The creature must succeed on a Dexterity saving throw or take 1d6 piercing damage. The piece of ammunition is then destroyed. The spell ends when no ammunition remains.

When you cast this spell, you can designate any creatures you choose, and the spell ignores them.

At Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, the amount of ammunition that can be affected increases by two for each slot level above 2nd."""
        spell_helper('Cordon of Arrows')

    @with_category('Spells')
    def do_counterspell(self, arg):
        """You attempt to interrupt a creature in the process of casting a spell. If the creature is casting a spell of 3rd level or lower, its spell fails and has no effect. If it is casting a spell of 4th level or higher, make an ability check using your spellcasting ability. The DC equals 10 + the spell's level. On a success, the creature's spell fails and has no effect.

At Higher Levels. When you cast this spell using a spell slot of 4th level or higher, the interrupted spell has no effect if its level is less than or equal to the level of the spell slot you used."""
        spell_helper('Counterspell')
        print(d20(), '+ Spellcasting Modifier')

    @with_category('Spells')
    def do_create_bonfire(self, arg):
        """You create a bonfire on ground that you can see within range. Until the spell ends, the magic bonfire fills a 5-foot cube. Any creature in the bonfire’s space when you cast the spell must succeed on a Dexterity saving throw or take 1d8 fire damage. A creature must also make the saving throw when it moves into the bonfire’s space for the first time on a turn or ends its turn there.

The bonfire ignites flammable objects in its area that aren’t being worn or carried.

The spell’s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."""
        spell_helper('Create Bonfire')
        global print_rolls
        die_rolls = 1
        minimum_spell_level = 1
        cast_d8(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_create_food_and_water(self, arg):
        """You create 45 pounds of food and 30 gallons of water on the ground or in containers within range, enough to sustain up to fifteen humanoids or five steeds for 24 hours. The food is bland but nourishing, and spoils if uneaten after 24 hours. The water is clean and doesn't go bad."""
        spell_helper('Create Food and Water')

    @with_category('Spells')
    def do_create_homunculus(self, arg):
        """While speaking an intricate incantation, you cut yourself with a jewel-encrusted dagger, taking 2d4 piercing damage that can’t be reduced in any way. You then drip your blood on the spell’s other components and touch them, transforming them into a special construct called a homunculus.

The statistics of the homunculus are in the Monster Manual. It is your faithful companion, and it dies if you die. Whenever you finish a long rest, you can spend up to half your Hit Dice if the homunculus is on the same plane of existence as you. When you do so, roll each die and add your Constitution modifier to it. Your hit point maximum is reduced by the total, and the homunculus’s hit point maximum and current hit points are both increased by it. This process can reduce you to no lower than 1 hit point, and the change to your and the homunculus’s hit points ends when you finish your next long rest. The reduction to your hit point maximum can’t be removed by any means before then, except by the homunculus’s death.

You can have only one homunculus at a time. If you cast this spell while your homunculus lives, the spell fails.

Material Components: Clay, ash, and mandrake root, all of which the spell consumes, and a jewel-encrusted dagger worth at least 1,000 gp

Link: https://www.dndbeyond.com/monsters/homunculus"""
        spell_helper('Create Homunculus')

    @with_category('Spells')
    def do_create_or_destroy_water(self, arg):
        """
You either create or destroy water.

Create Water. You create up to 10 gallons of clean water within range in an open container. Alternatively, the water falls as rain in a 30-foot cube within range, extinguishing exposed flames in the area.

Destroy Water. You destroy up to 10 gallons of water in an open container within range. Alternatively, you destroy fog in a 30-foot cube within range.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, you create or destroy 10 additional gallons of water, or the size of the cube increases by 5 feet, for each slot level above 1st.

Material Component: A drop of water if creating water or a few grains of sand if destroying it."""
        spell_helper('Create or Destroy Water')


    @with_category('Spells')
    def do_create_undead(self, arg):
        """You can cast this spell only at night. Choose up to three corpses of Medium or Small humanoids within range. Each corpse becomes a ghoul under your control. (The GM has game statistics for these creatures.)

As a bonus action on each of your turns, you can mentally command any creature you animated with this spell if the creature is within 120 feet of you (if you control multiple creatures, you can command any or all of them at the same time, issuing the same command to each one). You decide what action the creature will take and where it will move during its next turn, or you can issue a general command, such as to guard a particular chamber or corridor. If you issue no commands, the creature only defends itself against hostile creatures. Once given an order, the creature continues to follow it until its task is complete.

The creature is under your control for 24 hours, after which it stops obeying any command you have given it. To maintain control of the creature for another 24 hours, you must cast this spell on the creature before the current 24-hour period ends. This use of the spell reasserts your control over up to three creatures you have animated with this spell, rather than animating new ones.

At Higher Levels. When you cast this spell using a 7th-level spell slot, you can animate or reassert control over four ghouls. When you cast this spell using an 8th-level spell slot, you can animate or reassert control over five ghouls or two ghasts or wights. When you cast this spell using a 9th-level spell slot, you can animate or reassert control over six ghouls, three ghasts or wights, or two mummy(ies).

Ghoul Link: https://www.dndbeyond.com/monsters/ghoul

Material Components: One clay pot filled with grave dirt, one clay pot filled with brackish water, and one 150 gp black onyx stone for each corpse."""
        spell_helper('Create Undead')


    @with_category('Spells')
    def do_creation(self, arg):
        """You pull wisps of shadow material from the Shadowfell to create a nonliving object of vegetable matter within range: soft goods, rope, wood, or something similar. You can also use this spell to create mineral objects such as stone, crystal, or metal. The object created must be no larger than a 5-foot cube, and the object must be of a form and material that you have seen before.

The duration depends on the object's material. If the object is composed of multiple materials, use the shortest duration.

Using any material created by this spell as another spell's material component causes that spell to fail.

At Higher Levels. When you cast this spell using a spell slot of 6th level or higher, the cube increases by 5 feet for each slot level above 5th.

Material Component: A tiny piece of matter of the same type of the item you plan to create."""
        spell_helper('Creation')
        table = PrettyTable()
        table.add_column('Material', ['Vegetable Matter', 'Stone or Crystal', 'Precious Metals', 'Gems',
                                      'Adamantine or Mithral'])
        table.add_column('Duration', ['1 Day', '12 Hours', '1 Hour', '10 Minutes', '1 Minute'])
        print(table)

    @with_category('Spells')
    def do_crown_of_madness(self, arg):
        """One humanoid of your choice that you can see within range must succeed on a Wisdom saving throw or become charmed by you for the duration.
While the target is charmed in this way, a twisted crown of jagged iron appears on its head, and a madness glows in its eyes.

The charmed target must use its action before moving on each of its turns to make a melee attack against a creature other than itself that you mentally choose. The target can act normally on its turn if you choose no creature or if none are within its reach.

On your subsequent turns, you must use your action to maintain control over the target, or the spell ends. Also, the target can make a Wisdom saving throw at the end of each of its turns. On a success, the spell ends.

"""
        spell_helper('Crown of Madness')


    @with_category('Spells')
    def do_crown_of_stars(self, arg):
        """Seven star-like motes of light appear and orbit your head until the spell ends. You can use a bonus action to send one of the motes streaking toward one creature or object within 120 feet of you. When you do so, make a ranged spell attack. On a hit, the target takes 4d12 radiant damage. Whether you hit or miss, the mote is expended. The spell ends early if you expend the last mote.

If you have four or more motes remaining, they shed bright light in a 30-foot radius and dim light for an additional 30 feet. If you have one to three motes remaining, they shed dim light in a 30-foot radius.

At Higher Levels. When you cast this spell using a spell slot of 8th level or higher, the number of motes created increases by two for each slot level above 7th."""
        spell_helper('Crown of Stars')
        self.do_d12('4')

    @with_category('Spells')
    def do_crusaders_mantle(self, arg):
        """Holy power radiates from you in an aura with a 30-foot radius, awakening boldness in friendly creatures. Until the spell ends, the aura moves with you, centered on you. While in the aura, each nonhostile creature in the aura (including you) deals an extra 1d4 radiant damage when it hits with a weapon attack."""
        spell_helper("Crusader's Mantle")

    @with_category('Spells')
    def do_cure_wounds(self, arg):
        """A creature you touch regains a number of hit points equal to 1d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the healing increases by 1d8 for each slot level above 1st."""
        spell_helper('Cure Wounds')
        global print_rolls
        die_rolls = 1
        minimum_spell_level = 1
        cast_d8(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_dancing_lights(self, arg):
        """You create up to four torch-sized lights within range, making them appear as torches, lanterns, or glowing orbs that hover in the air for the duration. You can also combine the four lights into one glowing vaguely humanoid form of Medium size. Whichever form you choose, each light sheds dim light in a 10- foot radius.

As a bonus action on your turn, you can move the lights up to 60 feet to a new spot within range. A light must be within 20 feet of another light created by this spell, and a light winks out if it exceeds the spell's range.

Material Component: A bit of phosphorus or wychwood, or a glowworm."""
        spell_helper('Dancing Lights')

    @with_category('Spells')
    def do_danse_macabre(self, arg):
        """Threads of dark power leap from your fingers to pierce up to five Small or Medium corpses you can see within range. Each corpse immediately stands up and becomes undead. You decide whether it is a zombie or a skeleton (the statistics for zombies and skeletons are in the Monster Manual), and it gains a bonus to its attack and damage rolls equal to your spellcasting ability modifier.

You can use a bonus action to mentally command the creatures you make with this spell, issuing the same command to all of them. To receive the command, a creature must be within 60 feet of you. You decide what action the creatures will take and where they will move during their next turn, or you can issue a general command, such as to guard a chamber or passageway against your foes. If you issue no commands, the creatures do nothing except defend themselves against hostile creatures. Once given an order, the creatures continue to follow it until their task is complete.

The creatures are under your control until the spell ends, after which they become inanimate once more.

At Higher Levels. When you cast this spell using a spell slot of 6th level or higher, you animate up to two additional corpses for each slot level above 5th.

Zombie: https://www.dndbeyond.com/monsters/zombie
Skeleton: https://www.dndbeyond.com/monsters/skeleton"""
        spell_helper('Danse Macabre')

    @with_category('Spells')
    def do_darkness(self, arg):
        """Magical darkness spreads from a point you choose within range to fill a 15-foot-radius sphere for the duration. The darkness spreads around corners. A creature with darkvision can't see through this darkness, and nonmagical light can't illuminate it.

If the point you choose is on an object you are holding or one that isn't being worn or carried, the darkness emanates from the object and moves with it. Completely covering the source of the darkness with an opaque object, such as a bowl or a helm, blocks the darkness.

If any of this spell's area overlaps with an area of light created by a spell of 2nd level or lower, the spell that created the light is dispelled.

Material Components: Bat fur and a drop of pitch or piece of coal."""
        spell_helper('Darkness')

    @with_category('Spells')
    def do_darkvision(self, arg):
        """You touch a willing creature to grant it the ability to see in the dark. For the duration, that creature has darkvision out to a range of 60 feet.

Material Component: Either a pinch of dried carrot or an agate."""
        spell_helper('Darkvision')

    @with_category('Spells')
    def do_dawn(self, arg):
        """The light of dawn shines down on a location you specify within range. Until the spell ends, a 30-foot-radius, 40-foot-high cylinder of bright light glimmers there. This light is sunlight.

When the cylinder appears, each creature in it must make a Constitution saving throw, taking 4d10 radiant damage on a failed save, or half as much damage on a successful one. A creature must also make this saving throw whenever it ends its turn in the cylinder.

If you’re within 60 feet of the cylinder, you can move it up to 60 feet as a bonus action on your turn.

Material Component: A sunburst pendant worth at least 100 gp."""
        spell_helper('Dawn')
        self.do_d10('4')

    @with_category('Spells')
    def do_daylight(self, arg):
        """A 60-foot-radius sphere of light spreads out from a point you choose within range. The sphere is bright light and sheds dim light for an additional 60 feet.

If you chose a point on an object you are holding or one that isn't being worn or carried, the light shines from the object and moves with it. Completely covering the affected object with an opaque object, such as a bowl or a helm, blocks the light.

If any of this spell's area overlaps with an area of darkness created by a spell of 3rd level or lower, the spell that created the darkness is dispelled."""
        spell_helper('Daylight')

    @with_category('Spells')
    def do_death_ward(self, arg):
        """You touch a creature and grant it a measure of protection from death.

The first time the target would drop to 0 hit points as a result of taking damage, the target instead drops to 1 hit point, and the spell ends.

If the spell is still in effect when the target is subjected to an effect that would kill it instantaneously without dealing damage, that effect is instead negated against the target, and the spell ends."""
        spell_helper('Death Ward')

    @with_category('Spells')
    def do_delayed_blast_fireball(self, arg):
        """A beam of yellow light flashes from your pointing finger, then condenses to linger at a chosen point within range as a glowing bead for the duration. When the spell ends, either because your concentration is broken or because you decide to end it, the bead blossoms with a low roar into an explosion of flame that spreads around corners. Each creature in a 20-foot-radius sphere centered on that point must make a Dexterity saving throw. A creature takes fire damage equal to the total accumulated damage on a failed save, or half as much damage on a successful one.

The spell's base damage is 12d6. If at the end of your turn the bead has not yet detonated, the damage increases by 1d6.

If the glowing bead is touched before the interval has expired, the creature touching it must make a Dexterity saving throw. On a failed save, the spell ends immediately, causing the bead to erupt in flame. On a successful save, the creature can throw the bead up to 40 feet. When it strikes a creature or a solid object, the spell ends, and the bead explodes.

The fire damages objects in the area and ignites flammable objects that aren't being worn or carried.

At Higher Levels. When you cast this spell using a spell slot of 8th level or higher, the base damage increases by 1d6 for each slot level above 7th.

Material Components: A tiny ball of bat guano and sulfur."""
        spell_helper('Delayed Blast Fireball')
        global print_rolls
        rounds = input('Number of rounds since spell was cast: ')
        try:
            if int(rounds) <= 10:
                die_rolls = 12 + int(rounds)
                minimum_spell_level = 7
                cast_d6(die_rolls, minimum_spell_level, arg, print_rolls)
            else:
                print('Input has to be a number between 1 and 10')
                return
        except ValueError:
            print('Input Has to be a number between 1 and 10')

    @with_category('Spells')
    def do_demiplane(self, arg):
        """You create a shadowy door on a flat solid surface that you can see within range. The door is large enough to allow Medium creatures to pass through unhindered. When opened, the door leads to a demiplane that appears to be an empty room 30 feet in each dimension, made of wood or stone. When the spell ends, the door disappears, and any creatures or objects inside the demiplane remain trapped there, as the door also disappears from the other side.

Each time you cast this spell, you can create a new demiplane, or have the shadowy door connect to a demiplane you created with a previous casting of this spell. Additionally, if you know the nature and contents of a demiplane created by a casting of this spell by another creature, you can have the shadowy door connect to its demiplane instead.
"""
        spell_helper('Demiplane')

    @with_category('Spells')
    def do_destructive_wave(self, arg):
        """You strike the ground, creating a burst of divine energy that ripples outward from you. Each creature you choose within 30 feet of you must succeed on a Constitution saving throw or take 5d6 thunder damage, as well as 5d6 radiant or necrotic damage (your choice), and be knocked prone. A creature that succeeds on its saving throw takes half as much damage and isn’t knocked prone.

"""
        spell_helper('Destructive Wave')
        self.do_d6('5')

    @with_category('Spells')
    def do_detect_evil_and_good(self, arg):
        """For the duration, you know if there is an aberration, celestial, elemental, fey, fiend, or undead within 30 feet of you, as well as where the creature is located. Similarly, you know if there is a place or object within 30 feet of you that has been magically consecrated or desecrated.

The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt."""
        spell_helper('Detect Evil and Good')

    @with_category('Spells')
    def do_detect_magic(self, arg):
        """For the duration, you sense the presence of magic within 30 feet of you. If you sense magic in this way, you can use your action to see a faint aura around any visible creature or object in the area that bears magic, and you learn its school of magic, if any.

The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt."""
        spell_helper('Detect Magic')

    @with_category('Spells')
    def do_detect_poison_and_disease(self, arg):
        """For the duration, you can sense the presence and location of poisons, poisonous creatures, and diseases within 30 feet of you. You also identify the kind of poison, poisonous creature, or disease in each case.

The spell can penetrate most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt.

Material Component: A yew leaf."""
        spell_helper('Detect Poison and Disease')


    '''
    @with_category('Spells')
    def do_spell_name(self, arg):
        """FULL SPELL DESCRIPTION"""
        print_description('LEVEL', 'NAME', 'CASTING TIME', 'DURATION', 'RANGE/AREA', 'ATTACK/SAVE', 'DAMAGE/EFFECT',
                          'COMPONENTS', 'SCHOOL')
        global print_rolls
        die_rolls = x
        minimum_spell_level = y
        cast_dz(die_rolls, minimum_spell_level, arg, print_rolls)

    @with_category('Spells')
    def do_(self, arg):
        """"""
        spell_helper('')
        global print_rolls
        die_rolls = x
        minimum_spell_level = y
        cast_dz(die_rolls, minimum_spell_level, arg, print_rolls)

    '''


def print_item(item):
    if dict.get(item, 'entries'):
        print(dict.pop(item, 'entries'))
    table = PrettyTable()
    table.field_names = dict.keys(item)
    table.add_row(dict.values(item))
    print(table)


def print_description(level, name, casting_time, duration, range_area, attack_save, damage_effect, components, school):
    table = PrettyTable()
    table.field_names = ['LEVEL', 'NAME', 'CASTING TIME', 'DURATION', 'RANGE/AREA', 'ATTACK/SAVE', 'DAMAGE/EFFECT',
                         'COMPONENTS', 'SCHOOL']
    table.add_row([level, name, casting_time, duration, range_area, attack_save, damage_effect, components, school])
    print(table)


def check_arg_range_100(arg):
    arg = shlex.split(arg)
    if len(arg) == 1 and str.isdigit(arg[0]):
        nr = int(arg[0])
        if 1 <= nr <= 100:
            return nr
        else:
            print('Number has to be between (and including) 1 - 100')
    else:
        print('Invalid Argument')


def check_arg_range_20(arg):
    arg = shlex.split(arg)
    if len(arg) == 1 and str.isdigit(arg[0]):
        nr = int(arg[0])
        if 1 <= nr <= 20:
            return nr
        else:
            print('Number has to be between (and including) 1 - 20')
            return nr
    else:
        print('Invalid Argument')
        return 21


def check_arg_string(arg):
    if str.isprintable(arg):
        return arg
    else:
        print('Invalid Argument')
        return 'error'


def encounter_helper(arg, encounter_location):
    # Checks if argument is not None
    if arg:
        # Loads the encounters.json file
        encounters_json = open('data/encounters.json')
        encounters_json = json.load(encounters_json)
        encounters = encounters_json['encounter']
        region_encounters = None
        # Retrieves all encounters in the "encounter_location" region
        for encounter in encounters:
            if encounter['location'] == encounter_location:
                region_encounters = encounter
                break
        # Checks if arg is a number between 1 - 20
        nr = check_arg_range_20(arg)
        if nr > 20:
            return
        # Retrieves all the encounters of the correct challenge rating
        for encounter in region_encounters['tables']:
            if dict.get(encounter, 'minlvl') <= nr <= dict.get(encounter, 'maxlvl'):
                region_encounters = encounter['table']
                break
        # Prints the encounter corresponding with the d100 roll
        d100_roll = d100()
        for encounter in region_encounters:
            if dict.get(encounter, 'min') <= d100_roll - 1 <= dict.get(encounter, 'max'):
                print(dict.get(encounter, 'enc'))
                break
    else:
        print("This feature requires the players' level as input (1 - 20).")


# This function looks like a mess.
# The (awesome) guy(s) who made the json file didn't make it to be used by a python application.
def spell_helper(arg):
    all_spells_json = open('data/allSpells.json')
    all_spells_json = json.load(all_spells_json)
    all_spells = all_spells_json['spell']
    table = PrettyTable()
    table.field_names = ['LEVEL', 'NAME', 'CASTING TIME', 'DURATION', 'RANGE/AREA', 'ATTACK/SAVE', 'DAMAGE',
                         'COMPONENTS', 'SCHOOL']
    attack_save, damage_effect, components, level, name, casting_time, duration, range_area, school, d_e \
        = '', '', '', '', '', '', '', '', '', ''
    schools = {'A': 'Abjuration', 'C': 'Conjuration', 'D': 'Divination', 'E': 'Enchantment', 'V': 'Evocation',
               'I': 'Illusion', 'N': 'Necromancy', 'T': 'Transmutation'}
    for spell in all_spells:
        if spell['name'] == arg:
            level = spell['level']
            name = spell['name']
            casting_time = str(spell['time'][0]['number']) + ' ' + str(spell['time'][0]['unit']).capitalize()
            if 'meta' in spell:
                casting_time += ' [R]'
            if 'duration' in spell['duration'][0]:
                duration = str(spell['duration'][0]['duration']['amount']) + ' ' + str(
                    spell['duration'][0]['duration']['type']).capitalize()
            else:
                duration = str(spell['duration'][0]['type']).capitalize()
            if 'concentration' in spell['duration'][0]:
                duration += ' [C]'
            if 'distance' in spell['range']:
                if 'amount' in spell['range']['distance']:
                    range_area = str(spell['range']['distance']['amount']) + ' '
                range_area += str(spell['range']['distance']['type']).capitalize() + '/'
            range_area += str(spell['range']['type']).capitalize()
            if 'savingThrow' in spell:
                attack_save = str(spell['savingThrow'][0]).capitalize()
            elif 'spellAttack' in spell:
                attack_save = spell['spellAttack']
            else:
                attack_save = 'None'
            if 'damageInflict' in spell:
                damage_effect = spell['damageInflict']
                for word in damage_effect:
                    d_e += (str(word).capitalize() + ' ')
            else:
                d_e = 'None'
            if 'v' in spell['components']:
                components += 'V'
            if 's' in spell['components']:
                components += ' S'
            if 'm' in spell['components']:
                components += ' M'
            school = spell['school']
            break
    if attack_save[0] == 'R':
        attack_save = 'Ranged Spell Attack'
    elif attack_save[0] == 'M':
        attack_save = 'Melee Spell Attack'
    table.add_row(
        [level, name, casting_time, duration, range_area, attack_save, d_e, components, dict.get(schools, school)])
    print(table)


def all_spell_helper():
    all_spells_json = open('data/allSpells.json')
    all_spells_json = json.load(all_spells_json)
    all_spells = all_spells_json['spell']
    table = PrettyTable()
    table.field_names = ['LEVEL', 'NAME', 'CASTING TIME', 'DURATION', 'RANGE/AREA', 'ATTACK/SAVE', 'DAMAGE',
                         'COMPONENTS', 'SCHOOL']
    schools = {'A': 'Abjuration', 'C': 'Conjuration', 'D': 'Divination', 'E': 'Enchantment', 'V': 'Evocation',
               'I': 'Illusion', 'N': 'Necromancy', 'T': 'Transmutation'}
    for spell in all_spells:
        attack_save, damage_effect, components, level, name, casting_time, duration, range_area, school, d_e \
            = '', '', '', '', '', '', '', '', '', ''
        level = spell['level']
        name = spell['name']
        casting_time = str(spell['time'][0]['number']) + ' ' + str(spell['time'][0]['unit']).capitalize()
        if 'meta' in spell:
            casting_time += ' [R]'
        if 'duration' in spell['duration'][0]:
            duration = str(spell['duration'][0]['duration']['amount']) + ' ' + str(
                spell['duration'][0]['duration']['type']).capitalize()
        else:
            duration = str(spell['duration'][0]['type']).capitalize()
        if 'concentration' in spell['duration'][0]:
            duration += ' [C]'
        if 'distance' in spell['range']:
            if 'amount' in spell['range']['distance']:
                range_area = str(spell['range']['distance']['amount']) + ' '
            range_area += str(spell['range']['distance']['type']).capitalize() + '/'
        range_area += str(spell['range']['type']).capitalize()
        if 'savingThrow' in spell:
            attack_save = str(spell['savingThrow'][0]).capitalize()
        elif 'spellAttack' in spell:
            attack_save = spell['spellAttack']
        else:
            attack_save = 'None'
        if 'damageInflict' in spell:
            damage_effect = spell['damageInflict']
            for word in damage_effect:
                d_e += (str(word).capitalize() + ' ')
        else:
            d_e = 'None'
        if 'v' in spell['components']:
            components += 'V'
        if 's' in spell['components']:
            components += ' S'
        if 'm' in spell['components']:
            components += ' M'
        school = spell['school']
        if attack_save[0] == 'R':
            attack_save = 'Ranged Spell Attack'
        elif attack_save[0] == 'M':
            attack_save = 'Melee Spell Attack'
        table.add_row(
            [level, name, casting_time, duration, range_area, attack_save, d_e, components, dict.get(schools, school)])
    print(table)


if __name__ == '__main__':
    app = Spells()
    app.cmdloop()
