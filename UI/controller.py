import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        #Creo una lista in cui metto tutte le parole contenute nel dizionario
        self.parole_dizionario = []

    def popola_dizionario(self):
        self.parole_dizionario = self._model.cerca_parole_dizionario()
        #for parola in self.parole_dizionario:
            #print(parola)
        return self.parole_dizionario

    def calcola_anagrammi(self, e):
        parola = self._view.txt_word.value
        if parola == "":
            self._view.create_alert("Inserire una parola")
        else:
            anagrammi = self._model.calcola_anagrammi(parola)
            dizionario_italiano = self.popola_dizionario()
            for anagramma in anagrammi:
                if anagramma in dizionario_italiano:
                    self._view.lst_correct.controls.append(ft.Text(anagramma))
                else:
                    self._view.lst_wrong.controls.append(ft.Text(anagramma))
            self._view.update_page()

    def reset(self, e):
        self._view.txt_word.value = ""
        self._view.lst_correct.controls.clear()
        self._view.lst_wrong.controls.clear()
        self._view.update_page()

