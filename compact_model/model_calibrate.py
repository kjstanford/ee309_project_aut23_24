import sys
sys.path.insert(0, '../')
from funs import *

sys('hspice model_calibrate.sp -o e0')
lis_M = read_lis_general('e0.lis')

lis_vg = lis_M[:,0]
lis_id0p01 = -1*lis_M[:,1]
lis_id0p7 = -1*lis_M[:,2]

cad_M0p01 = pd.read_csv('../csv_tcad_model/main_m0p01_fet_dut_nanosheet_ns2_2D_NMOS_idvg.csv')
cad_M0p7 = pd.read_csv('../csv_tcad_model/main_m0p7_fet_dut_nanosheet_ns2_2D_NMOS_idvg.csv')
cad_vg0p01 = cad_M0p01.values[:,0]
cad_vg0p7 = cad_M0p7.values[:,0]
cad_id0p01 = cad_M0p01.values[:,1]
cad_id0p7 = cad_M0p7.values[:,1]

legend = [None]
# print(mvg)

logy_lin_plot(x=[lis_vg]*2+[cad_vg0p01, cad_vg0p7], y=[lis_id0p01*1e6, lis_id0p7*1e6, cad_id0p01*1e6, cad_id0p7*1e6], c=['r', 'g'], lw=2.5, s=['solid']*2+['None']*2, m=['None']*2+['o']*2,\
        xlabel="$V_{GS} (V)$", ylabel="$I_{D}$ (${\mu}A$)", l=legend, figname='temp.png', ms=6)