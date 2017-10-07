VT = 26e-3;

b0 = 100;
IC = 100e-6;
RC = 5e3;

gm = IC/VT;
Ri = b0/gm;
Ro = RC;
av = -gm*RC;
ai = b0;

fprintf('(a)\n');
fprintf('Ri=%f (kohm)\n', Ri*1e-3);
fprintf('Ro=%f (kohm)\n', Ro*1e-3);
fprintf('av=%f\n', av);
fprintf('ai=%f\n', ai);

RL = 10e3;
RS = 20e3;
av = -gm*(Ri/(RS+Ri))*resp(Ro, RL);

fprintf('(b)\n');
fprintf('av=%f\n', av);