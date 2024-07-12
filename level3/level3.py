def min_coins_solution_string(currency):
    max_amount = 100
    min_coins = [float('inf')] * (max_amount + 1)
    min_coins[0] = 0
    coin_count = [[] for _ in range(max_amount + 1)]
    
    for amount in range(1, max_amount + 1):
        for coin in currency:
            if amount >= coin:
                if min_coins[amount - coin] + 1 < min_coins[amount]:
                    min_coins[amount] = min_coins[amount - coin] + 1
                    coin_count[amount] = coin_count[amount - coin] + [coin]
    
    solution_lines = []
    for amount in range(1, max_amount + 1):
        count_dict = {}
        for coin in coin_count[amount]:
            if coin in count_dict:
                count_dict[coin] += 1
            else:
                count_dict[coin] = 1
        solution_line = ' '.join(f"{count}x{coin}" for coin, count in count_dict.items())
        solution_lines.append(solution_line)
    
    return '\n'.join(solution_lines)


file = 'level3_5.in'
output = file + ".out"
f = open(file, 'r')
out = open(output, 'a')

l = int(f.readline())
n = int(f.readline())
for _ in range(l):
  k = f.readline().split()
  a = [int(x) for x in k]


# Example currency list
# currency = [1, 3, 13]

# Output the solution string for the given currency
  solution_string = min_coins_solution_string(a)
  # print(f"Currency: {currency}")
  # print(f"Solution string:\n{solution_string}")
  
  out.write(solution_string + '\n')