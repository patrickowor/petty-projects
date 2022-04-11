try:
    import PySimpleGUI as sg
except:
    print('sorry PySimpleGUI module missing please install ')

# this is a column of button widget one to submit one to exit
column_button = [[sg.Submit()],
                [sg.Exit()]
]

# this is a column of input and text widget one to submit one to exit
column_layout = [[sg.Text('data',font=("Helvetica",10,"bold"),background_color='white',text_color='red')],
                	[sg.Text('solvent: '),sg.Input(key='solvent')],
                    [sg.Text('weight: '),sg.Input(key='weight')],
                    [sg.Text('volume: '),sg.Input(key='volume')]
]
# this is the overall layout everything including the column layout is inside this layout
layout = [[sg.T('calculator',font=("Helvetica",30,"bold"),background_color='white',text_color='red')],[sg.Column(column_layout,background_color='white', size=(500,500)),sg.Column(column_button,background_color='white')],
]
window = sg.Window('calculator', layout,resizable=True, size=(600,200), background_color='white')
# looping the window to keep it from exiting itself
while True:
	event, values = window.Read()
	if event is None or event == 'Exit':
	    break
	else:
	    if values['volume'] and values['weight'] and values['solvent']:
	       # here is the calculation
	       vol = float(values['volume'])
	       wg = float(values['weight'])
	       solubility = wg / vol  *1000
	       mM = float(solubility) / 306.98  *1000
	       result = ' the solubility of '+ str(values['solvent'])+ ' is ' +str(solubility)+ 'and the mM of '+ str(values['solvent'])+ 'is' + str(mM)
	       sg.Popup(result)
	    else:
	        # this is what pop up if a value is forgotten 
	        sg.Popup('one value missing ')
window.Close()