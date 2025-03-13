import tsapp

button_filenames = ("ArrowIconUp.png", "ArrowIconDown.png", "ArrowIconReset.png")

window = tsapp.GraphicsWindow()
background = tsapp.Sprite("TextEditor.jpg", 0, 0)
counter = 0
pages = 0

with open("poems.big.txt") as file:
    text_content = file.readlines()

def change_page():
    screen = ""
    for line in text_content[counter:counter+20]:
        screen += line
    display_text.text = screen
    return screen

display_text = tsapp.TextLabel("NotoMono-Regular.ttf", 25, 220, 50, 500, "", tsapp.BLACK)

screen = change_page()

up_button = tsapp.Sprite(button_filenames[0], 30, 30)
down_button = tsapp.Sprite(button_filenames[1], 30, 180)
reset_button = tsapp.Sprite(button_filenames[2], 30, 330)

window.add_object(background)
window.add_object(up_button)
window.add_object(down_button)
window.add_object(reset_button)
window.add_object(display_text)

while window.is_running:
    x, y = tsapp.get_mouse_position()
    if tsapp.was_mouse_pressed() and up_button.is_colliding_point(x, y) and pages > 0:
        counter -= 20
        screen = change_page()
        pages -= 1
    if tsapp.was_mouse_pressed() and reset_button.is_colliding_point(x, y):
        counter = 0
        screen = change_page()
        pages = 0
    if tsapp.was_mouse_pressed() and down_button.is_colliding_point(x, y):
        counter += 20
        screen = change_page()
        pages += 1
    window.finish_frame()
