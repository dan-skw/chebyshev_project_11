import numpy as np
import matplotlib as plt

'''
Definicja klasy ChebyshevNodes, odpowiedzalnej za generowanie n węzłów Czebyszewa na podanym przedziale [a, b].
# Wzór został zaczerpnięty ze strony https://ccfd.github.io/courses/info2_lab01.html oraz książki "Analiza numeryczna" autorstwa D. Kincaida i W. Cheney'a.
'''
class ChebyshevNodes:
    def __init__(self, a, b, n):
        '''
        Konstruktor klasy, inicjalizujący obiekt, dla którego:
        a - początek przedziału
        b - koniec przedziału
        n - liczba węzłów
        '''
        self.a = a
        self.b = b
        self.n = n

    def generate_nodes(self):
        '''
        Metoda odpowiedzialna za generowanie węzłów Czebyszyewa, na podstawie parametrów obiektu.
        zwraca: tablicę z węzłami Czebyszyewa -> return nodes
        '''
        nodes = np.array([
            0.5 * (self.a + self.b) + 0.5 * (self.b - self.a) * np.cos((2 * i - 1)/(2 * self.n) *np.pi)
            for i in range(1, self.n + 1)
        ])

        return nodes
    

