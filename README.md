# Ubuntu_access
This is a ubuntu access means if you install a distro using windows subsystem for linux(wsl)
like for example ubuntu, after you install it with windows subsystem for linux(wsl) it will ask you like enter unix name, password and retype password
in the backend this is a data which is stored in a datafile. after that you will be accesed to ubuntu. in your ubuntu distro .bashrc is the main file 
which is running servers to run the windows subsystem for linx(wsl) terminal in your windows computer.
This code which i written is same like that.
to understand this code you need to know couple of modules that are
sys, getpass and time
i used sys for quick exit. the sys.exit() function mean to exit quickly 
from sys import exit is a short code to reduce the code
typing sys.exit() is ok but writing just exit() is more better
so i written like that
i used getpass for hidding text, like the password.When you run this code after typing unix name it will ask password
then when you type a password the cursor will stay there but actualy you are typing the password. it is a module to hide text.
I used time pause the program, after retyping your password program will stay up to 2 seconds and then continoue the program.
Time is usefully to stop the program.
