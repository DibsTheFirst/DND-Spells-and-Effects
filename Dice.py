import random
import shlex


def d4():
    return random.randint(1, 4)


def d6():
    return random.randint(1, 6)


def d8():
    return random.randint(1, 8)


def d10():
    return random.randint(1, 10)


def d12():
    return random.randint(1, 12)


def d20():
    return random.randint(1, 20)


def d100():
    return random.randint(1, 100)


def roll_d4(number_of_rolls, print_rolls):
    total = 0
    if print_rolls:
        for i in range(number_of_rolls):
            if i == number_of_rolls - 1:
                number = d4()
                total += number
                print(number, end='')
            else:
                number = d4()
                total += number
                print(number, end=' + ')
    else:
        for i in range(number_of_rolls):
            number = d4()
            total += number
    return total


def roll_d6(number_of_rolls, print_rolls):
    total = 0
    if print_rolls:
        for i in range(number_of_rolls):
            if i == number_of_rolls - 1:
                number = d6()
                total += number
                print(number, end='')
            else:
                number = d6()
                total += number
                print(number, end=' + ')
    else:
        for i in range(number_of_rolls):
            number = d6()
            total += number
    return total


def roll_d8(number_of_rolls, print_rolls):
    total = 0
    if print_rolls:
        for i in range(number_of_rolls):
            if i == number_of_rolls - 1:
                number = d8()
                total += number
                print(number, end='')
            else:
                number = d8()
                total += number
                print(number, end=' + ')
    else:
        for i in range(number_of_rolls):
            number = d8()
            total += number
    return total


def roll_d10(number_of_rolls, print_rolls):
    total = 0
    if print_rolls:
        for i in range(number_of_rolls):
            if i == number_of_rolls - 1:
                number = d10()
                total += number
                print(number, end='')
            else:
                number = d10()
                total += number
                print(number, end=' + ')
    else:
        for i in range(number_of_rolls):
            number = d10()
            total += number
    return total


def roll_d12(number_of_rolls, print_rolls):
    total = 0
    if print_rolls:
        for i in range(number_of_rolls):
            if i == number_of_rolls - 1:
                number = d12()
                total += number
                print(number, end='')
            else:
                number = d12()
                total += number
                print(number, end=' + ')
    else:
        for i in range(number_of_rolls):
            number = d12()
            total += number
    return total


def roll_d20(number_of_rolls, print_rolls):
    total = 0
    if print_rolls:
        for i in range(number_of_rolls):
            if i == number_of_rolls - 1:
                number = d20()
                total += number
                print(number, end='')
            else:
                number = d20()
                total += number
                print(number, end=' + ')
    else:
        for i in range(number_of_rolls):
            number = d20()
            total += number
    return total


def roll_d100(number_of_rolls, print_rolls):
    total = 0
    if print_rolls:
        for i in range(number_of_rolls):
            if i == number_of_rolls - 1:
                number = d100()
                total += number
                print(number, end='')
            else:
                number = d100()
                total += number
                print(number, end=' + ')
    else:
        for i in range(number_of_rolls):
            number = d100()
            total += number
    return total


def roll_4d6_remove_lowest():
    rolls = []
    for i in range(4):
        rolls.append(d6())
    rolls.sort()
    total = 0
    for i in range(3, -1, -1):
        if i == 0:
            print(rolls[i], end=' = ')
        elif i == 1:
            total += rolls[i]
            print(rolls[i], end=' removed ')
        else:
            total += rolls[i]
            print(rolls[i], end=' + ')
    print(total)


def cast_d4(die_rolls, minimum_spell_level, arg, print_rolls, dice_per_level = 1):
    die_rolls
    minimum_spell_level
    arg = shlex.split(arg)
    if arg:
        if len(arg) > 2:
            print('Too many arguments')
            return
        elif len(arg) == 2:
            arg.sort()
            if str.isdigit(arg[0]) and arg[1] == 'crit':
                spell_level = int(arg.pop(0))
                if spell_level < minimum_spell_level:
                    print('Spell has to be cast at minimum %i level' % minimum_spell_level)
                else:
                    total = roll_d4(die_rolls + ((spell_level - minimum_spell_level) * dice_per_level), print_rolls)
                    print(' =', total, ' 2 *', total, ' =', 2 * total)
            else:
                print('Invalid Arguments')
        elif len(arg) == 1 and str.isdigit(arg[0]):
            spell_level = int(arg.pop())
            if spell_level < minimum_spell_level:
                print('Spell has to be cast at minimum %i level' % minimum_spell_level)
            else:
                total = roll_d4(die_rolls + ((spell_level - minimum_spell_level) * dice_per_level), print_rolls)
                print(' =', total)
        elif len(arg) == 1 and arg[0] == 'crit':
            total = roll_d4(die_rolls, print_rolls)
            print(' =', total, ' 2 *', total, ' =', 2 * total)
        else:
            print('Invalid Argument')
    else:
        total = roll_d4(die_rolls, print_rolls)
        print(' =', total)


