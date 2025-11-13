#L'obiettivo è mettere le 4 regine in una 4x4 in posizioni in cui non possono attaccarsi tra loro
import copy


class NRegine:
    def __init__(self):
        self._num_soluzioni = 0
        self._num_iterazioni = 0 #numero di ricorsioni
        self._soluzioni = []

    def _risolvi_n_regine(self, N):
        self._num_soluzioni = 0
        self._num_iterazioni = 0  # numero di ricorsioni
        self._soluzioni = []
        self._ricorsione([], N)

    def _ricorsione(self, parziale, N):
        self._num_iterazioni += 1
        #caso terminale
        if len(parziale) == N:
            print(parziale)
            self._num_soluzioni += 1
            if self._soluzione_nuova(parziale) == True:
                self._soluzioni.append(copy.deepcopy(parziale)) #parziale con le azioni di backtracking viene sempre svuotata, faccio dunque deepcopy per aggungere una lista non vuota

        #caso ricorsivo
        else:
            for row in range(N):
                for col in range(N):
                    parziale.append((row, col))   #regina, la coppia riga-colonna  è una tupla

                    #STUDIO LE CONDIZIONI VALIDE PERCHè LE REGINE VENGANO MESSE DOVE NON SI POSSONO ATTACCARE
                    if self._soluzione_ammissibile(parziale):
                        self._ricorsione(parziale, N)
                    parziale.pop()  #rimuove l'ultima regina (BACKTRACKING)

    def _soluzione_ammissibile(self, parziale):
        #True se ammissibile, False altrimenti

        ultima_regina = parziale[-1]
        for regina in parziale[: len(parziale)-1]:
            #Controllo tutte le condizioni di attaccabilità
            #controllare righe
            if ultima_regina[0] == regina[0]: #se l'ultima che ho aggiunto è uguale alla prima... (controllo le coordinate con le tuple)
                return False
            #controllare colonne
            if ultima_regina[1] == regina[1]:
                return False
            #controllare diagonali
            #matematicamente sfrutto che se riga-colonna è uguale allora sono sulla diagonale
            if ((ultima_regina[0]-ultima_regina[1])) == (regina[0]-regina[1]):
                return False
            if ((ultima_regina[0]+ultima_regina[1])) == (regina[0]+regina[1]):
                return False
        return True #ci sono comunque soluzioni già trovate che sono tra loro uguali

    def _soluzione_nuova(self, soluzione_nuova):
        for soluzione in self._soluzioni:
            for regina in soluzione_nuova:
                if regina in soluzione:
                    return False
        return True

if __name__ == '__main__':
    nr = NRegine()
    nr._risolvi_n_regine(4)
    print(f"Trovate {nr._num_soluzioni} soluzioni")
    print(f"Chiamata {nr._num_iterazioni} la funzione ricorsiva")
    #Inizialmente molte soluzioni non sono valide, non vengono rispettate le regole che abbiamo stabilito all'inizio
    print(nr._soluzioni)