from prettytable import PrettyTable

# A True 1d100 Wild Magic Surge Table, courtesy of /u/hillermylife.
# Link: https://www.reddit.com/r/UnearthedArcana/comments/67qei9/a_true_1d100_wild_magic_surge_table/
wild_magic_table = [
    'Roll on this table every round for 1 minute',
    'Caster and target switch positions after spell',
    'Can see invisible creatures',
    'A flaming horse appears (Not Nightmare, real horse',
    'A modron appears within 5 feet for one minute',
    'Caster explodes with plant growth',
    'Cast fireball at 3rd level centered on self',
    'Weapons in 60’ radius turn to food for 1 minute',
    'Cat magic missile as 5th-level spell',
    'Caster breathes 30’ fire cone next time they speak',
    'Change height by 1d10: Even: grow, Odd: shrink',
    'Target is cocooned in crystal until someone breaks it',
    'Cast confusion centered on self',
    'Cast thunder wave centered on self',
    'Regain 5 HP every round for 1 minute',
    'Target is transported to Ethereal Plane for 1 minute',
    'Grow long beard made of feathers until sneeze',
    'Swarm of rats carry caster 30’ in random direction',
    'Cast grease centered on self',
    'Creatures within 30’ are stuck in place vs Str DC 15',
    'For 1 minute, spell targets have disadv. on saves',
    'A mature oak sprouts in an unoccupied space in 60’',
    'Caster’s skin turns vibrant blue till remove curse',
    'Caster can only speak to animals for 24 hours',
    'Third eye grows; adv. on Perception for 1 minute',
    'Caster gains 100 lbs, move speed halved, 1 minute',
    'Spells cost additional bonus round cast time',
    'Next turn caster takes no action, vomits 1d100 SP',
    'Teleport up to 60 feet away to unoccupied space',
    'Caster’s hands become covered in sticky goop',
    'Transported to Astral Plane until end of next turn',
    'Cabbages sprout abundantly within a 30’ radius',
    'Max dmg of next damaging spell cast in next minute',
    'Caster can mimic target’s voice perfectly for 24 hrs',
    'Age changes 1d10 years. Odd: Younger, Even: Older',
    'Caster grows antlers, sheds them in 24 hours',
    '1d6 flumphs appear for 1 minute in 60’; scared',
    'Caster and target flung 10’ in opposite directions',
    'Regain 2d10 HP',
    'Gravity reverses in 30’ radius till start of next turn',
    'Become potted plant until start of next turn',
    'Caster distracted by cloud of gnats for next minute',
    'For next minute, teleport up to 20’ as bonus action',
    'Spell ricochets off target to random creature in 30’',
    'Cast levitate on self',
    'Caster’s money cycles: CP -> SP -> GP -> CP',
    'Unicorn appears within 5’ for next minute',
    'One of target’s eyes replaced by 500 GP sapphire',
    'Cannot speak, emit pink bubbles instead',
    'Smoke fumes from caster’s ears for 1 minute',
    'Spectral shield, +2 AC, no magic missile for 1 minute',
    'Caster gains 3’ prehensile tail for 1 hour',
    'Cannot get drunk for 5d6 days',
    'All unlocked doors/windows in 60’ fly open',
    'Hair falls out, grows back within 24 hours',
    'Caster’s face blackened by small explosion',
    'For 1 minute, flammable touch (not worn/carried',
    'Geyser lifts caster 50’ in air until start of next turn',
    'Regain lowest-level expended spell slot',
    'A confused bear appears within 60’ for 1 minute',
    'For 1 minute, can only shout when speaking',
    'Grass instantly sprouts to 3’ tall within 20’, 1 minute',
    'Cast fog cloud centered on self',
    'Caster can only breathe underwater for next minute',
    'Up to 3 creatures of choice in 30’:4d10 lightning dmg',
    'Caster falls Unconscious until start of next turn',
    'Frightened by nearest creature until end of next turn',
    'If target dies in next minute, its ghost haunts caster',
    'Everyone in 30’: invisible for 1 minute or till atk/cast',
    'All within 60’ saves vs Wis 15 or drops w/e they hold',
    'Resistance to all damage for next minute',
    'Everything within 20’ pulled 10’ toward caster',
    'Random creature within 60’ is poisoned for 24 hours',
    'Caster smells like lavender for 1d6 days',
    'Glow brightly for 1 minute. Blind others within 5’.',
    'Casters clothes become uncomfortably tight',
    'Cast polymorph on self. Fail save: Sheep form.',
    'If spell would kill target, target’s extremities fly apart',
    'Illusory butterflies/flowers flutter in 5’ radius 1 min.',
    'Caster trapped in a giant glass ball',
    'Take one additional action immediately',
    'Caster’s fists become huge, deal 1d8 B dmg, 1 min.',
    'Others in 30’: 1d10 necro dmg. Gain HP equal to loss',
    'Loud voice ridicules caster on init count 20 for 1 min',
    'Cast mirror image',
    'Caster’s arms become tentacles for 1 minute',
    'Cast fly on random creature within 60’',
    'Large floating eye follows caster for 1 hour',
    'Become invisible/silent for 1 minute or till atk/cast',
    'Caster’s INT and STR swap for 1 hour',
    'If you die in next minute, come back per reincarnate',
    'Caster sees everyone as a decaying corpse for 24h',
    'Size increases by 1 size category for 1 minute',
    'All light sources within 60’ radius extinguished',
    'You and all in 30’: vulnerable to piercing dmg, 1 min.',
    'Caster becomes frightened of a color for 1 hour',
    'Surrounded by faint ethereal music for 1 minute',
    'Caster suffers a head cold for 24 hours',
    'Regain all expended Sorcery Points',
    'Next phrase spoken by caster becomes true'
]


