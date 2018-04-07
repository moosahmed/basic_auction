#!/usr/bin/env python3

keyword = "crime"
bids = [("Alex", 0.1), ("Barry", 0.2), ("Cat", 0.3)]
weights = {"Alex": 0.9, "Barry": 0.5, "Cat": 0.2}
rank_by_revenue = False  # Set to False if rank by bid is required


def get_score(weight, bid_amount):
    """
    Calculates a score for every bidder depending on weights provided and bid amount
    """
    score = weight*bid_amount
    return score


def build_auction_dict(all_bids, weight_data, rank_by_revenue):
    """
    Takes all the bids organized in a list with tuples as pairs of bidders and their bids
    Takes in weights assigned to each bidder as a dictionary
    If rank by bid is required please set rank_by_revenue as False; True if rank by revenue
    """
    auc_dict = {}
    for bid_info in all_bids:
        bidder = bid_info[0]
        bid = bid_info[1]
        if rank_by_revenue:
            weight = weight_data[bidder]
        else:
            weight = 1
        score = get_score(weight, bid)
        auc_dict[bidder] = {"weight": weight, "bid": bid, "score": score}
    return auc_dict


if __name__ == '__main__':
    new_dict = build_auction_dict(bids, weights, rank_by_revenue)
    score_ordered_bidders = sorted(list(new_dict.keys()), key=lambda x: (new_dict[x]['score']), reverse=True)
    pay = new_dict[score_ordered_bidders[1]]['bid'] + 0.01  # Set to be one cent over the next highest bid
    print(score_ordered_bidders[0], 'Wins! They will pay', pay, 'per click for search keyword:', keyword)
