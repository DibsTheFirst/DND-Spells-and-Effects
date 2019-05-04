# DND-Spells-and-Effects
What started out as a simple Command Line Interface (CLI) which allowed you to enter the name of a spell and return the corresponding
dice rolls quickly evoled into a more advanced CLI with tonnes of useful features! 
Those features include:
## Technical Stuff
### 1) Tab-Completion
Theres nothing fun about having to write (and correctly spell) **abi_dalzims_horrid_wilting** and other long spells. Tab-completion allows
you to write abi, then press tab to auto-complete it. If there are multiple possible commands to auto-complete, 
it will show you all of them. For example writing **a** and pressing tab will show you a list of all commands starting with **a**.
### 2) History
Pressing the **up key** will copy the last command, pressing it again will move further up the history. Pressing the **down key** will 
move you down in the history. This history will persist across sessions by storing it in a file.
## D&D Stuff
### 1) All the spells! 
This application contains support for all 450+ official spells. And yes, I had to make a unique method for each one. Inputing the name of a spell 
returns a nice looking table with all the key information like duration or casting time. It will also roll the correct number and type
of dice for you. All spells have two optional argument: A number signifying the level you cast the spell at and "crit", which will double
the dice roll. 

So **fireball** will return the result of rolling 8d6, **fireball 8** will return the result of rolling 13d6, **fireball crit** will return
the result of rolling 8d6 * 2 and **fireball 8 crit** or **fireball crit 8** will return the result of rolling 13d6 * 2

If you want the full spell description, just type **help** followed by spell name. Example: **help fireball**
### 2) Random Encounters
I've added all the random encounters from Xanathar's Guide to Everything. Those are: **Arctic, Coastal, Desert, Forest, Grassland, Hill,
Mountain, Swamp, Underdark, Underwater and Urban.** They all require the level of the players as an argument. So **arctic 3** will
return a random encounter suitable for a group of level 1 - 4 players in an arctic region. 

More importantly; along with the random encounter it will also give you a direct link to the monsters page on d&dbeyond!
### 3) Dice Rolls
You can roll all the dice you'd expect, d4 - d100. All have a number as an optional argument. **d6 5** will return 5 d6 rolls and the sum.
### 4) Healing potions
The commands are **minor, greater, superior and supreme**. **Superior** will return the result of 8d4 + 8
### 5) Wild Magic
**wild_magic** will return one of 100 random wild magic effects. If you prefer to have the player roll the d100 themself, you can type in
**wild_magic _number_** instead.
### 6) Roll stats
**create_character** will _roll 4d6 and remove the lowest_ 6 times.
### Items
The **item** command can be used to look up the information of any magic item. You will have to type in the name of the item as one
single string (wrapped in quotation marks). So **item "alchemy jug"** is correct, **item alchemy jug** is not, as alchemy and jug is interprited as two arguments. Unlike most other commands, the arguments of **item** supports tab completion!
