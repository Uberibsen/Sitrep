# Sitrep - A Foxhole Discord bot
This project is a Discord bot providing status updates on the ongoing war within the game Foxhole.

[Foxhole](https://www.foxholegame.com/) is a massively multiplayer game where you will work with hundreds of players to shape the outcome of a persistent online war. The bot is developed with the [War API](https://github.com/clapfoot/warapi), and fetches data via the API every time the user initiates the bot with pre-written commands

*This project is in heavy development and features are subject to change.*
## Commands
The prefix for activating Sitrep is `!sr` followed by your command. Each argument in the commands requires a single space in between.

List of current commands:
- `!sr help` - Gives a list of all commands
- `!sr report` - Gives a report of the current wars' casualties and enlistments on both sides.
- `!sr hex "hex name"` - This command gives an overview of casualties and enlistments on both sides of the current war in a specific hex. Example: `!sr hex viper`
  - The command doesn't require the whole hexagons name. You can simply search with a minimum of 3 characters. For example, writing `!sr hex wild` will return with data from the hex Umbral Wildwood. 
- `!sr captures "hex name"` - This command returns a list of captures structures by each side.

## Roadmap
According to plan, the bot will have the following features:
- Overall war report
  - Casualties on both sides
  - War duration and outcome
- Individual Hex information
- Latest 24 hours
  - List of recent objectives captured/lost

If the project receives sufficient support and engagement, features that could be included are as follows:
- Prior wars outcomes
  - Total casualties, victors, etc.
- Majority control of key objectives
  - Number of factories, refineries, etc. that each side holds.

## Availablity
While in development, the bot will not be able to be invited into other Discords. The code, however, will remain open-source if you wish to try it out yourself and maybe contribute. Meanwhile, you can support my work by buying me a coffee right [here](https://www.buymeacoffee.com/uberibsen). 