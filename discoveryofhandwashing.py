import pandas as pd
yearly = pd.read_csv('https://raw.githubusercontent.com/debadrita1517/Discovery-of-Hand-Washing/main/yearly_deaths_by_clinic.csv')
yearly

yearly["proportion_deaths"] = yearly["deaths"] / yearly["births"]
yearly1 = yearly[yearly["clinic"] == "clinic 1"]
yearly2 = yearly[yearly["clinic"] == "clinic 2"]
yearly1

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
ax = yearly1.plot(x="year", y="proportion_deaths", label="Clinic 1")
yearly2.plot(x="year", y="proportion_deaths", label="Clinic 2", ax=ax)
ax.set_ylabel("Proportion deaths")

monthly = pd.read_csv('https://raw.githubusercontent.com/debadrita1517/Discovery-of-Hand-Washing/main/monthly_deaths.csv', parse_dates=["date"])
monthly["proportion_deaths"] = monthly["deaths"] / monthly["births"]
monthly.head()

ax = monthly.plot(x="date", y="proportion_deaths")
ax.set_ylabel("Proportion deaths")

import pandas as pd
handwashing_start = pd.to_datetime('1847-06-01')
before_washing = monthly[monthly["date"] < handwashing_start]
after_washing = monthly[monthly["date"] >= handwashing_start]
ax = before_washing.plot(x="date", y="proportion_deaths",
                         label="Before handwashing")
after_washing.plot(x="date", y="proportion_deaths",
                   label="After handwashing", ax=ax)
ax.set_ylabel("Proportion deaths")

before_proportion = before_washing["proportion_deaths"]
after_proportion = after_washing["proportion_deaths"]
mean_diff = after_proportion.mean() - before_proportion.mean()
mean_diff

# A bootstrap analysis of the reduction of deaths due to handwashing
boot_mean_diff = []
for i in range(3000):
    boot_before = before_proportion.sample(frac=1, replace=True)
    boot_after = after_proportion.sample(frac=1, replace=True)
    boot_mean_diff.append( boot_after.mean() - boot_before.mean() )
# Calculating a 95% confidence interval from boot_mean_diff 
confidence_interval = pd.Series(boot_mean_diff).quantile([0.025, 0.975])
confidence_interval

# The data Semmelweis collected points to that:
doctors_should_wash_their_hands = False
