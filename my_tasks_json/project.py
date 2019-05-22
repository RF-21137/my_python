import tkinter
import json
from tkinter import messagebox as mb

def add():  
    new = {"Задача": "-", "Категория": "-", "Время": "-"}

    task = taskName.get()
    category = categoryName.get()
    time = timeName.get()

    taskName.delete(0, "end")
    categoryName.delete(0, "end")
    timeName.delete(0, "end")

    if task == "":
        mb.showerror("Ошибка", "Введите задачу")
    else:
        new['Задача'] = task
        if category != "":
            new['Категория'] = category
        if time != "":
            new['Время'] = time
        todo.append(new)
        writer('list_of_tasks.json', todo)


def exit(): 
    window.destroy()


def writer(filename, numbers):
    import json
    try:
        with open(filename, 'w') as obj:
            json.dump(numbers, obj)
    except Exception as ex:
        print(ex)

def show():
    tasks = ""
    for task in todo:
        for option in task:
            tasks += option + ":" + task[option] + " "
        tasks += "\n"
    output.config(state="normal")
    output.delete("1.0", "end")
    output.insert("end", tasks)
    output.config(state="disabled")


global todo
todo = list()

window = tkinter.Tk()
window.title("Менеджер задач")
window.geometry("600x200+660+440")
window.resizable(False, False)

frame = tkinter.Frame(window)
frame.pack()

name1 = tkinter.Label(frame, text="Задача:")
name1.grid(row=0, column=0)
name2 = tkinter.Label(frame, text="Категория:")
name2.grid(row=1, column=0)
name3 = tkinter.Label(frame, text="Время:")
name3.grid(row=2, column=0)

taskName = tkinter.Entry(frame)
taskName.grid(row=0, column=1)
categoryName = tkinter.Entry(frame)
categoryName.grid(row=1, column=1)
timeName = tkinter.Entry(frame)
timeName.grid(row=2, column=1)

addButton = tkinter.Button(frame, text="Добавить", command=add)
addButton.grid(row=3, column=1)
openTasksButton = tkinter.Button(frame, text="Список задач", command=show)
openTasksButton.grid(row=4, column=1)
exitButton = tkinter.Button(frame, text="Выход", command=exit)
exitButton.grid(row=5, column=1)

output = tkinter.Text(frame, height=8, width=30, wrap="word", state="disabled")
output.grid(row=0, column=2, rowspan=6, padx=10, pady=4)

window.mainloop()
