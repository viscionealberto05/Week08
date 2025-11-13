#array di regine come lista di tuple (slide 65)

"""def ricorsione(parziale, N) #devo passare la soluzione che via via si sta affacciando, scelgo che la mia soluzione sia una lista che indica le coordinate dove stanno le regine
    #parziale è la soluzione parziale  (lista coordinate) e N che è la dimensione della lista, la funzione verrà chiamata più volte

    #devo inserire poi una condizione di terminazione (if-->si esce/else-->si continua)
    #la mia condizione di uscita è quando ho 4 coordinate di regine nella lista, ovvero if len(parzziale)==N allora posso uscire
    e faccio print(parziale)

    else:
    devo ricorrere e richiamare la mia funzione
        for each cell:  #esplora tutte le celle possibili (rows/columns)
            parziale.append(cell) #devo specificare che la regina sta
            ricorsione(parziale, N)
            backtracking"""