import PySimpleGUI as sg

label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter kilometers: ", key="kms")
convert_button= sg.Button("Convert")

window = sg.Window("km to miles converter",
                    layout=[
                        [label],[input_box],
                        [convert_button],
                   ])

while True:
    event, values = window.read()
    match event:
        case "Convert":
            km = values["kms"]
            result = km_to_miles(km)
            window['output'].update(value=result)
        case sg.WIN_CLOSED:
            break

window.close()