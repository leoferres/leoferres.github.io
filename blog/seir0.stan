functions {
  vector seir(real t, vector y, real beta, real sigma, real gamma) {
    real S = y[1];
    real E = y[2];
    real I = y[3];
    real R = y[4];
    real N = S + E + I + R;

    vector[4] dydt;
    dydt[1] = -beta * S * I / N;              // dS/dt
    dydt[2] = beta * S * I / N - sigma * E;   // dE/dt
    dydt[3] = sigma * E - gamma * I;          // dI/dt
    dydt[4] = gamma * I;                      // dR/dt

    return dydt;
  }
}

data {
  int<lower=1> n_days;
  real t0;
  vector[4] y0;  // Initial conditions [S0, E0, I0, R0]
  array[n_days] real ts;
  real<lower=0> beta;
  real<lower=0> sigma;
  real<lower=0> gamma;
}

model {
  // Nothing to estimate - just forward simulation
}

generated quantities {
  array[n_days] vector[4] y = ode_rk45(seir, y0, t0, ts,
				       beta, sigma, gamma);
}
