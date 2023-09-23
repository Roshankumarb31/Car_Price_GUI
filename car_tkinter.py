import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
sns.set(style="darkgrid",font_scale=1.5)
pd.set_option("display.max.columns",None)
pd.set_option("display.max.rows",None)

from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from xgboost import XGBRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler

from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.resizable(width=FALSE,height=FALSE)
root.title("Car Price")



bb, ww, gg, rr, bl  = "black", "white", "#00FFFF",  "#FF8000", "#00FFFF"

def mode_change(mode_temp):
    if mode_temp == 0:
        bb, ww, gg, rr , bl = "white", "black", "magenta", "#FF10F0", "#990099"
        mode.config(text = "☀️ Dark Mode", foreground = bl, bg = bb, activebackground = gg, command = lambda: mode_change(1))
    else:
        bb, ww, gg, rr, bl  = "black", "white", "#00FFFF",  "#FF8000", "#00FFFF"
        mode.config(text = "☀️Light Mode", foreground = bl, bg = bb, activebackground = gg, command = lambda: mode_change(0))
    
    root.configure(background = bb)
    status_down.configure(background = bb)
    status_left.configure(background = bb)
    status_middle.configure(background = bb)
    status_right.configure(background = bb)

    frame_s1.config(foreground = bl, bg = bb)
    wheel_base_s.config(bg = bb, fg = ww, troughcolor = bl, activebackground = rr)

    frame_s2.config(foreground = bl, bg = bb)
    car_length_s.config(bg = bb, fg = ww, troughcolor = bl, activebackground = rr)

    frame_s3.config(foreground = bl, bg = bb)
    car_width_s.config(bg = bb, fg = ww, troughcolor = bl, activebackground = rr)

    frame_s4.config(foreground = bl, bg = bb)
    curb_weight_s.config(bg = bb, fg = ww, troughcolor = bl, activebackground = rr)

    frame_s5.config(foreground = bl, bg = bb)
    engine_size_s.config(bg = bb, fg = ww, troughcolor = bl, activebackground = rr)

    frame_s6.config(foreground = bl, bg = bb)
    bore_ratio_s.config(bg = bb, fg = ww, troughcolor = bl, activebackground = rr)

    frame_s7.config(foreground = bl, bg = bb)
    horse_power_s.config(bg = bb, fg = ww, troughcolor = bl, activebackground = rr)

    frame_s8.config(foreground = bl, bg = bb)
    mileage_s.config(bg = bb, fg = ww, troughcolor = bl, activebackground = rr)

    frame_d1.config(foreground = bl, bg = bb)
    drop_d1.config(bg = bb, fg = ww, highlightbackground = rr, activebackground = rr)
    drop_d1["menu"].config(bg = bb, fg = ww)

    frame_d2.config(foreground = bl, bg = bb)
    drop_d2.config(bg = bb, fg = ww, highlightbackground = rr, activebackground = rr)
    drop_d2["menu"].config(bg = bb, fg = ww)

    frame_d3.config(foreground = bl, bg = bb)
    drop_d3.config(bg = bb, fg = ww, highlightbackground = rr, activebackground = rr)
    drop_d3["menu"].config(bg = bb, fg = ww)

    frame_d4.config(foreground = bl, bg = bb)
    drop_d4.config(bg = bb, fg = ww, highlightbackground = rr, activebackground = rr)
    drop_d4["menu"].config(bg=bb, fg = ww)


    frame_r1.config(foreground = bl, bg = bb)
    for widget in frame_r1.winfo_children():
        widget.destroy()
    Radiobutton(frame_r1, text = "Gas    ", variable = fuel_type_r, value = "gas", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()
    Radiobutton(frame_r1, text = "Diesel", variable = fuel_type_r, value = "diesel", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()


    frame_r2.config(foreground = bl, bg = bb)
    for widget in frame_r2.winfo_children():
        widget.destroy()
    Radiobutton(frame_r2, text = "Standard     ", variable = aspiration_r, value = "std", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()
    Radiobutton(frame_r2, text = "Turbo          ", variable = aspiration_r, value = "turbo", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()


    frame_r3.config(foreground = bl, bg = bb)
    for widget in frame_r3.winfo_children():
        widget.destroy()
    Radiobutton(frame_r3, text = "Four     ", variable = door_number_r, value = "four", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()
    Radiobutton(frame_r3, text = "Two      ", variable = door_number_r, value = "two", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()


    frame_r4.config(foreground = bl, bg = bb)
    for widget in frame_r4.winfo_children():
        widget.destroy()
    Radiobutton(frame_r4, text = "FWD", variable = drive_wheel_r, value = "fwd", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()
    Radiobutton(frame_r4, text = "RWD", variable = drive_wheel_r, value = "rwd", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()
    Radiobutton(frame_r4, text = "4WD", variable = drive_wheel_r, value = "4wd", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()


    frame_r5.config(foreground = bl, bg = bb)
    for widget in frame_r5.winfo_children():
        widget.destroy()
    Radiobutton(frame_r5, text = "Budget      ", variable = price_range_r, value = "Budget", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()
    Radiobutton(frame_r5, text = "Medium    ", variable = price_range_r, value = "Medium", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()
    Radiobutton(frame_r5, text = "Highend    ", variable = price_range_r, value = "Highend", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()

    price_display.config(foreground = ww, bg = bb, activebackground = gg)
    output_display.config(foreground = bl, bg = bb, activebackground = gg)

    mysubmit.config(foreground = bl, bg = bb, activebackground = gg)
    exit.config(foreground = bl, bg = bb, activebackground = gg)

    myhelp.config(foreground = rr, bg = bb, activebackground = gg)
    image1.config(foreground = rr, bg = bb, activebackground = rr)
    image2.config(foreground = rr, bg = bb, activebackground = rr)


root.configure(background = bb)
root.iconbitmap("C:\\Users\\B. Roshan Kumar\\Desktop\\Roshan\\My projects\\car-tkinter\\10868872.png")

global df

df = pd.read_csv("C:\\Users\\B. Roshan Kumar\\Desktop\\Roshan\\My projects\\car price detection\\Car_desc_dataset.csv")

Company_Name = df["CarName"].apply(lambda x: x.split(" ")[0])
df.insert(2,"CompanyName",Company_Name)

df.drop(columns=["CarName"],inplace=True)


def replace(a,b):
    df["CompanyName"].replace(a,b,inplace=True)

replace('maxda','mazda')
replace('porcshce','porsche')
replace('toyouta','toyota')
replace('vokswagen','volkswagen')
replace('vw','volkswagen')

z = round(df.groupby(["CompanyName"])["price"].agg(["mean"]),2).T

df = df.merge(z.T,how="left",on="CompanyName")

bins = [0,10000,20000,40000]
cars_bin=['Budget','Medium','Highend']
df['CarsRange'] = pd.cut(df['mean'],bins,right=False,labels=cars_bin)

def submit():
    
    col = ['fueltype','aspiration','doornumber','carbody','drivewheel','enginetype','cylindernumber','fuelsystem',
        'wheelbase','carlength','carwidth','curbweight','enginesize','boreratio','horsepower','citympg','highwaympg',
        'price','CarsRange']

    new_df = df[col]

    dictionary = {'fueltype' : fuel_type_r.get(),
            'aspiration' : aspiration_r.get(),
            'doornumber' : door_number_r.get(),
            'carbody' : car_body_clicked.get().strip(),
            'drivewheel' : drive_wheel_r.get(),
            'enginetype' : engine_type_clicked.get().strip(),
            'cylindernumber' : cylinder_clicked.get().strip(),
            'fuelsystem' : fuel_system_clicked.get().strip(),
            'wheelbase' : wheel_base_s.get(),
            'carlength' : car_length_s.get(),
            'carwidth' : car_width_s.get(),
            'curbweight' : curb_weight_s.get(),
            'enginesize': engine_size_s.get(),
            'boreratio' : bore_ratio_s.get()/100,
            'horsepower' : horse_power_s.get(),
            'citympg' : mileage_s.get(),
            'highwaympg' : mileage_s.get() + 4,
            'price' : 0,
            'CarsRange' : price_range_r.get()}

    ssd = pd.DataFrame(dictionary, index = [999])

    new_df = new_df.append(ssd)

    new_df = pd.get_dummies(columns=["fueltype","aspiration","doornumber","carbody","drivewheel","enginetype",
                                    "cylindernumber","fuelsystem","CarsRange"],data=new_df)

    scaler = StandardScaler()

    num_cols = ['wheelbase','carlength','carwidth','curbweight','enginesize','boreratio','horsepower',
                'citympg','highwaympg']

    new_df[num_cols] = scaler.fit_transform(new_df[num_cols])

    x = new_df.drop(columns=["price"])
    y = new_df["price"]

    select_prod = x.loc[[999]]
    x = x.drop([999])
    y = y.drop([999])

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)



    #  LinearRegression

    model1 = LinearRegression()
    model1.fit(x_train,y_train)


    #  DecisionTreeRegressor

    model2 = DecisionTreeRegressor()
    model2.fit(x_train,y_train)


    #  RandomForestRegressor

    model3 = RandomForestRegressor()
    model3.fit(x_train,y_train)


    #  AdaBoostRegressor

    model4 = AdaBoostRegressor()
    model4.fit(x_train,y_train)

    #  GradientBoostingRegressor

    model5 = GradientBoostingRegressor()
    model5.fit(x_train,y_train)


    #  XGBRegressor

    model6 = XGBRegressor()
    model6.fit(x_train,y_train)
    


    s = 0
    for i in [model1,model2,model3,model4,model5,model6]:
        temp = i.predict(select_prod)
        print(temp)
        s += temp
    s = s[0]
    s = s/6
    s = round(s,2)
    print('--->',s)
    print(type(s))
    
    
    output_display.config(text = '$ '+str(s))


status_down = Label(root, height = 1, width = 40, background = bb)
status_left = Label(root, height = 30, width = 1, background = bb)
status_middle = Label(root, height = 30, width = 1, background = bb)
status_right = Label(root, height = 30, width = 1, background = bb)


frame_s1 = LabelFrame(root, text = "Wheel Base", foreground = bl, bg = bb)
wheel_base_s = Scale(frame_s1, from_ = 86, to = 120, bg = bb, fg = ww, troughcolor = bl, activebackground = rr, highlightthickness = 0)
wheel_base_s.pack()
wheel_base_s.set(104)

frame_s2 = LabelFrame(root, text = "Car length", padx = 6, pady = 20, foreground = bl, bg = bb)
car_length_s = Scale(frame_s2, from_ =  140, to = 210, bg = bb, fg = ww, troughcolor = bl, activebackground = rr, highlightthickness = 0)
car_length_s.pack()
car_length_s.set(174.6)

frame_s3 = LabelFrame(root, text = "Car Width", padx = 13, pady = 10, foreground = bl, bg = bb)
car_width_s = Scale(frame_s3, from_ = 60, to = 73, bg = bb, fg = ww, troughcolor = bl, activebackground = rr, highlightthickness = 0)
car_width_s.pack()
car_width_s.set(66.3)

frame_s4 = LabelFrame(root, text = "Curb Weight", padx = 38, pady = 0, foreground = bl, bg = bb)
curb_weight_s = Scale(frame_s4, from_ = 1488, to = 4066, orient = HORIZONTAL, bg = bb, fg = ww, troughcolor = bl, activebackground = rr, highlightthickness = 0)
curb_weight_s.pack()
curb_weight_s.set(2777.0)

frame_s5 = LabelFrame(root, text = "Engine Size", padx = 38, pady = 0, foreground = bl, bg = bb)
engine_size_s = Scale(frame_s5, from_ = 61, to = 326 , orient = HORIZONTAL, bg = bb, fg = ww, troughcolor = bl, activebackground = rr, highlightthickness = 0)
engine_size_s.pack()
engine_size_s.set(193.5)

frame_s6 = LabelFrame(root, text = "Bore Ratio(/100)", padx = 38, pady = 0, foreground = bl, bg = bb)
bore_ratio_s = Scale(frame_s6, from_ = 254, to = 394, orient = HORIZONTAL, bg = bb, fg = ww, troughcolor = bl, activebackground = rr, highlightthickness = 0)
bore_ratio_s.pack()
bore_ratio_s.set(324)

frame_s7 = LabelFrame(root, text = "Horse Power", padx = 38, pady = 0, foreground = bl, bg = bb)
horse_power_s = Scale(frame_s7, from_ = 48, to = 288, orient = HORIZONTAL, bg = bb, fg = ww, troughcolor = bl, activebackground = rr, highlightthickness = 0)
horse_power_s.pack()
horse_power_s.set(168.0)

frame_s8 = LabelFrame(root, text = "Mileage", padx = 13, pady = 10, foreground = bl, bg = bb)
mileage_s = Scale(frame_s8, from_ = 13, to = 49, bg = bb, fg = ww, troughcolor = bl, activebackground = rr, highlightthickness = 0)
mileage_s.pack()
mileage_s.set(31.0)


frame_d1 = LabelFrame(root, text = "Car Body", padx = 20, pady = 3, foreground = bl, bg = bb)

car_body_options = [ 'Convertible             ',
                    'Hardtop                  ',
                    'Hatchback              ',
                    'Sedan                      ',
                    'Wagon                    ']

car_body_clicked = StringVar()
car_body_clicked.set("Hardtop                  ")

ac = "#"

drop_d1 = OptionMenu(frame_d1, car_body_clicked, *car_body_options)
drop_d1.config(bg = bb, fg = ww, highlightthickness = 1, highlightbackground = rr, activebackground = rr)
drop_d1["menu"].config(bg=bb, fg = ww)


frame_d2 = LabelFrame(root, text = "Engine Type", padx = 20, pady = 3, foreground = bl, bg = bb)

engine_type_options = [ 'dohc                        ',
                        'dohcv                      ',
                        'l                                ',
                        'ohc                          ',
                        'ohcf                         ',
                        'ohcv                        ',
                        'rotor                        ']


engine_type_clicked = StringVar()
engine_type_clicked.set("dohc                        ")

drop_d2 = OptionMenu(frame_d2, engine_type_clicked, *engine_type_options)
drop_d2.config(bg = bb, fg = ww, highlightthickness = 1, highlightbackground = rr, activebackground = rr)
drop_d2["menu"].config(bg=bb, fg = ww)


frame_d3 = LabelFrame(root, text = "No.of Cylinders", padx = 20, pady = 3, foreground = bl, bg = bb)

cylinder_options = ['Eight                        ',
                    'Twelve                     ',
                    'Four                         ',
                    'Five                          ',
                    'Six                            ',
                    'Three                       ',
                    'Two                          ']

cylinder_clicked = StringVar()
cylinder_clicked.set("Eight                        ")

drop_d3 = OptionMenu(frame_d3, cylinder_clicked, *cylinder_options)
drop_d3.config(bg = bb, fg = ww, highlightthickness = 1, highlightbackground = rr, activebackground = rr)
drop_d3["menu"].config(bg=bb, fg = ww)


frame_d4 = LabelFrame(root, text = "Fuel System", padx = 20, pady = 3, foreground = bl, bg = bb)

fuel_system_options = ['1bbl                         ',
                    '2bbl                         ',
                    '4bbl                         ',
                    'idi                             ',
                    'mfi                           ',
                    'mpfi                         ',
                    'spdi                          ',
                    'spfi                           ']

fuel_system_clicked = StringVar()
fuel_system_clicked.set("1bbl                         ")

drop_d4 = OptionMenu(frame_d4, fuel_system_clicked, *fuel_system_options)
drop_d4.config(bg = bb, fg = ww, highlightthickness = 1, highlightbackground = rr, activebackground = rr)
drop_d4["menu"].config(bg=bb, fg = ww)


frame_r1 = LabelFrame(root, text = "Fuel Type", padx = 25, pady = 0, foreground = bl, bg = bb)
fuel_type_r = StringVar()
fuel_type_r.set("gas")
Radiobutton(frame_r1, text = "Gas    ", variable = fuel_type_r, value = "gas", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()
Radiobutton(frame_r1, text = "Diesel", variable = fuel_type_r, value = "diesel", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()


frame_r2 = LabelFrame(root, text = "Aspiration", padx = 10, pady = 0, foreground = bl, bg = bb)
aspiration_r = StringVar()
aspiration_r.set("std")
Radiobutton(frame_r2, text = "Standard     ", variable = aspiration_r, value = "std", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()
Radiobutton(frame_r2, text = "Turbo          ", variable = aspiration_r, value = "turbo", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()


frame_r3 = LabelFrame(root, text = "Door Number", padx = 20, pady = 30, foreground = bl, bg = bb)
door_number_r = StringVar()
door_number_r.set("four")
Radiobutton(frame_r3, text = "Four     ", variable = door_number_r, value = "four", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()
Radiobutton(frame_r3, text = "Two      ", variable = door_number_r, value = "two", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()


frame_r4 = LabelFrame(root, text = "Drive Wheel", padx = 27, pady = 22, foreground = bl, bg = bb)
drive_wheel_r = StringVar()
drive_wheel_r.set("fwd")
Radiobutton(frame_r4, text = "FWD", variable = drive_wheel_r, value = "fwd", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()
Radiobutton(frame_r4, text = "RWD", variable = drive_wheel_r, value = "rwd", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()
Radiobutton(frame_r4, text = "4WD", variable = drive_wheel_r, value = "4wd", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()


frame_r5 = LabelFrame(root, text = "Price Range", padx = 10, pady = 22, foreground = bl, bg = bb)
price_range_r = StringVar()
price_range_r.set("Budget")
Radiobutton(frame_r5, text = "Budget      ", variable = price_range_r, value = "Budget", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()
Radiobutton(frame_r5, text = "Medium    ", variable = price_range_r, value = "Medium", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()
Radiobutton(frame_r5, text = "Highend    ", variable = price_range_r, value = "Highend", foreground = ww, bg = bb, activebackground = gg, selectcolor = bb).pack()


price_display = Label(root, text = "Price:", height = 2, width = 15 )
price_display.config(font=("Lato", "24"), foreground = ww, bg = bb, activebackground = gg)


output_display = Label(root, height = 2, width = 15 )
output_display.config(font=("Lato", "24",'bold'), foreground = bl, bg = bb, activebackground = gg)


def help():
    help_tab = Toplevel()
    help_tab.title("Image 1")
    btn_h = Button( help_tab, text = "Close Window", foreground = ww, bg = bb, activebackground = gg, command = help_tab.destroy).pack()


def img1():
    global imgwin_1, h_img
    imgwin_1 = Toplevel()
    imgwin_1.title("Image 1")
    temp_img = Image.open("C:\\Users\\B. Roshan Kumar\\Desktop\\Roshan\\My projects\\car-tkinter\\try\\h_img.png")
    resize_image = temp_img.resize((750,750))
    imgwin_1.config(bg = bb)

    h_img = ImageTk.PhotoImage(resize_image)
    img_label_1 = Label(imgwin_1, image = h_img).pack()
    btn1 = Button( imgwin_1, text = "Close Window", foreground = ww, bg = bb, activebackground = gg, command = imgwin_1.destroy)
    btn1.pack()

def img2():
    global imgwin_2, c_img
    imgwin_2 = Toplevel()
    imgwin_2.title("Image 1")
    temp_img = Image.open("C:\\Users\\B. Roshan Kumar\\Desktop\\Roshan\\My projects\\car-tkinter\\try\\compare.png")
    resize_image = temp_img.resize((1250,750))
    imgwin_2.config(bg = bb)

    c_img = ImageTk.PhotoImage(resize_image)
    img_label_1 = Label(imgwin_2, image = c_img).pack()
    btn1 = Button( imgwin_2, text = "Close Window", foreground = ww, bg = bb, activebackground = gg, command = imgwin_2.destroy)
    btn1.pack()
    
    

mysubmit = Button(root, text = "Submit", foreground = bl, bg = bb, activebackground = gg, command = lambda: submit())
exit = Button(root, text = "   Exit   ", foreground = bl, bg = bb, activebackground = gg, command = root.quit)
mode = Button(root, text = "☀️Light Mode", foreground = bl, bg = bb, activebackground = gg, command = lambda: mode_change(0))

myhelp = Button(root, text = "Help", foreground = bl, bg = bb, activebackground = gg, command = lambda: help())
image1 = Button(root, text = "C-Map", foreground = rr, bg = bb, activebackground = rr, command = lambda: img1())
image2 = Button(root, text = "Models", foreground = rr, bg = bb, activebackground = rr, command = lambda: img2())


frame_s1.grid(row = 1, column = 1, rowspan = 2)  #Wheel Base
frame_s2.grid(row = 3, column = 1, rowspan = 2)  #Car length
frame_s3.grid(row = 5, column = 1, rowspan = 2)  #Car Width
frame_s4.grid(row = 6, column = 2)  #Curb Weight

frame_s5.grid(row = 8, column = 2)  #Engine Size
frame_s6.grid(row = 5, column = 2)  #Bore Ratio
frame_s7.grid(row = 7, column = 2)  #Horse Power
frame_s8.grid(row = 7, column = 1, rowspan = 2)  #Mileage



frame_d1.grid(row = 1, column = 2)  #Car Body
frame_d2.grid(row = 2, column = 2)  #Engine Type
frame_d3.grid(row = 3, column = 2)  #No.of Cylinders
frame_d4.grid(row = 4, column = 2)  #Fuel System

drop_d1.grid(row = 1, column = 1)  #Car Body
drop_d2.grid(row = 1, column = 1)  #Engine Type
drop_d3.grid(row = 1, column = 1)  #No.of cylinders
drop_d4.grid(row = 1, column = 1)  #Fuel System

frame_r1.grid(row = 1, column = 4)  #Fuel Type
frame_r2.grid(row = 2, column = 4)  #Aspiration
frame_r3.grid(row = 3, column = 4, rowspan = 2)  #Door Number
frame_r4.grid(row = 5, column = 4, rowspan = 2)  #Drive Wheel
frame_r5.grid(row = 7, column = 4, rowspan = 2)  #Price Range



status_down.grid(row = 10, column = 0, columnspan = 3)
status_left.grid(row = 0, column = 0, rowspan = 7)
status_middle.grid(row = 0, column = 5, rowspan = 7)
status_right.grid(row = 0, column = 26, rowspan = 7)


price_display.grid(row = 2, column = 6, rowspan = 3, columnspan = 20)
output_display.grid(row = 3, column = 6, rowspan = 3, columnspan = 20)

mysubmit.grid(row = 5, column =6)
myhelp.grid(row = 5, column =13)
image1.grid(row = 5, column = 24)
image2.grid(row = 5, column = 25)
exit.grid( row = 8, column = 18)
mode.grid(row = 1, column = 25)


# call the main function
root.mainloop()