def cast_d6(die_rolls, minimum_spell_level, arg, print_rolls, dice_per_level=1):
    die_rolls
    minimum_spell_level
    arg = shlex.split(arg)
    if arg:
        if len(arg) > 2:
            print('Too many arguments')
            return
        elif len(arg) == 2:
            arg.sort()
            if str.isdigit(arg[0]) and arg[1] == 'crit':
                spell_level = int(arg.pop(0))
                if spell_level < minimum_spell_level:
                    print('Spell has to be cast at minimum %i level' % minimum_spell_level)
                else:
                    total = roll_d6(die_rolls + ((spell_level - minimum_spell_level) * dice_per_level), print_rolls)
                    print(' =', total, ' 2 *', total, ' =', 2 * total)
            else:
                print('Invalid Arguments')
        elif len(arg) == 1 and str.isdigit(arg[0]):
            spell_level = int(arg.pop())
            if spell_level < minimum_spell_level:
                print('Spell has to be cast at minimum %i level' % minimum_spell_level)
            else:
                total = roll_d6(die_rolls + ((spell_level - minimum_spell_level) * dice_per_level), print_rolls)
                print(' =', total)
        elif len(arg) == 1 and arg[0] == 'crit':
            total = roll_d6(die_rolls, print_rolls)
            print(' =', total, ' 2 *', total, ' =', 2 * total)
        else:
            print('Invalid Argument')
    else:
        total = roll_d6(die_rolls, print_rolls)
        print(' =', total)


def cast_d8(die_rolls, minimum_spell_level, arg, print_rolls, dice_per_level=1):
    die_rolls
    minimum_spell_level
    arg = shlex.split(arg)
    if arg:
        if len(arg) > 2:
            print('Too many arguments')
            return
        elif len(arg) == 2:
            arg.sort()
            if str.isdigit(arg[0]) and arg[1] == 'crit':
                spell_level = int(arg.pop(0))
                if spell_level < minimum_spell_level:
                    print('Spell has to be cast at minimum %i level' % minimum_spell_level)
                else:
                    total = roll_d8(die_rolls + ((spell_level - minimum_spell_level) * dice_per_level), print_rolls)
                    print(' =', total, ' 2 *', total, ' =', 2 * total)
            else:
                print('Invalid Arguments')
        elif len(arg) == 1 and str.isdigit(arg[0]):
            spell_level = int(arg.pop())
            if spell_level < minimum_spell_level:
                print('Spell has to be cast at minimum %i level' % minimum_spell_level)
            else:
                total = roll_d8(die_rolls + ((spell_level - minimum_spell_level) * dice_per_level), print_rolls)
                print(' =', total)
        elif len(arg) == 1 and arg[0] == 'crit':
            total = roll_d8(die_rolls, print_rolls)
            print(' =', total, ' 2 *', total, ' =', 2 * total)
        else:
            print('Invalid Argument')
    else:
        total = roll_d8(die_rolls, print_rolls)
        print(' =', total)


def cast_d10(die_rolls, minimum_spell_level, arg, print_rolls, dice_per_level=1):
    die_rolls
    minimum_spell_level
    arg = shlex.split(arg)
    if arg:
        if len(arg) > 2:
            print('Too many arguments')
            return
        elif len(arg) == 2:
            arg.sort()
            if str.isdigit(arg[0]) and arg[1] == 'crit':
                spell_level = int(arg.pop(0))
                if spell_level < minimum_spell_level:
                    print('Spell has to be cast at minimum %i level' % minimum_spell_level)
                else:
                    total = roll_d10(die_rolls + ((spell_level - minimum_spell_level) * dice_per_level), print_rolls)
                    print(' =', total, ' 2 *', total, ' =', 2 * total)
            else:
                print('Invalid Arguments')
        elif len(arg) == 1 and str.isdigit(arg[0]):
            spell_level = int(arg.pop())
            if spell_level < minimum_spell_level:
                print('Spell has to be cast at minimum %i level' % minimum_spell_level)
            else:
                total = roll_d10(die_rolls + ((spell_level - minimum_spell_level) * dice_per_level), print_rolls)
                print(' =', total)
        elif len(arg) == 1 and arg[0] == 'crit':
            total = roll_d10(die_rolls, print_rolls)
            print(' =', total, ' 2 *', total, ' =', 2 * total)
        else:
            print('Invalid Argument')
    else:
        total = roll_d10(die_rolls, print_rolls)
        print(' =', total)


