from matplotlib.widgets import Button, Slider
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(2, 4, figsize = (20, 10), dpi = 200)

def update():
    def get_sig_and_fft(w):
        sig = np.sin(2 * np.pi * w * t)
        freq = np.fft.fftfreq(len(sig), time_interval)[:N//2]
        mag = np.abs(np.fft.fft(sig))[:N//2]
        return sig, freq, mag / np.max(mag)
    T = T_slider.val #время измерения
    N = 1000 #количество измерений
    t = np.linspace(0, T, N) #моменты времени в которые были произведены измерения
    time_interval = np.mean(np.diff(t)) #интервалы между измерениями
    w_values = [2, 1, 0.5, 0.25]
    for ind, w in enumerate(w_values):
        sig, f, m = get_sig_and_fft(w)
        ax[0][ind].plot(t, sig)
        ax[1][ind].plot(f, m)
        ax[0][ind].set_title(w)
        ax[1][ind].set_xlim(0, 2.1)
        ax[1][ind].axvline(w, linestyle = '--', color = 'black')
        ax[0][ind].set_title(f'w = {w}')
    
    
axamp = fig.add_axes([0, 0.25, 0.0225, 0.63])
T_slider = Slider(
    ax=axamp,
    label="время измерения [с]",
    valmin = 2,
    valmax = 20,
    valinit=2,
    orientation="vertical"
)

T_slider.on_changed(update)
plt.show()