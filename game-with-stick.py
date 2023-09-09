def game_with_sticks(n, m):
  """
  Determines the winner of the game of sticks.

  Args:
    n: The number of horizontal sticks.
    m: The number of vertical sticks.

  Returns:
    "Akshat" if Akshat wins, "Malvika" if Malvika wins, or "Draw" if the game is a draw.
  """
  # Initialize the grid of sticks.
  grid = [[False] * m for _ in range(n)]

  # Add the horizontal sticks.
  for i in range(n):
    for j in range(m):
      grid[i][j] = True

  # Add the vertical sticks.
  for j in range(m):
    for i in range(n - 1, -1, -1):
      grid[i][j] = True

  # Initialize the set of intersection points.
  intersection_points = set()
  for i in range(n):
    for j in range(m):
      if grid[i][j]:
        intersection_points.add((i, j))

  # Play the game until there is a winner.
  while intersection_points:
    # Akshat's turn.
    i, j = intersection_points.pop()
    for k in range(n):
      if grid[k][j]:
        grid[k][j] = False
        intersection_points.remove((k, j))
      if grid[i][k]:
        grid[i][k] = False
        intersection_points.remove((i, k))

    # Check if Akshat won.
    if not intersection_points:
      return "Akshat"

    # Malvika's turn.
    i, j = intersection_points.pop()
    for k in range(m):
      if grid[i][k]:
        grid[i][k] = False
        intersection_points.remove((i, k))
      if grid[j][k]:
        grid[j][k] = False
        intersection_points.remove((j, k))

    # Check if Malvika won.
    if not intersection_points:
      return "Malvika"

  # The game is a draw.
  return "Draw"

def main():
  """
  The main function.
  """
  n, m = map(int, input().split())

  print(game_with_sticks(n, m))

if __name__ == '__main__':
  main()
