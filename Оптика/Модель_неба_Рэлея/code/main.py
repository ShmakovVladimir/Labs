import numpy as np
import serial
import cv2
import time
import datetime

def get_img(polarization_angle: int) -> np.ndarray:
    polarization_angle_to_angle = {0: 15, 45: 120, 135: 65, 90: 180}
    port.write(bytes(str(polarization_angle_to_angle[polarization_angle]), 'utf-8'))
    time.sleep(2)
    _, frame = cam.read()
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



def main():
    experiment_directory_name = '29_may_experiment/'
    
    while(True):
        current_time = datetime.datetime.now()
        time_prefix = str(datetime.datetime.time(current_time))[:-7].replace(':', '_')
        for polarization_angle in [0, 90, 45, 135]:
            img = get_img(polarization_angle)
            cv2.imwrite(experiment_directory_name + time_prefix + f'_polarization_{polarization_angle}.png', img)
            np.save(experiment_directory_name + time_prefix + f'_polarization_{polarization_angle}.npy', img)
        with open("sync.txt", "a") as sync_file: 
            sync_file.write('\n' + time_prefix)


        
        


experiment_directory_name = '29_may_experiment/'
port = serial.Serial('/dev/ttyUSB0', 9600)
cam = cv2.VideoCapture(2)
stokes_parametrs = np.loadtxt('stokes_parametrs.txt')

main()
