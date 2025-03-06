import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Генериране на кампании
def generate_campaigns(num_campaigns):
    campaigns = []
    for i in range(num_campaigns):
        campaigns.append({
            "Campaign": f"Campaign {i + 1}",
            "ROI": np.random.uniform(1.2, 2.5),  # Случайно ROI
            "Conversion Rate": np.random.uniform(0.01, 0.2)  # Случайна конверсия
        })
    return pd.DataFrame(campaigns)

# Симулиране на резултати
def simulate_results(budget_distribution, campaigns, total_budget):
    rewards = []
    for i, campaign in campaigns.iterrows():
        budget = budget_distribution[i] * total_budget
        conversions = budget * campaign["Conversion Rate"]
        reward = conversions * campaign["ROI"]
        rewards.append(reward)
    return sum(rewards)

# Основна функция за Streamlit
def main():
    st.title("Marketing Budget Simulation")
    st.write("Разпределете бюджета между различни кампании и симулирайте резултатите.")

    # Настройки
    total_budget = 10000
    num_campaigns = 3

    # Генериране на кампании
    campaigns = generate_campaigns(num_campaigns)
    st.subheader("Campaign Details")
    st.write(campaigns)

    # Слайдъри за разпределение на бюджета
    st.subheader("Budget Allocation")
    budget_distribution = []
    for i in range(num_campaigns):
        allocation = st.slider(f"Budget for {campaigns.loc[i, 'Campaign']}", 0, 100, 33, step=1)
        budget_distribution.append(allocation / 100)

    # Проверка за общо разпределение
    if sum(budget_distribution) > 1:
        st.error("The total budget allocation exceeds 100%. Adjust the sliders.")
        return

    # Бутон за симулация
    if st.button("Simulate"):
        reward = simulate_results(budget_distribution, campaigns, total_budget)
        st.success(f"Total Reward: {reward:.2f}")

        # Визуализация на разпределението
        fig, ax = plt.subplots()
        ax.pie(budget_distribution, labels=campaigns["Campaign"], autopct='%1.1f%%', startangle=90, colors=["#ff9999", "#66b3ff", "#99ff99"])
        ax.axis('equal')
        ax.set_title("Budget Distribution")
        st.pyplot(fig)

# Стартиране на приложението
if __name__ == "__main__":
    main()
