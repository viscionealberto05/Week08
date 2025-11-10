from database.DAO import DAO

class Model:
    def __init__(self):
        self.DAO = DAO()

    def cerca_parole_dizionario(self):
        lista_parole = self.DAO.recupera_parole()
        #print(lista_parole)
        return lista_parole

    def calcola_anagrammi(self, parola):
        self._anagrammi = []
        self.ricorsione("", parola) #anagramma parziale, lettere rimanenti
        return self._anagrammi

    def ricorsione(self, anagramma_parziale, lettere_rimanenti):
        if len(lettere_rimanenti) == 0:
            self._anagrammi.append(anagramma_parziale)
            return
        else:
            for i in range(len(lettere_rimanenti)):
                anagramma_parziale += lettere_rimanenti[i]
                nuove_lettere_rimanenti = lettere_rimanenti[:i]+lettere_rimanenti[i+1:] #ovvero [][og], poi [d][g]
                self.ricorsione(anagramma_parziale, nuove_lettere_rimanenti)
                anagramma_parziale = anagramma_parziale[:-1]

#Prova implementazione
if __name__ == '__main__':
    model = Model()
    print(model.calcola_anagrammi("dog"))

"""[][dog]
[d][og]
[do][g]
[dog][] finisco quando la lista di lettere limanenti è vuota

rivedere slide pptx prof con disegni spiegazione per anagramma"""