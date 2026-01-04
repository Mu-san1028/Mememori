import numpy as np
from scipy.integrate import dblquad

# キャラのスピード値と確率密度を定義
speed1 = 2839
speed2 = 2783

f1_density = 1 / (speed1 * 0.05)  # キャラ1の確率密度
f2_density = 1 / (speed2 * 0.05)  # キャラ2の確率密度

# キャラのスピード範囲
x_min, x_max = speed1 * 0.975, speed1 * 1.025
y_min, y_max = speed2 * 0.975, speed2 * 1.025

# f1(x) * f2(y) を計算する
def joint_density(x, y):
    if x > y:  # キャラ1がキャラ2より遅い場合
        return f1_density * f2_density
    return 0

# 二重積分の計算
p_slower = dblquad(joint_density, x_min, x_max, lambda x: y_min, lambda x: min(x, y_max))
print(f"キャラ1がキャラ2より遅く動く確率: {p_slower[0] * 100:.2f}%")