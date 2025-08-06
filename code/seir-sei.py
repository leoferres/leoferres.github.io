import numpy as np
import matplotlib.pyplot as plt
import cmdstanpy

# Compile the model
model = cmdstanpy.CmdStanModel(stan_file='seir_sei.stan')

# Set up data
N_h = 10000  # Human population
N_m = 20000  # Mosquito population (typically 2:1 ratio)

data = {
    'n_days': 200,
    't0': 0,
    'y0': [N_h-1, 0, 1, 0, N_m-1, 1, 0],  # [S_h0, E_h0, I_h0, R_h0, S_m0, E_m0, I_m0]
    'beta_h': 0.3,   # mosquito to human transmission probability
    'beta_m': 0.5,   # human to mosquito transmission probability
    'b': 0.5,        # biting rate (bites per mosquito per day)
    'sigma': 0.2,    # 1/human incubation period (5 days)
    'gamma': 0.1,    # 1/human infectious period (10 days)
    'nu': 0.1,       # 1/mosquito incubation period (10 days)
    'mu_m': 0.05     # mosquito mortality rate (20 day lifespan)
}

# Run the model (fixed_param since we're not sampling)
fit = model.sample(
    data=data,
    chains=1,
    iter_sampling=1,
    iter_warmup=500,
    fixed_param=True,
    seed=123
)

# Extract results
y = fit.stan_variable('y')
S_h = y[0, :, 0]
E_h = y[0, :, 1]
I_h = y[0, :, 2]
R_h = y[0, :, 3]
S_m = y[0, :, 4]
E_m = y[0, :, 5]
I_m = y[0, :, 6]

# Calculate R0 for vector-borne disease
R0 = np.sqrt((data['b']**2 * data['beta_h'] * data['beta_m'] * data['nu']) / 
             (data['gamma'] * data['mu_m'] * (data['nu'] + data['mu_m'])))
print(f"Basic reproduction number R₀ = {R0:.2f}")

# Plot human dynamics
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(range(1, 201), S_h, label='Susceptible', color='blue')
plt.plot(range(1, 201), E_h, label='Exposed', color='orange')
plt.plot(range(1, 201), I_h, label='Infected', color='red')
plt.plot(range(1, 201), R_h, label='Recovered', color='green')
plt.xlabel('Days')
plt.ylabel('Number of humans')
plt.title(f'Human Population Dynamics (SEIR)\nR₀ = {R0:.2f}')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot mosquito dynamics
plt.subplot(1, 2, 2)
plt.plot(range(1, 201), S_m, label='Susceptible', color='blue', linestyle='--')
plt.plot(range(1, 201), E_m, label='Exposed', color='orange', linestyle='--')
plt.plot(range(1, 201), I_m, label='Infected', color='red', linestyle='--')
plt.xlabel('Days')
plt.ylabel('Number of mosquitoes')
plt.title('Mosquito Population Dynamics (SEI)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('seir_sei.png', dpi=300, bbox_inches='tight')

# Print summary statistics
print(f"\nHuman population summary:")
print(f"  Peak infected: {max(I_h):.0f} on day {np.argmax(I_h)+1}")
print(f"  Final recovered: {R_h[-1]:.0f} ({100*R_h[-1]/N_h:.1f}%)")
print(f"\nMosquito population summary:")
print(f"  Peak infected: {max(I_m):.0f} on day {np.argmax(I_m)+1}")
print(f"  Final infected: {I_m[-1]:.0f} ({100*I_m[-1]/N_m:.1f}%)")