# Treadmill
Repository for the Treadmill for live experiments
## Setup
1. Install Ni Software (https://www.ni.com/de-de/support/downloads/drivers/download.ni-daqmx.html)
2. Create Angular Position Task
   - Open 'Ni Max'
   - Select your device
   - Click on 'Create Task'
   - Under 'Acquire Signals' / 'Counter Input' / 'Position' select 'Angular Position'
   - Select 'ctr0' and click 'Next'
   - Name the Task 'Treadmill Position' and click 'Finish'
   - Change the options to the following:
     - > The Input Terminals should be changed to the inputs you use!
     - ![Settings for Task](https://github.com/TimLeffke/Treadmill/blob/main/task_settings.jpg?raw=true)
   - Click 'Save'
3. Install Python bindings for Ni
   - In a fresh anaconda enviroment run 'pip install nidaqmx'
4. Run 'test.py'
