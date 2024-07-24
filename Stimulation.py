import time
from base import Stim       
from base import Device

""" PARAMETERS"""

trial_number = 110 # how many trials are done
# interstart_time = 1 # time between stimuli start in sec
stim2_length = 5 # stimulus length in sec for laser 2
inter_trial_time = 25  # time between trials in sec

#Trials repeat a number of times and a pause in between
# each trial is a sequence of stimuli with specific length and a pause between starts

"""Stimuli"""

input_port_stim1 = "Dev1/PFI0"
# input_port_stim2 = "Dev1/PFI1"
stim1 = Stim(name="Laser", color="blue")
# stim2 = Stim(name="AirPuff")
stim1_device = Device(input_port_stim1, "BlueLaser")
# stim2_device = Device(input_port_stim2, "OdorStim", )

"""Experiment"""
try:
    for trial in range(trial_number):
        print(str(trial)+"-"*20+" Starting trial number "+str(trial))
        # stim2_device.turn_on() #turn on air puff
        # print(f"Waiting interstart time ({interstart_time} sec)")
        # time.sleep(interstart_time) #wait for next stimulus
        stim1_device.turn_on() #turn on laser
        print(f"Waiting optical stimulation length ({stim2_length} sec)")
        time.sleep(stim2_length)
        #  stim2_device.turn_off()
        stim1_device.turn_off()
        print(f"Starting inter trial time ({inter_trial_time} sec)")
        time.sleep(inter_trial_time)
except:
    print("Interrupted")
    stim1_device.turn_off()