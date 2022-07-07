def prepare_data(corruption_matrix, gold_fraction=0.5, merge_valset=True):
    np.random.seed(1)

    twitter_tweets = np.copy(X_train)
    twitter_labels = np.copy(Y_train)
    if merge_valset:
        twitter_tweets = np.concatenate([twitter_tweets, np.copy(X_dev)], axis=0)
        twitter_labels = np.concatenate([twitter_labels, np.copy(Y_dev)])

    indices = np.arange(len(twitter_labels))
    np.random.shuffle(indices)

    twitter_tweets = twitter_tweets[indices]
    twitter_labels = twitter_labels[indices].astype(np.long)

    num_gold = int(len(twitter_labels)*gold_fraction)
    num_silver = len(twitter_labels) - num_gold

    for i in range(num_silver):
        twitter_labels[i] = np.random.choice(num_classes, p=corruption_matrix[twitter_labels[i]])

    dataset = {'x': twitter_tweets, 'y': twitter_labels}
    gold = {'x': dataset['x'][num_silver:], 'y': dataset['y'][num_silver:]}

    return dataset, gold, num_gold, num_silver 