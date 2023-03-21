def estimar_tiempo(ingredientes):
    n_ingredientes = len(ingredientes['ingredientes'])
    tiempo = 20 + n_ingredientes * 2
    return tiempo
if __name__ == '__main__':
    ingredientes_prueba = {
        'masa': 'Masa Tradicional', 'salsa':'Salsa de Tomate', 'ingrediente': ['queso']
    }
    print(estimar_tiempo(ingredientes_prueba))