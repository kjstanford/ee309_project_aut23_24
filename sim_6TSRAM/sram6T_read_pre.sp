** header **
.INCLUDE "../compact_model/cfet_2nm_model.pm"
.PARAM vmax = @vmax@ 
.PARAM vmin = @vmin@ 
.PARAM vin = @vin@
.PARAM step = @step@
.PARAM sim_time = @sim_time@
.PARAM wl_pw = @wl_pw@
.PARAM wl_del = @wl_del@
.PARAM rise = @rise@
.PARAM fall = @fall@
.PARAM tp = @tp@
.PARAM bl_cap = @bl_cap@ 

.PROBE TRAN
+ V(wl)
+ V(bl)
+ V(blb)
+ V(n1)
+ V(n2)

.PRINT TRAN
+ V(wl)
+ V(bl)
+ V(blb)
+ V(n1)
+ V(n2)

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

mpg1 bl wl n1 vss nmos_beol nfin=1
* mpg1 bl wl n1 vss nmos_sram nfin=2
mpu1 n1 n2 vdd vdd pmos_sram nfin=2
mpd1 n1 n2 vss vss nmos_sram nfin=2
mpg2 blb wl n2 vss nmos_beol nfin=1
* mpg2 blb wl n2 vss nmos_sram nfin=2
mpu2 n2 n1 vdd vdd pmos_sram nfin=2
mpd2 n2 n1 vss vss nmos_sram nfin=2
vsuph vdd 0 DC='vmax'
vsupl vss 0 DC='vmin'
vwl wl 0 PULSE 'vmin' 'vmax' 'wl_del' 'rise' 'fall' 'wl_pw' 'tp'
cbl bl 0 'bl_cap'
cblb blb 0 'bl_cap'

.END