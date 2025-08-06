import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def sir_model(t, y, beta, gamma):
    """
    SIR model differential equations
    """
    S, I, R = y
    N = S + I + R

    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I

    return [dSdt, dIdt, dRdt]

def generate_sir_synthetic_data(
    N=1000,
    beta=0.8,
    gamma=0.1,
    I0=1,
    n_days=50,
    observation_noise='poisson',
    noise_scale=1.0,
    seed=42,
    save_to_csv=True,
    plot=True
):
    """
    Generate synthetic epidemic data by solving the SIR equations.

    Parameters:
    -----------
    N : int
        Total population size
    beta : float
        Transmission rate
    gamma : float
        Recovery rate
    I0 : int
        Initial number of infected
    n_days : int
        Number of days to simulate
    observation_noise : str
        Type of observation noise ('poisson', 'negative_binomial', 'normal')
    noise_scale : float
        Scale of observation noise
    seed : int
        Random seed
    save_to_csv : bool
        Whether to save to CSV
    plot : bool
        Whether to plot

    Returns:
    --------
    pd.DataFrame with true SIR trajectories and noisy observations
    """

    np.random.seed(seed)

    # Initial conditions
    S0 = N - I0
    R0 = 0
    y0 = [S0, I0, R0]

    # Time points
    t_eval = np.arange(0, n_days + 1)

    # Solve SIR equations
    sol = solve_ivp(
        sir_model,
        [0, n_days],
        y0,
        args=(beta, gamma),
        t_eval=t_eval,
        dense_output=True,
        rtol=1e-8
    )

    if not sol.success:
        raise ValueError("SIR integration failed")

    # Extract trajectories
    S_true = sol.y[0]
    I_true = sol.y[1]
    R_true = sol.y[2]

    # Remove t=0 and keep only days 1 to n_days
    S_true = S_true[1:]
    I_true = I_true[1:]
    R_true = R_true[1:]
    days = np.arange(1, n_days + 1)

    # Add observation noise to infected counts
    if observation_noise == 'poisson':
        # Standard Poisson noise
        observed_cases = np.random.poisson(I_true * noise_scale)
    elif observation_noise == 'negative_binomial':
        # Negative binomial for overdispersion
        # Convert to negative binomial parameterization
        mu = I_true * noise_scale
        # Set overdispersion parameter (smaller = more overdispersed)
        r = 10  # You can adjust this
        p = r / (r + mu)
        observed_cases = np.random.negative_binomial(r, p)
    elif observation_noise == 'normal':
        # Normal noise (ensure non-negative)
        noise_std = np.sqrt(I_true * noise_scale)
        observed_cases = np.random.normal(I_true, noise_std)
        observed_cases = np.maximum(0, observed_cases).astype(int)
    else:
        # No noise
        observed_cases = I_true.astype(int)

    # Create DataFrame
    df = pd.DataFrame({
        'day': days,
        'S_true': S_true,
        'I_true': I_true,
        'R_true': R_true,
        'observed_cases': observed_cases
    })

    # Calculate R0 and other epidemic characteristics
    R0_true = beta / gamma
    infectious_period = 1 / gamma
    peak_day = days[np.argmax(I_true)]
    peak_infected = np.max(I_true)
    total_infected = R_true[-1]
    attack_rate = total_infected / N * 100

    print(f"\nTrue epidemic parameters:")
    print(f"  β = {beta:.3f}")
    print(f"  γ = {gamma:.3f}")
    print(f"  R₀ = {R0_true:.3f}")
    print(f"  Infectious period = {infectious_period:.1f} days")
    print(f"  Peak day = {peak_day}")
    print(f"  Peak infected = {peak_infected:.1f}")
    print(f"  Total infected = {total_infected:.1f}")
    print(f"  Attack rate = {attack_rate:.1f}%")

    # Save to CSV
    if save_to_csv:
        filename = f'sir_synthetic_data_beta{beta:.2f}_gamma{gamma:.2f}_N{N}_days{n_days}.csv'
        df.to_csv(filename, index=False)
        print(f"\nData saved to: {filename}")

    # Plot results
    if plot:
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))

        # Plot 1: True SIR trajectories
        axes[0, 0].plot(days, S_true, 'b-', label='Susceptible', linewidth=2)
        axes[0, 0].plot(days, I_true, 'r-', label='Infected', linewidth=2)
        axes[0, 0].plot(days, R_true, 'g-', label='Recovered', linewidth=2)
        axes[0, 0].set_xlabel('Days')
        axes[0, 0].set_ylabel('Number of people')
        axes[0, 0].set_title('True SIR Trajectories')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)

        # Plot 2: Observed vs true infected
        axes[0, 1].scatter(days, observed_cases, color='black', s=20, alpha=0.6,
                          label='Observed (with noise)', zorder=3)
        axes[0, 1].plot(days, I_true, 'r-', label='True infected', linewidth=2, zorder=2)
        axes[0, 1].set_xlabel('Days')
        axes[0, 1].set_ylabel('Number of infected')
        axes[0, 1].set_title('Observed vs True Infected')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)

        # Plot 3: Phase plot (S vs I)
        axes[1, 0].plot(S_true, I_true, 'purple', linewidth=2)
        axes[1, 0].scatter(S_true[0], I_true[0], color='green', s=50, label='Start', zorder=3)
        axes[1, 0].scatter(S_true[-1], I_true[-1], color='red', s=50, label='End', zorder=3)
        axes[1, 0].set_xlabel('Susceptible')
        axes[1, 0].set_ylabel('Infected')
        axes[1, 0].set_title('Phase Plot (S vs I)')
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)

        # Plot 4: Daily incidence (new cases)
        daily_incidence = np.diff(R_true)
        daily_incidence = np.concatenate([[I_true[0]], daily_incidence])  # Add first day
        axes[1, 1].plot(days, daily_incidence, 'orange', linewidth=2, label='True daily incidence')
        axes[1, 1].scatter(days, observed_cases, color='black', s=20, alpha=0.6,
                          label='Observed infected', zorder=3)
        axes[1, 1].set_xlabel('Days')
        axes[1, 1].set_ylabel('Number of cases')
        axes[1, 1].set_title('Daily Incidence vs Observed')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('sir_synthetic_data_validation.png', dpi=300, bbox_inches='tight')
        plt.show()

    return df

