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
               rise=0.3e-9, fall=0.3e-9, tp=3e-9, bl_cap=1e-13)
read_spice_netlist(fname='sram6T_read', params=params)

sys('hspice sram6T_read_post.sp -o s1')
lis_M = read_lis_general('s1.lis')

lis_t = lis_M[:,0]
lis_vwl = lis_M[:,1]
lis_vbl = lis_M[:,2]
lis_vblb = lis_M[:,3]

lin_plot(x=[lis_t], y=[lis_vbl], c=['r'], s=['solid'], xlabel="$time (s)$", ylabel="$V_{BL} (V)$", figname='temp.png')