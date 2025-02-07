import matplotlib.pyplot as plt
'''
Klasa odpowiedzialna za rysowanie wykresów za pomocą biblioteki matplotlib.
Przyjmuje jako argumenty:
- x_plot: wartości x dla wykresu funkcji
- y_plot: wartości y dla wykresu funkcji
- y_interpolated: wartości y dla wykresu wielomianu interpolacyjnego
- x_nodes: wartości x węzłów Czebyszewa
- y_nodes: wartości y węzłów Czebyszewa
'''
class Plots:
    @staticmethod
    def plot(x_plot, y_plot, y_interpolated, x_nodes, y_nodes):
        plt.figure(figsize=(10, 6))
        plt.plot(x_plot, y_plot, label="Oryginalna funkcja f(x)", color="blue")
        plt.plot(x_plot, y_interpolated, label="Wielomian interpolacyjny", color="red", linestyle="--")
        plt.scatter(x_nodes, y_nodes, color="black", label="Węzły Czebyszewa", zorder=5)
        plt.legend()
        plt.title("Interpolacja wielomianowa dla węzłów Czebyszewa")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.show()