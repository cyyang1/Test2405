import tkinter as tk
from tkinter import messagebox


# 創建主視窗
root = tk.Tk()
root.title("Tkinter 元件")

# 創建並排列標籤
label = tk.Label(root, text="標籤1")
label.grid(row=0, column=0)

# 創建並排列按鈕
button = tk.Button(root, text="按鈕1")
button.grid(row=1, column=0)

# 創建並排列輸入框
entry = tk.Entry(root)
entry.grid(row=2, column=0)

# 創建並排列文字區
text = tk.Text(root)
text.grid(row=3, column=0)
text.insert(tk.END, """時操在易州，按兵不動。夏侯惇、張遼入稟曰：「如不下遼東，可回許都；恐劉表生心。」
操曰：「待二袁首級至，即便回兵。」眾皆暗笑。
忽報遼東公孫康遣人送袁熙、袁尚首級至，眾皆大驚。
使者呈上書信。操大笑曰：「果不出奉孝之料！」重賞來使，封公孫康為襄平侯左將軍。
眾官問曰；「何為不出奉孝之所料？」操遂出郭嘉書以示之。
書略曰：今聞袁熙、袁尚往投遼東，明公切不可加兵。公孫康久畏袁氏吞併，二袁往投必疑。
若以兵擊之，必併力迎敵，急不可下；若緩之，公孫康、袁氏必自相圖，其勢然也。""")
text.mark_set("mark1","3.0")
text.mark_set("mark2","5.0")
text.tag_add("tag1","mark1","mark2")
text.tag_config("tag1",foreground="blue",background="lightyellow")


# 創建並排列框架
frame = tk.Frame(root, borderwidth=2, relief="groove" )
frame.grid(row=4, column=0)
label2 = tk.Label(frame,text="Account")   # account標籤
label2.grid(row=0,column=0)
label3 = tk.Label(frame,text="Password")      # pwd標籤
label3.grid(row=1,column=0)

entry2 = tk.Entry(frame)                  # 文字方塊account
entry2.grid(row=0,column=1)               # 定位文字方塊account
entry3 = tk.Entry(frame,show="*")             # 文字方塊pwd
entry3.grid(row=1,column=1,pady=10)           # 定位文字方塊pwd


# 創建並排列畫布
canvas = tk.Canvas(root, width=100, height=100, bg="white")
canvas.grid(row=5, column=0)
canvas.create_polygon(10,10, 100,10, 50,80, width=5,outline='blue',fill='yellow')

# 創建並排列核取方塊
checkbutton = tk.Checkbutton(root, text="核取方塊")
checkbutton.grid(row=0, column=1)

# 創建並排列單選按鈕
radiobutton = tk.Radiobutton(root, text="單選按鈕")
radiobutton.grid(row=1, column=1)

# 創建並排列滑桿
scale = tk.Scale(root, from_=0, to=10, orient="horizontal")
scale.grid(row=2, column=1)

# 創建並排列列表方塊
MonthList = ['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月']
listbox = tk.Listbox(root)
listbox.grid(row=3, column=1)
for item in MonthList:
    listbox.insert(tk.END, item)

# 創建並排列捲軸
scrollbar = tk.Scrollbar(root, orient="vertical")
scrollbar.grid(row=4, column=1, sticky="ns")
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

def new_file():
    messagebox.showinfo("Create a file","開新檔案")

def save_file():
    messagebox.showinfo("Save the file",'儲處檔案')

def aboutversion():
    messagebox.showinfo('版本', "Version 0.9987")

# 創建選單

menu = tk.Menu(root)
root.config(menu=menu)
filemenu=tk.Menu(menu)
aboutmenu=tk.Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
menu.add_cascade(label="About",menu=aboutmenu)
filemenu.add_command(label="New file", command=new_file)
filemenu.add_command(label="Save", command=save_file)
aboutmenu.add_command(label="Version",command=aboutversion)


# 創建並排列選單按鈕
menubutton = tk.Menubutton(root, text="選單按鈕",relief=tk.RAISED)
menubutton.grid(row=5,column=1)
menubutton.menu = tk.Menu(menubutton, tearoff=0)
menubutton["menu"] = menubutton.menu
menubutton.menu.add_command(label="選單項目 1")
menubutton.menu.add_command(label="選單項目 2")


# 創建並排列數值微調框
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.grid(row=0, column=2)

# 創建頂層視窗
toplevel = tk.Toplevel(root)
toplevel.title("頂層視窗")
toplevel.geometry("320x240")
button_tp = tk.Button(toplevel,text="確定")
button_tp.pack(side=tk.BOTTOM)

# 創建並排列訊息方塊
message = tk.Message(root, text="還記得紅遍網路的 ALOHA 家務機器人嗎？最近計畫導師史丹佛電腦科學與電機工程系教授 Chelsea Finn 在 X 宣布，與其他柏克萊大神學者、Google DeepMind 科學家共同創業，全力為機器人打造智慧大腦。",relief=tk.RAISED)
message.grid(row=1, column=2)

# 創建並排列分割視窗
panedwindow = tk.PanedWindow(root, orient="horizontal")  #ttk的PanedWindows才支援weight屬性
panedwindow.grid(row=2, column=2)
leftframe = tk.LabelFrame(panedwindow,text="Left Pane", width=70,height=80)
panedwindow.add(leftframe)
middleframe = tk.LabelFrame(panedwindow,text="Middle Pane", width=30,height=70)
panedwindow.add(middleframe)
rightframe = tk.LabelFrame(panedwindow,text="Right Pane", width=50,height=60)
panedwindow.add(rightframe)

# 創建並排列標籤框架
labelframe = tk.LabelFrame(root, text="標籤框架")
labelframe.grid(row=3, column=2)
accountL = tk.Label(labelframe,text="Account")
accountL.grid(row=0,column=0)
pwdL = tk.Label(labelframe,text="Password")
pwdL.grid(row=1,column=0)

accountE = tk.Entry(labelframe)
accountE.grid(row=0,column=1)
pwdE = tk.Entry(labelframe,show="*")
pwdE.grid(row=1,column=1,pady=10)


root.mainloop()