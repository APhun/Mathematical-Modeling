# Python解法

# 使用scipy中的optimize
# 标准形式为:
# min c^Tx
# s.t.
#     Ax <= b
#     Aeq * x = beq
#     LB <= x <= UB
#
# 求解函数 res = optimize.linprog(c,A,b,Aeq,beq,LB,UB,X0,OPTIONS)
# 目标函数最小值 res.fun
# 最优解 res.x

# max z = 2x1 + 3x2 - 5x3
# s.t.
#      x1 + x2 + x3 = 7
#      2x1 - 5x2 + x3 >= 10
#      x1 + 3x2 + x3 <= 12
#      x1, x2, x3 >= 0

from scipy import optimize
import numpy as np

c = np.array([2, 3, -5])
A = np.array([[-2, 5, -1], [1, 3, 1]])
b = np.array([-10, 12])
Aeq = np.array([[1, 1, 1]])
beq = np.array([7])
bound = np.array([(0,None), (0,None), (0,None)]) # LB和UB

res = optimize.linprog(-c, A, b, Aeq, beq, bound)
#print(res)
print(-res.fun)