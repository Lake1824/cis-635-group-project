from tkinter import*
from tkinter import ttk

from equivalent_kloc import EquivalentKloc
from process_scale_factors import DiseconomyOfScale
from process_effort_multipliers import EffortMultiplier
from effort_estimation import EffortEstimation
from schedule_estimation import ScheduleEstimation
from team_size import TeamSize

def calculate_TS(PM, TDEV):
    TS_Object = TeamSize(PM, TDEV)
    TS_Result = TS_Object.calculate()
    TS_Print = Label(text=f"{TS_Result:.2f}")
    TS_Print.grid(column=1, row=23)

def calculate_TDEV(PM, E_Scale_Factor_result, sced_value):
    SE_Object = ScheduleEstimation(PM, E_Scale_Factor_result, sced_value)

    SE_Result = SE_Object.calculate()
    TDEV_Print= Label(text=f"{SE_Result:.2f}")
    TDEV_Print.grid(column=1, row=22)

    calculate_TS(PM, SE_Result)

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
    print(f"PM result: {PM_result}")
    print(f"E: {E_Scale_Factor_result}")
    print(f"EM: {EM_Effort_Multipliiers_result}")

    PM_Print = Label(text=f"{PM_result:.2f}")
    PM_Print.grid(column=1, row=21)

    calculate_cost(PM_result)

    calculate_TDEV(PM_result, E_Scale_Factor_result, sced_value=EM_Object.SCED_VALUE)

def calculate_cost(effort_estimation):
    try:
        software_labor_rate = float(cost_entry.get())
    except ValueError:
        software_labor_rate = 0.0
    cost_print = Label(text=f"${(effort_estimation * software_labor_rate):.2f}")
    cost_print.grid(column=1, row=24)

def calculate_ekloc():
    try:
        equivalent_kloc_obj = EquivalentKloc(float(reuse_size_entry.get()), float(design_modified_entry.get()),
                                             float(code_modified_entry.get()),
                                             float(integration_required_entry.get()),
                                             software_understanding_var.get(),
                                             unfamiliarity_var.get(), aa_var.get(), float(at_percentage_entry.get()))
        ekloc_size = equivalent_kloc_obj.calculate()
    except ValueError:
        ekloc_size = 0.00

    ekloc_result = Label(text=f"{ekloc_size:.4f}")
    ekloc_result.grid(column=1, row=30)


#---Main Window---
window = Tk()
window.title("COCOMO 2 Calculator")
window.geometry("1800x1800")

SF_List = ["PREC", "FLEX", "RESL", "TEAM", "PMAT"]
EM_List = ["RELY","DATA","CPLX","RUSE","DOCU","TIME","STOR","PVOL","ACAP",
           "PCAP","APEX","PLEX","LTEX","PCON","TOOL","SITE","SCED"]


SIZE_Label = Label(text="Program Size(KLOC):")
SIZE_Label.grid(column=0, row=1)
SIZE_Entry = Entry(width=15)
SIZE_Entry.grid(column=1, row=1)

cost_label = Label(text="Cost per Person-Month(Dollars):")
cost_label.grid(column=0, row=2)
cost_entry = Entry(width=15)
cost_entry.grid(column=1, row=2)

SF_main = Label(window, text="Scale Factors")
SF_main.grid(column=1, row=4)

EM_main = Label(window, text="Effort Multipliers")
EM_main.grid(column=3, row=4)

####---Scale Factor Loop----------------

SF_row = 5
SF_column = 1

SF_dic = {}
for i in SF_List:
    SF_var = StringVar()
    SF_var.set("nominal")

    SF_Label = Label(window, text=i)
    SF_Label.grid(column=0, row=SF_row)
    dropdown_SF = ttk.Combobox(window, textvariable=SF_var)
    dropdown_SF['values'] = ('extra high','very high',"high", 'nominal', "low", "very low")
    dropdown_SF.current(3)
    dropdown_SF.grid(column=SF_column, row=SF_row)

    SF_dic[i] = SF_var
    SF_row+=1


####--Effort Multiplication Loop-----
EM_row = 5
EM_column = 3

EM_dic = {}

