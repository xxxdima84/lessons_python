number_of_stiks=10
player_turn=1

def can_take(stiks):
    return stiks >=1 and stiks <= 3

def switch_player_turn(turn):
    return 1 if player_turn == 2 else 2

def end_of_game(stiks):
    return number_of_stiks <= 0
while (not end_of_game (number_of_stiks)):
    print(f'Какое количество палоче хочет взять игрок? сейчас осталось {number_of_stiks}') #Какое количество палоче хочет взять игрок? и сколько сейчас осталось
    taken = int(input())# Сколько палочек взял игрок с конветацией в int
    
    if not can_take(taken):
        print(f'вы взяли {taken}, а можно взять 1,2,3')
        continue #  возврат на начало цикла
        
    number_of_stiks-=taken #  количество палочек = количество палочек - взятых
    print (f'взято палочек {taken}\n') # количество взято палочек 
    
    if end_of_game(number_of_stiks): 
           print(f'нет больше палочек в игре. \n Игрок {player_turn} проиграл') #Нет больше палочек проиграл текущй игрок
           break 
    
    player_turn = switch_player_turn(player_turn)# Смена игрока = (1) если смена игроа 2 то следующим тянет первый еслине первый игро сейчас второй