# Shamelessly copied from https://github.com/savagezen/dnd-tools/blob/master/scripts/dnd-tools :)
def expand(d):
    ret = {}
    for k in d:
        v = d[k]
        if isinstance(k, range):
            ret.update({i: v for i in k})
        else:
            ret[k] = v
    return ret


arctic_low = expand({
    1: 'giant owl - https://www.dndbeyond.com/monsters/giant-owl',
    range(2, 6): '1d6 + 3 kobolds - https://www.dndbeyond.com/monsters/kobold',
    range(6, 9): '1d4 + 3 trappers (commoners) - https://www.dndbeyond.com/monsters/commoner',
    range(9, 11): '1 owl - https://www.dndbeyond.com/monsters/owl',
    range(11, 13): '2d4 blood hawks - https://www.dndbeyond.com/monsters/blood-hawk',
    range(13, 18): '2d6 bandits - https://www.dndbeyond.com/monsters/bandit',
    range(18, 21): '1d3 winged kobolds with 1d6 kobolds - https://www.dndbeyond.com/monsters/winged-kobold - https://www.dndbeyond.com/monsters/kobold',
    range(21, 26): 'The partially eaten carcass of a mammoth, from which 1d4 weeks of rations can be harvested',
    range(26, 30): '2d8 hunters (tribal warriors) - https://www.dndbeyond.com/monsters/tribal-warrior',
    range(30, 36): '1 half-ogre - https://www.dndbeyond.com/monsters/half-ogre',
    range(36, 41): 'Single-file tracks in the snow that stop abruptly',
    range(41, 46): '1d3 ice mephits - https://www.dndbeyond.com/monsters/ice-mephit',
    range(46, 51): '1 brown bear - https://www.dndbeyond.com/monsters/brown-bear',
    range(51, 54): '1d6 + 1 orcs - https://www.dndbeyond.com/monsters/orc',
    range(54, 56): '1 polar bear - https://www.dndbeyond.com/monsters/polar-bear',
    range(56, 58): '1d6 scouts - https://www.dndbeyond.com/monsters/scout',
    range(58, 61): '1 saber-toothed tiger - https://www.dndbeyond.com/monsters/saber-toothed-tiger',
    range(61, 66): 'A frozen pond with a jagged hole in the ice that appears recently made',
    range(66, 69): '1 berserker - https://www.dndbeyond.com/monsters/berserker',
    range(69, 71): '1 ogre - https://www.dndbeyond.com/monsters/ogre',
    range(71, 73): '1 griffon - https://www.dndbeyond.com/monsters/griffon',
    range(73, 76): '1 druid - https://www.dndbeyond.com/monsters/druid',
    range(76, 81): '3d4 refugees (commoners) fleeing from orcs - https://www.dndbeyond.com/monsters/commoner - https://www.dndbeyond.com/monsters/orc',
    81: '1d3 veterans - https://www.dndbeyond.com/monsters/veteran',
    82: '1d4 orogs - https://www.dndbeyond.com/monsters/orog',
    83: '2 brown bears - https://www.dndbeyond.com/monsters/brown-bear',
    84: '1 orc Eye of Gruumsh with 2d8 orcs - https://www.dndbeyond.com/monsters/orc-eye-of-gruumsh - https://www.dndbeyond.com/monsters/orc',
    85: '1d3 winter wolves - https://www.dndbeyond.com/monsters/winter-wolf',
    range(86, 88): '1d4 yetis - https://www.dndbeyond.com/monsters/yeti',
    88: '1 half-ogre - https://www.dndbeyond.com/monsters/half-ogre',
    89: '1d3 manticores - https://www.dndbeyond.com/monsters/manticore',
    90: '1 bandit captain with 2d6 bandits - https://www.dndbeyond.com/monsters/bandit-captain - https://www.dndbeyond.com/monsters/bandit',
    91: '1 revenant - https://www.dndbeyond.com/monsters/revenant',
    range(92, 94):	'1 troll - https://www.dndbeyond.com/monsters/troll',
    range(94, 96):	'1 werebear - https://www.dndbeyond.com/monsters/werebear',
    range(96, 98):	'1 young remorhaz - https://www.dndbeyond.com/monsters/young-remorhaz',
    98: '1 mammoth - https://www.dndbeyond.com/monsters/mammoth',
    99: '1 young white dragon - https://www.dndbeyond.com/monsters/young-white-dragon',
    100: '1 frost giant - https://www.dndbeyond.com/monsters/frost-giant'
})

