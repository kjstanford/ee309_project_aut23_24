** header **
.INCLUDE "../compact_model/cfet_2nm_model.pm"
.PARAM vmax = 0.7
.PARAM vmin = 0
.PARAM vin = 0
.PARAM step = 1e-12
.PARAM sim_time = 5e-09
.PARAM wl_pw = 1e-10
.PARAM wl_del = 5e-10
.PARAM rise = 1e-10
.PARAM fall = 1e-10
.PARAM tp = 5e-09
.PARAM bl_cap = 2.5e-13

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
+ ARTIST=2
+ INGOLD=2
+ PARHIER=LOCAL
+ PSF=2

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