functions {
  vector seir_sei(real t, vector y, real beta_h, real beta_m, real b,
		  real sigma, real gamma, real nu, real mu_m) {
    real S_h = y[1];
    real E_h = y[2];
    real I_h = y[3];
    real R_h = y[4];
    real S_m = y[5];
    real E_m = y[6];
    real I_m = y[7];

    real N_h = S_h + E_h + I_h + R_h;
    real N_m = S_m + E_m + I_m;

    // Force of infection
    real lambda_h = b * beta_h * I_m / N_h;
    real lambda_m = b * beta_m * I_h / N_h;

    vector[7] dydt;
    // Human dynamics
    dydt[1] = -lambda_h * S_h;                    // dS_h/dt
    dydt[2] = lambda_h * S_h - sigma * E_h;       // dE_h/dt
    dydt[3] = sigma * E_h - gamma * I_h;          // dI_h/dt
    dydt[4] = gamma * I_h;                        // dR_h/dt

    // Mosquito dynamics
    dydt[5] = mu_m * N_m - lambda_m * S_m - mu_m * S_m;  // dS_m/dt
    dydt[6] = lambda_m * S_m - nu * E_m - mu_m * E_m;    // dE_m/dt
    dydt[7] = nu * E_m - mu_m * I_m;                     // dI_m/dt

    return dydt;
  }
}

data {
  int<lower=1> n_days;
  real t0;
  vector[7] y0;  // Initial conditions [S_h0, E_h0, I_h0, R_h0, S_m0, E_m0, I_m0]
  real<lower=0> beta_h;  // mosquito to human transmission
  real<lower=0> beta_m;  // human to mosquito transmission
  real<lower=0> b;       // biting rate
  real<lower=0> sigma;   // human incubation rate
  real<lower=0> gamma;   // human recovery rate
  real<lower=0> nu;      // mosquito incubation rate
  real<lower=0> mu_m;    // mosquito mortality rate
}

transformed data {
  array[n_days] real ts;
  for (i in 1:n_days) {
    ts[i] = i;
  }
}

parameters {
  real<lower=0> b;           // biting rate
  real<lower=0,upper=1> beta_h; // transmission probabilities
  real<lower=0,upper=1> beta_m;
  real<lower=0> k_h;         // incubation rates
  real<lower=0> k_m;
  real<lower=0> gamma_h;     // recovery rate
  real<lower=0> mu_m;        // mosquito mortality
  real<lower=0> phi_inv;     // overdispersion parameter
}

model {
  b ~ normal(1.0, 0.3);
  beta_h ~ beta(2, 5);       // weakly informative
  beta_m ~ beta(5, 2);       // higher human->mosquito transmission
  k_h ~ normal(0.18, 0.05);  // ~5.5 day incubation
  k_m ~ normal(0.10, 0.03);  // ~10 day incubation
  gamma_h ~ normal(0.167, 0.05); // ~6 day recovery
  mu_m ~ normal(0.15, 0.05);  // ~7 day mosquito lifespan
  phi_inv ~ exponential(5);
}

generated quantities {
  array[n_days] vector[7] y = ode_rk45(seir_sei, y0, t0, ts,
				       beta_h, beta_m, b,
				       sigma, gamma, nu, mu_m);
}