arctic_mid = expand({
    range(1, 7): '2 saber-toothed tigers - https://www.dndbeyond.com/monsters/saber-toothed-tiger',
    range(7, 8): '1d4 half-ogres - https://www.dndbeyond.com/monsters/half-ogre',
    range(8, 11): '1d3 + 1 brown bears - https://www.dndbeyond.com/monsters/brown-bear',
    range(11, 16): '1d3 polar bears - https://www.dndbeyond.com/monsters/polar-bear',
    range(16, 21): '2d4 berserkers - https://www.dndbeyond.com/monsters/berserker',
    range(21, 26): 'A half-orc druid tending to an injured polar bear. If the characters assist the druid, she gives them a vial of antitoxin. - https://www.dndbeyond.com/monsters/druid - https://www.dndbeyond.com/monsters/polar-bear',
    range(26, 31): '2d8 scouts - https://www.dndbeyond.com/monsters/scout',
    range(31, 36): '2d4 ice mephits - https://www.dndbeyond.com/monsters/ice-mephit',
    range(36, 41): '2d6 + 1 zombies aboard a galleon trapped in the ice. Searching the ship yields 2d20 days of rations. - https://www.dndbeyond.com/monsters/zombie',
    range(41, 46): '1 manticore - https://www.dndbeyond.com/monsters/manticore',
    range(46, 51): '2d6 + 3 orcs - https://www.dndbeyond.com/monsters/orc',
    range(51, 54): '1d6 + 2 ogres - https://www.dndbeyond.com/monsters/ogre',
    range(54, 56): '2d4 griffons - https://www.dndbeyond.com/monsters/griffon',
    range(56, 58): '1d4 veterans - https://www.dndbeyond.com/monsters/veteran',
    range(58, 61): '1 bandit captain with 1 druid, 1d3 berserkers, and 2d10 + 5 bandits - https://www.dndbeyond.com/monsters/bandit-captain - https://www.dndbeyond.com/monsters/druid - https://www.dndbeyond.com/monsters/berserker - https://www.dndbeyond.com/monsters/bandit',
    range(61, 66): '1d4 hours of extreme cold (see chapter 5 of the Dungeon Master’s Guide)',
    range(66, 69): '1 young remorhaz - https://www.dndbeyond.com/monsters/young-remorhaz',
    range(69, 73): '1 orc Eye of Gruumsh with 1d6 orogs and 2d8 + 6 orcs - https://www.dndbeyond.com/monsters/orc-eye-of-gruumsh - https://www.dndbeyond.com/monsters/orog - https://www.dndbeyond.com/monsters/orc',
    range(73, 76): '1 revenant - https://www.dndbeyond.com/monsters/revenant',
    range(76, 81): 'A howl that echoes over the land for 1d3 minutes',
    range(81, 83): '1d3 mammoths - https://www.dndbeyond.com/monsters/mammoth',
    range(83, 85): '1 young white dragon - https://www.dndbeyond.com/monsters/young-white-dragon',
    range(85, 87): '2d4 winter wolves - https://www.dndbeyond.com/monsters/winter-wolf',
    range(87, 89): '1d6 + 2 yetis - https://www.dndbeyond.com/monsters/yeti',
    range(89, 91): '1d2 frost giants - https://www.dndbeyond.com/monsters/frost-giant',
    range(91, 93): '1d3 werebears - https://www.dndbeyond.com/monsters/werebear',
    range(93, 95): '1d4 trolls - https://www.dndbeyond.com/monsters/troll',
    range(95, 97): '1 abominable yeti - https://www.dndbeyond.com/monsters/abominable-yeti',
    range(97, 99): '1 remorhaz - https://www.dndbeyond.com/monsters/remorhaz',
    99:	'1 roc - https://www.dndbeyond.com/monsters/roc',
    100: '2d4 young remorhazes - https://www.dndbeyond.com/monsters/young-remorhaz'
})

