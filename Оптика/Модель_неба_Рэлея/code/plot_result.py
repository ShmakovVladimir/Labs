import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime
from os import listdir
from os.path import isfile, join

def threshhold(arg):
    return (arg < 1) * arg + (arg > 1)


def polarization(polarization_0: np.ndarray,
                 polarization_90: np.ndarray,
                 polarization_45: np.ndarray,
                 polarization_135: np.ndarray) -> dict:
    """Рассчитавает степень и угол поляризации каждого пикселя

    Args:
        polarization_0 (np.ndarray): фотография через поляроид 
        polarization_90 (np.ndarray): фотография через поляроид, скрещенный к исходному
        polarization_45 (np.ndarray): фотография через поляроид с осью под 45 к исходному
        polarization_135 (np.ndarray): фотография через поляроид с осью под 135 к исходному

    Returns:
        dict: Степень поляризации и угол поляризации каждого из пикселей
    """
    global stokes_parametrs
    intensity_matrix = np.array([polarization_0,  
                                 polarization_90,  
                                 polarization_45,  
                                 polarization_135],
                                 dtype = np.float64)
    s = np.tensordot(stokes_parametrs, intensity_matrix, axes = 1) 
    dolp = np.sqrt(np.power(s[1], 2) + np.power(s[2], 2)) / s[0]
    aop = 0.5 * np.angle(s[1] + 1j * s[2])
    return {'linear_polarizatioin_degree': dolp,
            'angle_of_polarization': aop,
            's0': s[0],
            's1': s[1],
            's2': s[2]}

def find_max_time_string(paths):
    max_string = max(paths, key=lambda s: int(s[:8]))
    return max_string

def get_newest_images() -> tuple:
    """Возвращает названия самых новых полученных данных


    Returns:
        tuple: (polatization_0, polatization_90, polatization_45, polatization_135)
    """
    last_line = ''
    with open('sync.txt') as f:
        for line in f:
            last_line = line
            
    result = []
    for polarization in [0, 90, 45, 135]:
        result.append(experiment_directory_name + last_line + f'_polarization_{polarization}.npy')
    return tuple([np.load(path) for path in result])

def animate(i):
    global cb, cb2
    if cb is not None:
        cb.remove()
    if cb2 is not None:
        cb2.remove()
    img_0, img_90, img_45, img_135 = get_newest_images();
    polarization_info = polarization(img_0, img_90, img_45, img_135)
    for a in ax:
        for j in a: j.clear()
    ax[0, 0].imshow(img_0, cmap = 'gray')
    ax[0, 0].set_title("$0 \degree$", fontsize = 12)
    ax[0, 1].imshow(img_90, cmap = 'gray')
    ax[0, 1].set_title("$90 \degree$", fontsize = 12)
    ax[0, 2].imshow(img_45, cmap = 'gray')
    ax[0, 2].set_title("$45 \degree$", fontsize = 12)
    ax[0, 3].imshow(img_135, cmap = 'gray')
    ax[0, 3].set_title("$135 \degree$", fontsize = 12)
    im = ax[1, 0].imshow(threshhold(polarization_info['linear_polarizatioin_degree']), cmap = 'Pastel1')
    cb = plt.colorbar(im)
    ax[1, 0].set_title("Стпень поляризации", fontsize = 12)
    x = np.arange(0, img_0.shape[0], 10)
    y = np.arange(0, img_0.shape[1], 10)

    X, Y = np.meshgrid(x, y)

    U = np.sin(polarization_info['angle_of_polarization'][X, Y])
    V = np.cos(polarization_info['angle_of_polarization'][X, Y])

    ax[1, 1].quiver(Y, X, U, V, color = 'orange', headlength=0, headaxislength=0,)
    ax[1, 1].imshow(polarization_info['s0'],
                    cmap = 'gray')
    ax[1, 1].set_title("Угол поляризации", fontsize = 12)
    # if cb2 is not None:
    #     cb2.remove()
    im2 = ax[1, 2].imshow(polarization_info['angle_of_polarization'], cmap = 'Pastel1')
    cb2 = plt.colorbar(im2)
    x = np.arange(0, img_0.shape[0], 20)
    y = np.arange(0, img_0.shape[1], 20)
    ax[1, 2].set_title("Угол поляризации", fontsize = 12)
    X, Y = np.meshgrid(x, y)

    U = np.sin(polarization_info['angle_of_polarization'][X, Y])
    V = np.cos(polarization_info['angle_of_polarization'][X, Y])

    ax[1, 3].quiver(Y, X, U, V, color = 'orange', headlength=0, headaxislength=0,)
    ax[1, 3].imshow(polarization_info['s0'],
                    cmap = 'gray')
    ax[1, 3].set_title("Угол поляризации", fontsize = 12)


cb, cb2 = None, None
experiment_directory_name = '29_may_experiment/'
stokes_parametrs = np.loadtxt('stokes_parametrs.txt')
fig, ax = plt.subplots(2, 4, figsize = (32, 18), dpi = 100)



ani = animation.FuncAnimation(fig, animate, interval=50)
plt.show()
