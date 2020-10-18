import tello
from tello_control_ui import TelloUI


def main():

    drone = tello.Tello('', 8889)  
    vplayer = TelloUI(drone,"./img/")
    
	# start the Tkinter mainloop
    try:
        vplayer.root.mainloop() 
    except KeyboardInterrupt:
        vplayer.onClose()

if __name__ == "__main__":
    main()