arctic_high = expand({
    1:	'1 abominable yeti - https://www.dndbeyond.com/monsters/abominable-yeti',
    range(2, 5): '1d6 revenants - https://www.dndbeyond.com/monsters/revenant',
    range(5, 11): '1d4 + 1 werebears - https://www.dndbeyond.com/monsters/werebear',
    range(11, 21): '1d3 young white dragons - https://www.dndbeyond.com/monsters/young-white-dragon',
    range(21, 26): 'A blizzard that reduces visibility to 5 feet for 1d6 hours',
    range(26, 36): '1 roc - https://www.dndbeyond.com/monsters/roc',
    range(36, 41): 'A herd of 3d20 + 60 caribou (deer) moving through the snow - https://www.dndbeyond.com/monsters/deer',
    range(41, 51): '1d4 mammoths - https://www.dndbeyond.com/monsters/mammoth',
    range(51, 61): '1d8 + 1 trolls - https://www.dndbeyond.com/monsters/troll',
    range(61, 66): 'A mile-wide frozen lake in which the preserved corpses of strange creatures can be seen',
    range(66, 76): '2d4 young remorhazes - https://www.dndbeyond.com/monsters/young-remorhaz',
    range(76, 81): 'A crumbling ice castle littered with the frozen bodies of blue-skinned humanoids',
    range(81, 91): '1 adult white dragon - https://www.dndbeyond.com/monsters/adult-white-dragon',
    range(91, 97): '1d8 + 1 frost giants - https://www.dndbeyond.com/monsters/frost-giant',
    range(97, 100): '1d4 remorhazes - https://www.dndbeyond.com/monsters/remorhaz',
    100: '1 ancient white dragon - https://www.dndbeyond.com/monsters/ancient-white-dragon'
})

arctic_epic = expand({
    range(1, 3): '2d10 revenants - https://www.dndbeyond.com/monsters/revenant',
    range(3, 5): '2d8 trolls - https://www.dndbeyond.com/monsters/troll',
    range(5, 7): '2d10 werebears - https://www.dndbeyond.com/monsters/werebear',
    range(7, 9): '1 frost giant - https://www.dndbeyond.com/monsters/frost-giant',
    range(9, 11): '2d4 young remorhazes - https://www.dndbeyond.com/monsters/young-remorhaz',
    range(11, 21): '1d4 frost giants - https://www.dndbeyond.com/monsters/frost-giant',
    range(21, 26): 'A circular patch of black ice on the ground. The air temperature around the patch is warmer than in the surrounding area, and characters who inspect the ice find bits of machinery frozen within.',
    range(26, 36): '1 ancient white dragon - https://www.dndbeyond.com/monsters/ancient-white-dragon',
    range(36, 41): 'An adventurer frozen 6 feet under the ice; 50% chance the corpse has a rare magic item of the DM’s choice',
    range(41, 51): '1d3 abominable yetis - https://www.dndbeyond.com/monsters/abominable-yeti',
    range(51, 61): '1d4 remorhazes - https://www.dndbeyond.com/monsters/remorhaz',
    range(61, 66): 'A 500-foot-high wall of ice that is 300 feet thick and spread across 1d4 miles',
    range(66, 76): '1d4 rocs - https://www.dndbeyond.com/monsters/roc',
    range(76, 81): 'The likeness of a stern woman with long, flowing hair, carved into the side of a mountain',
    range(81, 91): '1d10 frost giants with 2d4 polar bears - https://www.dndbeyond.com/monsters/frost-giant - https://www.dndbeyond.com/monsters/polar-bear',
    range(91, 97): '1d3 adult white dragons - https://www.dndbeyond.com/monsters/adult-white-dragon',
    range(97, 100): '2d4 abominable yetis - https://www.dndbeyond.com/monsters/abominable-yeti',
    100: '1 ancient white dragon with 1d3 young white dragons - https://www.dndbeyond.com/monsters/ancient-white-dragon - https://www.dndbeyond.com/monsters/young-white-dragon'
})

