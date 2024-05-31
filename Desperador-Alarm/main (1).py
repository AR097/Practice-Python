# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *
# library

# Create Object
root = Tk()
#/ Create

# Set geometry
root.geometry("400x250")
#/ tamanho da janela

# Use Threading
def Threading():
	t1=Thread(target=alarm)
	t1.start()

def alarm():
	# Infinite Loop
	while True:
		# Set Alarm
		set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

		# Wait for one seconds
		time.sleep(1)

		# Get current time
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		print(current_time,set_alarm_time)

		# Check whether set alarm is equal to current time or not
		if current_time == set_alarm_time:
			print("Time to Wake up")
			# Playing sound
			winsound.PlaySound("sound.wav",winsound.SND_ASYNC)

# Add Labels, Frame, Button, Optionmenus
#titulo Despertador
Label(root,text="Despertador",font=("Helvetica 20 bold"),fg="black").pack(pady=15) #__ bold é o tamanho da fonte
Label(root,text="Selecione o horário:",font=("Helvetica 15 bold")).pack() #__ bold é o tamanho da fonte

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])#inicia em zero

#configuraçoes do botão horas
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
hrs.configure(background="white", border="5")
#/ configuraçoes do botão horas

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15','16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47',	'48', '49', '50', '51', '52', '53', '54', '55',	'56', '57', '58', '59', '60')
minute.set(minutes[0]) #inicia em zero

#configuraçoes do botão minutos
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
mins.configure(background="white", border="5")
#/configuraçoes do botão minutos

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15','16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47',	'48', '49', '50', '51', '52', '53', '54', '55',	'56', '57', '58', '59', '60')
second.set(seconds[0])#inicia em zero

#configuraçoes do botão segundos
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)
secs.configure(background="white", border="5")
#/configuraçoes do botão segundos

#configuraçoes do botão confirmar alarme
Button(root,text="Definir alarme", background="white", border="5",font=("Helvetica 15"),command=Threading).pack(pady=20)

#/configuraçoes do botão confirmar alarme

# Execute Tkinter
root.mainloop()