from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def test1():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make the grid
    x, y, z = np.meshgrid(np.array([1]),
                          np.array([1]),
                          np.array([1]))
    print(x)
    print(y)
    print(z)
    # Make the direction data for the arrows
    u = np.array([1, 2, 3])
    v = np.array([4, 5, 6])
    w = np.array([0, 0, 1])

    # ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
    plt.subplot(2, 1, 1)

    # （X，Y，Z，U，V，W，** kwargs）
    #
    # 参数：
    #
    # X，Y，Z：箭头位置的x，y和z坐标
    #
    # U，V，W：箭头vector的x，y和z分量
    #
    # 参数可以是数组或标量。
    #
    # 关键字参数：
    #
    # 长度： [1.0 | float]每个颤抖的长度，默认为1.0，单位与坐标轴相同
    #
    # arrow_length_ratio： [0.3 | float]箭头相对于箭袋的比率，默认为0.3
    #
    # pivot： ['tail'| '中间'| 'tip']在网格点的箭头部分; 箭头围绕这个点旋转，因此名称枢轴。 默认是“尾巴”
    #
    # 正常化： [False | 真]当为真，所有的箭头将是相同的长度。 默认为False，箭头的长度取决于u，v，w的值。
    ax.quiver(0, 0, 0, 1, 2, 3, length=1, normalize=True)
    plt.subplot(2, 1, 2)
    ax.quiver(0, 0, 0, 4, 5, 6, length=1, normalize=True)

    plt.show()



def test2():
    fig = plt.figure(figsize=plt.figaspect(0.5))
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax.quiver(1, 1, 1, 1, 2, 3, length=1, normalize=True)
    # ax = fig.add_subplot(1, 2, 2, projection='3d')
    ax.quiver(1, 1, 1, 4, 5, 6, length=1, normalize=True)
    plt.show()

