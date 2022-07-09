# Unbeatable-TicTacToe-DiscordBot 

# Table of contents
1. [About](#about)
    * [Built With](#builtwith)
2. [Getting Started](#gettingstarted)
    * [Installation](#installation) 
3. [Contact](#contact)

# About <a name="about"></a>
This is my Discord Bot I made with discord.py rewrite. This discord bot is a Tic Tac Toe bot which is unbeatable and uses an AI algorithm called MiniMax.

## How it Works
This bot has 4 commands: $tictactoe, which starts a new game, $place which places your piece where you want it, $quitGame, which quits the game, and $commands which gives you a list of commands with a brief explination of what they do. So to start playing, you first need to initiate a game using the $tictactoe command. Then, the bot places his piece first. Then it is your turn, and you place your piece with $place, and you and the bot go back and fourth in the game until there is a winner, and the game ends. 

## How the MiniMax Algorithim Works
The bot (player X) uses the MiniMax algorithim to determine which move is the best. In the current positions of the board, the bot simulates all of the possible positions it can go to. Then, the bot simulates all of the possible positions the other player can go to. It does this until the game is over. The bot makes these branches/paths of the possible moves the bot can make and the player can make. Then the bot looks at the final positions, and then gives a value.

## Built With <a name="builtwith"></a>
This program is built with the following languages:
* Python


add this bot to discord server:


https://discord.com/api/oauth2/authorize?client_id=994358014700163072&permissions=0&scope=bot
