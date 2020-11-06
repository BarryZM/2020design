# 割圆术
# 【内逼近】：割之弥细，失之弥少，割之又圆，以至于不可割，则与圆和体，而无所失矣。
# [外逼近】：觚面之外，又有余径。以面乘余径，则幂出弧表。若夫觚之细者与圆全体，则表无余径，则幂不外出矣。
# 解题步骤：
# 1、从圆正六边形开始，逐步加倍圆内接正多边形边数，设为2n
# 2、依次计算正多边形面积，S6、S12、S24、…、S2n
# 3、过正多边形的每条边向外做高为余径的矩形
# 得出结论：
# S2n < S < S2n + (S2n - Sn)
# 分析算法：
# 设圆的半径为1，弦心距为hn，正n边形的边长为xn，面积为Sn
# 则正2n边形的边长为x2n，面积为S2n,
# S2n=Sn + n * xn * (1 - hn)/2  (n>=6) 或 S2n = n * xn / 2
# hn = SQRT(1- (xn/2)**2)
# x2n = SQRT((xn/2)**2+(1-hn)**2) = SQRT(2-SQRT(4-xn**2)
# 进而得出圆周率的近似值：
# s6= 2.598 S12=3 S24=3.106 ……
# 刘徽求出192边形的面积，得出圆周率为3.14的结论，化成分数157/50,这就是著名的徽率。

import math


def cyclotomic_method(n, flag=False):
    if flag:
        n = 6 * 2 ** n
    k = 6
    x = 1
    s = 6 * math.sqrt(3) / 4
    while k <= n // 2:
        h = math.sqrt(1 - (x / 2) ** 2)
        # s += k * x * (1 - h) / 2
        s = k * x / 2
        x = math.sqrt((x / 2) ** 2 + (1 - h) ** 2)
        k *= 2
    return k, s


for i in range(28):
    print(cyclotomic_method(i, True))
