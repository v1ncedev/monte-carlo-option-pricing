# Monte Carlo Option Pricing

##  Overview
This project implements **Monte Carlo simulations** to price European options and compares them against the **Black–Scholes analytical solution**.  

Monte Carlo methods are widely used in **quantitative finance** when closed-form solutions are unavailable (e.g., exotic options).  
This repo demonstrates:
- Simulation of stock price paths under **Geometric Brownian Motion (GBM)**
- Pricing **European Call & Put options** via Monte Carlo
- Benchmarking against the **Black–Scholes model**
- Visualising **distributions** and **convergence**

---

##  The Mathematics

Stock prices are assumed to follow **Geometric Brownian Motion (GBM):**

\[
dS_t = r S_t \, dt + \sigma S_t \, dW_t
\]

where:
- \( S_t \) = stock price at time \( t \)  
- \( r \) = risk-free interest rate  
- \( \sigma \) = volatility  
- \( W_t \) = Wiener process (Brownian motion)  

The **Black–Scholes formula** for a European call is:

\[
C = S_0 \Phi(d_1) - K e^{-rT} \Phi(d_2)
\]

\[
d_1 = \frac{\ln(S_0/K) + (r + \tfrac{1}{2}\sigma^2)T}{\sigma \sqrt{T}}, 
\quad d_2 = d_1 - \sigma \sqrt{T}
\]

The put price follows from **put–call parity**:

\[
P = K e^{-rT} \Phi(-d_2) - S_0 \Phi(-d_1)
\]

Monte Carlo estimates option price as the **discounted average payoff**:

\[
C \approx e^{-rT} \frac{1}{N} \sum_{i=1}^N \max(S_T^{(i)} - K, 0)
\]

\[
P \approx e^{-rT} \frac{1}{N} \sum_{i=1}^N \max(K - S_T^{(i)}, 0)
\]

---

##  Usage

### 1. Clone the repo
```bash
git clone https://github.com/YOURUSERNAME/monte-carlo-option-pricing.git
cd monte-carlo-option-pricing
