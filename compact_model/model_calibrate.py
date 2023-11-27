import sys
sys.path.insert(0, '../')
from funs import *

sys('hspice model_calibrate.sp -o e0')
lis_M = read_lis_general('e0.lis')

vgate = lis_M[:,0]
id0p01 = lis_M[:,1]
id0p7 = lis_M[:,2]

legend = [None]
# print(mvg)

logy_lin_plot(x=[vgate]*2, y=[abs(id0p01)*1e6, abs(id0p7)*1e6], c=['r', 'g', 'b', 'k'], lw=2.5, s=['solid']*4+['dashed']*4, m=['None'],\
        xlabel="$V_{GS} (V)$", ylabel="$I_{D}$ (${\mu}A$)", l=legend, figname='temp.png')