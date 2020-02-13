# import math
# import numpy as np
# import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False


def calc(T):
    for i in range(0, len(T) - 1):
        S.append(S[i] - r * b * S[i] * I[i] / N)
        E.append(E[i] + r * b * S[i] * I[i] / N - a * E[i])
        I.append(I[i] + a * E[i] - y * I[i])
        R.append(R[i] + y * I[i])


def plot(T, S, E, I, R):
    plt.figure()
    plt.title("SEIR-病毒传播时间曲线")
    plt.plot(T, S, color='r', label='易感者')
    plt.plot(T, E, color='k', label='潜伏者')
    plt.plot(T, I, color='b', label='传染者')
    plt.plot(T, R, color='g', label='康复者')
    plt.grid(False)
    plt.legend()
    plt.xlabel("时间(天)")
    plt.ylabel("人数")
    plt.show()


if __name__ == '__main__':
    # 首先还是设置一下参数,之后方便修改
    N = 130000000  # 人口总数
    E = []  # 潜伏携带者
    E.append(0)

    I = []  # 传染者
    I.append(1)

    S = []  # 易感者
    S.append(N - I[0])

    R = []  # 康复者
    R.append(0)

    r = 20  # 传染者接触人数
    b = 0.03  # 传染者传染概率
    a = 0.1  # 潜伏者患病概率
    y = 0.1  # 康复概率

    T = [i for i in range(0, 360)]  # 时间
    calc(T)
    plot(T, S, E, I, R)
