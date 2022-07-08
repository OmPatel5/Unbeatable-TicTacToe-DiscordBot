from http import client
import discord
from discord.ext import commands
import time


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents = intents)


board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

game_started = False
player = ''

def display_board():
    print('|'+board[0]+'|'+board[1]+'|'+board[2]+'|')
    print('|'+board[3]+'|'+board[4]+'|'+board[5]+'|')
    print('|'+board[6]+'|'+board[7]+'|'+board[8]+'|')

@client.command()
async def place(ctx, number: int):
    global game_started

    if game_started:
        if player == str(ctx.message.author.mention):
            while True:
                number = int(number)
                number = number -1
                if -1<number<9:
                    if board[number] == '-':
                        board[number] = 'O'
                    else:    
                        await ctx.send('That spot was already taken!')     
                        break 

                else:
                    await ctx.send('That number was not a number between 1 and 9!')
                    break
                
        
                    #print board
                line = ""
                for i in range(len(board)):
                    if i == 2 or i == 5:
                        if board[i] == '-':
                            line += ':white_large_square:'
                            
                        elif board[i] == 'O':
                            line += ':o2:'
                                
                        else:
                            line += ':regional_indicator_x:'
                        
                        line += '\n'

                    else:
                        if board[i] == '-':
                            line += ':white_large_square:'
                            
                        elif board[i] == 'O':
                            line += ':o2:'
                                
                        else:
                            line += ':regional_indicator_x:' 
                await ctx.send(line)

                if check_horizontal_player() == 'Player O wins!' or check_verticle_player() == 'Player O wins!' or check_diagonal_player() == 'Player O wins!':
                    embed = discord.Embed(title = 'Winner!', description = 'The winner is... ' + str(ctx.message.author.mention) + '!')
                    await ctx.send(content=None, embed=embed)
                    game_started = False
                    break
                    
                    
                if check_draw() == 'The game is a Tie!':
                    embed = discord.Embed(title = "It's a Tie!", description = "It's a Tie!")
                    await ctx.send(content=None, embed=embed)
                    game_started = False
                    break
                    

                ai_turn()
                line = ""
                for i in range(len(board)):
                    if i == 2 or i == 5:
                        if board[i] == '-':
                            line += ':white_large_square:'
                            
                        elif board[i] == 'O':
                            line += ':o2:'
                                
                        else:
                            line += ':regional_indicator_x:'
                        
                        line += '\n'

                    else:
                        if board[i] == '-':
                            line += ':white_large_square:'
                            
                        elif board[i] == 'O':
                            line += ':o2:'
                                
                        else:
                            line += ':regional_indicator_x:' 
                await ctx.send("<@" + str(994358014700163072) + ">'s turn:")
                await ctx.send(line)


                if check_horizontal_player() == 'Player X wins!' or check_verticle_player() == 'Player X wins!' or check_diagonal_player() == 'Player X wins!':
                    # await ctx.send('Player X is the Winner!')
                    embed = discord.Embed(title = 'Winner!', description = 'The winner is... <@' + str(994358014700163072) + '>!')
                    await ctx.send(content=None, embed=embed)
                    game_started = False
                    break
                    
                    
                if check_draw() == 'The game is a Tie!':
                    embed = discord.Embed(title = "It's a Tie!", description = 'The game is a tie!')
                    await ctx.send(content = None, embed = embed)
                    game_started = False
                    break

                await ctx.send("It's your move " + str(ctx.message.author.mention) + ".")
                
                break
        else:
            await ctx.send('Oops! I think someone else is already playing.')
    else:
        await ctx.send('Start a new game by using the $tictactoe command.')    
            
            
            

def ai_turn():
    best_score = -1000
    best_move = 0

    for place in range(len(board)):
        if board[place] == '-':
            board[place] = 'X'
            score = minimax(board,0,False)
            board[place] = '-'

            if score > best_score:
                best_score = score
                best_move = place
            
    board[best_move] = 'X'
    return

