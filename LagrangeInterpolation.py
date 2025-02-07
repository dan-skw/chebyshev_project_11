import numpy as np

'''
Definicja klasy LagrangeInterpolation, odpowiedzalnej za interpolację wielomianową Lagrange'a.
Implementacja została zaczerpnięta ze strony https://math.libretexts.org/Courses/Angelo_State_University/Mathematical_Computing_with_Python/3%3A_Interpolation_and_Curve_Fitting/3.2%3A_Polynomial_Interpolation oraz książki "Analiza numeryczna" autorstwa D. Kincaida i W. Cheney'a.
'''

class LagrangeInterpolation:
    def __init__(self, x_nodes, y_nodes):
        '''
        Konstruktor klasy, inicjalizujący obiekt, dla którego:
        x_nodes - węzły x
        y_nodes - węzły y
        '''
        self.x_nodes = x_nodes
        self.y_nodes = y_nodes

    def interpolate(self, x):
        '''
        Metoda odpowiedzialna za interpolację wielomianową Lagrange'a, na podstawie parametrów obiektu.
        x - argument, dla którego wykonywana jest interpolacja
        zwraca: wartość wielomianu interpolacyjnego w punkcie x -> return result
        '''
        n = len(self.x_nodes)
        result = 0
        for i in range(n):
            term = self.y_nodes[i]
            for j in range(n):
                if i != j:
                    term *= (x - self.x_nodes[j]) / (self.x_nodes[i] - self.x_nodes[j])
            result += term

        return result