# test2()
#{"code":"00000000","message":"成功","data":{"updateDate":"2018-07-26 14:02:59","status":2,
# "datas":["{\"date\":\"2018-07-26 14:02:16\",\"data\":{\"date\":[\"2017-01-13 22:30:00\",\"2017-01-16 22:30:00\",\"2017-01-17 22:30:00\",\"2017-01-18 22:30:00\",\"2017-01-19 22:30:00\",\"2017-01-20 22:30:00\",\"2017-01-23 22:30:00\",\"2017-01-24 22:30:00\",\"2017-01-25 22:30:00\",\"2017-01-26 22:30:00\",\"2017-01-27 22:30:00\",\"2017-01-30 22:30:00\",\"2017-01-31 22:30:00\",\"2017-02-01 22:30:00\",\"2017-02-02 22:30:00\",\"2017-02-03 22:30:00\",\"2017-02-06 22:30:00\",\"2017-02-07 22:30:00\",\"2017-02-08 22:30:00\",\"2017-02-09 22:30:00\",\"2017-02-10 22:30:00\",\"2017-02-13 22:30:00\",\"2017-02-14 22:30:00\",\"2017-02-15 22:30:00\",\"2017-02-16 22:30:00\",\"2017-02-17 22:30:00\",\"2017-02-20 22:30:00\",\"2017-02-21 22:30:00\",\"2017-02-22 22:30:00\",\"2017-02-23 22:30:00\",\"2017-02-24 22:30:00\",\"2017-02-27 22:30:00\",\"2017-02-28 22:30:00\",\"2017-03-01 22:30:00\",\"2017-03-02 22:30:00\",\"2017-03-03 22:30:00\",\"2017-03-06 22:30:00\",\"2017-03-07 22:30:00\",\"2017-03-08 22:30:00\",\"2017-03-09 22:30:00\",\"2017-03-10 22:30:00\",\"2017-03-13 21:30:00\",\"2017-03-14 21:30:00\",\"2017-03-15 21:30:00\",\"2017-03-16 21:30:00\",\"2017-03-17 21:30:00\",\"2017-03-20 21:30:00\",\"2017-03-21 21:30:00\",\"2017-03-22 21:30:00\",\"2017-03-23 21:30:00\",\"2017-03-24 21:30:00\",\"2017-03-27 21:30:00\",\"2017-03-28 21:30:00\",\"2017-03-29 21:30:00\",\"2017-03-30 21:30:00\",\"2017-03-31 21:30:00\",\"2017-04-03 21:30:00\",\"2017-04-04 21:30:00\",\"2017-04-05 21:30:00\",\"2017-04-06 21:30:00\",\"2017-04-07 21:30:00\",\"2017-04-10 21:30:00\",\"2017-04-11 21:30:00\",\"2017-04-12 21:30:00\",\"2017-04-13 21:30:00\",\"2017-04-14 21:30:00\",\"2017-04-17 21:30:00\",\"2017-04-18 21:30:00\",\"2017-04-19 21:30:00\",\"2017-04-20 21:30:00\",\"2017-04-21 21:30:00\",\"2017-04-24 21:30:00\",\"2017-04-25 21:30:00\",\"2017-04-26 21:30:00\",\"2017-04-27 21:30:00\",\"2017-04-28 21:30:00\",\"2017-05-01 21:30:00\",\"2017-05-02 21:30:00\",\"2017-05-03 21:30:00\",\"2017-05-04 21:30:00\",\"2017-05-05 21:30:00\",\"2017-05-08 21:30:00\",\"2017-05-09 21:30:00\",\"2017-05-10 21:30:00\",\"2017-05-11 21:30:00\",\"2017-05-12 21:30:00\",\"2017-05-15 21:30:00\",\"2017-05-16 21:30:00\",\"2017-05-17 21:30:00\",\"2017-05-18 21:30:00\",\"2017-05-19 21:30:00\",\"2017-05-22 21:30:00\",\"2017-05-23 21:30:00\",\"2017-05-24 21:30:00\",\"2017-05-25 21:30:00\",\"2017-05-26 21:30:00\",\"2017-05-29 21:30:00\",\"2017-05-30 21:30:00\",\"2017-05-31 21:30:00\",\"2017-06-01 21:30:00\",\"2017-06-02 21:30:00\",\"2017-06-05 21:30:00\",\"2017-06-06 21:30:00\",\"2017-06-07 21:30:00\",\"2017-06-08 21:30:00\",\"2017-06-09 21:30:00\",\"2017-06-12 21:30:00\",\"2017-06-13 21:30:00\",\"2017-06-14 21:30:00\",\"2017-06-15 21:30:00\",\"2017-06-16 21:30:00\",\"2017-06-19 21:30:00\",\"2017-06-20 21:30:00\",\"2017-06-21 21:30:00\",\"2017-06-22 21:30:00\",\"2017-06-23 21:30:00\",\"2017-06-26 21:30:00\",\"2017-06-27 21:30:00\",\"2017-06-28 21:30:00\",\"2017-06-29 21:30:00\",\"2017-06-30 21:30:00\",\"2017-07-03 21:30:00\",\"2017-07-04 21:30:00\",\"2017-07-05 21:30:00\",\"2017-07-06 21:30:00\",\"2017-07-07 21:30:00\",\"2017-07-10 21:30:00\",\"2017-07-11 21:30:00\",\"2017-07-12 21:30:00\",\"2017-07-13 21:30:00\",\"2017-07-14 21:30:00\",\"2017-07-17 21:30:00\",\"2017-07-18 21:30:00\",\"2017-07-19 21:30:00\",\"2017-07-20 21:30:00\",\"2017-07-21 21:30:00\",\"2017-07-24 21:30:00\",\"2017-07-25 21:30:00\",\"2017-07-26 21:30:00\",\"2017-07-27 21:30:00\",\"2017-07-28 21:30:00\",\"2017-07-31 21:30:00\",\"2017-08-01 21:30:00\",\"2017-08-02 21:30:00\",\"2017-08-03 21:30:00\",\"2017-08-04 21:30:00\",\"2017-08-07 21:30:00\",\"2017-08-08 21:30:00\",\"2017-08-09 21:30:00\",\"2017-08-10 21:30:00\",\"2017-08-11 21:30:00\",\"2017-08-14 21:30:00\",\"2017-08-15 21:30:00\",\"2017-08-16 21:30:00\",\"2017-08-17 21:30:00\",\"2017-08-18 21:30:00\",\"2017-08-21 21:30:00\",\"2017-08-22 21:30:00\",\"2017-08-23 21:30:00\",\"2017-08-24 21:30:00\",\"2017-08-25 21:30:00\",\"2017-08-28 21:30:00\",\"2017-08-29 21:30:00\",\"2017-08-30 21:30:00\",\"2017-08-31 21:30:00\",\"2017-09-01 21:30:00\",\"2017-09-04 21:30:00\",\"2017-09-05 21:30:00\",\"2017-09-06 21:30:00\",\"2017-09-07 21:30:00\",\"2017-09-08 21:30:00\",\"2017-09-11 21:30:00\",\"2017-09-12 21:30:00\",\"2017-09-13 21:30:00\",\"2017-09-14 21:30:00\",\"2017-09-15 21:30:00\",\"2017-09-18 21:30:00\",\"2017-09-19 21:30:00\",\"2017-09-20 21:30:00\",\"2017-09-21 21:30:00\",\"2017-09-22 21:30:00\",\"2017-09-25 21:30:00\",\"2017-09-26 21:30:00\",\"2017-09-27 21:30:00\",\"2017-09-28 21:30:00\",\"2017-09-29 21:30:00\",\"2017-10-02 21:30:00\",\"2017-10-03 21:30:00\",\"2017-10-04 21:30:00\",\"2017-10-05 21:30:00\",\"2017-10-06 21:30:00\",\"2017-10-09 21:30:00\",\"2017-10-10 21:30:00\",\"2017-10-11 21:30:00\",\"2017-10-12 21:30:00\",\"2017-10-13 21:30:00\",\"2017-10-16 21:30:00\",\"2017-10-17 21:30:00\",\"2017-10-18 21:30:00\",\"2017-10-19 21:30:00\",\"2017-10-20 21:30:00\",\"2017-10-23 21:30:00\",\"2017-10-24 21:30:00\",\"2017-10-25 21:30:00\",\"2017-10-26 21:30:00\",\"2017-10-27 21:30:00\",\"2017-10-30 21:30:00\",\"2017-10-31 21:30:00\",\"2017-11-01 21:30:00\",\"2017-11-02 21:30:00\",\"2017-11-03 21:30:00\",\"2017-11-06 22:30:00\",\"2017-11-07 22:30:00\",\"2017-11-08 22:30:00\",\"2017-11-09 22:30:00\",\"2017-11-10 22:30:00\",\"2017-11-13 22:30:00\",\"2017-11-14 22:30:00\",\"2017-11-15 22:30:00\",\"2017-11-16 22:30:00\",\"2017-11-17 22:30:00\",\"2017-11-20 22:30:00\",\"2017-11-21 22:30:00\",\"2017-11-22 22:30:00\",\"2017-11-23 22:30:00\",\"2017-11-24 22:30:00\",\"2017-11-27 22:30:00\",\"2017-11-28 22:30:00\",\"2017-11-29 22:30:00\",\"2017-11-30 22:30:00\",\"2017-12-01 22:30:00\",\"2017-12-04 22:30:00\",\"2017-12-05 22:30:00\",\"2017-12-06 22:30:00\",\"2017-12-07 22:30:00\",\"2017-12-08 22:30:00\",\"2017-12-11 22:30:00\",\"2017-12-12 22:30:00\",\"2017-12-13 22:30:00\",\"2017-12-14 22:30:00\",\"2017-12-15 22:30:00\",\"2017-12-18 22:30:00\",\"2017-12-19 22:30:00\",\"2017-12-20 22:30:00\",\"2017-12-21 22:30:00\",\"2017-12-22 22:30:00\",\"2017-12-25 22:30:00\",\"2017-12-26 22:30:00\",\"2017-12-27 22:30:00\",\"2017-12-28 22:30:00\",\"2017-12-29 22:30:00\",\"2018-01-01 22:30:00\",\"2018-01-02 22:30:00\",\"2018-01-03 22:30:00\",\"2018-01-04 22:30:00\",\"2018-01-05 22:30:00\",\"2018-01-08 22:30:00\",\"2018-01-09 22:30:00\",\"2018-01-10 22:30:00\",\"2018-01-11 22:30:00\",\"2018-01-12 22:30:00\",\"2018-01-15 22:30:00\",\"2018-01-16 22:30:00\",\"2018-01-17 22:30:00\",\"2018-01-18 22:30:00\",\"2018-01-19 22:30:00\",\"2018-01-22 22:30:00\",\"2018-01-23 22:30:00\",\"2018-01-24 22:30:00\",\"2018-01-25 22:30:00\",\"2018-01-26 22:30:00\",\"2018-01-29 22:30:00\",\"2018-01-30 22:30:00\",\"2018-01-31 22:30:00\",\"2018-02-01 22:30:00\",\"2018-02-02 22:30:00\",\"2018-02-05 22:30:00\",\"2018-02-06 22:30:00\",\"2018-02-07 22:30:00\",\"2018-02-08 22:30:00\",\"2018-02-09 22:30:00\",\"2018-02-12 22:30:00\",\"2018-02-13 22:30:00\",\"2018-02-14 22:30:00\",\"2018-02-15 22:30:00\",\"2018-02-16 22:30:00\",\"2018-02-19 22:30:00\",\"2018-02-20 22:30:00\",\"2018-02-21 22:30:00\",\"2018-02-22 22:30:00\",\"2018-02-23 22:30:00\",\"2018-02-26 22:30:00\",\"2018-02-27 22:30:00\",\"2018-02-28 22:30:00\",\"2018-03-01 22:30:00\",\"2018-03-02 22:30:00\",\"2018-03-05 22:30:00\",\"2018-03-06 22:30:00\",\"2018-03-07 22:30:00\",\"2018-03-08 22:30:00\",\"2018-03-09 22:30:00\",\"2018-03-12 21:30:00\",\"2018-03-13 21:30:00\",\"2018-03-14 21:30:00\",\"2018-03-15 21:30:00\",\"2018-03-16 21:30:00\",\"2018-03-19 08:00:00\",\"2018-03-19 21:00:00\",\"2018-03-20 08:00:00\",\"2018-03-21 21:30:00\",\"2018-03-22 21:30:00\",\"2018-03-23 21:30:00\",\"2018-03-26 21:30:00\",\"2018-03-27 21:30:00\",\"2018-03-28 21:30:00\",\"2018-03-29 21:30:00\",\"2018-03-30 21:30:00\",\"2018-04-02 21:30:00\",\"2018-04-03 21:30:00\",\"2018-04-04 21:30:00\",\"2018-04-05 21:00:00\",\"2018-04-06 21:30:00\",\"2018-04-09 21:30:00\",\"2018-04-10 21:30:00\",\"2018-04-11 21:30:00\",\"2018-04-12 21:30:00\",\"2018-04-13 21:30:00\",\"2018-04-16 21:30:00\",\"2018-04-17 21:30:00\",\"2018-04-18 21:30:00\",\"2018-04-19 21:30:00\",\"2018-04-20 21:30:00\",\"2018-04-23 21:30:00\",\"2018-04-24 21:30:00\",\"2018-04-25 21:30:00\",\"2018-04-26 21:30:00\",\"2018-04-27 21:30:00\",\"2018-04-30 21:30:00\",\"2018-05-01 21:30:00\",\"2018-05-02 21:30:00\",\"2018-05-03 21:30:00\",\"2018-05-04 21:30:00\",\"2018-05-07 21:30:00\",\"2018-05-08 21:30:00\",\"2018-05-09 21:30:00\",\"2018-05-10 21:30:00\",\"2018-05-11 21:30:00\",\"2018-05-14 21:30:00\",\"2018-05-15 21:30:00\",\"2018-05-16 21:30:00\",\"2018-05-17 21:30:00\",\"2018-05-18 21:30:00\",\"2018-05-21 21:30:00\",\"2018-05-22 21:30:00\",\"2018-05-23 21:30:00\",\"2018-05-24 21:30:00\",\"2018-05-25 21:30:00\",\"2018-05-28 21:30:00\",\"2018-05-29 21:30:00\",\"2018-05-30 21:30:00\",\"2018-05-31 21:30:00\",\"2018-06-01 21:30:00\",\"2018-06-04 21:30:00\",\"2018-06-05 21:30:00\",\"2018-06-06 21:30:00\",\"2018-06-07 21:30:00\",\"2018-06-08 21:30:00\",\"2018-06-11 21:30:00\",\"2018-06-12 21:30:00\",\"2018-06-13 21:30:00\",\"2018-06-14 21:30:00\",\"2018-06-15 21:30:00\",\"2018-06-18 21:30:00\",\"2018-06-19 21:30:00\",\"2018-06-20 21:30:00\",\"2018-06-21 21:30:00\",\"2018-06-22 21:30:00\",\"2018-06-25 21:30:00\",\"2018-06-26 21:30:00\",\"2018-06-27 21:30:00\",\"2018-06-28 21:30:00\",\"2018-06-29 21:30:00\",\"2018-07-02 21:30:00\",\"2018-07-03 21:30:00\",\"2018-07-04 21:30:00\",\"2018-07-05 21:30:00\",\"2018-07-06 21:30:00\",\"2018-07-09 21:30:00\",\"2018-07-10 21:30:00\",\"2018-07-11 21:30:00\",\"2018-07-12 21:30:00\",\"2018-07-13 21:30:00\",\"2018-07-16 21:30:00\",\"2018-07-17 21:30:00\",\"2018-07-18 21:30:00\",\"2018-07-19 21:30:00\",\"2018-07-20 21:30:00\",\"2018-07-23 21:30:00\",\"2018-07-24 21:30:00\",\"2018-07-25 21:30:00\"],\"sell\":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\"buy\":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\"indication\":{\"K\":{\"name\":\"K\",\"info\":\"kdj 信息1\",\"style\":{\"lineType\":\"LINE\",\"color\":\"#FF0000\"},\"data\":[null,null,null,null,null,null,null,null,null,91.860886,93.68119,85.38699,76.78677,79.83526,80.64759,83.78954,87.66938,88.63487,90.97988,91.65809,92.73083,93.76063,95.833374,96.811775,94.68061,96.45374,97.635826,97.90747,97.99857,91.38388,90.01932,89.44969,79.71577,84.15203,76.9378,75.75976,70.29473,63.442764,61.90574,60.548336,68.58669,76.99418,76.80339,80.65595,81.69231,81.163475,82.482544,56.128246,49.368347,41.173553,38.33842,41.27173,52.1158,65.56769,75.32517,79.79473,81.385185,84.43783,77.144035,72.76172,64.2187,51.82509,45.295143,35.016106,23.344072,15.562715,22.41548,29.18288,36.679222,53.816185,64.75764,75.35682,81.985466,84.3849,89.268585,90.422356,92.15879,94.6287,93.330154,91.40199,94.268,96.178665,94.373535,93.51052,89.430336,91.22502,93.50373,95.59311,64.267876,55.147552,54.464016,64.23317,71.59017,80.6183,84.88894,89.220245,92.10779,93.9701,91.25984,94.173225,96.115486,95.44975,89.48839,89.54425,90.56297,71.03267,56.790287,52.798588,47.016357,39.860107,32.64158,39.27199,37.902786,44.06195,58.27207,70.88498,69.946075,52.47708,52.08324,41.976173,34.40762,23.520401,16.262255,18.283007,14.455646,23.727488,37.2955,55.05682,69.070404,77.50565,84.16185,86.989395,91.29077,93.53014,94.37244,94.88538,95.070274,92.890144,94.50439,81.53816,71.36868,54.677807,46.924812,46.08994,40.296886,38.41302,45.076622,47.61361,49.285336,33.70627,30.941786,42.576332,50.255318,57.078682,40.331535,30.207336,26.318876,38.610554,43.109306,43.13476,41.109238,42.42562,52.549095,67.036095,77.09455,81.5178,84.46663,78.23258,76.81135,77.82281,70.92588,73.9108,78.73019,84.38616,79.20405,80.20157,76.71421,77.55754,72.55943,54.937935,43.411324,34.22555,30.798988,39.39822,44.22102,58.825806,67.854904,76.52467,82.208176,87.82561,91.86721,90.79507,89.951096,92.68232,89.36941,90.86608,93.68348,95.7581,91.875374,81.419685,80.31433,60.53776,52.689987,47.521526,39.213654,57.89744,68.69541,77.17147,81.31579,82.53606,88.119896,91.541916,93.48795,95.4803,89.38357,84.63225,83.01992,77.0147,59.772026,69.6129,69.555176,67.93132,78.30664,84.51171,88.64842,92.185394,92.32724,94.20472,70.059616,66.29137,61.17457,43.997597,34.473415,33.208603,36.403427,43.450916,58.789284,68.633125,75.0437,77.436935,84.32812,88.46246,86.26091,81.91118,78.39598,72.87395,67.85064,56.675743,46.290848,40.574917,27.049944,18.033297,44.880894,62.624928,72.08904,81.18764,87.09834,90.17537,90.30696,93.53798,95.20014,96.10317,84.70984,86.13707,87.00296,90.009865,93.33991,94.941956,88.38329,82.929504,88.619675,88.34833,79.32701,75.222404,63.228504,42.414207,28.276138,33.917942,33.383152,22.268959,24.95099,31.264189,36.94146,48.133656,64.81463,73.10762,78.63628,82.76739,82.957436,80.09437,86.700874,91.133705,83.95612,70.429535,53.588356,51.177273,56.121822,62.37887,68.07722,75.33118,83.554115,87.39884,82.99433,79.71708,74.515564,66.48248,49.473484,41.504066,34.66716,27.260448,18.25547,12.170313,22.548628,17.845163,15.036657,20.60795,24.697933,20.17985,22.746477,31.95324,40.555874,34.83603,38.881954,56.645153,64.30752,73.77687,75.85518,81.42693,86.24534,89.08961,85.727486,70.885864,55.99235,41.091717,34.12536,40.005924,44.445915,43.46773,50.880104,55.843365,59.547768,71.70379,79.185555,82.7576,88.25018,91.943886,93.34302,92.440155,86.437126,84.36824,74.6449,63.204784,58.423817,47.662334,53.81359,57.10102,66.10264,72.103714,67.632484,75.74986,74.28576,82.72955,88.15129,90.69858,93.79906,89.75275,87.03364,86.024124,89.99709,85.96774,88.61681,86.18749,83.80575,78.12309,80.77303,69.24303,57.67229,44.55919,38.826008,26.017742,24.88906,24.989548,30.342922,26.219786,24.885218,42.520275,60.48033,73.52005,80.88988,81.79775,87.66147,90.72494,90.91646,92.71102,92.11854,83.5686,77.508316,77.11375,73.20378,81.74111]},\"D\":{\"name\":\"D\",\"info\":\"kdj 信息2\",\"style\":{\"lineType\":\"LINE\",\"color\":\"#00FF00\"},\"data\":[null,null,null,null,null,null,null,null,null,91.860886,92.46765,90.10743,85.66721,83.72323,82.69801,83.06186,84.5977,85.94342,87.622246,88.96752,90.221954,91.40151,92.8788,94.1898,94.3534,95.05351,95.91428,96.57868,97.05198,95.16261,93.44818,92.11535,87.982155,86.70545,83.44956,80.8863,77.355774,72.71811,69.11398,66.258766,67.034744,70.35455,72.504166,75.22143,77.37839,78.64008,79.920906,71.99002,64.44946,56.690826,50.573357,47.472813,49.020477,54.536213,61.465866,67.575485,72.17872,76.26509,76.558075,75.29262,71.60131,65.00924,58.437874,50.63062,41.535103,32.87764,29.390253,29.321129,31.773827,39.12128,47.666733,56.89676,65.25966,71.63474,77.51269,81.81591,85.263535,88.38526,90.03356,90.4897,91.74914,93.22565,93.60828,93.57569,92.19391,91.87094,92.41521,93.47451,83.73897,74.208496,67.627,66.49573,68.19388,72.33535,76.51988,80.753334,84.538155,87.68214,88.8747,90.64088,92.46575,93.46042,92.136406,91.272354,91.0359,84.36816,75.17553,67.71655,60.816486,53.831028,46.76788,44.26925,42.147095,42.78538,47.94761,55.5934,60.377625,57.74411,55.857155,51.23016,45.622646,38.25523,30.924238,26.710495,22.625546,22.992859,27.760406,36.85921,47.596275,57.566067,66.43133,73.28402,79.28627,84.034225,87.48029,89.94866,91.65586,92.06729,92.879654,89.09916,83.189,73.68527,64.765114,58.54006,52.459,47.777008,46.876877,47.122456,47.843414,43.13103,39.06795,40.23741,43.576714,48.07737,45.495426,40.399395,35.70589,36.67411,38.819176,40.257706,40.54155,41.169575,44.962746,52.32053,60.578537,67.55829,73.194405,74.873795,75.519646,76.28736,74.500206,74.303734,75.77922,78.6482,78.83348,79.28951,78.431076,78.1399,76.27974,69.16581,60.58098,51.795837,44.796886,42.99733,43.405228,48.54542,54.981915,62.162834,68.84461,75.171616,80.73681,84.08956,86.0434,88.25638,88.62739,89.37362,90.81024,92.459526,92.26481,88.649765,85.87129,77.42678,69.18118,61.961296,54.37875,55.551647,59.932903,65.67909,70.89132,74.7729,79.2219,83.32857,86.715034,89.63679,89.55238,87.91234,86.28153,83.19259,75.385735,73.46146,72.15936,70.750015,73.26889,77.016495,80.89381,84.65767,87.214195,89.54437,83.04945,77.463425,72.033806,62.6884,53.283405,46.591805,43.19568,43.280758,48.450264,55.177887,61.799824,67.01219,72.78417,78.01027,80.76048,81.14405,80.22803,77.776665,74.467995,68.53724,61.121777,54.272823,45.198532,36.14345,39.05593,46.912266,55.304523,63.932228,71.65427,77.827965,81.98763,85.837746,88.95854,91.34009,89.130005,88.13236,87.7559,88.50722,90.11812,91.72607,90.61181,88.05104,88.240585,88.2765,85.293335,81.936356,75.70041,64.605,52.495384,46.302902,41.99632,35.420532,31.930685,31.708519,33.452835,38.34644,47.16917,55.81532,63.422306,69.87067,74.23292,76.18674,79.69145,83.50553,83.65573,79.247,70.694115,64.1885,61.499607,61.792694,63.887535,67.70208,72.98609,77.790344,79.525,79.58903,77.89787,74.09274,65.88632,57.758904,50.061657,42.461254,34.39266,26.98521,25.50635,22.952621,20.313967,20.41196,21.840618,21.28703,21.773512,25.166754,30.296461,31.80965,34.167084,41.659775,49.209023,57.398304,63.5506,69.50938,75.08803,79.75522,81.74598,78.12594,70.74808,60.862625,51.950203,47.968777,46.79449,45.68557,47.41708,50.22584,53.333153,59.4567,66.03298,71.60786,77.1553,82.08482,85.837555,88.03842,87.504654,86.45918,82.52109,76.08232,70.19615,62.68488,59.727783,58.852196,61.26901,64.88058,65.79788,69.115204,70.83872,74.80234,79.25198,83.06752,86.6447,87.68072,87.46502,86.984726,87.988846,87.31515,87.74903,87.22852,86.08759,83.43276,82.54619,78.1118,71.29863,62.385483,54.532326,45.027462,38.314663,33.872955,32.696278,30.537447,28.653372,33.275673,42.34389,52.735943,62.12059,68.67964,75.00692,80.246254,83.802986,86.77233,88.5544,86.89247,83.76442,81.54752,78.76627,79.75789]},\"J\":{\"name\":\"J\",\"info\":\"kdj 信息3\",\"style\":{\"lineType\":\"LINE\",\"color\":\"#0000FF\"},\"data\":[null,null,null,null,null,null,null,null,null,91.860886,96.10827,75.946106,59.025887,72.05932,76.546745,85.24493,93.81274,94.01778,97.69517,97.03921,97.74856,98.47884,101.74252,102.05575,95.33503,99.254196,101.07891,100.56505,99.89177,83.826416,83.16159,84.11838,63.182995,79.045204,63.914265,65.50669,56.172646,44.892086,47.489246,49.127476,71.69059,90.27342,85.40184,91.524994,90.320145,86.21026,87.60583,24.404705,19.206123,10.13901,13.868546,28.869558,58.306442,87.63064,103.043785,104.23322,99.79813,100.783295,78.31597,67.699905,49.45347,25.456793,19.009687,3.7870848,-13.037992,-19.067137,8.465933,28.906385,46.490013,83.20599,98.93945,112.27693,115.437065,109.88523,112.780365,107.63524,105.9493,107.115585,99.923355,93.22657,99.30572,102.0847,95.90406,93.38018,83.903206,89.93317,95.680786,99.830315,25.325706,17.02567,28.138048,59.708065,78.382774,97.18421,101.62705,106.15407,107.247055,106.546036,96.03012,101.23793,103.41496,99.42843,84.19235,86.08804,89.617134,44.361694,20.019798,22.962666,19.416101,11.918273,4.3889804,29.277477,29.414171,46.615093,78.92099,101.46813,89.08298,41.943024,44.53541,23.468199,11.977567,-5.94926,-13.061714,1.4280304,-1.8841547,25.196743,56.365696,91.45204,112.018654,117.38483,119.62289,114.400154,115.299774,112.52199,108.156715,104.75883,101.8991,94.53586,97.753845,66.41617,47.728058,16.662878,11.244204,21.189701,15.972655,19.68505,41.476105,48.595917,52.16917,14.856742,14.689457,47.254173,63.61253,75.0813,30.003757,9.823218,7.544851,42.48344,51.689564,48.888878,42.244614,44.93772,67.72179,96.46723,110.12657,109.43681,107.01108,84.95015,79.394745,80.893684,63.77723,73.12492,84.632126,95.86209,79.945175,82.02569,73.280464,76.39282,65.11881,26.482191,9.07201,-0.91501707,2.8031912,32.199993,45.852604,79.38657,93.60088,105.24835,108.935295,113.1336,114.128006,104.20607,97.766464,101.534195,90.85345,93.85101,99.429955,102.355255,91.096504,66.95952,69.20041,26.759724,19.707602,18.641989,8.883466,62.58903,86.22043,100.156235,102.16471,98.06236,105.91589,107.9686,107.0338,107.16733,89.045944,78.07207,76.4967,64.65893,28.544613,61.915783,64.34681,62.293922,88.38214,99.50214,104.15765,107.24085,102.553345,103.52542,44.07994,43.94725,39.4561,6.6159873,-3.146563,6.442197,22.818922,43.79123,79.467316,95.54361,101.531456,98.28641,107.41602,109.36685,97.26177,83.44544,74.731895,63.068512,54.615936,32.952744,16.628986,13.179103,-9.247228,-18.187016,56.53081,94.050255,105.65808,115.69845,117.986496,114.87018,106.945625,108.93843,107.683334,105.62934,75.86951,82.1465,85.4971,93.01516,99.7835,101.37375,83.92626,72.68644,89.377846,88.492,67.394356,61.7945,38.284695,-1.967392,-20.162354,9.148018,16.156816,-4.034189,10.991603,30.375528,43.918716,67.708084,100.10555,107.692215,109.06422,108.56082,100.40646,87.90964,100.71973,106.39004,84.556915,52.7946,19.376827,25.154816,45.366245,63.551212,76.45657,90.589355,104.69016,106.61584,89.93298,79.973175,67.75094,51.261967,16.6478,8.994391,3.8781633,-3.1411605,-14.018909,-17.459482,16.633183,7.63025,4.4820395,20.999931,30.412561,17.96549,24.69241,45.52621,61.074703,40.888786,48.31169,86.61591,94.5045,106.534004,100.46435,105.262054,108.55995,107.75838,93.69051,56.40571,26.480904,1.5499033,-1.5243272,24.080225,39.748764,39.032055,57.806152,67.07841,71.977005,96.197975,105.49069,105.05709,110.43996,111.662,108.35394,101.24361,84.30206,80.186356,58.89252,37.449707,34.879143,17.617239,41.98521,53.59867,75.76989,86.54998,71.30169,89.01917,81.17983,98.584,105.9499,105.96071,108.107765,93.89682,86.17087,84.102936,94.01359,83.27294,90.35236,84.10543,79.24205,67.50375,77.22673,51.505478,30.419613,8.906599,7.41338,-12.001701,-1.9621447,7.222727,25.636211,17.58446,17.34891,61.009476,96.75321,115.088264,118.42845,108.033966,112.970566,111.6823,105.14339,104.5884,99.2468,76.92087,64.99611,68.24618,62.078785,85.70756]}}}}"],"infos":["{\"date\":\"2018-07-26 14:02:16\",\"data\":\"数据解析完成...\"}","{\"date\":\"2018-07-26 14:02:16\",\"data\":\"正在执行数据...\"}",

