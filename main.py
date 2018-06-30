from graphics import *
from Logic import *
from GraphicsUnit import GraphicsUnit as Gu


def main():
    window_width = 750
    window_height = 750
    cell_size = 25
    weights = [3]  # Weights the different Rule-compsed temp grids to compose the next iteration grid

    # Initialize Window
    window = GraphWin("PY-CA", window_width, window_height, autoflush=False)

    # Initialize automat with propability vector
    automat = CellAutomata(window_width, window_height, cell_size)

    period = 0
    while True:
        drawn_elements = (Gu.draw_grid(window, automat.cells, cell_size))
        window.update()
        Gu.undraw_elements(drawn_elements)
        automat.run_rules(period, weights)
        period += 1
main()
