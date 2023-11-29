import gymnasium as gym
import random
import numpy as np


class WeatherEnv(gym.Env):
    def __init__(self):
        super(WeatherEnv, self).__init__()
        # Action space: [Accessory (3 options), Clothing (3 options)]
        self.action_space = gym.spaces.MultiDiscrete(
            [3, 3]
        )  # 0: Umbrella, 1: Snow Boots, 2: Sunscreen for accessory; Warm, Medium, Summer for clothing

        # State space: 7 days of temperature and weather conditions
        self.observation_space = gym.spaces.Dict(
            {
                "temperature": gym.spaces.Box(
                    low=-50, high=120, shape=(7,), dtype=float
                ),
                "conditions": gym.spaces.MultiDiscrete(
                    [3] * 7
                ),  # 0: Snow, 1: Rain, 2: Sunny
            }
        )

    def reset(self):
        temperatures = [random.uniform(-50, 120) for _ in range(7)]
        conditions = [random.randint(0, 2) for _ in range(7)]

        # Adjust conditions based on temperatures
        # no snow if temperature is above 50
        conditions = [
            1 if temp > 50 and condition == 0 else condition
            for temp, condition in zip(temperatures, conditions)
        ]

        self.state = {"temperature": temperatures, "conditions": conditions}
        return self.state

    def step(self, action):
        correct_decisions = self._decide_optimal_choices(self.state)
        reward = sum([50 if action[i] == correct_decisions[i] else 0 for i in range(2)])
        done = True
        return self.state, reward, done, {}

    def _decide_optimal_choices(self, state):
        # Determine the ideal accessory based on the most common weather condition
        most_common_condition = max(
            set(state["conditions"]), key=state["conditions"].count
        )
        accessory_choice = self._decide_accessory(most_common_condition)

        # Determine the ideal clothing based on the average temperature
        average_temp = np.mean(state["temperature"])
        clothing_choice = self._decide_clothing(average_temp)

        return [accessory_choice, clothing_choice]

    def _decide_accessory(self, weather_condition):
        # 0: Umbrella for Rain, 1: Snow Boots for Snow, 2: Sunscreen for Sunny
        if weather_condition == 1:  # Rain
            print("Umbrella")
            return 0
        elif weather_condition == 0:  # Snow
            print("Snow Boots")
            return 1
        else:  # Sunny
            print("Sunscreen")
            return 2

    def _decide_clothing(self, average_temp):
        # 0: Warm, 1: Medium, 2: Summer
        if average_temp < 32:  # Below freezing
            print("Warm")
            return 0
        elif 32 <= average_temp < 70:  # Moderate
            print("Medium")
            return 1
        else:  # Warm
            print("Summer")
            return 2

    def render(self, mode="human"):
        print(f"Current State: {self.state}")


if __name__ == "__main__":
    env = WeatherEnv()
    for _ in range(5):  # Run 5 test cases
        state = env.reset()
        action = env.action_space.sample()  # Random action
        next_state, reward, done, info = env.step(action)
        print(f"State: {state}, Action: {action}, Reward: {reward}, Done: {done}")
