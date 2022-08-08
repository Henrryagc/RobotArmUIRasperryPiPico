# Azul
hsv_blue_min = (100, 150, 0)
hsv_blue_max = (140, 255, 255)

# Verde
hsv_green_min = (36, 25, 25)
hsv_green_max = (70, 255, 255)

# Rojo
hsv_red_min = (0, 50, 50)
hsv_red_max = (10, 255, 255)

global masks_names
masks_names = ['azul', 'verde', 'rojo']

class Counter(UserControl):
    def add_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        self.counter = 0
        self.text = Text(str(self.counter))
        return Row([self.text, FilledButton("Add", on_click=self.add_click)])


def find_object(img, mask, color, num_mask):
    cnts, hireachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) != 0:
        c = max(cnts, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
        text = masks_names[num_mask]
        text_position = (round(x+w/2), round(y+h/2))
        cv2.putText(img, text, text_position, cv2.FONT_ITALIC, 0.6, (255, 255, 255), 1)

        return (round(x+w/2), round(y+h/2))
    return (0, 0)
