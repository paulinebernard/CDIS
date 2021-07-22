function state_dot = compute_dyn_OL(state)

sigma =10;
beta = 8/3;
rho = 28;

state_dot = [sigma*(state(2)-state(1)),rho*state(1)-state(2)-state(1)*state(3),state(1)*state(2)-beta*state(3)];
