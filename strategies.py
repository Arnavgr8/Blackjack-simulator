class StrategyBase:
    """Base class for a Blackjack strategy."""
    
    def __init__(self, name):
        """
        Initializes the strategy with a given name and sets up tracking variables.
        
        :param name: The name of the strategy (used for identification).
        """
        self.name = name  # Name of the strategy (e.g., "Conservative", "Aggressive")
        self.moves = []  # List to track the moves made by this strategy
        self.hand_value = 0  # Variable to store the current value of the hand (used for internal calculations)

    def record_move(self, move):
        """Records the move made by this strategy."""
        self.moves.append(move)  # Adds the current move ('hit' or 'stand') to the strategy's history

    def play(self, hand, deck):
        """Determines the next action (hit or stand). To be implemented by subclasses."""
        raise NotImplementedError("This method should be implemented by the strategy subclasses.")
    

class ConservativeStrategy(StrategyBase):
    """A conservative strategy that stands on 17 and hits otherwise."""
    
    def __init__(self):
        super().__init__("Conservative")  # Initializes the strategy with the name "Conservative"

    def play(self, hand, deck):
        """
        This strategy is cautious and only stands when the hand value is 17 or higher.
        Otherwise, it hits to try and improve the hand.

        :param hand: The current hand of the player (a list of card values).
        :param deck: The remaining deck (not used in this strategy, but required for the interface).
        :return: The next move ('stand' or 'hit').
        """
        if sum(hand) >= 17:  # If the hand's total value is 17 or more, stand.
            self.record_move('stand')
            return 'stand'
        else:  # If the hand's total value is less than 17, hit to improve the hand.
            self.record_move('hit')
            return 'hit'


class AggressiveStrategy(StrategyBase):
    """An aggressive strategy that always hits until reaching 21."""
    
    def __init__(self):
        super().__init__("Aggressive")  # Initializes the strategy with the name "Aggressive"

    def play(self, hand, deck):
        """
        This strategy is very aggressive and always tries to hit until the hand value is 21.
        It only stops hitting when it reaches 21, which is the best possible hand value.

        :param hand: The current hand of the player (a list of card values).
        :param deck: The remaining deck (not used in this strategy, but required for the interface).
        :return: The next move ('stand' or 'hit').
        """
        if sum(hand) < 21:  # If the hand's value is less than 21, always hit.
            self.record_move('hit')
            return 'hit'
        else:  # If the hand's value is 21, stand.
            self.record_move('stand')
            return 'stand'


class GamblerStrategy(StrategyBase):
    """A gambler strategy that takes risks and hits aggressively until 19."""
    
    def __init__(self):
        super().__init__("Gambler")  # Initializes the strategy with the name "Gambler"

    def play(self, hand, deck):
        """
        This strategy is riskier than others, as it keeps hitting until the hand value is 19 or more.
        It aims to push the hand value high, but once it hits 19, it plays conservatively.

        :param hand: The current hand of the player (a list of card values).
        :param deck: The remaining deck (not used in this strategy, but required for the interface).
        :return: The next move ('stand' or 'hit').
        """
        if sum(hand) < 19:  # If the hand's value is less than 19, keep hitting.
            self.record_move('hit')
            return 'hit'
        else:  # Once the hand's value is 19 or more, stand.
            self.record_move('stand')
            return 'stand'


class BalancedStrategy(StrategyBase):
    """A balanced strategy that hits until 17, then switches to conservative play."""
    
    def __init__(self):
        super().__init__("Balanced")  # Initializes the strategy with the name "Balanced"

    def play(self, hand, deck):
        """
        This strategy is more balanced: it hits until the hand value is 17, and then stands,
        adopting a more conservative approach to avoid busting.

        :param hand: The current hand of the player (a list of card values).
        :param deck: The remaining deck (not used in this strategy, but required for the interface).
        :return: The next move ('stand' or 'hit').
        """
        if sum(hand) < 17:  # Hit if the hand's total value is less than 17.
            self.record_move('hit')
            return 'hit'
        else:  # Stand once the hand reaches 17 or more.
            self.record_move('stand')
            return 'stand'


class CautiousStrategy(StrategyBase):
    """A cautious strategy that always stands at 16 or more."""
    
    def __init__(self):
        super().__init__("Cautious")  # Initializes the strategy with the name "Cautious"

    def play(self, hand, deck):
        """
        This strategy plays it very safe, standing as soon as the hand value reaches 16 or more.
        It avoids risk by hitting only when the hand value is below 16.

        :param hand: The current hand of the player (a list of card values).
        :param deck: The remaining deck (not used in this strategy, but required for the interface).
        :return: The next move ('stand' or 'hit').
        """
        if sum(hand) >= 16:  # Stand once the hand's value is 16 or more.
            self.record_move('stand')
            return 'stand'
        else:  # Hit if the hand's total value is less than 16.
            self.record_move('hit')
            return 'hit'