def minimax(board, depth, isMaximizing):
    if check_diagonal_player() == 'Player X wins!' or check_horizontal_player() == 'Player X wins!' or check_verticle_player() == 'Player X wins!':
        return 1
    elif check_diagonal_player() == 'Player O wins!' or check_horizontal_player() == 'Player O wins!' or check_verticle_player() == 'Player O wins!':
        return -1
    
    elif check_draw() == 'The game is a Tie!':
        return 0

    if isMaximizing:
        best_score = -1000

        for place in range(len(board)):
            if board[place] == '-':
                board[place] = 'X'
                score = minimax(board,depth+1,False)
                board[place] = '-'

                if score > best_score:
                    best_score = score
        return best_score
    
    else:
        best_score = 1000

        for place in range(len(board)):
            if board[place] == '-':
                board[place] = 'O'
                score = minimax(board,depth+1,True)
                board[place] = '-'

                if score < best_score:
                    best_score = score
        return best_score
        
def check_horizontal_player():
    list = []
    for i in range(3):
        list.append(board[i])

    list2 = []
    for i in range(3, 6):
        list2.append(board[i])

    list3 = []
    for i in range(6, 9):
        list3.append(board[i])

    if list[0] == 'O' and list[1] == 'O' and list[2] == 'O':
        return 'Player O wins!'

    elif list2[0] == 'O' and list2[1] == 'O' and list2[2] == 'O':
        return 'Player O wins!'
    
    elif list3[0] == 'O' and list3[1] == 'O' and list3[2] == 'O':
        return 'Player O wins!'

    elif list[0] == 'X' and list[1] == 'X' and list[2] == 'X':
        return 'Player X wins!'

    elif list2[0] == 'X' and list2[1] == 'X' and list2[2] == 'X':
        return 'Player X wins!'
    
    elif list3[0] == 'X' and list3[1] == 'X' and list3[2] == 'X':
        return 'Player X wins!'

    else:
        return 'No one has won yet!'

def check_verticle_player():
    list = []
    for i in range(0, 7, 3):
        list.append(board[i])

    list2 = []
    for i in range(1, 8, 3):    
        list2.append(board[i])

    list3 = []
    for i in range(2, 9, 3):
        list3.append(board[i])

    if list[0] == 'O' and list[1] == 'O' and list[2] == 'O':
        return 'Player O wins!'

    elif list2[0] == 'O' and list2[1] == 'O' and list2[2] == 'O':
        return 'Player O wins!'
    
    elif list3[0] == 'O' and list3[1] == 'O' and list3[2] == 'O':
        return 'Player O wins!'

    if list[0] == 'X' and list[1] == 'X' and list[2] == 'X':
        return 'Player X wins!'

    elif list2[0] == 'X' and list2[1] == 'X' and list2[2] == 'X':
        return 'Player X wins!'
    
    elif list3[0] == 'X' and list3[1] == 'X' and list3[2] == 'X':
        return 'Player X wins!'

    else:
        return 'No one has won yet!'

def check_diagonal_player():
    list = [board[0], board[4], board[8]]

    list2 = [board[2], board[4], board[6]]

    if list[0] == 'O' and list[1] == 'O' and list[2] == 'O':
        return 'Player O wins!'

    elif list2[0] == 'O' and list2[1] == 'O' and list2[2] == 'O':
        return 'Player O wins!'

    elif list[0] == 'X' and list[1] == 'X' and list[2] == 'X':
        return 'Player X wins!'

    elif list2[0] == 'X' and list2[1] == 'X' and list2[2] == 'X':
        return 'Player X wins!'
    
    else:
        return 'No one has won yet!'
    
def check_draw():
    if (check_horizontal_player() == 'No one has won yet!' and check_diagonal_player() == 'No one has won yet!' and check_horizontal_player() == 'No one has won yet!'):
        if board.count('-') == 0:
            return 'The game is a Tie!'
    

