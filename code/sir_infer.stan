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
  array[n_days] int<lower=0> cases;  // OBSERVED DATA instead of beta/gamma
}

parameters {
  real<lower=0.001> beta;   // TO BE INFERRED
  real<lower=0.001> gamma;  // TO BE INFERRED
  real<lower=0> phi;  // overdispersion parameter
}

transformed parameters {
  array[n_days] vector[3] y = ode_rk45(sir, y0, t0, ts, beta, gamma);
}

model {
  beta ~ lognormal(-0.69, 0.5);   // log(0.5) ≈ -0.69
  gamma ~ lognormal(-2.30, 0.5);  // log(0.1) ≈ -2.30
  phi ~ exponential(0.1);  // prior on overdispersion

  // Likelihood: observed cases come from true infected count
  cases ~ neg_binomial_2(y[,2], phi);
}

generated quantities {
  real R0 = beta / gamma;

  // Posterior predictive checks
  array[n_days] int cases_pred;
  for (i in 1:n_days) {
    cases_pred[i] =  neg_binomial_2_rng(fmax(1e-3, y[i][2]), phi);
  }
}
