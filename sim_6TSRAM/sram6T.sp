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

mpg1 bl wl n1 vss nmos_sram w=27e-9 l=20e-9 nfin=1
mpu1 n1 n2 vdd vdd pmos_sram w=27e-9 l=20e-9 nfin=1
mpd1 n1 n2 vss vss nmos_sram w=27e-9 l=20e-9 nfin=1
mpg2 blb wl n2 vss nmos_sram w=27e-9 l=20e-9 nfin=1
mpu2 n2 n1 vdd vdd pmos_sram w=27e-9 l=20e-9 nfin=1
mpd2 n2 n1 vss vss nmos_sram w=27e-9 l=20e-9 nfin=1
vsuph vdd 0 DC=vmax
vsupl vss 0 DC=vmin
vwl wl 0 DC=vmax
vbl bl 0 DC=vmax
vblb blb 0 DC=vmax
vn2 n2 0 DC=vin

.END