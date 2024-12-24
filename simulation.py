import math
import random
from strategies import *  # Importing predefined strategies (assumed to be defined elsewhere)

class BlackjackGame:
    """Simulates a simple blackjack game between two players using two strategies."""

    def __init__(self, strategy1, strategy2):
        """
        Initializes the game with two strategies and creates a shuffled deck.

        :param strategy1: First player's strategy (object).
        :param strategy2: Second player's strategy (object).
        """
        self.strategy1 = strategy1
        self.strategy2 = strategy2
        self.deck = self.create_deck()

    def create_deck(self):
        """
        Creates and shuffles a standard deck of cards represented by integers.

        The deck contains:
            - Numbers 2 to 10, which represent their respective card values.
            - 10 for face cards (Jack, Queen, King).
            - 11 for Aces (we treat Aces as 11 initially).
        
        After creating the deck, we shuffle it for randomness.

        :return: A shuffled deck (list of integers).
        """
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  # 4 copies of each card
        random.shuffle(deck)  # Shuffle to ensure randomness
        return deck

    def deal_card(self):
        """
        Deals one card from the shuffled deck.

        :return: The card value (integer).
        """
        return self.deck.pop()  # Remove and return the top card from the deck

    def hand_value(self, hand):
        """
        Calculates the total value of a hand, accounting for Aces which can be 1 or 11.

        The function adjusts the value of Aces if the total hand value exceeds 21.

        :param hand: List of card values (integers).
        :return: The total value of the hand (integer).
        """
        value = sum(hand)  # Sum the card values (Aces treated as 11 initially)
        ace_count = hand.count(11)  # Count how many Aces are in the hand

        # If the value exceeds 21, adjust Aces to be 1 instead of 11
        while value > 21 and ace_count:
            value -= 10  # Treat one Ace as 1 instead of 11
            ace_count -= 1  # Reduce the number of Aces treated as 11

        return value

    def play_round(self):
        """
        Simulates one round of Blackjack where two strategies play against each other.

        Each player is dealt two cards initially, then both players take turns drawing cards until they reach 17 or higher.

        :return: An integer indicating the winner:
            - 1 if Player 1 wins,
            - 2 if Player 2 wins,
            - 0 if it's a tie.
        """
        hand1 = [self.deal_card(), self.deal_card()]  # Deal two cards to Player 1
        hand2 = [self.deal_card(), self.deal_card()]  # Deal two cards to Player 2

        # Player 1's strategy: Draw cards until hand value reaches at least 17
        while self.hand_value(hand1) < 17:
            hand1.append(self.deal_card())

        # Player 2's strategy: Draw cards until hand value reaches at least 17
        while self.hand_value(hand2) < 17:
            hand2.append(self.deal_card())

        value1 = self.hand_value(hand1)  # Get Player 1's final hand value
        value2 = self.hand_value(hand2)  # Get Player 2's final hand value

        # Update strategies with the final hand values
        self.strategy1.hand_value = value1
        self.strategy2.hand_value = value2

        # Determine the winner based on hand values and busts (over 21)
        if value1 > 21:
            return 2  # Player 1 busts, Player 2 wins
        if value2 > 21:
            return 1  # Player 2 busts, Player 1 wins
        if value1 > value2:
            return 1  # Player 1 wins if their hand value is higher
        elif value2 > value1:
            return 2  # Player 2 wins if their hand value is higher
        else:
            return 0  # Tie if both hand values are equal

