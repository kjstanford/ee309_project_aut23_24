** header **
.INCLUDE "../compact_model/7nm_TT_160803.pm"
.PARAM vmax=0.7 vmin=0 vin=0
.PARAM step=1e-12
.PARAM sim_time=5e-9
.PARAM wl_pw=1e-09
.PARAM wl_del=1e-09
.PARAM rise=0.3e-9
.PARAM fall=0.3e-9
.PARAM tp=5e-9
.PARAM bl_cap=1e-12 

.PROBE TRAN
+ V(wl)
+ V(bl)
+ V(blb)

.PRINT TRAN
+ V(wl)
+ V(bl)
+ V(blb)

.DCVOLT n1 'vmin'
.DCVOLT n2 'vmax'
.DCVOLT bl 'vmax'
.DCVOLT blb 'vmax'
.TRAN 'step' 'sim_time'

.TEMP 25.0
.OPTION
+    ARTIST=2
+    INGOLD=2
+    PARHIER=LOCAL
+    PSF=2

mpg1 bl wl n1 vss nmos_sram l=20e-9 nfin=1
mpu1 n1 n2 vdd vdd pmos_sram l=20e-9 nfin=1
mpd1 n1 n2 vss vss nmos_sram l=20e-9 nfin=1
mpg2 blb wl n2 vss nmos_sram l=20e-9 nfin=1
mpu2 n2 n1 vdd vdd pmos_sram l=20e-9 nfin=1
mpd2 n2 n1 vss vss nmos_sram l=20e-9 nfin=1
vsuph vdd 0 DC='vmax'
vsupl vss 0 DC='vmin'
vwl wl 0 PULSE 'vmin' 'vmax' 'wl_del' 'rise' 'fall' 'wl_pw' 'tp'
cbl bl 0 'bl_cap'
cblb blb 0 'bl_cap'

.END