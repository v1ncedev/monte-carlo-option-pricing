import numpy as np

class MonteCarloOption:
    def __init__(self, S0, K, T, r, sigma, n_sims=100000, seed=None):
        """
        Monte Carlo Option Pricing

        Parameters:
        -----------
        S0 : float  - initial stock price
        K  : float  - strike price
        T  : float  - time to maturity (in years)
        r  : float  - risk-free interest rate
        sigma : float - volatility (annualised)
        n_sims : int - number of Monte Carlo simulations
        seed : int - random seed for reproducibility
        """
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.n_sims = n_sims
        if seed is not None:
            np.random.seed(seed)

    def simulate_price_paths(self):
        """Simulate terminal stock price using Geometric Brownian Motion."""
        Z = np.random.standard_normal(self.n_sims)   # random draws
        ST = self.S0 * np.exp(
            (self.r - 0.5 * self.sigma**2) * self.T + 
            self.sigma * np.sqrt(self.T) * Z
        )
        return ST

    def price_european_call(self):
        """Price a European Call option via Monte Carlo."""
        ST = self.simulate_price_paths()
        payoff = np.maximum(ST - self.K, 0)
        price = np.exp(-self.r * self.T) * np.mean(payoff)
        return price

    def price_european_put(self):
        """Price a European Put option via Monte Carlo."""
        ST = self.simulate_price_paths()
        payoff = np.maximum(self.K - ST, 0)
        price = np.exp(-self.r * self.T) * np.mean(payoff)
        return price
