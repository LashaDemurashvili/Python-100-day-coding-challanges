from tkinter import *


def miles_to_km_fn():
    entry_text = miles_input.get()

    if not entry_text:
        miles_label.config(text="Enter number")
    else:
        miles = float(miles_input.get())
        miles_label.config(text='Miles')

        km = miles * 1.609  # round 2 decimal
        kilometer_result_label.config(text=f"{km:.2f} KM")  # configuration again as - string  and round 2 decimal :.2f


window = Tk()
window.title("Miles To Kilometer Converter")
window.config(padx=50, pady=50)
# configure padding

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="km")

calculate_button = Button(text="Calculate", command=miles_to_km_fn)
calculate_button.grid(column=1, row=2)

window.mainloop()