@client.command()
async def tictactoe(ctx):
    global board
    global game_started
    global player

    board = ['-', '-', '-',
            '-', '-', '-',
            '-', '-', '-']
    
    if not game_started:
        game_started = True

        player = str(ctx.message.author.mention)

        
        await ctx.send('Welcome to TicTacToe! To place, use $place pos. Good Luck!')
        time.sleep(0.5)
        await ctx.send('I will go first. Here is the board:')
        time.sleep(0.5)
        line = ""
        for i in range(len(board)):
            if i == 2 or i == 5:
                if board[i] == '-':
                    line += ':white_large_square:'
                    
                elif board[i] == 'O':
                    line += ':o2:'
                        
                else:
                    line += ':regional_indicator_x:'
                
                line += '\n'

            else:
                if board[i] == '-':
                    line += ':white_large_square:'
                    
                elif board[i] == 'O':
                    line += ':o2:'
                        
                else:
                    line += ':regional_indicator_x:' 
        await ctx.send(line)
        line = ""
        time.sleep(1)
        await ctx.send('I am thinking....')
        ai_turn()
        time.sleep(3)

        for i in range(len(board)):
            if i == 2 or i == 5:
                if board[i] == '-':
                    line += ':white_large_square:'
                    
                elif board[i] == 'O':
                    line += ':o2:'
                        
                else:
                    line += ':regional_indicator_x:'
                
                line += '\n'

            else:
                if board[i] == '-':
                    line += ':white_large_square:'
                    
                elif board[i] == 'O':
                    line += ':o2:'
                        
                else:
                    line += ':regional_indicator_x:' 
        await ctx.send(line)
        line = ""


        if check_horizontal_player() == 'Player X wins!' or check_verticle_player() == 'Player X wins!' or check_diagonal_player() == 'Player X wins!':
            for i in range(len(board)):
                if i == 2 or i == 5:
                    if board[i] == '-':
                        line += ':white_large_square:'
                        
                    elif board[i] == 'O':
                        line += ':o2:'
                            
                    else:
                        line += ':regional_indicator_x:'
                    
                    line += '\n'

                else:
                    if board[i] == '-':
                        line += ':white_large_square:'
                        
                    elif board[i] == 'O':
                        line += ':o2:'
                            
                    else:
                        line += ':regional_indicator_x:' 
                await ctx.send(line)
                await ctx.send('Player X wins!') 
                line = ""                   

        if check_draw() == 'The game is a Tie!':
            for i in range(len(board)):
                if i == 2 or i == 5:
                    if board[i] == '-':
                        line += ':white_large_square:'
                        
                    elif board[i] == 'O':
                        line += ':o2:'
                            
                    else:
                        line += ':regional_indicator_x:'
                    
                    line += '\n'

                else:
                    if board[i] == '-':
                        line += ':white_large_square:'
                        
                    elif board[i] == 'O':
                        line += ':o2:'
                            
                    else:
                        line += ':regional_indicator_x:' 
            await ctx.send(line)
            await ctx.send('The game is a tie!')
            line = ""
        await ctx.send("It's your move " + str(ctx.message.author.mention) + ".")
    else:
        await ctx.send('Please quit your game to start a new one, unless you are not the one playing right now.')
    
    
@client.command()
async def quitGame(ctx):
    global game_started
    if player == str(ctx.message.author.mention):
        game_started = False
        await ctx.send('Game has ended.')
    else:
        await ctx.send("You can't quit another person's game!")

@client.command()
async def commands(ctx):
    embed = discord.Embed(title = 'TicTacToe BOT', description = 'Commands to get started on this BOT.')
    embed.add_field(name = '$tictactoe', value='Starts a new game')
    embed.add_field(name = '$place pos', value = 'Places a mark on game board')
    embed.add_field(name = '$quitGame', value = "Quit's the game.")
    await ctx.send(content = None, embed=embed)

#PUT YOUR TOKEN HERE:
client.run('place your token here')