for i in EM_List:
    EM_var = StringVar()
    EM_var.set("nominal")

    EM_Label = Label(window, text=i)
    EM_Label.grid(column=2, row=EM_row)
    dropdown_EM = ttk.Combobox(window, textvariable=EM_var)
    dropdown_EM['values'] = ('extra high','very high',"high", 'nominal', "low", "very low")
    dropdown_EM.current(3)
    dropdown_EM.grid(column=EM_column, row=EM_row)

    EM_dic[i] = EM_var
    EM_row+=1

for i, v in SF_dic.items():
    print(f"{i} {v}")

PM_label = Label(text="Effort Estimation(PM): ")
PM_label.grid(column=0, row=21)
TDEV_Label = Label(text=f"Schedule Estimation(TDEV): ")
TDEV_Label.grid(column=0, row=22)
TS_Label = Label(text="Team Size:")
TS_Label.grid(column=0, row=23)
cost_result_label = Label(text="Cost(Dollars): ")
cost_result_label.grid(column=0, row=24)

calculate_button = Button(text="Calculate", command=calculate_PM)
calculate_button.grid(column=0, row=25)

reuse_size_label = Label(text="Calculate Equivalent KLOC",font=('Helvetica', 12, 'bold'))
reuse_size_label.grid(column=0, row=26)

reuse_size_label = Label(text="Adapted Size(KLOC):")
reuse_size_label.grid(column=0, row=27)
reuse_size_entry = Entry(width=15)
reuse_size_entry.grid(column=1, row=27)

design_modified_label = Label(text="Design Modified %:")
design_modified_label.grid(column=0, row=28)
design_modified_entry = Entry(width=15)
design_modified_entry.grid(column=1, row=28)

code_modified_label = Label(text="Code Modified %:")
code_modified_label.grid(column=2, row=28)
code_modified_entry = Entry(width=15)
code_modified_entry.grid(column=3, row=28)

integration_required_label = Label(text="Integration Required %:")
integration_required_label.grid(column=4, row=28)
integration_required_entry = Entry(width=15)
integration_required_entry.grid(column=5, row=28)

at_percentage_label = Label(text="Code Re-Engineered By Automatic Translation %:")
at_percentage_label.grid(column=6, row=28)
at_percentage_entry = Entry(width=15)
at_percentage_entry.grid(column=7, row=28)

software_understanding_label = Label(text="Software Understanding Increment:")
software_understanding_label.grid(column=0, row=29)
software_understanding_var = StringVar(value="nominal")
software_understanding_dropdown = ttk.Combobox(window, textvariable=software_understanding_var)
software_understanding_dropdown['values'] = ('very low', 'low', 'nominal', 'high', 'very high')
software_understanding_dropdown.current(2)
software_understanding_dropdown.grid(column=1, row=29)

unfamiliarity_label = Label(text="Programmer Unfamiliarity:")
unfamiliarity_label.grid(column=2, row=29)
unfamiliarity_var = StringVar(value='completely familiar')
unfamiliarity_dropdown = ttk.Combobox(window, textvariable=unfamiliarity_var)
unfamiliarity_dropdown['values'] = ('completely familiar', 'mostly familiar', 'somewhat familiar', 'considerably familiar', 'mostly unfamiliar', 'completely unfamiliar')
unfamiliarity_dropdown.current(0)
unfamiliarity_dropdown.grid(column=3, row=29)

aa_label = Label(text="Assessment and Assimilation Increment:")
aa_label.grid(column=4, row=29)
aa_var = StringVar(value="none")
aa_dropdown = ttk.Combobox(window, textvariable=aa_var)
aa_dropdown['values'] = ('none', 'basic module search and documentation', 'some T&E, documentation', 'considerable T&E, documentation', 'extensive T&E, documentation')
aa_dropdown.current(2)
aa_dropdown.grid(column=5, row=29)

ekloc_result_label = Label(text="Equivalent KLOC: ")
ekloc_result_label.grid(column=0, row=30)

calculate_ekloc_button = Button(text="Calculate", command=calculate_ekloc)
calculate_ekloc_button.grid(column=0, row=31)

window.mainloop()