coastal_low = expand({
    1: '1 pseudodragon - https://www.dndbeyond.com/monsters/pseudodragon',
    range(2, 6): '2d8 crabs - https://www.dndbeyond.com/monsters/crab',
    range(6, 11): '2d6 fishers (commoners) - https://www.dndbeyond.com/monsters/commoner',
    11:	'1d3 poisonous snakes - https://www.dndbeyond.com/monsters/poisonous-snake',
    range(12, 14): '1d6 guards protecting a stranded noble - https://www.dndbeyond.com/monsters/guard - https://www.dndbeyond.com/monsters/noble',
    range(14, 16): '2d4 scouts - https://www.dndbeyond.com/monsters/scout',
    range(16, 19): '2d10 merfolk - https://www.dndbeyond.com/monsters/merfolk',
    range(19, 21): '1d6 + 2 sahuagin - https://www.dndbeyond.com/monsters/sahuagin',
    range(21, 26): '1d4 ghouls feeding on corpses aboard the wreckage of a merchant ship. A search uncovers 2d6 bolts of ruined silk, a 50-foot length of rope, and a barrel of salted herring. - https://www.dndbeyond.com/monsters/ghoul',
    range(26, 28): '1d4 winged kobolds with 1d6 + 1 kobolds - https://www.dndbeyond.com/monsters/winged-kobold - https://www.dndbeyond.com/monsters/kobold',
    range(28, 30): '2d6 tribal warriors - https://www.dndbeyond.com/monsters/tribal-warrior',
    range(30, 32): '3d4 kobolds - https://www.dndbeyond.com/monsters/kobold',
    range(32, 34): '2d4 + 5 blood hawks - https://www.dndbeyond.com/monsters/blood-hawk',
    range(34, 36): '1d8 + 1 pteranodons - https://www.dndbeyond.com/monsters/pteranodon',
    range(36, 41): 'A few dozen baby turtles struggling to make their way to the sea',
    range(41, 43): '1d6 + 2 giant lizards - https://www.dndbeyond.com/monsters/giant-lizard',
    range(43, 45): '1d6 + 4 giant crabs - https://www.dndbeyond.com/monsters/giant-crab',
    range(45, 47): '2d4 stirges - https://www.dndbeyond.com/monsters/stirge',
    range(47, 49): '2d6 + 3 bandits - https://www.dndbeyond.com/monsters/bandit',
    range(49, 54): '2d4 sahuagin - https://www.dndbeyond.com/monsters/sahuagin',
    range(54, 56): '1d6 + 2 scouts - https://www.dndbeyond.com/monsters/scout',
    range(56, 61): '1 sea hag - https://www.dndbeyond.com/monsters/sea-hag',
    range(61, 66): 'A momentary formation in the waves that looks like an enormous humanoid face',
    range(66, 71): '1 druid - https://www.dndbeyond.com/monsters/druid',
    range(71, 76): '1d4 harpies - https://www.dndbeyond.com/monsters/harpy',
    range(76, 81): 'A lone hermit (acolyte) sitting on the beach, contemplating the meaning of the multiverse - https://www.dndbeyond.com/monsters/acolyte',
    81: '1d4 berserkers - https://www.dndbeyond.com/monsters/berserker',
    82:	'1d6 giant eagles - https://www.dndbeyond.com/monsters/giant-eagle',
    83:	'2d4 giant toads - https://www.dndbeyond.com/monsters/giant-toad',
    84:	'1d4 ogres or 1d4 merrow - https://www.dndbeyond.com/monsters/ogre - https://www.dndbeyond.com/monsters/merrow',
    85:	'3d6 sahuagin - https://www.dndbeyond.com/monsters/sahuagin',
    86:	'1d4 veterans - https://www.dndbeyond.com/monsters/veteran',
    87:	'1d2 plesiosauruses - https://www.dndbeyond.com/monsters/plesiosaurus',
    88:	'1 bandit captain with 2d6 bandits - https://www.dndbeyond.com/monsters/bandit-captain - https://www.dndbeyond.com/monsters/bandit',
    89:	'1d3 manticores - https://www.dndbeyond.com/monsters/manticore',
    90:	'1 banshee - https://www.dndbeyond.com/monsters/banshee',
    range(91, 93): '1d4 + 3 griffons - https://www.dndbeyond.com/monsters/griffon',
    range(93, 95): '1 sahuagin priestess with 1d3 merrow and 2d6 sahuagin - https://www.dndbeyond.com/monsters/priest - https://www.dndbeyond.com/monsters/merrow - https://www.dndbeyond.com/monsters/sahuagin',
    range(95, 97): '1 sahuagin baron - https://www.dndbeyond.com/monsters/sahuagin-baron',
    range(97, 99): '1 water elemental - https://www.dndbeyond.com/monsters/water-elemental',
    99:	'1 cyclops - https://www.dndbeyond.com/monsters/cyclops',
    100: '1 young bronze dragon - https://www.dndbeyond.com/monsters/young-bronze-dragon'
})

