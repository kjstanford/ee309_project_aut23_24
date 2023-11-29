import sys
sys.path.insert(0, '../')
from funs import *

# plotting section
SMALL_SIZE = 22
MEDIUM_SIZE = 26
BIGGER_SIZE = 32

plt.rc('font', size=SMALL_SIZE, weight='bold')          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
plt.rcParams["figure.figsize"] = (13, 10)
plt.rcParams['axes.linewidth'] = 2.5

def lin_plot(x, y, c, s, mask=[True], m=[None], l=[None], xlim=0, ylim=0, xticks=0, yticks=0, xticklabels=0, lw=2.0, xlabel='', ylabel='', title='', figname='temp.png', ms=12):
    fig, ax = plt.subplots()
    for i in range(len(x)):
        if mask[i%len(mask)]:
            ax.plot(x[i], y[i], linewidth=lw, marker=m[i%len(m)], color=c[i%len(c)], linestyle=s[i%len(s)], markersize=ms)
    # ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    plt.xlabel(xlabel=xlabel, fontweight='bold')
    plt.ylabel(ylabel=ylabel, fontweight='bold')
    plt.title(label=title, fontweight='bold')
    # ax.xaxis.set_minor_locator(AutoMinorLocator())
    # ax.yaxis.set_minor_locator(AutoMinorLocator())
    
    labels = ax.xaxis.get_ticklabels() + ax.yaxis.get_ticklabels()
    [label.set_fontweight('bold') for label in labels]
    ax.minorticks_on()
    ax.tick_params(direction='in', length=6, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='major')
    ax.tick_params(direction='in', length=3, width=2, colors='k',
               grid_color='k', grid_alpha=0.5, which='minor')
    
    if not l == [None]:
        ax.legend(l)
    if not xlim == 0:
        ax.set(xlim=xlim)
    if not ylim == 0:
        ax.set(ylim=ylim)
    if not xticks == 0:
        ax.set(xticks=xticks)
    if not yticks == 0:
        ax.set(yticks=yticks)
    # if not xticklabels == 0:
    #     ax.set_xticks(x[0])
    #     ax.set_xticklabels(xticklabels)
    # plt.figure(figsize=(1,1))
    plt.grid()
    # plt.show(block=True)
    plt.savefig(fname=figname)

dvbl_pw_6T = pd.read_csv('../sim_6TSRAM/dvbl_pw_table.csv')
dvbl_pw_8T = pd.read_csv('../sim_8TSRAM/dvbl_pw_table.csv')

lin_plot(x=[dvbl_pw_6T.values[:,0], dvbl_pw_8T.values[:,0]], y=[dvbl_pw_6T.values[:,1]*1e3, dvbl_pw_8T.values[:,1]*1e3], c=['r', 'k'], s=['solid'], m=['o'],\
         ylim=[0, 200], xticks=[0.1, 0.5, 1, 2, 3], yticks=[0, 50, 100, 150, 200], ms=20, lw=4.5,\
            xlabel='WL pulse width (ns)', ylabel='$\Delta V_{BL}$ ($mV$)',l=['6T SRAM', '8T SRAM'])