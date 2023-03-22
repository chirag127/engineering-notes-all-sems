 Here is the content in markdown format without any emojis or external links:

### Optimal Decisions in Games

- Games can be represented as a tree of decisions and chance outcomes. The solution of a game is finding an optimal strategy that maximizes the expected outcome (reward/payoff) for a player.
- Minimax algorithm is used to determine the optimal strategy for both players in a zero-sum game (where one player's gain is another player's loss). It involves minimizing the possible loss/maximizing possible win for each player at every decision point.
- Alpha-beta pruning is a search technique used to speed up minimax search by avoiding examining unnecessary nodes. It works by keeping track of the highest alpha (α) value (best possible outcome for max player) and lowest beta (β) value (worst possible outcome for max player) attained so far and pruning those nodes that cannot affect the final decision.
- Evaluation function determines the desirability of a game state/position to help in comparing possible next moves and determining an optimal move. The values assigned to game states guide the search process towards promising moves.
- In modern game-playing programs, machine learning techniques are used to learn the evaluation function from data rather than manually designing it. This has led to systems that can learn to play at superhuman level in complex games like chess and Go.

The content summarizes key points about optimal decisions in games and some techniques/algorithms used to find optimal strategies. The tone is formal and no emojis or external links are included as specified. Let me know if you would like me to modify or expand the answer.