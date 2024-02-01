# Autorun Scripts

This repository contains scripts to automatically run `3 servers` at startup.

## Setup Instructions

Follow these steps to set up the autorun scripts:

1. **Update autorun_hiraya.py**: Open `autorun_hiraya.py` then change the directory to your desired folder and the variables that need to be changed.

2. **Edit the Batch File**: Open the `.bat` file and update the following:

   - Change the location of `python.exe` to match your system.
   - Specify the directory of your `autorun_hiraya.py` file.

3. **Create a shortcut of autorun_hiraya.bat**

4. **Batch File in startup folder**: Move the `.bat` file to the startup folder.
   -Press Windows+R
   -type there 'shell:startup'
   -place the shortcut of the `autorun_hiraya.bat`

After completing these steps, the `on_prem_dashboard`, `on_prem_rtap_admin_api`, and `on_prem_plc_opcua` should automatically run at startup.
