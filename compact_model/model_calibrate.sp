** header **
.INCLUDE "cfet_2nm_model.pm"
* .INCLUDE "7nm_TT_160803.pm"
.PARAM vgmin=0.0 vgmax=0.7 vdpar0=0.01 vdpar1=0.7 vgate=0

.PROBE DC
+ I(vd0)
+ I(vd1)
+ I(vdp0)
+ I(vdp1)

.PRINT DC
+ I(vd0)
+ I(vd1)
+ I(vdp0)
+ I(vdp1)

.DC vgate LIN 100.0 vgmin vgmax

.TEMP 25.0
.OPTION
+    ARTIST=2
+    INGOLD=2
+    PARHIER=LOCAL
+    PSF=2

vg g 0 DC=vgate
vgp gp 0 DC='-1*vgate'
mn0 d0 g 0 nmos_sram nfin=2
vd0 d0 0 DC=vdpar0
mn1 d1 g 0 nmos_sram nfin=2
vd1 d1 0 DC=vdpar1
mp0 dp0 gp 0 pmos_sram nfin=2
vdp0 dp0 0 DC='-1*vdpar0'
mp1 dp1 gp 0 pmos_sram nfin=2
vdp1 dp1 0 DC='-1*vdpar1'

.END