def generate_multiple_sir_scenarios():
    """Generate multiple SIR scenarios with different parameters."""

    scenarios = [
        {"name": "Low transmission", "beta": 0.5, "gamma": 0.1},
        {"name": "Medium transmission", "beta": 0.8, "gamma": 0.1},
        {"name": "High transmission", "beta": 1.2, "gamma": 0.1},
        {"name": "Fast recovery", "beta": 0.8, "gamma": 0.2},
        {"name": "Slow recovery", "beta": 0.8, "gamma": 0.05},
    ]

    all_dfs = {}

    plt.figure(figsize=(15, 10))

    for i, scenario in enumerate(scenarios):
        print(f"\n{'='*50}")
        print(f"Generating: {scenario['name']}")
        print(f"{'='*50}")

        df = generate_sir_synthetic_data(
            beta=scenario['beta'],
            gamma=scenario['gamma'],
            plot=False,
            save_to_csv=True
        )

        all_dfs[scenario['name']] = df

        # Plot infected trajectories
        plt.subplot(2, 3, i + 1)
        plt.plot(df['day'], df['I_true'], 'r-', linewidth=2, label='True')
        plt.scatter(df['day'], df['observed_cases'], color='black', s=10, alpha=0.6, label='Observed')
        plt.title(f"{scenario['name']}\nR₀={scenario['beta']/scenario['gamma']:.1f}")
        plt.xlabel('Days')
        plt.ylabel('Infected')
        plt.legend()
        plt.grid(True, alpha=0.3)

    # Summary comparison plot
    plt.subplot(2, 3, 6)
    for name, df in all_dfs.items():
        plt.plot(df['day'], df['I_true'], linewidth=2, label=name)
    plt.xlabel('Days')
    plt.ylabel('Infected')
    plt.title('All Scenarios Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('sir_multiple_scenarios.png', dpi=300, bbox_inches='tight')
    plt.show()

    return all_dfs

if __name__ == "__main__":
    # Generate default dataset with parameters that should work well for inference
    print("Generating SIR synthetic data...")
    df = generate_sir_synthetic_data(
        N=1000,
        beta=0.8,
        gamma=0.1,
        I0=1,
        n_days=50,
        observation_noise='negative_binomial',
        noise_scale=1.0,
        seed=42
    )

    print("\nFirst 10 rows:")
    print(df.head(10))

    print("\nLast 10 rows:")
    print(df.tail(10))

    # Generate multiple scenarios
    print("\n\nGenerating multiple SIR scenarios...")
    all_scenarios = generate_multiple_sir_scenarios()

    print("\n\nAll SIR synthetic datasets generated!")
    print("\nFiles created:")
    print("- sir_synthetic_data_beta0.80_gamma0.10_N1000_days50.csv (main dataset)")
    print("- sir_synthetic_data_validation.png (validation plots)")
    print("- sir_multiple_scenarios.png (comparison plots)")
