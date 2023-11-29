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
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
plt.rcParams["figure.figsize"] = (12, 10)
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
    if not xticklabels == 0:
        ax.set_xticks(x[0])
        ax.set_xticklabels(xticklabels)
    # plt.figure(figsize=(1,1))
    plt.grid()
    # plt.show(block=True)
    plt.savefig(fname=figname)

snm_pd_6T = pd.read_csv('../sim_6TSRAM/nm_table.csv')
snm_pd_8T = pd.read_csv('../sim_8TSRAM/nm_table.csv')

lin_plot(x=[[1, 2, 3, 4]]*2, y=[snm_pd_6T.values[:,1], snm_pd_8T.values[:,1]], c=['r', 'k'], s=['solid'], m=['o'],\
         ylim=[0.2, 0.4], xticklabels=['111', '112', '123', '122'], yticks=[0.2, 0.25, 0.3, 0.35, 0.4], ms=20, lw=4.5,\
            xlabel='#fins (PU, PG, PD)', ylabel='SVNM (V)')

lin_plot(x=[[1, 2, 3, 4]]*2, y=[snm_pd_6T.values[:,2], snm_pd_8T.values[:,2]], c=['r', 'k'], s=['solid'], m=['o'],\
         ylim=[20, 80], xticklabels=['111', '112', '123', '122'], yticks=[20, 40, 60, 80], ms=20, lw=4.5,\
            xlabel='#fins (PU, PG, PD)', ylabel='SINM ($\mu A$)')