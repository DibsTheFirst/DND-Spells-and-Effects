from Dice import *
from prettytable import PrettyTable
from cmd2 import Cmd, with_argparser
from cmd2.argparse_completer import *
import shlex
from Info import *
import json
from cmd2.rl_utils import readline


print_rolls = True
list_of_items = []


def item_completer(text, state):
    options = [item for item in list_of_items if item.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None


class Spells(Cmd):

    intro = 'Hello! Please type the name of a spell or effect (all lowercase, underscore in place of space). ' \
            'Type help or ? to list all spells, or help "spell_name" for its full description.'
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

    def do_quit(self, arg):
        """Exit the application"""
        print('Goodbye!')
        exit()

    def do_clear(self, arg):
        """Clears the screen of text by printing 100 empty lines"""
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
              '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    def do_print_rolls(self, arg):
        """Turned on by default. Turning it off results in only the end sum of die rolls being shown."""
        global print_rolls
        print_rolls = not print_rolls

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

    def do_wild_magic(self, arg):
        """Rolls on the wild magic table, can also be used to look up a roll. Optional input: Number from 1 - 100"""
        if arg:
            nr = check_arg_range_100(arg)
            print(wild_magic_table[nr - 1])
        else:
            print(wild_magic_table[d100() - 1])

    @with_argparser(item_parser)
    def do_item(self, arg):
        items = open('data/items.json')
        arg = vars(arg)
        #arg = check_arg_string(arg)
        item_dict = json.load(items)
        items.close()
        for item in item_dict['item']:
            if item['name'].lower() == str.lower(arg['item']):
                print_item(item)


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

    def do_create_character(self, arg):
        """Rolls 4d6 and removes the lowest roll. Does it once for every stat(6 times)."""
        for i in range(6):
            roll_4d6_remove_lowest()

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

    def do_aid(self, arg):
        """Your spell bolsters your allies with toughness and resolve. Choose up to three creatures within range.
Each target's hit point maximum and current hit points increase by 5 for the duration.
At Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, a target's hit points increase by an additional 5 for each slot level above 2nd.
Material component: A tiny strip of white cloth."""
        print_description('2nd', 'Aid', '1 Action', '8 Hours', '30ft/3 Creatures', 'None', '+5 To Max HP',
                          'V, S, M', 'Abjuration')

    def do_alarm(self, arg):
        """You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot cube.
Until the spell ends, an alarm alerts you whenever a Tiny or larger creature touches or enters the warded area.
When you cast the spell, you can designate creatures that won't set off the alarm. You also choose whether the alarm is mental or audible.
A mental alarm alerts you with a ping in your mind if you are within 1 mile of the warded area. This ping awakens you if you are sleeping.
An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet.
Material component: A tiny bell and a piece of fine silver wire."""
        print_description('1st', 'Alarm', '1 Minute/Ritual', '8 Hours', '30ft/20ft cube', 'None', 'Detection',
                          'V, S, M', 'Abjuration')

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
        print_description('8th', 'Animal Shapes', '1 Action', '24 Hours [C]', '30ft/Willing Creatures', 'None', 'Shapechanging',
                          'V, S', 'Transmutation')

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

    def do_antilife_shell(self, arg):
        """A shimmering barrier extends out from you in a 10-foot radius and moves with you,
remaining centered on you and hedging out creatures other than undead and constructs.
The barrier lasts for the duration.

The barrier prevents an affected creature from passing or reaching through.
An affected creature can cast spells or make attacks with ranged or reach weapons through the barrier.

If you move so that an affected creature is forced to pass through the barrier, the spell ends."""
        print_description('5th', 'Antilife Shell', '1 Action', '1 Hour [C]', 'Self/10ft Sphere', 'None', 'Control',
                          'V, S', 'Abjuration')

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

    def do_arcane_lock(self, arg):
        """You touch a closed door, window, gate, chest, or other entryway, and it becomes locked for the duration. You and the creatures you designate when you cast this spell can open the object normally. You can also set a password that, when spoken within 5 feet of the object, suppresses this spell for 1 minute. Otherwise, it is impassable until it is broken or the spell is dispelled or suppressed. Casting knock on the object suppresses arcane lock for 10 minutes.

While affected by this spell, the object is more difficult to break or force open; the DC to break it or pick any locks on it increases by 10.

Material Component: Gold dust worth at least 25 gp, which the spell consumes."""
        print_description('2nd', 'Arcane Lock', '1 Action', 'Until Dispelled', 'Touch', 'None', 'Utility',
                          'V, S, M', 'Abjuration')

    def do_arcane_weapon(self, arg):
        """You channel arcane energy into one simple or martial weapon you’re holding, and choose one damage type: acid, cold, fire, lightning, poison, or thunder. Until the spell ends, you deal an extra 1d6 damage of the chosen type to any target you hit with the weapon. If the weapon isn’t magical, it becomes a magic weapon for the spell’s duration.

As a bonus action, you can change the damage type, choosing from the options above.

At Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, you can maintain your concentration on the spell for up to 8 hours."""
        print_description('1st', 'Arcane Weapon', '1 Bonus Action', '1 Hour [C]', 'Self', 'None', 'Elemental/Buff',
                          'V, S', 'Transmutation')

    def do_arcanists_magic_aura(self, arg):
        """You place an illusion on a creature or an object you touch so that divination spells reveal false information about it. The target can be a willing creature or an object that isn't being carried or worn by another creature.
When you cast the spell, choose one or both of the following effects. The effect lasts for the duration. If you cast this spell on the same creature or object every day for 30 days, placing the same effect on it each time, the illusion lasts until it is dispelled.

False Aura. You change the way the target appears to spells and magical effects, such as detect magic, that detect magical auras. You can make a nonmagical object appear magical, a magical object appear nonmagical, or change the object's magical aura so that it appears to belong to a specific school of magic that you choose. When you use this effect on an object, you can make the false magic apparent to any creature that handles the item.

Mask. You change the way the target appears to spells and magical effects that detect creature types, such as a paladin's Divine Sense or the trigger of a symbol spell. You choose a creature type and other spells and magical effects treat the target as if it were a creature of that type or of that alignment.

Material Component: A small square of silk."""
        print_description('2nd', "Arcanist's Magic Aura", '1 Action', '24 Hours', 'Touch', 'None', 'Deception',
                          'V, S, M', 'Illusion')

    def do_armor_of_agathys(self, arg):
        """A protective magical force surrounds you, manifesting as a spectral frost that covers you and your gear. You gain 5 temporary hit points for the duration. If a creature hits you with a melee attack while you have these hit points, the creature takes 5 cold damage.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, both the temporary hit points and the cold damage increase by 5 for each slot.

Material Component: A cup of water."""
        print_description('1st', 'Armor of Agathys', '1 Action', '1 Hour', 'Self', 'None', 'Cold',
                          'V, S, M', 'Abjuration')

    def do_arms_of_hadar(self, arg):
        """You invoke the power of Hadar, the Dark Hunger. Tendrils of dark energy erupt from you and batter all creatures within 10 feet of you. Each creature in that area must make a Strength saving throw. On a failed save, a target takes 2d6 necrotic damage and can’t take reactions until its next turn. On a successful save, the creature takes half damage, but suffers no other effect.

At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot level above 1st."""
        print_description('1st', 'Arms of Hadar', '1 Action', 'Instantaneous', 'Self/10ft Sphere', 'STR Save', 'Necrotic',
                          'V, S', 'Conjuration')
        global print_rolls
        die_rolls = 2
        minimum_spell_level = 1
        cast_d6(die_rolls, minimum_spell_level, arg, print_rolls)

    '''
   def do_spell_name(self, arg):
        """
        print_description('LEVEL', 'NAME', 'CASTING TIME', 'DURATION', 'RANGE/AREA', 'ATTACK/SAVE', 'DAMAGE/EFFECT',
         'COMPONENTS', 'SCHOOL')
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
    table.field_names = ['LEVEL', 'NAME', 'CASTING TIME', 'DURATION', 'RANGE/AREA', 'ATTACK/SAVE', 'DAMAGE/EFFECT', 'COMPONENTS', 'SCHOOL']
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


if __name__ == '__main__':
    app = Spells()
    app.cmdloop()
