** header **
.INCLUDE "../compact_model/7nm_TT_160803.pm"
.PARAM vmax=0.7 vmin=0 vin=0

.PROBE DC
+ I(vn2)

.PRINT DC
+ I(vn2)

.DC vin LIN 100.0 vmin vmax

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
vsuph vdd 0 DC=vmax
vsupl vss 0 DC=vmin
vwwl wwl 0 DC=vmin
vwbl wbl 0 DC=vmax
vwblb wblb 0 DC=vmax
vrwl rwl 0 DC=vmax
vrbl rbl 0 DC=vmax
vn2 n2 0 DC=vin

.END