import sys
sys.path.insert(0, '../')
from funs import *

sys('hspice model_calibrate.sp -o e0')
lis_M = read_lis_general('e0.lis')

lis_vg = lis_M[:,0]
lis_id0p01 = -1*lis_M[:,1]
lis_id0p7 = -1*lis_M[:,2]
lis_idp0p01 = lis_M[:,3]
lis_idp0p7 = lis_M[:,4]

sys('hspice beol_osfet.sp -o be0')
lis_M = read_lis_general('be0.lis')

lis_vgb = lis_M[:,0]
lis_idb0p01 = -1*lis_M[:,1]
lis_idb0p7 = -1*lis_M[:,2]

# cad_M0p01 = pd.read_csv('../csv_tcad_model/main_m0p01_fet_dut_nanosheet_ns2_2D_NMOS_idvg.csv')
# cad_M0p7 = pd.read_csv('../csv_tcad_model/main_m0p7_fet_dut_nanosheet_ns2_2D_NMOS_idvg.csv')
# cad_vg0p01 = cad_M0p01.values[:,0]
# cad_vg0p7 = cad_M0p7.values[:,0]
# cad_id0p01 = cad_M0p01.values[:,1]
# cad_id0p7 = cad_M0p7.values[:,1]

legend = [None]
# print(mvg)

logy_plot(x=[lis_vg, -1*lis_vg, lis_vgb], y=[lis_id0p7*1e3, lis_idp0p7*1e3, lis_idb0p7*1e3], c=['r', 'g'], lw=2.5, s=['solid']*2+['dashed']*2, m=['None']*2+['None']*2,\
        xlabel="$V_{GS} (V)$", ylabel="$I_{D}$ (${m}A$)", l=legend, figname='temp1.png', ms=6)

np.savetxt('idvg_vd0p7_cfet_beol.csv', X= np.transpose(np.array([lis_vg, -1*lis_vg, lis_vgb, lis_id0p7, lis_idp0p7, lis_idb0p7])))