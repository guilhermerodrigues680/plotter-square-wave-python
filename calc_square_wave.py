# f Frequencia em Hz
# T Periodo em s
def generateSquareWave(f, T):

    if T < 1:
        raise ('O perido deve ser inteiro > 0')

    titleX = 'Tempo(s)'
    titleY = 'Tensão(V)'
    p = 1/f
    # x = [0, p/2, p/2, p, p]
    # y = [0, 0, 5, 5, 0]
    x =[]
    y =[]

    for i in range(T):
        # print(i)
        x.extend([p*i, (p*i)+(p/2), (p*i)+(p/2), p*(i+1), p*(i+1)])
        y.extend([0, 0, 5, 5, 0])

    waveInfo = "Frequencia: {}Hz :: Periodo: {}s :: Nº periodos plotados: {}".format(f, p, T)

    res = {
        'x': x,
        'y': y,
        'titleX': titleX,
        'titleY': titleY,
        'waveInfo': waveInfo,
    }

    print(waveInfo)
    return res


def generateSquareWavePWM(f, T, dutyCicle):
    if T < 1:
        raise ('O perido deve ser inteiro > 0')

    titleX = 'Tempo(s)'
    titleY = 'Tensão(V)'
    p = 1/f
    # x = [0, p*(dutyCicle/100), p*(dutyCicle/100), p, p]
    # y = [5, 5, 0, 0, 5]
    x =[]
    y =[]

    for i in range(T):
        # print(i)
        x.extend([p*i, (p*i)+p*(dutyCicle/100), (p*i)+p*(dutyCicle/100), p*(i+1), p*(i+1)])
        y.extend([5, 5, 0, 0, 5])

    waveInfo = "Frequencia: {}Hz :: Periodo: {}s :: DutyCicle {}% :: Nº periodos plotados: {}".format(f, p, dutyCicle, T)

    res = {
        'x': x,
        'y': y,
        'titleX': titleX,
        'titleY': titleY,
        'waveInfo': waveInfo,
    }

    print(res)
    print(waveInfo)
    return res

# print(generateSquareWave(30, 1))