coastal_mid = expand({
    1: '2d8 giant wolf spiders - https://www.dndbeyond.com/monsters/giant-wolf-spider',
    range(2, 4): '3d6 pteranodons - https://www.dndbeyond.com/monsters/pteranodon',
    range(4, 6): '2d4 scouts - https://www.dndbeyond.com/monsters/scout',
    range(6, 8): '1d6 + 2 sahuagin - https://www.dndbeyond.com/monsters/sahuagin',
    8: '1 sea hag - https://www.dndbeyond.com/monsters/sea-hag',
    range(9, 11): '1d4 + 1 giant toads - https://www.dndbeyond.com/monsters/giant-toad',
    range(11, 16): '3d6 sahuagin - https://www.dndbeyond.com/monsters/sahuagin',
    range(16, 21): '2d6 giant eagles - https://www.dndbeyond.com/monsters/giant-eagle',
    range(21, 26): 'A pseudodragon chasing gulls through the air - https://www.dndbeyond.com/monsters/pseudodragon',
    range(26, 30): '1d2 druids - https://www.dndbeyond.com/monsters/druid',
    range(30, 33): '2d4 + 1 giant toads - https://www.dndbeyond.com/monsters/giant-toad',
    range(33, 36): '1 commoner singing a dirge (day only) or 1 banshee (night only) - https://www.dndbeyond.com/monsters/commoner - https://www.dndbeyond.com/monsters/banshee',
    range(36, 41): 'A stoppered bottle containing an illegible note and half buried in the sand',
    range(41, 44): '3 sea hags - https://www.dndbeyond.com/monsters/sea-hag',
    range(44, 47): '1d8 + 1 harpies - https://www.dndbeyond.com/monsters/harpy',
    range(47, 51): '1d4 plesiosauruses - https://www.dndbeyond.com/monsters/plesiosaurus',
    range(51, 54): '1d4 manticores - https://www.dndbeyond.com/monsters/manticore',
    range(54, 57): '2d4 ogres - https://www.dndbeyond.com/monsters/ogre',
    range(57, 61): '1d10 griffons - https://www.dndbeyond.com/monsters/griffon',
    range(61, 66): 'A battle at sea between two galleons',
    range(66, 71): '1d4 + 3 merrow - https://www.dndbeyond.com/monsters/merrow',
    range(71, 76): 'A pirate crew consisting of 1 bandit captain, 1 druid, 2 berserkers, and 2d12 bandits, all searching for buried treasure - https://www.dndbeyond.com/monsters/bandit-captain - https://www.dndbeyond.com/monsters/druid - https://www.dndbeyond.com/monsters/berserker - https://www.dndbeyond.com/monsters/bandit',
    range(76, 81): 'A severed humanoid hand tangled in a net',
    range(81, 83): '1 water elemental - https://www.dndbeyond.com/monsters/water-elemental',
    range(83, 85): '1 cyclops - https://www.dndbeyond.com/monsters/cyclops',
    range(85, 87): '1d4 banshees (night only) - https://www.dndbeyond.com/monsters/banshee',
    range(87, 89): '2d4 veterans - https://www.dndbeyond.com/monsters/veteran',
    range(89, 91): '1 young bronze dragon - https://www.dndbeyond.com/monsters/young-bronze-dragon',
    range(91, 94): '1d3 cyclopes - https://www.dndbeyond.com/monsters/cyclops',
    range(94, 96): '1 young blue dragon - https://www.dndbeyond.com/monsters/young-blue-dragon',
    96:	'1 sahuagin baron with 1d3 sahuagin priestesses and 2d8 sahuagin - https://www.dndbeyond.com/monsters/sahuagin-baron - https://www.dndbeyond.com/monsters/sahuagin-priestess - https://www.dndbeyond.com/monsters/sahuagin',
    97:	'1 djinni - https://www.dndbeyond.com/monsters/djinni',
    98:	'1 roc - https://www.dndbeyond.com/monsters/roc',
    99:	'1 marid - https://www.dndbeyond.com/monsters/marid',
    100: '1 storm giant - https://www.dndbeyond.com/monsters/storm-giant',
})

