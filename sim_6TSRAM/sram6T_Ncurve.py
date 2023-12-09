import sys
sys.path.insert(0, '../')
from funs import *

def evaluateSVNM(Vin, Iin):
    root_list = []
    for i in range(1, len(Vin)):
        flag = abs(Iin[i])/Iin[i]
        flag_prev = abs(Iin[i-1])/Iin[i-1]
        if flag != flag_prev:
            root_list.append(Vin[i])
    # print(root_list)
    return root_list[1]-root_list[0]

sys('hspice sram6T_Ncurve.sp -o s0')
lis_M = read_lis_general('s0.lis')

lis_Vin = lis_M[:,0]
lis_Iin = -lis_M[:,1]

lin_plot(x=[lis_Vin], y=[lis_Iin*1e6], c=['r'], s=['solid'], xlabel="$V_{in} (V)$", ylabel="$I_{in}$ (${\mu}A$)", figname='temp.png', lw=4.5)

SINM = max(lis_Iin)
SVNM = evaluateSVNM(lis_Vin, lis_Iin)

print(f'SVNM: {SVNM}V and SINM: {SINM*1e6}uA')

np.savetxt('Ncurve_beol_pg.csv', np.transpose(np.array([lis_Vin, lis_Iin])))
