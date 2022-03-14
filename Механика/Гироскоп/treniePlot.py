import main as m
import matplotlib.pyplot as plt
mass = [m.exp[i].mass for i in range(len(m.exp))]
moment = [m.exp[i].Mtr for i in range(len(m.exp))]
plt.errorbar(x=[mass[i].value for i in range(len(mass))],
            y = [moment[i].value for i in range(len(moment))],
            xerr=[mass[i].error for i in range(len(mass))],
            yerr=[moment[i].error for i in range(len(moment))],
            fmt='_')
plt.xticks([i/100 for i in range(0,45,2)])
plt.yticks([i/1000 for i in range(25)])
plt.grid()
plt.show()