coastal_high = expand({
    1: '1d4 banshees (night only) - https://www.dndbeyond.com/monsters/banshee',
    range(2, 5): '1 cyclops - https://www.dndbeyond.com/monsters/cyclops',
    range(5, 9): '1d6 + 2 manticores - https://www.dndbeyond.com/monsters/manticore',
    range(9, 11): '1d8 + 2 veterans - https://www.dndbeyond.com/monsters/veteran',
    range(11, 21): '1 young blue dragon - https://www.dndbeyond.com/monsters/young-blue-dragon',
    range(21, 26): 'A nest of 1d6 dragon turtle eggs',
    range(26, 36): '1d4 sahuagin barons - https://www.dndbeyond.com/monsters/sahuagin-baron',
    range(36, 41): 'A trident partially buried in the sand',
    range(41, 51): '1 young bronze dragon - https://www.dndbeyond.com/monsters/young-bronze-dragon',
    range(51, 56): '1 marid - https://www.dndbeyond.com/monsters/marid',
    range(56, 61): '1d6 water elementals - https://www.dndbeyond.com/monsters/water-elemental',
    range(61, 66): '2d6 ghasts crawling over 1d6 wrecked ships and feeding on the dead - https://www.dndbeyond.com/monsters/ghast',
    range(66, 71): '1 djinni - https://www.dndbeyond.com/monsters/djinni',
    range(71, 76): '1d3 young bronze dragons - https://www.dndbeyond.com/monsters/young-bronze-dragon',
    range(76, 81): 'A beached whale, dead and bloated. If it takes any damage, it explodes, and each creature within 30 feet of it must make a DC 15 Dexterity saving throw, taking 5d6 bludgeoning damage on a failed save, or half as much damage on a successful one.',
    range(81, 83): '2d4 cyclopes - https://www.dndbeyond.com/monsters/cyclops',
    range(83, 85): '1 storm giant - https://www.dndbeyond.com/monsters/storm-giant',
    range(85, 87): '1d3 young blue dragons - https://www.dndbeyond.com/monsters/young-blue-dragon',
    range(87, 89): '1 adult bronze dragon - https://www.dndbeyond.com/monsters/adult-bronze-dragon',
    range(89, 91): '1 adult blue dragon - https://www.dndbeyond.com/monsters/adult-blue-dragon',
    range(91, 94): '1d3 rocs - https://www.dndbeyond.com/monsters/roc',
    range(94, 98): '1 dragon turtle - https://www.dndbeyond.com/monsters/dragon-turtle',
    range(98, 100): '1 ancient bronze dragon - https://www.dndbeyond.com/monsters/ancient-bronze-dragon',
    100: '1 ancient blue dragon - https://www.dndbeyond.com/monsters/ancient-blue-dragon'
})

coastal_epic = expand({
    range(1, 11): '1 roc - https://www.dndbeyond.com/monsters/roc',
    range(11, 21): '1 storm giant - https://www.dndbeyond.com/monsters/storm-giant',
    range(21, 26): 'An adult bronze dragon fighting an adult blue dragon to the death - https://www.dndbeyond.com/monsters/adult-bronze-dragon - https://www.dndbeyond.com/monsters/adult-blue-dragon',
    range(26, 41): '2d6 cyclopes - https://www.dndbeyond.com/monsters/cyclops',
    range(41, 51): '1 adult bronze dragon or 1 adult blue dragon - https://www.dndbeyond.com/monsters/adult-bronze-dragon - https://www.dndbeyond.com/monsters/adult-blue-dragon',
    range(51, 61): '1d3 djinn or 1d3 marids - https://www.dndbeyond.com/monsters/djinni - https://www.dndbeyond.com/monsters/marid',
    range(61, 71): '1 dragon turtle - https://www.dndbeyond.com/monsters/dragon-turtle',
    range(71, 76): '1d3 rocs - https://www.dndbeyond.com/monsters/roc',
    range(76, 81): '1d6 + 2 waterspouts that dance on the water before stopping abruptly',
    range(81, 91): '1d6 young blue dragons - https://www.dndbeyond.com/monsters/young-blue-dragon',
    range(91, 97): '1 ancient bronze dragon - https://www.dndbeyond.com/monsters/ancient-bronze-dragon',
    range(97, 100): '1 ancient blue dragon - https://www.dndbeyond.com/monsters/ancient-blue-dragon',
    100: '1d3 + 1 storm giants - https://www.dndbeyond.com/monsters/storm-giant'
})

# At this point I decided it was time to look for a computer-readable file with the encounters.
# I found one, though it required some reformatting and I still had to manually copy all the dndbeyond links.
# The rest of the encounters can be found in the encounters.json file.

