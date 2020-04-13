from subprocess import call
import os
import dynate
import proice 
import prant
# import proice

id = 'setup'
fid = ""
# Bluetooth --> install devcon, acquire bluetooth hardware id.

# Installing / Checking Python modules...

#%dynate-1.open
proice.core("Please enter the OS platform (win/ub)...", id, fid)
platform = input()
if platform == "win":
    ver = ".7"
else:
    ver = ""
#%dynate-1.close

# proice.core('>> Checking dependencies, please standby...', id)

req_modules = ('time', 'numpy', 'pyttsx3', 'playsound', 'openwaether',
               'docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*', 'kivy_deps.gstreamer==0.1.*', 'kivy==1.11.1')

def update(ver):
    fid = "update"

    import pkg_resources
    packages = [dist.project_name for dist in pkg_resources.working_set]
    call("pip3"+ver+" install --upgrade " + ' '.join(packages), shell=True)

def getmodule(x, ver):
    fid = "getmodule"
    
    module=""

    if x==0:
        for module in req_modules:
            print("\n\n# Installing required python module: ", module)
            os.system("pip3"+ver+" install " + module)
        print("\n>>>> Modules checked successfully...")
    
def upgrade(x):
    fid = "upgrade"
    # Use this to upgrade to a new version of python. 

    module = ""

    if x == 0:
        print(">> Setup.upgrade is working...")

    if x != 0:
        for module in req_modules:
            print("\n\n# Uninstalling existing python module: ", module)
            os.system("pip3"+ver+" uninstall " + module)
            print("done...")
        print("\n>>>> Existing modules uninstalled successfully...")

        for module in req_modules:
            print("\n\n# Installing new python module: ", module)
            os.system("pip3"+x+" install " + module)
            print("done...")
        print("\n>>>> New modules installed successfully...")

        dynate.core(1)





    print("")

getmodule(0, ver)
update(ver)
