import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cmdstanpy

df = pd.read_csv('sir_synthetic_data_beta1.20_gamma0.10_N1000_days50.csv')
observed_cases = df['observed_cases'].values

n_days = len(observed_cases)
N = 1000

print("Compiling inference model...")
model = cmdstanpy.CmdStanModel(stan_file='sir_infer.stan')

ts = list(range(1, n_days + 1))

# Set up data - NOW WITH OBSERVED CASES INSTEAD OF BETA/GAMMA
data = {
    'n_days': n_days,
    't0': 0,
    'ts': ts,
    'y0': [N-1, 1, 0],  # [S0, I0, R0]
    'cases': observed_cases  # THIS IS THE KEY CHANGE
}

# Run MCMC to infer parameters
print("Running MCMC inference...")
fit = model.sample(
    data=data,
    chains=4,
    iter_sampling=1000,
    iter_warmup=1000,
    seed=123,
    show_progress=True
)

# Extract inferred parameters
beta_samples = fit.stan_variable('beta')
gamma_samples = fit.stan_variable('gamma')
R0_samples = fit.stan_variable('R0')
y_samples = fit.stan_variable('y')
cases_pred = fit.stan_variable('cases_pred')

# Print results
print(f"\nInferred parameters (mean ± std):")
print(f"  β = {np.mean(beta_samples):.3f} ± {np.std(beta_samples):.3f}")
print(f"  γ = {np.mean(gamma_samples):.3f} ± {np.std(gamma_samples):.3f}")
print(f"  R₀ = {np.mean(R0_samples):.3f} ± {np.std(R0_samples):.3f}")
print(f"  Infectious period = {1/np.mean(gamma_samples):.1f} days")

# Plot results
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Posterior distributions
axes[0, 0].hist(beta_samples, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')
axes[0, 0].set_xlabel('β')
axes[0, 0].set_ylabel('Density')
axes[0, 0].set_title(f'Posterior of β\n(mean={np.mean(beta_samples):.3f})')

axes[0, 1].hist(gamma_samples, bins=30, density=True, alpha=0.7, color='green', edgecolor='black')
axes[0, 1].set_xlabel('γ')
axes[0, 1].set_ylabel('Density')
axes[0, 1].set_title(f'Posterior of γ\n(mean={np.mean(gamma_samples):.3f})')

# Plot 2: Fitted curves vs observed data
days = np.arange(1, n_days + 1)
S_mean = np.mean(y_samples[:, :, 0], axis=0)
I_mean = np.mean(y_samples[:, :, 1], axis=0)
R_mean = np.mean(y_samples[:, :, 2], axis=0)

I_lower = np.percentile(y_samples[:, :, 1], 2.5, axis=0)
I_upper = np.percentile(y_samples[:, :, 1], 97.5, axis=0)

axes[1, 0].plot(days, observed_cases, 'ko', markersize=4, alpha=0.5, label='Observed cases')
axes[1, 0].plot(days, I_mean, 'r-', linewidth=2, label='Posterior mean')
axes[1, 0].fill_between(days, I_lower, I_upper, alpha=0.3, color='red', label='95% CI')
axes[1, 0].set_xlabel('Days')
axes[1, 0].set_ylabel('Number of infected')
axes[1, 0].set_title('Fitted vs Observed')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# Plot 3: Full SIR curves
axes[1, 1].plot(days, S_mean, 'b-', label='Susceptible', linewidth=2)
axes[1, 1].plot(days, I_mean, 'r-', label='Infected', linewidth=2)
axes[1, 1].plot(days, R_mean, 'g-', label='Recovered', linewidth=2)
axes[1, 1].set_xlabel('Days')
axes[1, 1].set_ylabel('Number of people')
axes[1, 1].set_title('Inferred SIR Trajectories')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sir_inference_results.png', dpi=300, bbox_inches='tight')


# Diagnostics
print("\nMCMC Diagnostics:")
print(fit.diagnose())

# Check R-hat values
summary = fit.summary()
print("\nR-hat values:")
print(f"  β: {summary.loc['beta', 'R_hat']:.3f}")
print(f"  γ: {summary.loc['gamma', 'R_hat']:.3f}")

plt.show()
