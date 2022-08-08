import flet
from flet import ElevatedButton, Page, Text
import csv


def main(page: Page):
    page.title = "Elevated button with 'click' event"
    
        
    def button_clicked(e):
        for i in range(500):

            b.data += 1
            if b.data > 9:
                b.data = 0
            t.value = f"Button clicked {b.data} time(s)"
            data = [
                1 + b.data,
                2 + b.data, 
                5 + b.data, 
                11 + b.data, 
                5 + b.data, 
                6 + b.data, 
                11 + b.data, 
                8 + b.data, 
                9 + b.data, 
                10 + b.data, 
                11 + b.data, 
                12 + b.data, 
                6 + b.data, 
                10 + b.data
                ] 
            headerNames = ['x', 'y', 'gripper1', 'wrist1', 'arm_top1', 'arm_bottom1', 'shoulders1', 'base1', 'gripper2', 'wrist2', 'arm_top2', 'arm_bottom2', 'shoulders2', 'base2']
            with open('data.csv', 'a', newline='') as csvfile:   
                #writer = csv.writer(csvfile)            
                writer = csv.DictWriter(csvfile, fieldnames=headerNames)

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
                    'base2': data[13]
                    })
                print(data)
                data.clear()


        page.update()

    b = ElevatedButton("Button with 'click' event", on_click=button_clicked, data=0)
    t = Text()

    page.add(b, t)

flet.app(target=main)