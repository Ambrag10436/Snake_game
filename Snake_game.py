import tkinter as tk
import random



#размеры окна

WIDTH = 400
HEIGHT = 400
DIRECTIONS = ["Up", "Down", "Left", "Right"]
CELL_SIZE = 10
DELAY = 100 #задержка между движениями змеи



# создаем главное окно
root = tk.Tk()
root.title("Змейка | Счет: 0")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="black",
    highlightthickness=0
)
canvas.pack()

snake = [(100, 100), (90, 100), (80, 100)]
direction = "Right"
score = 0
game_over = False


def create_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if (x, y) not in snake: # проверка не находится ли еда внутри змеи
            return (x, y)
food = create_food()

def draw_food():
    canvas.create_rectangle(
        food[0], food[1],
        food[0] + CELL_SIZE, food[1] + CELL_SIZE,
        fill="red",
    )

def game_loop():
    global snake, food, score

    canvas.delete("all")
    draw_food()
    root.after(DELAY, game_loop)

draw_food()
root.after(DELAY, game_loop)

#Запуск главного цикла программы
root.mainloop()
