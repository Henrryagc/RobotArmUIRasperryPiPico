import flet
from flet import Page, Slider, Text, Row, Container, colors, Card, Column, alignment, padding, FilledButton, theme, Image
import numpy as np
from time import sleep
import cv2
from PIL import Image as pilImage, ImageTk
import os
import csv
from robot_arm.ui import ui_comands as uic


def main(page: Page):
    page.title = "ROBOARM"
    page.padding = 50    
    page.theme = theme.Theme(color_scheme_seed="red")    
    data_csv = []
    data = []

    def slider_changed_gripper(e):        
        text_1.value = f"Brazo Pinzas {int(e.control.value)}"
        print(f"Brazo Pinzas {text_1.value}")
        global gripper
        gripper = int(e.control.value)       
        uic.gripper(int(e.control.value))
        page.update()

    def slider_changed_wrist(e):        
        text_2.value = f"Brazo Muñeca {int(e.control.value)}"
        global wrist
        wrist = int(e.control.value)  
        uic.wrist(int(e.control.value))
        page.update()
        print(f"Brazo Muñeca {text_2.value}")

    def slider_changed_arm_top(e):       
        text_3.value = f"Brazo Arriba {int(e.control.value)}"
        global arm_top
        arm_top = int(e.control.value)
        uic.arm_top(int(e.control.value))
        page.update()
        print(f"Brazo Arriba {text_3.value}")

    def slider_changed_arm_bottom(e):        
        text_4.value = f"Brazo Abajo {int(e.control.value)}"
        global arm_bottom
        arm_bottom = int(e.control.value)
        uic.arm_bottom(int(e.control.value))
        page.update()
        print(f"Brazo Abajo {text_4.value}")
    
    def slider_changed_shoulders(e):        
        text_5.value = f"Brazo Hombros {int(e.control.value)}"
        global shoulders
        shoulders = int(e.control.value)
        uic.shoulders(int(e.control.value))
        page.update()
        print(f"Brazo Hombros {text_5.value}")

    def slider_changed_base(e):        
        text_6.value = f"Brazo Base {int(e.control.value)}"
        global base
        base = int(e.control.value)
        uic.base(int(e.control.value))
        page.update()
        print(f"Brazo Base {text_6.value}")



    text_1 = Text("Brazo Pinzas 0", size=18)
    container_1 = Container(
        content = Row(
            controls = [                
                Container( expand = 1,
                    content=Slider(min=180, max=280, divisions=20, label="{value}", on_change=slider_changed_gripper)),
                Container(content=text_1, padding=padding.only(right=25))
            ],
            spacing = 10,            
        ),
        # bgcolor = colors.DEEP_PURPLE_ACCENT_100
    )    


    text_2 = Text("Brazo Muñeca 0", size=18)
    container_2 = Container(
        content = Row(
            controls = [
                Container( expand=1, 
                    content=Slider(min=180, max=600, divisions=40, label="{value}", on_change=slider_changed_wrist)
                ),
                Container(content=text_2, padding=padding.only(right=25))
            ],
            spacing = 10,            
        ),
        # bgcolor = colors.DEEP_PURPLE_ACCENT_100
    )


    text_3 = Text("Brazo Arriba 0", size=18)
    container_3 = Container(
        content = Row(
            controls = [ 
                Container( expand=1,
                    content=Slider(min=180, max=600, divisions=40, label="{value}", on_change=slider_changed_arm_top)),
                Container(content=text_3, padding=padding.only(right=25))
            ],
            spacing = 10,            
        ),
        # bgcolor = colors.DEEP_PURPLE_ACCENT_100
    )


    text_4 = Text("Brazo Abajo 0", size=18)
    container_4 = Container(
        content = Row(
            controls = [
                Container( expand=1,
                    content=Slider(min=180, max=600, divisions=40, label="{value}", on_change=slider_changed_arm_bottom)),                
                Container(content=text_4, padding=padding.only(right=25))
            ],
            spacing = 10,            
        ),
        # bgcolor = colors.DEEP_PURPLE_ACCENT_100
    )


    text_5 = Text("Brazo Hombros 0", size=18)
    container_5 = Container(
        content = Row(
            controls = [
                Container( expand=1,
                    content=Slider(min=180, max=600, divisions=40, label="{value}", on_change=slider_changed_shoulders)),
                Container(content=text_5, padding=padding.only(right=25))
            ],
            spacing = 10,            
        ),
        # bgcolor = colors.DEEP_PURPLE_ACCENT_100
    )


    text_6 = Text("Brazo Base 0", size=18)
    container_6 = Container(
        content = Row(
            controls = [
                Container( expand = 1,
                    content= Slider(min=180, max=600, divisions=40, label="{value}", on_change=slider_changed_base)),
                Container(content=text_6, padding=padding.only(right=25))
            ],
            spacing = 10,           
        ),
        # bgcolor = colors.DEEP_PURPLE_ACCENT_100        
    )

    container_sliders = Card(
        content = Container(
            content = Column(
                [   
                    container_1,                    
                    container_2,
                    container_3,
                    container_4,
                    container_5,
                    container_6
                ]
            )
        ),
        width = 600,
        elevation = 16,
        margin = 10               
    )    


    def find_object(img, mask, color, num_mask):
        cnts, hireachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(cnts) != 0:
            c = max(cnts, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
            text = masks_names[num_mask]
            text_position = (round(x+w/2), round(y+h/2))
            cv2.putText(img, text, text_position, cv2.FONT_ITALIC, 0.6, (255, 255, 255), 1)
            if num_mask == 2:
                global x_position_object
                x_position_object = round(x+w/2)
                global y_position_object
                y_position_object = round(y+h/2)

            return (round(x+w/2), round(y+h/2))
        return


    def open_camera(e):
        paths = [f"2-6.jpg", f"circuit-1.jpg", f"servoCodes.jpg"]
        counter = 0
        vid = cv2.VideoCapture(0)
        while vid.isOpened():
            ret, img = vid.read()

            if ret == False:
                break
            
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            
            if len(hsv) > 0:        
                mask_blue = cv2.inRange(hsv, hsv_blue_min, hsv_blue_max)
                mask_green = cv2.inRange(hsv, hsv_green_min, hsv_green_max)
                mask_red = cv2.inRange(hsv, hsv_red_min, hsv_red_max)

                #pblue = find_object(img, mask_blue, (255, 0, 0), 0)
                #pgreen = find_object(img, mask_green, (255, 0, 0), 1)
                pred = find_object(img, mask_red, (255, 0, 0), 2)
                #if pred:
                    #print(f"{pred}")
                cv2.imshow('Image', img)        
            cv2.imshow('Image', img)

            if cv2.waitKey(1) & 0xFF == 27:
                break

        vid.release()
        cv2.destroyAllWindows()


    def save_object_position(e):        
        data.append(x_position_object)    
        data.append(y_position_object)
        print(data)

    def save_first_movement(e):        
        data.append(gripper)
        data.append(wrist)
        data.append(arm_top)
        data.append(arm_bottom)
        data.append(shoulders)
        data.append(base)
        print(data)
        

    def save_second_movement(e):        
        data.append(gripper)
        data.append(wrist)
        data.append(arm_top)
        data.append(arm_bottom)
        data.append(shoulders)
        data.append(base)        
        print(data)

    
    def save_data_array(e):                
        #data_csv.append(data)
        
        #np.savetxt("data.csv", data_csv, fmt='%10.5f', delimiter=',')
        with open('data.csv', 'a', newline='') as csvfile:   
            #writer = csv.writer(csvfile)
            fieldnames = ['x', 'y', 'gripper1', 'wrist1', 'arm_top1', 'arm_bottom1', 'shoulders1', 'base1', 'gripper2', 'wrist2', 'arm_top2', 'arm_bottom2', 'shoulders2', 'base2', 'x2','y2']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            #writer.writeheader()        
            writer.writerow({
                'x': data[0], 
                'y': data[1], 
                'gripper1': data[2],
                'wrist1': data[3],
                'arm_top1': data[4],
                'arm_bottom1': data[5], 
                'shoulders1': data[6], 
                'base1': data[7],                
                'gripper2': data[8], 
                'wrist2': data[9], 
                'arm_top2': data[10], 
                'arm_bottom2': data[11],
                'shoulders2': data[12],
                'base2': data[13],
                'x2':data[14],
                'y2':data[15]
                })
            print(data)
            data.clear()
        
        

 #numpy.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None) : This method is used to save an array to a text file. #
    imageTest = Image(src=f"circuit-1.jpg", fit="contain")    
    container_rigth = Column(    
            controls=[
                Card(
                    content=Container( 
                            content=Row(
                                controls=[
                                    FilledButton("Activar Camara", on_click=open_camera),
                                    FilledButton("Guardar (x,y)", on_click=save_object_position),
                                    FilledButton("Guardar Movimiento 1", on_click=save_first_movement),
                                    FilledButton("Guardar Movimiento 2", on_click=save_second_movement),
                                    FilledButton("Guardar Lista de movimientos", on_click=save_data_array),
                                    #FilledButton("Crear csv", on_click=save_csv),
                                ], 
                                alignment="center",
                                wrap=True,                        
                            ),
                            padding=10,
                        ),
                    width = 600,
                    elevation = 16,
                    #margin = 10,
                ),
                Card(
                    content= Container(content=imageTest, padding=10),
                    height = 400,
                    width = 600,
                    elevation = 16,
                    margin = 10,
                )            
            ],            
        )

    container_left = Container(     
        content = Column( 
            alignment = "center",
            controls = [                              
                Card(
                    content=Container(
                        content = Text("CONTROLES DEL BRAZO ROBÓTICO", size=22),
                        margin = 10,
                        alignment = alignment.center                        
                    ),                    
                    width = 600,
                    elevation = 16,
                    margin = 10 
                   ),
                container_sliders
            ]
        ),
        alignment = alignment.center
    )
    
    main_frame = Row(
        controls= [container_left, container_rigth],
        spacing=10        
    )

    page.add(main_frame)
        


global masks_names
masks_names = ['azul', 'verde', 'rojo']

    
# MASCARA PARA DETECTAR LOS OBJETOS POR COLORES
# Azul
hsv_blue_min = (100, 150, 0)
hsv_blue_max = (140, 255, 255)

# Verde
hsv_green_min = (36, 25, 25)
hsv_green_max = (70, 255, 255)

# Rojo
hsv_red_min = (0, 50, 50)
hsv_red_max = (10, 255, 255)

flet.app(target=main,assets_dir="img")
