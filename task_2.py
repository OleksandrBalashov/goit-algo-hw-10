import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x**2

a, b = 0, 2

# Monte-Karlo method
N = 100000
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)


under_curve = y_rand < f(x_rand)
monte_carlo_integral = (under_curve.sum() / N) * (b * f(b))

# Method quad
quad_result, error = spi.quad(f, a, b)

# Results
print(f"Monte-Karlo method: {monte_carlo_integral}")
print(f"Quad method: {quad_result}, with error {error}")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(np.linspace(a, b), f(np.linspace(a, b)), color='gray', alpha=0.3)
ax.scatter(x_rand[under_curve], y_rand[under_curve], color='blue', s=0.5, alpha=0.3, label='Під кривою')
ax.scatter(x_rand[~under_curve], y_rand[~under_curve], color='red', s=0.5, alpha=0.3, label='Над кривою')
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Monte-Karlo method: {monte_carlo_integral:.5f}\nMethod quad: {quad_result:.5f}')
plt.legend()
plt.grid()
plt.show()