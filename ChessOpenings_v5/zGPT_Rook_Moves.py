def is_valid_move(rook, destination):
    # Check if the destination is on the same rank or file as the rook
    return rook['rank'] == destination['rank'] or rook['file'] == destination['file']

def get_rook_able_to_move(rooks, destination):
    for rook in rooks.values():
        if is_valid_move(rook, destination):
            return rook
    return None

# Assuming a dictionary of rooks on a1 and h1
rooks = {
    'a1': {'square': 'a1', 'file': 'a', 'rank': 1, 'gridRow': 7, 'gridCol': 0, 'colour': '#769656', 'squareType': 'Dark', 'pieceObj': 'wR'},
    'h1': {'square': 'h1', 'file': 'h', 'rank': 1, 'gridRow': 7, 'gridCol': 7, 'colour': '#769656', 'squareType': 'Dark', 'pieceObj': 'wR'}
}

destination = {'square': 'a5', 'file': 'a', 'rank': 5, 'gridRow': 3, 'gridCol': 0, 'colour': '#769656', 'squareType': 'Dark', 'pieceObj': None}

rook_able_to_move = get_rook_able_to_move(rooks, destination)

if rook_able_to_move:
    print(f"The rook on {rook_able_to_move['square']} can move to {destination['square']}")
else:
    print("No rook can move to the destination square")
