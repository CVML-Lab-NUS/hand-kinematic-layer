import numpy as np
import torch
ANGLETYPE=0

boneLenStd=torch.tensor([ 0.0000, 50.6858, 17.4128, 19.0476, 49.1769, 22.6516, 21.1011, 49.2413,
        25.6330, 13.1088, 47.6088, 18.6265, 16.1167, 22.6208, 16.0547, 22.1285,
        31.6857, 22.6970, 25.6609, 30.5429, 18.8797],dtype=torch.float32)/1000
boneLenMean=torch.tensor([  0.0000, 109.6933,  39.7755,  31.5339, 108.4382,  40.1482,  33.6498,
         97.9310,  38.1820,  20.9875, 103.0075,  34.7108,  31.1847,  45.9793,
         45.2308,  39.3103,  33.7517,  31.1771,  34.5877,  34.9935,  25.2674],dtype=torch.float32)/1000



if ANGLETYPE==0:
    # csc defined
    abangle=torch.tensor([ 0.0000, 20,  0.0000,  0.0000, 20,  0.0000,  0.0000, 20,
             0.0000,  0.0000, 20,  0.0000,  0.0000, 20,  0.0000,  0.0000,
             0.0000,  0.0000,  0.0000,  0.0000,  0.0000],dtype=torch.float32)/180*3.14
    twangle=torch.tensor([ 0.0000, 20,  0.0000,  0.0000, 20,  0.0000,  0.0000, 20,
             0.0000,  0.0000, 20,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,
             0.0000,  0.0000,  0.0000,  0.0000,  0.0000],dtype=torch.float32)/180*3.14
    flexangle=torch.tensor([  0.0000,  90,  135,  90,  90,  135,  90,
             90,  135,  90,  90,  135,  90,  45,  45,  90,
             0.0000,   0.0000,   0.0000,   0.0000,   0.0000],dtype=torch.float32)/180*3.14
    extenangle=torch.tensor([ 0.0000, 45,  10, 45,  45,  10, 45,
             45,  10, 45,  45,  10, 45, 45,  10, 45,
             0.0000,  0.0000,  0.0000,  0.0000],dtype=torch.float32)/180*3.14
elif ANGLETYPE==1:
    #max RHD
    abangle=torch.tensor([ 0.0000, 35.0805,  0.0000,  0.0000, 60.6750,  0.0000,  0.0000, 87.7954,
             0.0000,  0.0000, 71.2308,  0.0000,  0.0000, 33.6927,  0.0000,  0.0000,
             0.0000,  0.0000,  0.0000,  0.0000,  0.0000],dtype=torch.float32)/180*3.14
    twangle=torch.tensor([ 0.0000, 25.7945,  0.0000,  0.0000, 20.2052,  0.0000,  0.0000, 62.3652,
             0.0000,  0.0000, 52.1062,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,
             0.0000,  0.0000,  0.0000,  0.0000,  0.0000],dtype=torch.float32)/180*3.14
    flexangle=torch.tensor([  0.0000,  77.3628,  95.0576,  53.4902,  87.3540, 107.9342,  70.9354,
             90.1866, 113.4716,  74.6294,  93.6878, 111.6966,  72.2735,  56.4854,
             45.1618,  50.9132,   0.0000,   0.0000,   0.0000,   0.0000,   0.0000],dtype=torch.float32)/180*3.14
    extenangle=torch.tensor([ 0.0000, 44.2844,  5.6530, 18.1857, 23.7940,  0.0000,  8.6077, 26.9244,
             1.7827, 12.6639, 13.7637,  1.0398, 14.8350, 56.5105, 52.9489, 47.0765,
             0.0000,  0.0000,  0.0000,  0.0000,  0.0000],dtype=torch.float32)/180*3.14

