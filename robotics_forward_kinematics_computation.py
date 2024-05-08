## 정기구학

import numpy as np
import matplotlib.pyplot as plt

## 정기구학 계산 코드
# 1. 링크 길이와 Twist된 각도 기입
# i=1
alpha_0 = 0
a_0 = 0
d_1 = 0
theta_1  = 0

# i=2
alpha_1 = 0
a_1 = 0
d_2 = 0
theta_2  = 0

# i=3
alpha_2 = 0
a_2 = 0
d_3 = 0
theta_3  = 0

# i=4
alpha_3 = 0
a_3 = 0
d_4 = 0
theta_4  = 0

# i=5
alpha_4 = 0
a_4 = 0
d_5 = 0
theta_5  = 0

# 2. DH 파라미터를 이용하여 정기구학 matrix 계산
t_01 = np.array([
    [np.cos(theta_1), -np.sin(theta_1), 0, a_0],
    [np.sin(theta_1) * np.cos(alpha_0), np.cos(theta_1) * np.cos(alpha_0), -np.sin(alpha_0), -np.sin(alpha_0) * d_1],
    [np.sin(theta_1) * np.sin(alpha_0), np.cos(theta_1) * np.sin(alpha_0), np.cos(alpha_0),np.cos(alpha_0) * d_1],
    [0,0,0,1]
])

t_12 = np.array([
    [np.cos(theta_2), -np.sin(theta_2), 0, a_1],
    [np.sin(theta_2) * np.cos(alpha_1), np.cos(theta_2) * np.cos(alpha_1), -np.sin(alpha_1), -np.sin(alpha_1) * d_2],
    [np.sin(theta_2) * np.sin(alpha_1), np.cos(theta_2) * np.sin(alpha_1), np.cos(alpha_1),np.cos(alpha_1) * d_2],
    [0,0,0,1]
])

t_23 = np.array([
    [np.cos(theta_3), -np.sin(theta_3), 0, a_2],
    [np.sin(theta_3) * np.cos(alpha_2), np.cos(theta_3) * np.cos(alpha_2), -np.sin(alpha_2), -np.sin(alpha_2) * d_3],
    [np.sin(theta_3) * np.sin(alpha_2), np.cos(theta_3) * np.sin(alpha_2), np.cos(alpha_2),np.cos(alpha_2) * d_3],
    [0,0,0,1]
])

t_34 = np.array([
    [np.cos(theta_4), -np.sin(theta_4), 0, a_3],
    [np.sin(theta_4) * np.cos(alpha_3), np.cos(theta_4) * np.cos(alpha_3), -np.sin(alpha_3), -np.sin(alpha_3) * d_4],
    [np.sin(theta_3) * np.sin(alpha_2), np.cos(theta_4) * np.sin(alpha_3), np.cos(alpha_3),np.cos(alpha_3) * d_4],
    [0,0,0,1]
])

t_45 = np.array([
    [np.cos(theta_5), -np.sin(theta_5), 0, a_4],
    [np.sin(theta_5) * np.cos(alpha_4), np.cos(theta_5) * np.cos(alpha_4), -np.sin(alpha_4), -np.sin(alpha_4) * d_5],
    [np.sin(theta_4) * np.sin(alpha_3), np.cos(theta_5) * np.sin(alpha_4), np.cos(alpha_4),np.cos(alpha_4) * d_5],
    [0,0,0,1]
])

# 3. 행렬곱
t_05 = t_01 @ t_12 @ t_23 @ t_34 @ t_45

# 역기구학

# 필요한 라이브러리 

import numpy as np
import matplotlib.pyplot as plt

# 정사영 했을 때의 1번 모터에서 End effector 까지의 거리 설정
xc = 0.0
yc = 0.0
phi = 0.0
# theta 1 설정
theta1 = np.arctan2(yc / xc)
r = np.sqrt(xc ** 2 + yc ** 2)
A2 = np.arccos(a_3 ** 2 - a_4 ** 2 + r ** 2) / (a_3 ** 2 * r)
theta2_1 = theta_1 + A2
theta2_2 = theta_1 - A2
theta3 = np.arccos(a_3 ** 2 + a_4 ** 2 + r ** 2) / (a_3 ** 2 * a_4)
theta_4_1 = phi - theta2_1 - theta3
theta_4_2 = phi - theta2_2 - theta3