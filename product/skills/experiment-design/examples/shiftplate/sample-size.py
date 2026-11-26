"""Sample-size maths for the Shiftplate check-in experiment.

Standard library only. Run: python3 sample-size.py
Every input below is assumed; change them and rerun.
"""
import math
import random
from statistics import NormalDist, mean, stdev

random.seed(11)
Z = NormalDist()
ALPHA, POWER = 0.05, 0.80
ZA, ZB = Z.inv_cdf(1 - ALPHA / 2), Z.inv_cdf(POWER)

BASELINE = 0.40          # assumed: current check-in completion per worked shift
MDE = 0.20               # smallest rise worth acting on (absolute)
NURSES = 20
SHIFTS_PER_NURSE = 12    # assumed: 3 twelve-hour shifts a week for 4 weeks
TAU = 0.10               # assumed: how much the true effect varies between nurses


def t_quantile(p, df):
    """Student t quantile by bisection on a Simpson-rule CDF."""
    c = math.gamma((df + 1) / 2) / (math.sqrt(df * math.pi) * math.gamma(df / 2))
    pdf = lambda t: c * (1 + t * t / df) ** (-(df + 1) / 2)

    def cdf(x, steps=4000):
        h = x / steps
        s = pdf(0) + pdf(x) + sum((4 if i % 2 else 2) * pdf(i * h) for i in range(1, steps))
        return 0.5 + s * h / 3

    lo, hi = 0.0, 10.0
    for _ in range(50):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if cdf(mid) < p else (lo, mid)
    return (lo + hi) / 2


def n_two_proportions(p1, p2):
    pbar = (p1 + p2) / 2
    num = (ZA * math.sqrt(2 * pbar * (1 - pbar)) + ZB * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return num / (p2 - p1) ** 2


def mde_two_proportions(n, p1):
    lo, hi = 0.001, 0.59
    for _ in range(60):
        d = (lo + hi) / 2
        lo, hi = (d, hi) if n_two_proportions(p1, p1 + d) > n else (lo, d)
    return d


print("1. Independent shifts, 40% -> 60%")
n = n_two_proportions(BASELINE, BASELINE + MDE)
print(f"   {math.ceil(n)} shifts per group (rule of thumb 16*p(1-p)/d^2 = {16 * 0.24 / MDE**2:.0f})")

print("\n2. A/B by nurse: 10 nurses per group, 12 shifts each = 120 shifts per group")
for icc in (0.1, 0.2, 0.3, 0.5):
    deff = 1 + (SHIFTS_PER_NURSE - 1) * icc
    eff = NURSES / 2 * SHIFTS_PER_NURSE / deff
    print(f"   ICC {icc}: design effect {deff:.2f}, effective n {eff:.1f}, "
          f"reachable MDE {mde_two_proportions(eff, BASELINE) * 100:.0f} points, "
          f"nurses needed per group for +20 {math.ceil(n * deff / SHIFTS_PER_NURSE)}")

print("\n3. Crossover: every nurse uses both versions, 6 shifts each")
k = SHIFTS_PER_NURSE // 2
for nurses in (20, 16):
    t1, t2 = t_quantile(0.975, nurses - 1), t_quantile(POWER, nurses - 1)
    for tau in (0.0, 0.10, 0.15):
        sd = math.sqrt(0.24 / k + 0.24 / k + tau**2)
        print(f"   {nurses} nurses, tau {tau}: sd of difference {sd:.3f}, "
              f"reachable MDE {(t1 + t2) * sd / math.sqrt(nurses) * 100:.1f} points")


def beta(mu, icc):
    s = 1 / icc - 1
    return random.betavariate(mu * s, (1 - mu) * s)


def simulate_ab(effect, icc=0.3, reps=3000):
    crit, hits = t_quantile(0.975, 18), 0
    for _ in range(reps):
        a = [sum(random.random() < p for _ in range(SHIFTS_PER_NURSE)) / SHIFTS_PER_NURSE
             for p in (beta(BASELINE, icc) for _ in range(10))]
        b = [sum(random.random() < p for _ in range(SHIFTS_PER_NURSE)) / SHIFTS_PER_NURSE
             for p in (beta(BASELINE + effect, icc) for _ in range(10))]
        sp = math.sqrt((stdev(a) ** 2 + stdev(b) ** 2) / 2)
        hits += abs(mean(b) - mean(a)) / (sp * math.sqrt(2 / 10)) > crit
    return hits / reps


def simulate_crossover(effect, nurses=20, icc=0.3, tau=TAU, reps=3000):
    crit, hits = t_quantile(0.975, nurses - 1), 0
    for _ in range(reps):
        diffs = []
        for _ in range(nurses):
            p = beta(BASELINE, icc)
            q = min(max(p + effect + random.gauss(0, tau if effect else 0), 0), 1)
            diffs.append(sum(random.random() < q for _ in range(k)) / k
                         - sum(random.random() < p for _ in range(k)) / k)
        s = stdev(diffs)
        hits += s > 0 and abs(mean(diffs)) / (s / math.sqrt(nurses)) > crit
    return hits / reps


print("\n4. Simulated power (3,000 runs each, ICC 0.3)")
print(f"   A/B by nurse, true +20: {simulate_ab(0.20):.0%}")
print(f"   Crossover, 20 nurses, true +20: {simulate_crossover(0.20):.0%}")
print(f"   Crossover, 20 nurses, true +15: {simulate_crossover(0.15):.0%}")
print(f"   Crossover, 16 nurses, true +20: {simulate_crossover(0.20, nurses=16):.0%}")
print(f"   Crossover, 20 nurses, no effect (false positives): {simulate_crossover(0.0):.0%}")

print("\n5. Guardrail precision: 40 audited binned portions per version (assumed), 80% caught")
print(f"   95% interval half-width: +/-{1.96 * math.sqrt(0.8 * 0.2 / 40) * 100:.0f} points")
