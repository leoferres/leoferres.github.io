functions {
  vector sir(real t, vector y, real beta, real gamma) {
    real S = y[1];
    real I = y[2];
    real R = y[3];
    real N = S + I + R;

    vector[3] dydt;
    dydt[1] = -beta * S * I / N;            // dS/dt
    dydt[2] = beta * S * I / N - gamma * I; // dI/dt
    dydt[3] = gamma * I;                    // dR/dt

    return dydt;
  }
}

data {
  int<lower=1> n_days;
  real t0;
  vector[3] y0;  // Initial conditions [S0, I0, R0]
  array[n_days] real ts;
  real<lower=0> beta;
  real<lower=0> gamma;
}

model {
  // Nothing to estimate - just forward simulation
}

generated quantities {
  array[n_days] vector[3] y = ode_rk45(sir, y0, t0, ts, beta, gamma);
}