class RoundRobinTournament:
    """Simulates a round-robin tournament where each strategy faces every other strategy once."""

    def __init__(self, strategies, num_simulations=3, rating_threshold=0.001, max_reruns=5, perturbation_factor=0.0005):
        """
        Initializes the tournament with given strategies and parameters.

        :param strategies: List of strategy objects participating in the tournament.
        :param num_simulations: Number of simulations to run (default is 3).
        :param rating_threshold: Threshold for determining if reruns are necessary (default is 0.001).
        :param max_reruns: Maximum number of reruns for strategies with similar ratings (default is 5).
        :param perturbation_factor: Random factor to avoid tie situations (default is 0.0005).
        """
        self.strategies = strategies
        self.num_simulations = num_simulations
        self.rating_threshold = rating_threshold
        self.max_reruns = max_reruns
        self.perturbation_factor = perturbation_factor

        # Initialize a dictionary to track scores for each strategy
        self.scores = {strategy.name: {
            "wins": 0, "losses": 0, "busts": 0, "total_hand_value": 0, "games": 0, "hand_values": []
        } for strategy in strategies}

    def play_match(self, strategy1, strategy2):
        """
        Simulates a match between two strategies and updates the scores.

        :param strategy1: First player's strategy object.
        :param strategy2: Second player's strategy object.
        """
        game = BlackjackGame(strategy1, strategy2)  # Create a new Blackjack game with the two strategies
        result = game.play_round()  # Play one round and get the result

        # Update the scores based on the result of the match
        if result == 1:
            self.scores[strategy1.name]["wins"] += 1
            self.scores[strategy2.name]["losses"] += 1
        elif result == 2:
            self.scores[strategy2.name]["wins"] += 1
            self.scores[strategy1.name]["losses"] += 1

        # Track busts (how many times a strategy busts in a match)
        self.scores[strategy1.name]["busts"] += (1 if game.hand_value([strategy1.hand_value]) > 21 else 0)
        self.scores[strategy2.name]["busts"] += (1 if game.hand_value([strategy2.hand_value]) > 21 else 0)

        # Track hand values for each strategy
        self.scores[strategy1.name]["hand_values"].append(game.hand_value([strategy1.hand_value]))
        self.scores[strategy2.name]["hand_values"].append(game.hand_value([strategy2.hand_value]))

        # Track the number of games played for each strategy
        self.scores[strategy1.name]["games"] += 1
        self.scores[strategy2.name]["games"] += 1

    def calculate_metrics(self):
        """
        Calculates and displays performance metrics and rankings for each strategy.

        This includes win rates, bust rates, average hand values, consistency, and fairness.
        """
        ratings = {}

        # Output both basic stats (Wins, Losses, Total Matches) and performance metrics
        for strategy in self.strategies:
            stats = self.scores[strategy.name]

            # Calculate win rate (percentage of games won)
            win_rate = stats["wins"] / stats["games"] if stats["games"] > 0 else 0

            # Calculate bust rate (percentage of games where the strategy busts)
            bust_rate = stats["busts"] / stats["games"] if stats["games"] > 0 else 0

            # Calculate the average hand value (average value of hands over all games)
            avg_hand_value = sum(stats["hand_values"]) / stats["games"] if stats["games"] > 0 else 0

            # Calculate consistency (standard deviation of hand values across games)
            if len(stats["hand_values"]) > 1:
                stddev = math.sqrt(sum((x - avg_hand_value) ** 2 for x in stats["hand_values"]) / len(stats["hand_values"]))
            else:
                stddev = 0  # No consistency if only 1 game

            # Normalize the metrics for fairness (scale to [0, 1] range)
            win_rate_normalized = win_rate
            bust_rate_normalized = 1 - bust_rate  # Lower bust rate is better
            avg_hand_value_normalized = 1 - abs(17 - avg_hand_value) / 17  # Closer to 17 is better
            consistency_normalized = 1 / (1 + stddev)  # Lower standard deviation (more consistency) is better

            # Combine all the normalized scores into a final rating (average of all metrics)
            final_rating = (
                win_rate_normalized + bust_rate_normalized + avg_hand_value_normalized + consistency_normalized
            ) / 4  # Average of all metrics

            # Add a small random perturbation to the final rating to avoid ties
            final_rating += random.uniform(-self.perturbation_factor, self.perturbation_factor)

            ratings[strategy.name] = final_rating

            # Print the performance metrics for each strategy
            print(f"Strategy: {strategy.name}")
            print(f"  Matches Played: {stats['games']}")
            print(f"  Wins: {stats['wins']}")
            print(f"  Losses: {stats['losses']}")
            print(f"  Busts: {stats['busts']}")
            print(f"  Win Rate: {win_rate * 100:.2f}%")
            print(f"  Bust Rate: {bust_rate * 100:.2f}%")
            print(f"  Avg Hand Value: {avg_hand_value:.2f}")
            print(f"  Consistency (Std. Dev.): {stddev:.2f}")
            print(f"  Rating: {final_rating:.8f}")
            print()

        # Sort strategies by their final rating (highest to lowest)
        sorted_ratings = sorted(ratings.items(), key=lambda x: x[1], reverse=True)

        # Display the final rankings after all simulations
        print("Final Rankings:")
        for i, (strategy_name, rating) in enumerate(sorted_ratings):
            print(f"{i + 1}. {strategy_name} - Rating: {rating:.8f}")

# Sample Tournament Execution

# Define some strategies (these are assumed to be predefined elsewhere)
strategies = [ConservativeStrategy(), AggressiveStrategy(), GamblerStrategy(), BalancedStrategy(), CautiousStrategy()]

# Create a tournament instance and simulate the matches
tournament = RoundRobinTournament(strategies)

# Simulate the round-robin tournament
for _ in range(tournament.num_simulations):
    for i in range(len(strategies)):
        for j in range(i + 1, len(strategies)):
            tournament.play_match(strategies[i], strategies[j])

# Calculate and print out the results and rankings
tournament.calculate_metrics()
