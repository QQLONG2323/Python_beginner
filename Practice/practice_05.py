'''HomeWork
利用2層迴圈列印「井」字，將其排列成直角三角形

顯示:
#
##
###
####
#####'''


for i in range(1, 6):
    for j in range(i):
        i = "#"
        print('#', end="")
    print()