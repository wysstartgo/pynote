from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

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

test2()
