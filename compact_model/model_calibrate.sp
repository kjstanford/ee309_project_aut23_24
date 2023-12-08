** header **
.INCLUDE "cfet_2nm_model.pm"
* .INCLUDE "7nm_TT_160803.pm"
.PARAM vgmin=-0.5 vgmax=1.5 vdpar0=0.01 vdpar1=0.7 vgate=0

.PROBE DC
+ I(vd0)
+ I(vd1)

.PRINT DC
+ I(vd0)
+ I(vd1)

.DC vgate LIN 100.0 vgmin vgmax

.TEMP 25.0
.OPTION
+    ARTIST=2
+    INGOLD=2
+    PARHIER=LOCAL
+    PSF=2

vg g 0 DC=vgate
mm0 d0 g 0 nmos_sram l=21e-9 nfin=1
vd0 d0 0 DC=vdpar0
mm1 d1 g 0 nmos_sram l=21e-9 nfin=1
vd1 d1 0 DC=vdpar1

.END


