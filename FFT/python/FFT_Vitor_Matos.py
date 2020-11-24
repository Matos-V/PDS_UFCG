def FFT_Vitor_Matos(x):
    import numpy as np
    N = len(x)
    if N == 2:
        borboleta = np.zeros(2)
        borboleta[0] = x[0] + x[1]
        borboleta[1] = x[0] - x[1]
        return borboleta
    else:
        pares = FFT_Vitor_Matos(x[::2])
        impares = FFT_Vitor_Matos(x[1::2])
        indices = np.arange(N)
        W = np.exp(-2j*np.pi*indices/N)
        W_primeira_metade = W[:int(N/2)]
        W_segunda_metade = W[int(N/2):]
        return np.concatenate([pares + W_primeira_metade*impares, pares + W_segunda_metade*impares])