# OptionsSwap
OptionsSwap changes the settings file used in standardoptions.txt for all of your instances at once. 



The files aa.txt and rsg.txt in this folder are examples of what you might switch between, you can edit them or add more.

Edit instances.py so that: \
mc_path is the path to your MultiMC, it should look like this: r"C:\Users\user\Downloads\MultiMC" \
inst_setup is what your instance folders are called with an asterik where the number would be, for example "inst*" if they are called inst1, inst2, inst3 and so on. \
inst_number is how many instances you have.


Copy standardoptions.txt from your config folder and paste it into this folder. You can name it whatever you want (mine is rsg.txt). Add whichever options files you will be swapping between as well.

Double click run.bat to run the program and type in the settings file you want to use (for example, rsg.txt). The new settings will be applied on your next reset without relaunching your instances. If the file you type is not located in this folder it will not work.

Make sure you download python and restart your computer before running the program if you haven't already.

Credits to macusmacus for the idea to make this :d
