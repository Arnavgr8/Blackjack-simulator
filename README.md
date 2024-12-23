---

# Blackjack Strategy Battle

Welcome to the **Blackjack Strategy Battle**! This project simulates a series of Blackjack games between various strategies and evaluates their performance based on key metrics. Participants are invited to contribute their own Blackjack strategies and see how well they fare against others in a tournament setup.

## Table of Contents

1. [Introduction](#introduction)
2. [Basic Rules of Blackjack](#basic-rules-of-blackjack)
3. [Tournament Evaluation Criteria](#tournament-evaluation-criteria)
4. [How to Participate](#how-to-participate)
5. [Usage](#usage)
6. [Requirements](#requirements)
7. [License](#license)

## Introduction

In this project, multiple Blackjack strategies face off against each other in a **Round-Robin Tournament**. The goal is to see which strategies perform the best in terms of wins, consistency, and overall game management. Every strategy will be evaluated based on its performance in the tournament, and rankings will be generated accordingly.

## Basic Rules of Blackjack

Before participating in the tournament, it's important to understand the basic rules of **Blackjack** that govern the game:

1. **Objective**: The goal of Blackjack is to have a hand value as close to 21 as possible without going over. A hand that exceeds 21 is called a **bust**, and the player loses that round.
   
2. **Card Values**:
   - Number cards (2-10) are worth their face value.
   - Face cards (Jack, Queen, King) are each worth 10 points.
   - Aces can be worth either 1 or 11 points, depending on which value keeps the hand under 21.
   
3. **Gameplay**:
   - Both players are dealt two cards at the start of the game.
   - Players may choose to **hit** (draw a card) or **stand** (end their turn) based on their hand's value.
   - Players continue drawing cards until they either reach a hand value of 17 or higher or bust.
   - A player who exceeds 21 with their hand value is said to have **busted** and automatically loses the round.

4. **Winning**: The player whose hand value is closer to 21, without exceeding it, wins the round. If both players have the same hand value, the round is a **tie**.

---

## Tournament Evaluation Criteria

The performance of each strategy will be evaluated based on the following **criteria**:

1. **Basic Stats**:
   - **Matches Played**: Total number of games the strategy participated in.
   - **Wins**: Total number of games won by the strategy.
   - **Losses**: Total number of games lost by the strategy.
   - **Busts**: Total number of times the strategy busted (hand value exceeds 21).

2. **Advanced Metrics**:
   - **Win Rate**: Percentage of games won by the strategy. This is a measure of how effective the strategy is in winning rounds.
   - **Bust Rate**: Percentage of games where the strategy busts. A lower bust rate is generally better.
   - **Average Hand Value**: The average value of the hand at the end of the game. A hand value closer to 21 is considered better.
   - **Consistency**: Measured as the standard deviation of the hand values across all games played by the strategy. Lower values indicate more consistent performance.
   - **Risk-to-Reward Ratio**: A measure of how often a strategy busts compared to how often it wins. A lower ratio indicates a better balance between risk and reward.

3. **Final Rating**: The final rating for each strategy is computed by normalizing and combining the metrics mentioned above. A small random perturbation is added to avoid ties. Strategies with the highest ratings will be ranked the best.

---

## How to Participate

To participate in the **Blackjack Strategy Battle**, follow these steps:

1. **Create Your Strategy**:
   - Write your own Blackjack strategy code by implementing the `play` method inside a new class. Your class should inherit from the `StrategyBase` class.
   - The strategy you create should decide whether to **hit** or **stand** based on the hand value.

2. **Naming Your Strategy**:
   - Your strategy class should be named after your school's name followed by "Strategy". For example, if your school is *"WhateverPublicSchool"*, your class name should be `WhateverPublicSchoolStrategy`.
   
3. **Filing Your Code**:
   - Save your strategy class code in a file named after your school. For example, if you are from *"WhateverPublicSchool"*, your filename should be `WhateverPublicSchool.py`.
   - Push your code to the repository in the `strategies/` directory.

4. **Format of Your Code**:
   - Your code should be placed in the `strategies` directory, and the class name should match the filename.
   - Example class:
   
     ```python
     class WhateverPublicSchoolStrategy(StrategyBase):
         def __init__(self):
             super().__init__("WhateverPublicSchool")

         def play(self, hand, deck):
             # Your strategy implementation here
             pass
     ```

---

## Usage

Once you’ve added your strategy, you can participate in the tournament by running the main script.

1. Clone the repository:
   
   ```bash
   git clone https://github.com/yourusername/blackjack-strategy-battle.git
   cd blackjack-strategy-battle
   ```

2. Add your strategy class in the `strategies/` directory (as per the instructions above).

3. Run the tournament:

   ```bash
   python main.py
   ```

4. View the results, which will display:
   - Basic statistics (matches played, wins, losses, busts).
   - Performance metrics such as win rate, bust rate, and average hand value.
   - Final rankings of all strategies.

---

## Requirements

This project requires Python 3.x. You can install the necessary dependencies by creating a virtual environment and running:

```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Example Output

After the tournament, you will see something like this:

```
Strategy: WhateverPublicSchool
  Matches Played: 15
  Wins: 10
  Losses: 5
  Busts: 2
  Win Rate: 66.67%
  Bust Rate: 13.33%
  Avg Hand Value: 18.32
  Consistency (Std. Dev.): 1.18
  Risk-to-Reward Ratio: 0.50
  Rating: 0.76254830

Strategy: AnotherInternationalSchool
  Matches Played: 15
  Wins: 8
  Losses: 7
  Busts: 1
  Win Rate: 53.33%
  Bust Rate: 6.67%
  Avg Hand Value: 17.12
  Consistency (Std. Dev.): 1.25
  Risk-to-Reward Ratio: 0.30
  Rating: 0.73867485

Final Rankings:
1. WhateverPublicSchool - Rating: 0.76254830
2. AnotherInternationalSchool - Rating: 0.73867485
...
```

This will give you an overview of how each strategy performed and its final ranking in the tournament.

---
