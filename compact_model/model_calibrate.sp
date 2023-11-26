** header **
.INCLUDE "tcad_calibrated_model.pm"
.PARAM vgmin=-0.5 vgmax=1.5 vdpar0=0.01 vdpar1=0.7 vgate=0

.DC vgate LIN 100.0 vgmin vgmax

.TEMP 25.0
.OPTION
+    ARTIST=2
+    INGOLD=2
+    PARHIER=LOCAL
+    PSF=2

vg g 0 DC=vgate
mm0 d0 g 0 0 nmos_sram w=100e-9 l=20e-9 nfin=2
vd0 d0 0 DC=vdpar0
mm1 d1 g 0 0 nmos_sram w=100e-9 l=20e-9 nfin=2
vd1 d1 0 DC=vdpar1

.END


