romans=dict(I=1, V=5, X=10, L=50, C=100, D=500, M=100) # создаем словарь

#может быть передано XIV
def parse_roman(roman):   # создать функцию парсинга
    result = 0           # созаем переменную аккумулятор которая позволит накапливать число
    for i, c in enumerate (roman): #запускаем цикл и так как нам индекс и текущий элемент использую enumerate
        if i+1<len(roman) and romans[roman[i]] < romans[roman[i+1]]:
            result-=romans[roman[i]]
        else:
            result+= romans[roman[i]]
    return result 