import flet
from flet import Page, Slider, Text, Row, Container, colors, Card, Column, alignment, padding

import src.ui.ui_comands as uic


def main(page: Page):
    page.title = "ROBOARM"
    page.padding = 50


    def slider_changed_gripper(e):        
        text_1.value = f"Brazo Pinzas {int(int(e.control.value))}"
        print(f"Brazo Pinzas {text_1.value}")
        uic.gripper(int(int(e.control.value)))
        page.update()

    def slider_changed_wrist(e):        
        text_2.value = f"Brazo Muñeca {int(e.control.value)}"
        uic.wrist(int(int(e.control.value)))
        page.update()
        print(f"Brazo Muñeca {text_2.value}")

    def slider_changed_arm_top(e):        
        text_3.value = f"Brazo Arriba {int(e.control.value)}"
        uic.arm_top(int(int(e.control.value)))
        page.update()
        print(f"Brazo Arriba {text_3.value}")

    def slider_changed_arm_bottom(e):        
        text_4.value = f"Brazo Abajo {int(e.control.value)}"
        uic.arm_bottom(int(int(e.control.value)))
        page.update()
        print(f"Brazo Abajo {text_4.value}")
    
    def slider_changed_shoulders(e):        
        text_5.value = f"Brazo Hombros {int(e.control.value)}"
        uic.shoulders(int(int(e.control.value)))
        page.update()
        print(f"Brazo Hombros {text_5.value}")

    def slider_changed_base(e):        
        text_6.value = f"Brazo Base {int(e.control.value)}"
        uic.base(int(int(e.control.value)))
        page.update()
        print(f"Brazo Base {text_6.value}")



    text_1 = Text("Brazo Pinzas 0", size=18)
    container_1 = Container(
        content = Row(
            controls = [                
                Container( expand=1,
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

    card = Card(
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
    
    main_container = Container(     
        content = Column( 
            alignment = "center",
            controls = [                              
                Card(
                    content = Container(
                        content = Text("CONTROLES DEL BRAZO ROBÓTICO", size=22),
                        margin = 10,
                        alignment = alignment.center                        
                    ),                    
                    width = 600,
                    elevation = 16,
                    margin = 10 
                   ),
                card
            ]
        ),
        alignment = alignment.center
    )
    
    page.add(main_container)
        

flet.app(target=main)
