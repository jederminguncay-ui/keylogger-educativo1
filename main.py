import keyboard
print("Tu primer keyboard")
print("Presiona ESC para salir")

while True:
    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_DOWN:
        print(event.name)
    if event.name == "esc":
        break
   