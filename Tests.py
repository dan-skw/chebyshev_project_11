from ChebyshevNodes import ChebyshevNodes
from LagrangeInterpolation import LagrangeInterpolation
from Plots import Plots  

import numpy as np

class Tests:
    @staticmethod
    def test():
        run_script = input("""
                           DSkwarczek - Metody Numeryczne temat 11.

        Program do interpolacji wielomianowej zadanej funkcji za pomocą węzłów Czebyszewa i metody Lagrange'a.
        Aby kontynuować wpisz t/T i zatwierdź Enterem.    
        Następnie wypełnij dane zgodnie z instrukcjami.           
        
                            ----
                           
        Jeżeli chcesz opuścić program, wciśnij Ctrl+C.
                           
                            ----
                           
        Czy chcesz kontynuować? (t/T): """)
        
        if run_script == "t" or run_script == "T":
            pass
        else:
            return
        
        '''
        Funkcją parsująca wprowadzony przez użytkownika string na funkcję matematyczną interpretowaną przez Pythona.
        Należy stosować składnie pythonową, na ten moment obsługuje podstawową trygonometrię, logarytm naturalny i pierwiastek kwadratowy oraz potęge liczby eulera.
        '''
        def parse_function(string_x):
            string_x = string_x.replace('sin', 'np.sin')
            string_x = string_x.replace('cos', 'np.cos')
            string_x = string_x.replace('tan', 'np.tan')
            string_x = string_x.replace('log', 'np.log')
            string_x = string_x.replace('exp', 'np.exp')
            string_x = string_x.replace('sqrt', 'np.sqrt')

            def f(x):
                return eval(string_x)
            
            return f

        # parametry
        input_correct = True
        input_correct = True
        while input_correct:
            try:
                func = input('''
        Podaj funkcję f(x): ''')
                a = float(input('''
        Podaj początek przedziału: '''))
                b = float(input('''
        Podaj koniec przedziału: '''))
                n = int(input('''
        Podaj liczbę węzłów: '''))
                if n <= 0:
                    print('''
        ! Podano niepoprawne dane. Liczba węzłów musi być liczbą naturalną. Spróbuj jeszcze raz.''')
                    continue  

                if a >= b:
                    print('''
        ! Podano niepoprawne dane. Początek przedziału musi być mniejszy od końca przedziału. Spróbuj jeszcze raz.''')
                    continue  
                
                input_correct = False

            except ValueError:
                print('''! 
        Podano niepoprawne dane. Wartości muszą być liczbami. Spróbuj jeszcze raz.''')

        # generowanie węzłów Czebyszewa
        chebyshev = ChebyshevNodes(a, b, n)
        x_nodes = chebyshev.generate_nodes()
        y_nodes = parse_function(func)(x_nodes)

        # interpolacja Lagrange'a
        interpolation = LagrangeInterpolation(x_nodes, y_nodes)

        # wyświetlenie wyników
        print(f"Węzły Czebyszewa: {x_nodes}")
        print(f"Wartości funkcji w węzłach: {y_nodes}")

        # tworzenie wykresu
        x_plot = np.linspace(a, b, 1000)
        y_plot = parse_function(func)(x_plot)
        y_interpolated = [interpolation.interpolate(x) for x in x_plot]

        # wyświetlenie wykresu
        Plots.plot(x_plot, y_plot, y_interpolated, x_nodes, y_nodes)

if __name__ == "__main__":
    Tests.test()
