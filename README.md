# Blackjack Strategy Battle

This project simulates a **Round-Robin Blackjack Tournament** where multiple strategies face off in a series of Blackjack games. Each strategy represents a different approach to the game of Blackjack, and the goal is to assess how well each strategy performs across multiple matches. The tournament evaluates the strategies based on key performance metrics such as **win rate**, **bust rate**, **average hand value**, and other factors.

## Table of Contents

1. [Introduction](#introduction)
2. [How It Works](#how-it-works)
3. [Strategies](#strategies)
4. [Tournament Structure](#tournament-structure)
5. [Metrics and Evaluation](#metrics-and-evaluation)
6. [Usage](#usage)
7. [Requirements](#requirements)
8. [License](#license)

## Introduction

The project simulates a **Blackjack game** between two players using different strategies. The strategies are evaluated based on how often they win, lose, and bust, as well as the quality of their gameplay in terms of hand value, consistency, and risk-to-reward ratios. The project organizes these strategies into a **Round-Robin tournament**, where each strategy faces every other strategy in a series of matches.

## How It Works

1. **Blackjack Game**: A single round of Blackjack is simulated between two strategies. Both players are dealt two cards and will continue to draw cards until they reach a hand value of 17 or higher.
   
2. **Strategies**: The strategies are represented as different classes (e.g., **Conservative**, **Aggressive**, **Balanced**, etc.) that define how a player behaves during the game. These strategies determine how the player draws cards and when they stop.

3. **Tournament**: A round-robin tournament is played between the strategies. In a round-robin format, each strategy faces every other strategy once. The results are collected and used to generate detailed performance metrics.

4. **Metrics and Rankings**: After the tournament, each strategy's performance is evaluated based on several key metrics, including:
   - **Win Rate**: Percentage of games won.
   - **Bust Rate**: Percentage of games where the strategy busts (goes over 21).
   - **Average Hand Value**: The average value of the hand at the end of the game.
   - **Consistency**: Standard deviation of hand values (lower values mean more consistent performance).
   - **Risk-to-Reward Ratio**: A measure of how often a strategy busts versus how often it wins.

5. **Final Rankings**: Based on the metrics, the strategies are ranked from best to worst. The final rankings consider both **basic statistics** (e.g., wins, losses, busts) and **advanced metrics** (e.g., consistency, risk-to-reward ratio).

## Strategies

The tournament supports multiple predefined strategies, each with a different approach to playing Blackjack. Some of the possible strategies are:

- **Conservative Strategy**: Focuses on minimizing risk by sticking to low-risk card draws.
- **Aggressive Strategy**: Takes high-risk actions by drawing cards more aggressively, aiming for higher hand values.
- **Balanced Strategy**: A middle ground between the aggressive and conservative approaches, balancing risk and reward.
- **Cautious Strategy**: Similar to the conservative strategy, but with a more cautious approach to busting.
- **Gambler Strategy**: Takes risks with the intention of maximizing potential wins, even if it means busting more often.

Each strategy has its own behavior for how cards are drawn and when to stop.

## Tournament Structure

The tournament follows a **Round-Robin** format:
1. Each strategy plays against every other strategy once.
2. A total of **num_simulations** rounds are played, which means each match-up occurs multiple times to ensure fairness.
3. After all the matches are played, performance metrics for each strategy are calculated, and the strategies are ranked.

## Metrics and Evaluation

Each strategy is evaluated based on the following metrics:

1. **Basic Stats**:
   - **Matches Played**: Total number of games the strategy participated in.
   - **Wins**: Total number of games the strategy won.
   - **Losses**: Total number of games the strategy lost.
   - **Busts**: Total number of times the strategy busted (went over 21).

2. **Advanced Metrics**:
   - **Win Rate**: Percentage of games won.
   - **Bust Rate**: Percentage of games where the strategy busts.
   - **Average Hand Value**: The average value of the hand at the end of the game.
   - **Consistency (Std. Dev.)**: Standard deviation of hand values across all games. Lower values represent more consistent performance.
   - **Risk-to-Reward Ratio**: The ratio of bust rate to win rate, indicating the balance between taking risks and achieving rewards.

3. **Final Rating**: All metrics are normalized and combined into a final rating. A small random perturbation is added to avoid ties. The strategies are then ranked based on this rating.

## Usage

To run the **Blackjack Strategy Battle**:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/blackjack-strategy-battle.git
   cd blackjack-strategy-battle
   ```

2. Define your strategies or use the predefined ones in the `strategies.py` file.

3. Run the main script to start the tournament:

   ```bash
   python main.py
   ```

4. View the tournament results, which will include both basic stats (e.g., wins, losses, busts) and detailed performance metrics (e.g., win rate, risk-to-reward ratio, consistency, etc.).

## Requirements

The project requires Python 3.x and the following libraries:

- **math** (for statistical calculations)
- **random** (for simulating randomness in card dealing)

To install the required dependencies, create a virtual environment and install them:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Example Output

After running the tournament, you will see an output like this:

```
Strategy: Conservative
  Matches Played: 15
  Wins: 8
  Losses: 6
  Busts: 1
  Win Rate: 53.33%
  Bust Rate: 6.67%
  Avg Hand Value: 17.18
  Consistency (Std. Dev.): 1.25
  Risk-to-Reward Ratio: 0.30
  Rating: 0.73867485

Strategy: Aggressive
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

Final Rankings:
1. Aggressive - Rating: 0.76254830
2. Conservative - Rating: 0.73867485
...
```
