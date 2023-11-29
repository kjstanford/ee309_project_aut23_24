import sys
sys.path.insert(0, '../')
from funs import *

def read_spice_netlist(fname, params):
    i_lines = list(fi.input(files = fname+'_pre.sp'))
    o_lines = []

    for line in i_lines:
        line_list = line.split()
        if len(line_list) == 4:
            if line_list[0] == ".PARAM" and line_list[3][0]=='@':
                line_list[3] = str(params[line_list[1]])
        o_lines.append(' '.join(line_list))

    # print(o_lines)
    with open(fname+'_post.sp', 'w') as fp:
        fp.write('\n'.join(o_lines))
    fp.close()


params = dict(vmax=0.7, vmin=0, vin=0, step=1e-12, sim_time=3e-9, wl_pw=0.5e-9, wl_del=0.5e-9,\
               rise=0.1e-9, fall=0.1e-9, tp=3e-9, bl_cap=1e-13)
read_spice_netlist(fname='sram6T_read', params=params)

sys('hspice sram6T_read_post.sp -o s1')
lis_M = read_lis_general('s1.lis')

lis_t = lis_M[:,0]
lis_vwl = lis_M[:,1]
lis_vbl = lis_M[:,2]
lis_vblb = lis_M[:,3]
lis_vn1 = lis_M[:,4]
lis_vn2 = lis_M[:,6]

# lin_plot(x=[lis_t]*5, y=[lis_vwl, lis_vbl, lis_vblb, lis_vn1, lis_vn2], c=['r', 'g', 'b', 'k', 'm'], s=['solid'], xlabel="$time (s)$", ylabel="$voltage (V)$", figname='temp.png')

plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rcParams["figure.figsize"] = (12, 10)
fig, ((ax1, ax2, ax3)) = plt.subplots(3,1,sharex=True)
ax1.plot(lis_t*1e9, lis_vwl, linewidth=4, color='r')
ax2.plot(lis_t*1e9, lis_vbl, linewidth=4, color='b')
ax2.plot(lis_t*1e9, lis_vblb, linewidth=4, color='r')
ax3.plot(lis_t*1e9, lis_vn1, linewidth=4, color='r')
ax3.plot(lis_t*1e9, lis_vn2, linewidth=4, color='r')
ax1.set(ylabel='$WL(V)$')
ax1.set(ylim=[-0.1, 0.8])
ax1.set(yticks=[0, 0.7])
ax2.set(ylabel='$BL,BLB(V)$')
ax2.set(ylim=[-0.1, 0.8])
ax2.set(yticks=[0, 0.7])
ax3.set(ylabel='$N1,N2(V)$')
ax3.set(ylim=[-0.1, 0.8])
ax3.set(yticks=[0, 0.7])
ax1.minorticks_on()
ax1.tick_params(direction='in', length=6, width=2, colors='k',
            grid_color='k', grid_alpha=0.5, which='major')
ax1.tick_params(direction='in', length=3, width=2, colors='k',
            grid_color='k', grid_alpha=0.5, which='minor')
ax2.minorticks_on()
ax2.tick_params(direction='in', length=6, width=2, colors='k',
            grid_color='k', grid_alpha=0.5, which='major')
ax2.tick_params(direction='in', length=3, width=2, colors='k',
            grid_color='k', grid_alpha=0.5, which='minor')
ax3.minorticks_on()
ax3.tick_params(direction='in', length=6, width=2, colors='k',
            grid_color='k', grid_alpha=0.5, which='major')
ax3.tick_params(direction='in', length=3, width=2, colors='k',
            grid_color='k', grid_alpha=0.5, which='minor')
plt.xlabel(xlabel='time (ns)', fontweight='bold')
plt.savefig(fname='temp.png')
