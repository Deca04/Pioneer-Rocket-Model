%simple parachute simulation

r = linspace(0, 1, 100);

m = 0.534; %kg
g = 9.81; %m/s^2
ro = 1.3; %kg/m^3
C_d = 1.2;
sup = 2*pi*r.^2;

v_t = sqrt((2*m*g)./(ro*sup*C_d));
y = 5; 

plot(r, y*ones(size(r)), 'LineWidth',2); % Plot horizontal line
hold on

plot(r, v_t,'LineWidth',2);

xlabel('radius');
ylabel('terminar impact velocity [m/s]');
title('impact velocity');

