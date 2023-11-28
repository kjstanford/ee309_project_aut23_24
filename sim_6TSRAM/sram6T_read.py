import sys
sys.path.insert(0, '../')
from funs import *

sys('hspice sram6T_Ncurve.sp -o s1')
lis_M = read_lis_general('s1.lis')