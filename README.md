# Unbeatable TicTacToe DiscordBot

https://user-images.githubusercontent.com/104532194/178116981-239e6385-b891-4bc6-b687-271a29a02e05.mp4


# Table of Contents
1. [About](#about)
    * [Built With](#builtwith)
2. [Getting Started](#gettingstarted)
    * [Installation](#installation) 
3. [Usage](#usage)
4. [Contact](#contact)

# About <a name="about"></a>
This is my Discord Bot I made with discord.py rewrite. This discord bot is a Tic Tac Toe bot which is unbeatable and uses an AI algorithm called MiniMax.

## How it Works
This bot has 4 commands: $tictactoe, which starts a new game, $place which places your piece where you want it, $quitGame, which quits the game, and $commands which gives you a list of commands with a brief explination of what they do. So to start playing, you first need to initiate a game using the $tictactoe command. Then, the bot places his piece first. Then it is your turn, and you place your piece with $place, and you and the bot go back and fourth in the game until there is a winner, and the game ends. 

## How the MiniMax Algorithim Works
The bot (player X) uses the MiniMax algorithim to determine which move is the best. In the current positions of the board, the bot simulates all of the possible positions it can go to. Then, the bot simulates all of the possible positions the other player can go to. It does this until the game is over. The bot makes these branches/paths of the possible moves the bot can make and the player can make. Then the bot looks at all of the final positions. Player X wants to have the maximizing score, and player O wants to have the lowest score to win. The bot goes through every possible move, and gives each position a value. If the bot wins, it gives the board a value of 1, if the other player wins the bot gives the board a -1, and if it is a tie, the bot gives it a value of 0. With that value, the bot can pick which of these paths leads to the best outcome of the game, and from there the bot can pick which move leads to the highest score.

## Built With <a name="builtwith"></a>
This program is built with the following languages:
* Python

# Getting Started <a name="gettingstarted"></a>
**To get this project running follow these steps**

## Installation <a name="installation"></a>
1. Clone the Repository
```sh
   git clone https://github.com/OmPatel5/Unbeatable-TicTacToe-DiscordBot.git
   ```
2. Install discord.py Rewrite
```sh
   pip install -U git+https://github.com/Rapptz/discord.py@rewrite
   ```
3. Put your bot's Discord Token on this line
```sh
   client.run('place your token here')
   ```
   (line 437)

# Usage <a name="usage"></a>
If you want to try out this bot on your server, click this link:

https://discord.com/api/oauth2/authorize?client_id=994358014700163072&permissions=0&scope=bot


# Contact <a name="contact"></a>
Om Patel - omp091216@gmail.com

Project Link: https://github.com/OmPatel5/Unbeatable-TicTacToe-DiscordBot
