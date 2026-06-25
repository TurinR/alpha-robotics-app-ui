import customtkinter as ctk
#from CONS1 import *

app = ctk.CTk()

app.geometry("1920x1080")

class NavMenu:
    
    def __init__(self, width, height, corner_rad, text: str | None = None):
        self.width = width
        self.height = height
        self.corner_rad = corner_rad
        self.text = text

    def nav_highlight(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

        nav_main_h = ctk.CTkFrame(master=app, width=self.width, height=self.height, corner_radius=self.corner_rad, fg_color="white")
        nav_main_h.pack(pady=20)
        nav_main_h.place(relx=self.pos_x-0.0005, rely=self.pos_y-0.0005, anchor='center')   
    
    def nav_shadow(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

        nav_main_s = ctk.CTkFrame(master=app, width=self.width, height=self.height, corner_radius=self.corner_rad, fg_color="black")
        nav_main_s.pack(pady=20)
        nav_main_s.place(relx=self.pos_x+0.0005, rely=self.pos_y+0.0005, anchor='center')   
    
    def nav_frame(self, posx, posy):
        self.posx = posx
        self.posy = posy

        self.nav_main_frame = ctk.CTkFrame(master=app, width=self.width, height=self.height, corner_radius=self.corner_rad)
        self.nav_main_frame.pack(pady=20)
        self.nav_main_frame.place(relx=self.posx, rely=self.posy, anchor='center')

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def nav_sec(self, posx, posy, sec_width, sec_height, sec_corner_rad: int | None = 20):
        self.posx = posx
        self.posy = posy
        self.sec_width = sec_width
        self.sec_height = sec_height
        self.sec_corner_rad = sec_corner_rad

        self.nav_main = ctk.CTkFrame(master=app, width=self.sec_width, height=self.sec_height, corner_radius=self.sec_corner_rad, fg_color="transparent", bg_color='transparent')
        self.nav_main.pack(pady=20)
        self.nav_main.place(relx=self.posx, rely=self.posy, anchor='center')

    def nav_sec_text(self, text_posx: float | None = None, text_posy: float | None = None, sec_text_width: int | None = None, sec_text_height: int | None = None, sec_corner_rad: int | None = 20):
        if text_posx is None:
            text_posx = self.posx
        if text_posy is None:
            text_posy = self.posy
        if sec_text_width is None:
            sec_text_width = self.sec_width
        if sec_text_height is None:
            sec_text_height = self.sec_height

        self.text_posx = text_posx
        self.text_posy = text_posy
        self.sec_width = sec_text_width
        self.sec_height = sec_text_height
        self.sec_corner_rad = sec_corner_rad

        nav_label = ctk.CTkLabel(master=self.nav_main, width=self.sec_width, height=self.sec_height * 0.9, corner_radius=self.sec_corner_rad, fg_color="transparent", bg_color='transparent', text=self.text, text_color="black")
        nav_label.pack(pady=2)
        nav_label.place(relx=self.text_posx, rely=self.text_posy, anchor='center')


    def nav_button(self, command: callable):
        button = ctk.CTkButton(master=app, width=50, height= 25, corner_radius = self.corner_rad - 5, command=command, text=self.text)
        button.pack(pady = 20)
        button.place(relx= self.posx, rely = self.posy + 0.1, anchor='center')


class FieldFrame:
    """
    This class instantiates the Frame around which the iamges are centered. It acts as the container object to them.
    It is the parent class to FieldImage and serves to drastically simplify the process of adding and editing new fields inot the application. 

    It takes the following arguemnts:

    ### ARGUMENTS:
    - master: 
    - width: float
    - height: float
    - corner_rad: float

    These controls are very self explanatory
    """
    def __init__(self, master, width: float, height: float, corner_rad: float | None = 20):
        self.master = master
        self.width = width
        self.height = height
        self.corner_rad = corner_rad

        self.frame = ctk.CTkFrame(
            master=self.master, 
            width=self.width, 
            height=self.height, 
            corner_radius=self.corner_rad)

    def move_to(self, pos_x: float | None = 0.65, pos_y: float | None = 0.4):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.frame.pack(pady=20)
        self.frame.place(relx=self.pos_x, rely=pos_y, anchor='center')

    def hide(self):
        self.frame.pack_forget()
        self.frame.place_forget()

class FieldImage(FieldFrame):
    """
    
    """
    fields_list: list = []
    field_index: int = 0

    def __init__(self, master, width: float, height: float, corner_rad: float, field_image_path: str, field_id):
        
        super().__init__(master, width, height, corner_rad)

        self.field_image_path = field_image_path
        self.field_id = field_id

        FieldImage.fields_list.append(self)

    def field_image(self):

        self.vex_field = ctk.CTkImage(light_image=self.field_image_path, size=(self.width-10, self.height-10))
        self.vex_label = ctk.CTkLabel(master=self.frame, text="", image=self.vex_field)

    def nav_highlight(self):

        nav_high = ctk.CTkFrame(master=app, width=self.width, height=self.height, corner_radius=self.corner_rad, fg_color="white")
        nav_high.pack(pady=20)
        nav_high.place(relx=self.posx-0.001, rely=self.posy+0.001, anchor='center')   

    def nav_shadow(self):

        nav_shad = ctk.CTkFrame(master=app, width=self.width, height=self.height, corner_radius=self.corner_rad, fg_color="black")
        nav_shad.pack(pady=20)
        nav_shad.place(relx=0.65-0.001, rely=0.4+0.001, anchor='center')   

    @staticmethod
    def change_right(event=None):
        FieldImage.field_index += 1
        print("Image caorusel moved 1 to the right")

    @staticmethod
    def change_left(event=None):
        FieldImage.field_index -= 1
        print("Image caorusel moved 1 to the left")

    @staticmethod
    def field_button(command_right: change_right, command_left: change_left):
        field_right = ctk.CTkButton(master=app, width=50, height=50, corner_radius = 150, text=">", command=command_right)
        field_right.pack(pady = 20)
        field_right.place(relx= 0.825, rely = 0.8)

        field_left = ctk.CTkButton(master=app, width=40, height=50, corner_radius = 150, text="<", command=command_left)
        field_left.pack(pady = 20)
        field_left.place(relx= 0.45, rely = 0.8)

def game_fields(app):
    
    # Have a gatter function for the fields list index that dchnages the field iamge based on how many times the right or left buttons have been pressed
    override = FieldImage(app, 750, 600, 20, "images/VEX_fields/OVERRIDE.png", 0)
    pushback = FieldImage(app, 750, 600, 20, "images/VEX_fields/PUSHBACK.png", 1)
    highstakes = FieldImage(app, 750, 600, 20, "images/VEX_fields/HIGHSTAKES.png", 2)
    overunder = FieldImage(app, 750, 600, 20, "images/VEX_fields/OVERUNDER.png", 3)

def show_current_field():

    game_fields(app)
    # This function will be used to display the current field based on the index of the fields list that is being tracked by the left and right buttons
    for field in FieldImage.fields_list:
        field.hide()

    FieldImage.fields_list[FieldImage.field_index].move_to(0.65, 0.4)

def main_menu():
    nav_bar_inp = NavMenu(350, 400, 20, text="Input")
    nav_bar_inp.nav_frame(0.15, 0.32)
    nav_bar_inp.nav_sec(0.15, 0.32, 300, 350)

    # Nav bar menu for the constants and settings; uses Hassaan AI or manually calculates the PID constants or other such constants for other control systems
    nav_bar_con = NavMenu(350, 250, 20, text="PID Constants")
    nav_bar_con.nav_frame(0.15, 0.8)
    nav_bar_con.nav_sec(0.15, 0.7, 320, 50, 15)
    nav_bar_con.nav_sec_text()
    nav_bar_con.text = "Calculate"
    nav_bar_con.nav_sec(0.08, 0.775, 100, 30, 15)
    nav_bar_con.text = "Hassaan AI"
    nav_bar_con.nav_sec(0.23, 0.775, 75, 30, 15)
    nav_bar_con.text = "kP: 0.71"
    nav_bar_con.nav_sec(0.08, 0.875, 100, 100, 15)
    nav_bar_con.text = "kI: 0.71"
    nav_bar_con.nav_sec(0.15, 0.875, 100, 100, 15)
    nav_bar_con.text = "kD: 0.71"
    nav_bar_con.nav_sec(0.22, 0.875, 100, 100, 15)

main_menu()
show_current_field()

    # Have a getter function for the fields list index that dchnages the field iamge based on how many times the right or left buttons have been pressed
app.mainloop()
