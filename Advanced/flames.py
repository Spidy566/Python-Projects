import tkinter as tk


def flames():
    name1 = entry1.get().lower().replace(" ", "")
    name2 = entry2.get().lower().replace(" ", "")

    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    count = len(name1) + len(name2)

    flames_result = ["Friend", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(flames_result) > 1:
        index = (count % len(flames_result)) - 1
        if index >= 0:
            flames_result = flames_result[index + 1:] + flames_result[:index]
        else:
            flames_result = flames_result[:len(flames_result) - 1]

    label_result.config(text=flames_result[0])


root = tk.Tk()
root.title("FLAMES Game")
root.geometry("300x200")

label1 = tk.Label(root, text="Enter First Name:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="Enter Second Name:")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

button = tk.Button(root, text="Calculate", command=flames)
button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
