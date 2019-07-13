% Matlab

% min c^Tx
% s.t.
%     Ax <= b
%     Aeq * x = beq
%     LB <= x <= UB

% max z = 2x1 + 3x2 - 5x3
% s.t.
%      x1 + x2 + x3 = 7
%      2x1 - 5x2 + x3 >= 10
%      x1 + 3x2 + x3 <= 12
%      x1, x2, x3 >= 0

f = [2, 3, -5];
f = -f
A = [-2, 5, -1; 1, 3, 1];
b = [-10, 12];
Aeq = [1, 1, 1];
beq = [7];
LB = [0, 0, 0];
UB = [inf, inf, inf];
[X, FVAL, EXITFLAG] = linprog(f, A, b, Aeq, beq, LB, UB)
FVAL = -FVAL
