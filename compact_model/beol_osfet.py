import sys
sys.path.insert(0, '../')
from funs import *

sys('hspice beol_osfet.sp -o be0')
lis_M = read_lis_general('be0.lis')

lis_vg = lis_M[:,0]
lis_id0p01 = -1*lis_M[:,1]
lis_id0p7 = -1*lis_M[:,2]

legend = [None]

logy_lin_plot(x=[lis_vg]*2, y=[lis_id0p01*1e3, lis_id0p7*1e3], c=['r'], lw=2.5, s=['solid']*1+['dashed']*1, m=['None']*1+['None']*1,\
        xlabel="$V_{GS} (V)$", ylabel="$I_{D}$ (${m}A$)", l=legend, figname='temp.png', ms=6)