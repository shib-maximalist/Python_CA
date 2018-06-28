from graphics import *


class GraphicsUnit:
    @staticmethod
    def draw_grid(window, cells, cell_size):
        for row in range(0, len(cells)):
            for col in range(0, len(cells[0])):
                GraphicsUnit.draw_cell(window, col * cell_size, row * cell_size, cell_size, cells[row][col])

    @staticmethod
    def draw_cell(window, x_up_left, y_up_left, cell_size, cell):
        p1 = Point(x_up_left, y_up_left)
        p2 = Point(x_up_left + cell_size, y_up_left + cell_size)

        if cell.state_person == 1:
            square = Rectangle(p1, p2)
            square.setFill("black")
            square.setOutline("white")
            square.setWidth(1)

            # Human specific Data
            txt1 = Text(Point((p1.getX() + cell_size / 5), (p1.getY() + cell_size / 5)), cell.state_wealth)
            txt2 = Text(Point((p1.getX() + 4 * cell_size / 5), (p1.getY() + cell_size / 5)), "x")
            txt3 = Text(Point((p1.getX() + cell_size / 5), (p1.getY() + 3.5 * cell_size / 5)), "x")
            txt4 = Text(Point((p1.getX() + 4 * cell_size / 5), (p1.getY() + 3.5 * cell_size / 5)), "x")

            # Wealth on uninhabited cells is cost
            txt_list = [txt1, txt2, txt3, txt4]
            for i in txt_list:
                i.setSize(int(round(cell_size / 3.25)))

            txt1.setTextColor("orange")
            txt2.setTextColor("yellow")
            txt3.setTextColor("red")
            txt4.setTextColor("green")

        else:
            square = Rectangle(p1, p2)
            square.setFill("white")
            square.setOutline("black")
            square.setWidth(1)

            # Space cost instead of persons welath
            txt1 = Text(Point((p1.getX() + cell_size / 2), (p1.getY() + cell_size / 2)), cell.state_wealth)
            txt1.draw(window)
            return

        square.draw(window)
        for i in txt_list:
            i.draw(window)