# "{\"date\":\"2018-07-26 14:02:16\",\"data\":\"数据执行完成...\"}"],"finished":true,"overtime":false}}
def test3():
    resStr2 = [0,0,0,0,0,0,0,0,0,91.860886,92.46765,90.10743,85.66721,83.72323,82.69801,83.06186,84.5977,85.94342,87.622246,88.96752,90.221954,91.40151,92.8788,94.1898,94.3534,95.05351,95.91428,96.57868,97.05198,95.16261,93.44818,92.11535,87.982155,86.70545,83.44956,80.8863,77.355774,72.71811,69.11398,66.258766,67.034744,70.35455,72.504166,75.22143,77.37839,78.64008,79.920906,71.99002,64.44946,56.690826,50.573357,47.472813,49.020477,54.536213,61.465866,67.575485,72.17872,76.26509,76.558075,75.29262,71.60131,65.00924,58.437874,50.63062,41.535103,32.87764,29.390253,29.321129,31.773827,39.12128,47.666733,56.89676,65.25966,71.63474,77.51269,81.81591,85.263535,88.38526,90.03356,90.4897,91.74914,93.22565,93.60828,93.57569,92.19391,91.87094,92.41521,93.47451,83.73897,74.208496,67.627,66.49573,68.19388,72.33535,76.51988,80.753334,84.538155,87.68214,88.8747,90.64088,92.46575,93.46042,92.136406,91.272354,91.0359,84.36816,75.17553,67.71655,60.816486,53.831028,46.76788,44.26925,42.147095,42.78538,47.94761,55.5934,60.377625,57.74411,55.857155,51.23016,45.622646,38.25523,30.924238,26.710495,22.625546,22.992859,27.760406,36.85921,47.596275,57.566067,66.43133,73.28402,79.28627,84.034225,87.48029,89.94866,91.65586,92.06729,92.879654,89.09916,83.189,73.68527,64.765114,58.54006,52.459,47.777008,46.876877,47.122456,47.843414,43.13103,39.06795,40.23741,43.576714,48.07737,45.495426,40.399395,35.70589,36.67411,38.819176,40.257706,40.54155,41.169575,44.962746,52.32053,60.578537,67.55829,73.194405,74.873795,75.519646,76.28736,74.500206,74.303734,75.77922,78.6482,78.83348,79.28951,78.431076,78.1399,76.27974,69.16581,60.58098,51.795837,44.796886,42.99733,43.405228,48.54542,54.981915,62.162834,68.84461,75.171616,80.73681,84.08956,86.0434,88.25638,88.62739,89.37362,90.81024,92.459526,92.26481,88.649765,85.87129,77.42678,69.18118,61.961296,54.37875,55.551647,59.932903,65.67909,70.89132,74.7729,79.2219,83.32857,86.715034,89.63679,89.55238,87.91234,86.28153,83.19259,75.385735,73.46146,72.15936,70.750015,73.26889,77.016495,80.89381,84.65767,87.214195,89.54437,83.04945,77.463425,72.033806,62.6884,53.283405,46.591805,43.19568,43.280758,48.450264,55.177887,61.799824,67.01219,72.78417,78.01027,80.76048,81.14405,80.22803,77.776665,74.467995,68.53724,61.121777,54.272823,45.198532,36.14345,39.05593,46.912266,55.304523,63.932228,71.65427,77.827965,81.98763,85.837746,88.95854,91.34009,89.130005,88.13236,87.7559,88.50722,90.11812,91.72607,90.61181,88.05104,88.240585,88.2765,85.293335,81.936356,75.70041,64.605,52.495384,46.302902,41.99632,35.420532,31.930685,31.708519,33.452835,38.34644,47.16917,55.81532,63.422306,69.87067,74.23292,76.18674,79.69145,83.50553,83.65573,79.247,70.694115,64.1885,61.499607,61.792694,63.887535,67.70208,72.98609,77.790344,79.525,79.58903,77.89787,74.09274,65.88632,57.758904,50.061657,42.461254,34.39266,26.98521,25.50635,22.952621,20.313967,20.41196,21.840618,21.28703,21.773512,25.166754,30.296461,31.80965,34.167084,41.659775,49.209023,57.398304,63.5506,69.50938,75.08803,79.75522,81.74598,78.12594,70.74808,60.862625,51.950203,47.968777,46.79449,45.68557,47.41708,50.22584,53.333153,59.4567,66.03298,71.60786,77.1553,82.08482,85.837555,88.03842,87.504654,86.45918,82.52109,76.08232,70.19615,62.68488,59.727783,58.852196,61.26901,64.88058,65.79788,69.115204,70.83872,74.80234,79.25198,83.06752,86.6447,87.68072,87.46502,86.984726,87.988846,87.31515,87.74903,87.22852,86.08759,83.43276,82.54619,78.1118,71.29863,62.385483,54.532326,45.027462,38.314663,33.872955,32.696278,30.537447,28.653372,33.275673,42.34389,52.735943,62.12059,68.67964,75.00692,80.246254,83.802986,86.77233,88.5544,86.89247,83.76442,81.54752,78.76627,79.75789]
    resStr3 = [0,0,0,0,0,0,0,0,0,91.860886,96.10827,75.946106,59.025887,72.05932,76.546745,85.24493,93.81274,94.01778,97.69517,97.03921,97.74856,98.47884,101.74252,102.05575,95.33503,99.254196,101.07891,100.56505,99.89177,83.826416,83.16159,84.11838,63.182995,79.045204,63.914265,65.50669,56.172646,44.892086,47.489246,49.127476,71.69059,90.27342,85.40184,91.524994,90.320145,86.21026,87.60583,24.404705,19.206123,10.13901,13.868546,28.869558,58.306442,87.63064,103.043785,104.23322,99.79813,100.783295,78.31597,67.699905,49.45347,25.456793,19.009687,3.7870848,-13.037992,-19.067137,8.465933,28.906385,46.490013,83.20599,98.93945,112.27693,115.437065,109.88523,112.780365,107.63524,105.9493,107.115585,99.923355,93.22657,99.30572,102.0847,95.90406,93.38018,83.903206,89.93317,95.680786,99.830315,25.325706,17.02567,28.138048,59.708065,78.382774,97.18421,101.62705,106.15407,107.247055,106.546036,96.03012,101.23793,103.41496,99.42843,84.19235,86.08804,89.617134,44.361694,20.019798,22.962666,19.416101,11.918273,4.3889804,29.277477,29.414171,46.615093,78.92099,101.46813,89.08298,41.943024,44.53541,23.468199,11.977567,-5.94926,-13.061714,1.4280304,-1.8841547,25.196743,56.365696,91.45204,112.018654,117.38483,119.62289,114.400154,115.299774,112.52199,108.156715,104.75883,101.8991,94.53586,97.753845,66.41617,47.728058,16.662878,11.244204,21.189701,15.972655,19.68505,41.476105,48.595917,52.16917,14.856742,14.689457,47.254173,63.61253,75.0813,30.003757,9.823218,7.544851,42.48344,51.689564,48.888878,42.244614,44.93772,67.72179,96.46723,110.12657,109.43681,107.01108,84.95015,79.394745,80.893684,63.77723,73.12492,84.632126,95.86209,79.945175,82.02569,73.280464,76.39282,65.11881,26.482191,9.07201,-0.91501707,2.8031912,32.199993,45.852604,79.38657,93.60088,105.24835,108.935295,113.1336,114.128006,104.20607,97.766464,101.534195,90.85345,93.85101,99.429955,102.355255,91.096504,66.95952,69.20041,26.759724,19.707602,18.641989,8.883466,62.58903,86.22043,100.156235,102.16471,98.06236,105.91589,107.9686,107.0338,107.16733,89.045944,78.07207,76.4967,64.65893,28.544613,61.915783,64.34681,62.293922,88.38214,99.50214,104.15765,107.24085,102.553345,103.52542,44.07994,43.94725,39.4561,6.6159873,-3.146563,6.442197,22.818922,43.79123,79.467316,95.54361,101.531456,98.28641,107.41602,109.36685,97.26177,83.44544,74.731895,63.068512,54.615936,32.952744,16.628986,13.179103,-9.247228,-18.187016,56.53081,94.050255,105.65808,115.69845,117.986496,114.87018,106.945625,108.93843,107.683334,105.62934,75.86951,82.1465,85.4971,93.01516,99.7835,101.37375,83.92626,72.68644,89.377846,88.492,67.394356,61.7945,38.284695,-1.967392,-20.162354,9.148018,16.156816,-4.034189,10.991603,30.375528,43.918716,67.708084,100.10555,107.692215,109.06422,108.56082,100.40646,87.90964,100.71973,106.39004,84.556915,52.7946,19.376827,25.154816,45.366245,63.551212,76.45657,90.589355,104.69016,106.61584,89.93298,79.973175,67.75094,51.261967,16.6478,8.994391,3.8781633,-3.1411605,-14.018909,-17.459482,16.633183,7.63025,4.4820395,20.999931,30.412561,17.96549,24.69241,45.52621,61.074703,40.888786,48.31169,86.61591,94.5045,106.534004,100.46435,105.262054,108.55995,107.75838,93.69051,56.40571,26.480904,1.5499033,-1.5243272,24.080225,39.748764,39.032055,57.806152,67.07841,71.977005,96.197975,105.49069,105.05709,110.43996,111.662,108.35394,101.24361,84.30206,80.186356,58.89252,37.449707,34.879143,17.617239,41.98521,53.59867,75.76989,86.54998,71.30169,89.01917,81.17983,98.584,105.9499,105.96071,108.107765,93.89682,86.17087,84.102936,94.01359,83.27294,90.35236,84.10543,79.24205,67.50375,77.22673,51.505478,30.419613,8.906599,7.41338,-12.001701,-1.9621447,7.222727,25.636211,17.58446,17.34891,61.009476,96.75321,115.088264,118.42845,108.033966,112.970566,111.6823,105.14339,104.5884,99.2468,76.92087,64.99611,68.24618,62.078785,85.70756]
    plt.plot(resStr2,'-,b')
    plt.plot(resStr3,'-,r')
    plt.ylabel('kdj指标')
    plt.show()
#test3()

def test4():
    re1 = [1,2,3]
    plt.plot(re1,'-,b')
    re2 = [4,5,6]
    plt.plot(re2,'-,r')
    plt.ylabel('金叉')
    plt.show()

test4()