from tkinter import*
from tkinter import ttk
from process_scale_factors import DiseconomyOfScale
from process_effort_multipliers import EffortMultiplier
from effort_estimation import EffortEstimation


def calculate_PM():
    ################### Send to process_scale_factor to get E

    SF_values = {key: var.get() for key, var in SF_dic.items()}

    # Create Scale Factor Object
    SF_Object = DiseconomyOfScale()
    SF_Object.update_scale_factors(SF_values)

    # Result of Scale Factor calculation
    E_Scale_Factor_result = SF_Object.calculate_diseconomy_of_scale()

    ################### Send to process_effort_multiplication to get EM

    EM_values = {key: var.get() for key, var in EM_dic.items()}

    EM_Object = EffortMultiplier()
    EM_Object.update_effort_multipliers(EM_values)

    EM_Effort_Multipliiers_result = EM_Object.calculate_effort_multiplier()
    print(EM_Effort_Multipliiers_result)

    try:
        size_value = float(SIZE_Entry.get())  # Преобразуем введённое значение в float
    except ValueError:
        size_value = 0.0  #

    EE_Object = EffortEstimation(size=size_value,
                                 diseconomy_of_scale=E_Scale_Factor_result,
                                 effort_modifier=EM_Effort_Multipliiers_result)
    PM_result = EE_Object.calculate()

    PM_Print = Label(text=f"{PM_result}")
    PM_Print.grid(column=1, row=21)

#---Main Window---
window = Tk()
window.title("CoCoMo2 Calculator")
window.geometry("700x700")

SF_List = ["PREC", "FLEX", "RESL", "TEAM", "PMAT"]
EM_List = ["RELY","DATA","CPLX","RUSE","DOCU","TIME","STOR","PVOL","ACAP",
           "PCAP","APEX","PLEX","LTEX","PCON","TOOL","SITE","SCED"]


SIZE_Label = Label(text="SIZE")
SIZE_Label.grid(column=0, row=1)
SIZE_Entry = Entry(width=15)
SIZE_Entry.grid(column=1, row=1)

SF_main = Label(window, text="Scale Factors")
SF_main.grid(column=1, row=3)

EM_main = Label(window, text="Effort Multiplication")
EM_main.grid(column=3, row=3)

####---Scale Factor Loop----------------

SF_row = 4
SF_column = 1

SF_dic = {}
for i in SF_List:
    dropdown_SF = StringVar()
    dropdown_SF.set("nominal")

    SF_Label = Label(window, text=i)
    SF_Label.grid(column=0, row=SF_row)
    dropdown_SF = ttk.Combobox(window, textvariable=dropdown_SF)
    dropdown_SF['values'] = ('extra high','very high',"high", 'nominal', "Low", "very low")
    dropdown_SF.grid(column=SF_column, row=SF_row)

    SF_dic[i] = dropdown_SF
    SF_row+=1


####--Effort Multiplication Loop-----
EM_row = 4
EM_column = 3

EM_dic = {}

for i in EM_List:
    dropdown_EM = StringVar()
    dropdown_EM.set("nominal")

    EM_Label = Label(window, text=i)
    EM_Label.grid(column=2, row=EM_row)
    dropdown_EM = ttk.Combobox(window, textvariable=dropdown_EM)
    dropdown_EM['values'] = ('extra high','very high',"high", 'nominal', "Low", "very low")
    dropdown_EM.grid(column=EM_column, row=EM_row)

    EM_dic[i] = dropdown_EM
    EM_row+=1







PM_label = Label(text="PM: ")
PM_label.grid(column=0, row=21)

generate_password_button = Button(text="Calculate PM", command=calculate_PM)
generate_password_button.grid(column=0, row=23)

window.mainloop()