blinded = "A blinded creature can't see and automatically fails any ability check that requires sight. " \
          "\nAttack rolls against the creature have advantage, and the creature's attack rolls have disadvantage."

charmed = "A charmed creature can't attack the charmer or target the charmer with harmful abilities or magical effects." \
          "\nThe charmer has advantage on any ability check to interact socially with the creature."

deafened = "A deafened creature can't hear and automatically fails any ability check that requires hearing."


def exhaustion():
    print("Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing"
          " or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in"
          " six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's "
          "description.")
    table = PrettyTable()
    table.add_column('Level', ['1', '2', '3', '4', '5', '6'])
    table.add_column('Effect', ['Disadvantage on ability checks', 'Speed halved',
                                'Disadvantage on attack rolls and saving throws', 'Hit point maximum halved',
                                'Speed reduced to 0', 'Death]'])
    print(table)
    print("If an already exhausted creature suffers another effect that causes exhaustion,"
          " its current level of exhaustion increases by the amount specified in the effect's description."
          "\nA creature suffers the effect of its current level of exhaustion as well as all lower levels. "
          "For example, a creature suffering level 2 exhaustion has its speed halved and has disadvantage on ability checks."
          "\nAn effect that removes exhaustion reduces its level as specified in the effect's description, "
          "with all exhaustion effects ending if a creature's exhaustion level is reduced below 1."
          "\nFinishing a long rest reduces a creature's exhaustion level by 1, provided that the creature has also "
          "ingested some food and drink. Also, being raised from the dead reduces a creature’s exhaustion level by 1.")


frightned = "A frightened creature has disadvantage on ability checks and attack rolls while the source of its fear" \
            " is within line of sight. \nThe creature can't willingly move closer to the source of its fear."

grappled = "A grappled creature's speed becomes 0, and it can't benefit from any bonus to its speed. " \
           "\nThe condition ends if the grappler is incapacitated (see the condition). " \
           "\nThe condition also ends if an effect removes the grappled creature from the reach of the grappler or " \
           "grappling effect, such as when a creature is hurled away by the thunderwave spell."

incapacitated = "An incapacitated creature can't take actions or reactions."

invisible = "An invisible creature is impossible to see without the aid of magic or a special sense. " \
            "For the purpose of hiding, the creature is heavily obscured. " \
            "The creature's location can be detected by any noise it makes or any tracks it leaves. " \
            "\nAttack rolls against the creature have disadvantage, and the creature's attack rolls have advantage."

paralyzed = "A paralyzed creature is incapacitated (see the condition) and can't move or speak. " \
            "\nThe creature automatically fails Strength and Dexterity saving throws. " \
            "\nAttack rolls against the creature have advantage. " \
            "\nAny attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature."

petrified = "A petrified creature is transformed, along with any nonmagical object it is wearing or carrying, " \
            "into a solid inanimate substance (usually stone). " \
            "Its weight increases by a factor of ten, and it ceases aging. " \
            "\nThe creature is incapacitated (see the condition), can't move or speak, and is unaware of its surroundings." \
            "\nAttack rolls against the creature have advantage. " \
            "\nThe creature automatically fails Strength and Dexterity saving throws. " \
            "\nThe creature has resistance to all damage. " \
            "\nThe creature is immune to poison and disease, although a poison or disease already in its system is suspended, not neutralized."

poisoned = "A poisoned creature has disadvantage on attack rolls and ability checks."

prone = "A prone creature's only movement option is to crawl, unless it stands up and thereby ends the condition. " \
        "\nThe creature has disadvantage on attack rolls. " \
        "\nAn attack roll against the creature has advantage if the attacker is within 5 feet of the creature. " \
        "Otherwise, the attack roll has disadvantage."

restrained = "A restrained creature's speed becomes 0, and it can't benefit from any bonus to its speed. " \
             "\nAttack rolls against the creature have advantage, and the creature's attack rolls have disadvantage. " \
             "\nThe creature has disadvantage on Dexterity saving throws."

stunned = "A stunned creature is incapacitated (see the condition), can't move, and can speak only falteringly. " \
          "\nThe creature automatically fails Strength and Dexterity saving throws. " \
          "\nAttack rolls against the creature have advantage."

unconscious = "An unconscious creature is incapacitated, can't move or speak, and is unaware of its surroundings " \
              "\nThe creature drops whatever it's holding and falls prone. " \
              "\nThe creature automatically fails Strength and Dexterity saving throws. " \
              "\nAttack rolls against the creature have advantage. " \
              "\nAny attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature."
