__author__ = 'stathis'

H=[[0,10], [1,5], [2,7],
   [3,6],[4,5],[5,2],[6,3],
   [7,5],[8,4],[9,1]]

H.sort(key=lambda x: x[1],reverse=True)

H_robbed = []
H_robbed_money_l = []
H_total_money_l = []

for i in H:
    H_total_money_l.append(i[1])
    append_flag = True
    for j in H_robbed:
        if i[0] == j+1 or i[0] == j-1 or i[0] == j :
            append_flag = False
            break
    if append_flag :
        H_robbed.append(i[0])
        H_robbed_money_l.append(i[1])
    print("houses robbed:",H_robbed)

print("sum of money robbed :",sum(H_robbed_money_l), "out of",sum(H_total_money_l))
