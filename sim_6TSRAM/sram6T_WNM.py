import sys
sys.path.insert(0, '../')
from funs import *

lis_n2 = read_lis_general('n2.lis')
lis_n1 = read_lis_general('n1.lis')

n1_n2 = lis_n2[:,1]
n2_n2 = lis_n2[:,2]
n1_n1 = lis_n1[:,1]
n2_n1 = lis_n1[:,2]

wnm = 0.7
for i in range(len(n2_n1)-1, -1, -1):
    diff = n2_n1[i] - n1_n1[i]
    # print(diff)
    for j in range(1, len(n2_n2)):
        if (n2_n2[j] - n1_n2[j] >= diff) and (n2_n2[j-1] - n1_n2[j-1] <= diff):
            # print(n2_n2[j] - n1_n2[j])
            if diff > 0:
                wnm= min(wnm, abs(n2_n2[j]-n2_n1[i]))
                # print(n2_n2[j], n2_n1[i], abs(n2_n2[j]-n2_n1[i]))
            break
print(wnm)

lin_plot(x=[n2_n1, n2_n2], y=[n1_n1, n1_n2], c=['r', 'b'], s=['solid'], xlabel="$V_{N2} (V)$", ylabel="$V_{N1} (V)$", figname='temp.png', lw=4.5)

# np.savetxt('WNM_beol_w72_nf2_pg.csv', np.transpose(np.array([n2_n1, n2_n2, n1_n1, n1_n2])))