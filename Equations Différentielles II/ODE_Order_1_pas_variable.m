% Programm structure for solving an ODE via an explicit Euler scheme
% with on-line selection of the time step-size.
% The ODE is:
% dx/dt (t) = f(x(t),t)
%
% The Euler scheme gives the error
% e(t) = x(t+dt) - x(t) - f(x(t),t) dt) dt
% We know e(t) is of order dt^2 but it cannot be computed since,
% of course, x(t+dt) is unknown.
% We use a "come back" technique to evaluate it:
% We compute via a forward step:
% x(t + dt) = x(t) + dt * f(x(t),t)
% and from this re-estimate x(t) by a backward step
% x_re_est(t) = x(t + dt) - dt * f(t + dt, t+dt)
% So an approximation of e(t) is
% e(t) = x_re_est(t) - x(t)
% Assuming this error is proportional to dt^2, we look for dt_good such
% that the corresponding error would be smaller than desired_absolute_error
% Because of the quadratic dependence the error we should get by using
% dt_good instead of dt is
% e(t) * dt_good^2/dt^2
% So dt_good should satisfy
% |e(t)| * dt_good^2/dt^2 < desired_absolute_error
% The rule we choose is
% dt_good = rho_absolute_error  * dt * sqrt(desired_absolute_error/|e(t)|)
% with rho_absolute_error  < 1 as a safe guard.

clear all, close all
disp(' ')
disp(['------- New run starting at = ',datestr(clock),' -------'])
disp(' ')

%% Data

% Data: parameters
dimstate= 3;

% Data: Initial conditions
state_init= [1,1,1];

% Data: Integration scheme
Tfin=100;% Final integration time
DT = 0.1;% Sampling period
nbpoint_asked= Tfin/DT+1;% number of stored points

dt=DT/10;% initial itegration step
dt_min=sqrt(eps);% minimum value allowed for dt

% To check if the integration step is appropriate, we need to define
desired_absolute_error = 1e-6; %absolute error on the solution we want to impose at each time
rho_absolute_error = 0.9;%safe gurad to get the desired absolute error typically between .9 and .99

% Buffers
state_storage=zeros(nbpoint_asked,dimstate);
time_storage=zeros(nbpoint_asked,1);
absolute_error_storage=zeros(nbpoint_asked,dimstate);
sampling_time_storage=zeros(nbpoint_asked,1);

%% Integration loop with samples

% Initilization
state= state_init;
T = 0;
t=0;

absolute_error=zeros(dimstate,1);

emergency_exit=0;


% Initial state_dot
state_dot= compute_dyn_OL(state);% This is the malab script for f(state_init,0)

% integration loop per sample
% ---------------------------
for ipoint=1:nbpoint_asked-1
    state_storage(ipoint,:)=state;
    time_storage(ipoint,1)=T;
    absolute_error_storage(ipoint,:)=absolute_error;
    sampling_time_storage(ipoint) = dt;
    t=0;
    while t<DT
        % Inter sample integration
        % ------------------------
        % Next state at times t+dt
        state_new=state+dt*state_dot;
        t_new=t+dt;
        T_new=T+dt;
        % Sate dot comptuted for state_new
        state_dot= compute_dyn_OL(state_new);% This is the malab script for f(state_new,t_new)
        % Reconstruction of state at time t
        state_re_estim=state_new-dt*state_dot;
        % Estimated integration error
        absolute_error=abs(state_re_estim-state);
        % Update of dt
        dt = rho_absolute_error  * dt * min(sqrt(desired_absolute_error./absolute_error));
        if dt<dt_min
            % Emergency exit: dt is smaller than the lower bound
            emergency_exit=1;
            break
        elseif dt> DT/2
            dt = DT/2;
        end
        % Loop update
        state=state_new;
        t=t_new;
        T=T_new;
    end
        if emergency_exit == 1
        % Emergency exit
        nbpoint_done=ipoint+1;
        state_storage(nbpoint_done,:)=state_new;
        time_storage(nbpoint_done,1)=T;
        absolute_error_storage(nbpoint_done,:)=absolute_error;
        disp(' ')
        disp('Emergency exit: dt is smaller than the lower bound')
        disp('+++++++++++++++')
        disp(' ')
        disp(['  global time         = ',num2str(T)])
        disp(['  local time          = ',num2str(t)])
        disp(['  done sample number  = ',num2str(ipoint)])
        disp(['  current old state   = ',num2str(state')])
        disp(['  current new state   = ',num2str(state_new')])
        disp(' ')
        break
    else
        % Nominal behaviour
    % Completing the integration up to the next sampling time
    % -------------------------------------------------------
    dt2DT=DT-t;
    % Next state at times t+dt2DT = DT
    state_new=state+dt2DT*state_dot;
    t_new=t+dt2DT;
    T_new=T+dt2DT;
    % Sate dot comptuted for state_new
    state_dot= compute_dyn_OL(state_new);% This is the malab script for f(state_new,t_new)
    
    % Update
    state=state_new;
    t=t_new;
    T=T_new;
        end
end

if emergency_exit == 0
    % Nominal behaviour
    nbpoint_done=nbpoint_asked;

    % Last storage
    state_storage(nbpoint_done,:)=state;
    time_storage(nbpoint_done)=T;
    absolute_error_storage(nbpoint_done,:)=absolute_error;
    sampling_time_storage(nbpoint_done,1) = dt;
end

% The results are in
%    state_storage(1:nbpoint_done,:) for the sampled sate
%    time_storage(1:nbpoint_done,1) for the sampled time
%    absolute_error_storage for the absolute_error at sampling time
indexwindow=1:nbpoint_done;

figure
hold on
for i=1:dimstate
    plot(time_storage,state_storage(:,i))
end

figure
plot(sampling_time_storage)
title('Sampling time')