else:
    #95 percentage RHD
    abangle=torch.tensor([ 0.0000, 26.4607,  0.0000,  0.0000, 21.6089,  0.0000,  0.0000, 53.9532,
             0.0000,  0.0000, 37.8925,  0.0000,  0.0000, 20.4506,  0.0000,  0.0000,
             0.0000,  0.0000,  0.0000,  0.0000,  0.0000], dtype=torch.float32)/180*3.14
    twangle=torch.tensor([ 0.0000, 16.7597,  0.0000,  0.0000, 13.9880,  0.0000,  0.0000, 33.7476,
             0.0000,  0.0000, 28.6342,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,
             0.0000,  0.0000,  0.0000,  0.0000,  0.0000], dtype=torch.float32)/180*3.14
    flexangle=torch.tensor([  0.0000,  60.7270,  93.8734,  52.4785,  72.2847, 107.4027,  66.2667,
             80.4936, 101.7120,  56.5170,  83.6248, 109.4197,  57.7303,  37.7303,
             47.1699,  34.8366,   0.0000,   0.0000,   0.0000,   0.0000,   0.0000], dtype=torch.float32)/180*3.14
    extenangle=torch.tensor([ 0.0000, 23.0607,  0.0000,  7.0390,  8.4027,  0.0000,  7.6596, 21.3979,
             0.0000,  9.1255,  7.1636,  0.0000,  5.7255, 15.5698,  0.0000, 22.7461,
             0.0000,  0.0000,  0.0000,  0.0000,  0.0000], dtype=torch.float32)/180*3.14





#
# ab tensor([ 0.0000, 10.3747,  0.0000,  0.0000,  7.4522,  0.0000,  0.0000, 18.6771,
#          0.0000,  0.0000, 18.4159,  0.0000,  0.0000, 17.7332,  0.0000,  0.0000,
#          0.0000,  0.0000,  0.0000,  0.0000,  0.0000], dtype=torch.float64)
# tw tensor([ 0.0000,  7.5552,  0.0000,  0.0000,  6.0704,  0.0000,  0.0000, 21.1145,
#          0.0000,  0.0000, 20.6143,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,
#          0.0000,  0.0000,  0.0000,  0.0000,  0.0000], dtype=torch.float64)
# flex tensor([ 0.0000, 40.9305, 62.2646, 21.5024, 59.5141, 83.7460, 22.0839, 65.0673,
#         87.9579, 28.7561, 66.7906, 88.6292, 32.0943, 19.9002, 29.1260,  0.0000,
#          0.0000,  0.0000,  0.0000,  0.0000,  0.0000], dtype=torch.float64)
# exten tensor([ 0.0000,  0.0000,  0.0000,  2.2435,  0.0000,  0.0000,  2.0022,  0.0000,
#          0.0000,  0.0000,  0.0000,  0.0000,  0.0000, 12.4902, 28.6398, 27.3414,
#          0.0000,  0.0000,  0.0000,  0.0000,  0.0000], dtype=torch.float64)
# ab tensor([  0.0000, 100.3336,   0.0000,   0.0000,  81.9984,   0.0000,   0.0000,
#          87.9137,   0.0000,   0.0000,  98.1341,   0.0000,   0.0000,  45.5575,
#           0.0000,   0.0000,   0.0000,   0.0000,   0.0000,   0.0000,   0.0000])
# tw tensor([ 0.0000, 29.7038,  0.0000,  0.0000, 18.2680,  0.0000,  0.0000, 37.8632,
#          0.0000,  0.0000, 30.9854,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,
#          0.0000,  0.0000,  0.0000,  0.0000,  0.0000])
# flex tensor([  0.0000, 104.8372, 124.3543, 110.0020, 113.8009, 120.8249, 104.9325,
#         106.3094, 128.8968, 122.6169, 108.7011, 127.3922, 106.8787,  59.7003,
#          60.8770,  72.1011,   0.0000,   0.0000,   0.0000,   0.0000,   0.0000])
# exten tensor([ 0.0000, 49.8888,  5.4216, 38.2556, 47.3101,  0.0000, 24.9287, 43.2074,
#          2.7869, 28.7151, 30.6741,  5.5705, 21.2961, 58.7087, 60.2271, 72.1236,
#          0.0000,  0.0000,  0.0000,  0.0000,  0.0000])






