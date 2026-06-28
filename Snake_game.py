import tkinter as tk

#размеры окна

WIDTH = 400
HEIGHT = 400

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
DIRECTIONS = ["Up", "Down", "Left", "Right"]

food = None
score = 0

game_over = False



#Запуск главного цикла программы
root.mainloop()
