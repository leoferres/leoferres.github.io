import numpy as np
import matplotlib.pyplot as plt
import cmdstanpy

# Compile the model
model = cmdstanpy.CmdStanModel(stan_file='seir0.stan')

# Set up data
N = 1000
n_days = 100
ts = list(range(1, n_days + 1))

data = {
    'n_days': 100,
    't0': 0,
    'y0': [N-1, 0, 1, 0],  # [S0, E0, I0, R0]
    'ts': ts,
    'beta': 0.5,
    'sigma': 0.2,  # 1/incubation period (5 days)
    'gamma': 0.1
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
S = y[0, :, 0]
E = y[0, :, 1]
I = y[0, :, 2]
R = y[0, :, 3]

R0 = data['beta'] / data['gamma']
print(f"Basic reproduction number R₀ = {R0}")

# Plot
plt.figure(figsize=(10, 6))
plt.plot(range(1, 101), S, label='Susceptible', color='blue')
plt.plot(range(1, 101), E, label='Exposed', color='orange')
plt.plot(range(1, 101), I, label='Infected', color='red')
plt.plot(range(1, 101), R, label='Recovered', color='green')
plt.xlabel('Days')
plt.ylabel('Number of people')
plt.title(f'SEIR Model (Stan) - R₀ = {R0}')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('seir0.png', dpi=300, bbox_inches='tight')