def cast_d12(die_rolls, minimum_spell_level, arg, print_rolls, dice_per_level=1):
    die_rolls
    minimum_spell_level
    arg = shlex.split(arg)
    if arg:
        if len(arg) > 2:
            print('Too many arguments')
            return
        elif len(arg) == 2:
            arg.sort()
            if str.isdigit(arg[0]) and arg[1] == 'crit':
                spell_level = int(arg.pop(0))
                if spell_level < minimum_spell_level:
                    print('Spell has to be cast at minimum %i level' % minimum_spell_level)
                else:
                    total = roll_d12(die_rolls + ((spell_level - minimum_spell_level) * dice_per_level), print_rolls)
                    print(' =', total, ' 2 *', total, ' =', 2 * total)
            else:
                print('Invalid Arguments')
        elif len(arg) == 1 and str.isdigit(arg[0]):
            spell_level = int(arg.pop())
            if spell_level < minimum_spell_level:
                print('Spell has to be cast at minimum %i level' % minimum_spell_level)
            else:
                total = roll_d12(die_rolls + ((spell_level - minimum_spell_level) * dice_per_level), print_rolls)
                print(' =', total)
        elif len(arg) == 1 and arg[0] == 'crit':
            total = roll_d12(die_rolls, print_rolls)
            print(' =', total, ' 2 *', total, ' =', 2 * total)
        else:
            print('Invalid Argument')
    else:
        total = roll_d12(die_rolls, print_rolls)
        print(' =', total)


def cast_d20(die_rolls, minimum_spell_level, arg, print_rolls, dice_per_level=1):
    die_rolls
    minimum_spell_level
    arg = shlex.split(arg)
    if arg:
        if len(arg) > 2:
            print('Too many arguments')
            return
        elif len(arg) == 2:
            arg.sort()
            if str.isdigit(arg[0]) and arg[1] == 'crit':
                spell_level = int(arg.pop(0))
                if spell_level < minimum_spell_level:
                    print('Spell has to be cast at minimum %i level' % minimum_spell_level)
                else:
                    total = roll_d20(die_rolls + ((spell_level - minimum_spell_level) * dice_per_level), print_rolls)
                    print(' =', total, ' 2 *', total, ' =', 2 * total)
            else:
                print('Invalid Arguments')
        elif len(arg) == 1 and str.isdigit(arg[0]):
            spell_level = int(arg.pop())
            if spell_level < minimum_spell_level:
                print('Spell has to be cast at minimum %i level' % minimum_spell_level)
            else:
                total = roll_d20(die_rolls + ((spell_level - minimum_spell_level) * dice_per_level), print_rolls)
                print(' =', total)
        elif len(arg) == 1 and arg[0] == 'crit':
            total = roll_d20(die_rolls, print_rolls)
            print(' =', total, ' 2 *', total, ' =', 2 * total)
        else:
            print('Invalid Argument')
    else:
        total = roll_d20(die_rolls, print_rolls)
        print(' =', total)


def cast_d100(die_rolls, minimum_spell_level, arg):
    global print_rolls
    die_rolls
    minimum_spell_level
    arg = shlex.split(arg)
    if arg:
        if len(arg) > 2:
            print('Too many arguments')
            return
        elif len(arg) == 2:
            arg.sort()
            if str.isdigit(arg[0]) and arg[1] == 'crit':
                spell_level = int(arg.pop(0))
                if spell_level < minimum_spell_level:
                    print('Spell has to be cast at minimum %i level' % minimum_spell_level)
                else:
                    total = roll_d100(die_rolls + spell_level - minimum_spell_level, print_rolls)
                    print(' =', total, ' 2 *', total, ' =', 2 * total)
            else:
                print('Invalid Arguments')
        elif len(arg) == 1 and str.isdigit(arg[0]):
            spell_level = int(arg.pop())
            if spell_level < minimum_spell_level:
                print('Spell has to be cast at minimum %i level' % minimum_spell_level)
            else:
                total = roll_d100(die_rolls + spell_level - minimum_spell_level, print_rolls)
                print(' =', total)
        elif len(arg) == 1 and arg[0] == 'crit':
            total = roll_d100(die_rolls, print_rolls)
            print(' =', total, ' 2 *', total, ' =', 2 * total)
        else:
            print('Invalid Argument')
    else:
        total = roll_d100(die_rolls, print_rolls)
        print(' =', total)
