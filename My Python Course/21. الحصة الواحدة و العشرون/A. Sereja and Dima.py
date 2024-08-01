n = int(input())  # Number of cards
cards = list(map(int, input().split()))  # List of numbers on the cards

sergey_points = 0  # Sereja's points
dima_points = 0  # Dima's points

left = 0  # Index of the leftmost card
right = n - 1  # Index of the rightmost card

turn = 1  # Variable to keep track of whose turn it is, starting with Sereja (1)

while left <= right:
    if turn == 1:
        # It's Sereja's turn, he chooses the card with the larger number
        if cards[left] > cards[right]:
            sergey_points += cards[left]
            left += 1
        else:
            sergey_points += cards[right]
            right -= 1
        turn = 2  # Switch turn to Dima
    else:
        # It's Dima's turn, he chooses the card with the larger number
        if cards[left] > cards[right]:
            dima_points += cards[left]
            left += 1
        else:
            dima_points += cards[right]
            right -= 1
        turn = 1  # Switch turn to Sereja

print(sergey_points, dima_points)
