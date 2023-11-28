** header **
.INCLUDE "../compact_model/7nm_TT_160803.pm"
.PARAM vmax=0.7 vmin=0 vin=0
.PARAM step=1e-12
.PARAM sim_time=5e-9
.PARAM wl_pw=1e-09
.PARAM wl_del=1e-09
.PARAM bl_pw=1e-09
.PARAM bl_del=1e-09
.PARAM wrise=0.3e-9
.PARAM wfall=0.3e-9
.PARAM brise=0.5e-9
.PARAM bfall=0.5e-9
.PARAM tp=5e-9

.PROBE TRAN
+ V(wwl)
+ V(wblb)
+ V(n1)
+ V(n2)

.PRINT TRAN
+ V(wwl)
+ V(wblb)
+ V(n1)
+ V(n2)

.DCVOLT n1 'vmin'
.DCVOLT n2 'vmax'
.DCVOLT wbl 'vmax'
.DCVOLT wblb 'vmax'

.TRAN 'step' 'sim_time'

.TEMP 25.0
.OPTION
+    ARTIST=2
+    INGOLD=2
+    PARHIER=LOCAL
+    PSF=2

mpgw1 wbl wwl n1 vss nmos_sram l=20e-9 nfin=1
mpu1 n1 n2 vdd vdd pmos_sram l=20e-9 nfin=1
mpd1 n1 n2 vss vss nmos_sram l=20e-9 nfin=1
mpgw2 wblb wwl n2 vss nmos_sram l=20e-9 nfin=1
mpu2 n2 n1 vdd vdd pmos_sram l=20e-9 nfin=1
mpd2 n2 n1 vss vss nmos_sram l=20e-9 nfin=1
mpgr1 nr n2 vss vss nmos_sram l=20e-9 nfin=1
mpgr2 rbl rwl nr vss nmos_sram l=20e-9 nfin=1
vsuph vdd 0 DC='vmax'
vsupl vss 0 DC='vmin'
vwwl wwl 0 PULSE 'vmin' 'vmax' 'wl_del' 'wrise' 'wfall' 'wl_pw' 'tp'
vwbl wbl 0 DC='vmax'
vwblb wblb 0 PULSE 'vmax' 'vmin' 'bl_del' 'brise' 'bfall' 'bl_pw' 'tp'
vrwl rwl 0 DC='vmin'
vrbl rbl 0 DC='vmax'

.END