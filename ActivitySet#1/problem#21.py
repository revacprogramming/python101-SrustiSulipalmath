def prepare_data(corruption_matrix, gold_fraction=0.5, merge_valset=True):
    np.random.seed(1)

    mnist_images = np.copy(mnist.train.images)
    mnist_labels = np.copy(mnist.train.labels)
    if merge_valset:
        mnist_images = np.concatenate([mnist_images, np.copy(mnist.validation.images)], axis=0)
        mnist_labels = np.concatenate([mnist_labels, np.copy(mnist.validation.labels)])

    indices = np.arange(len(mnist_labels))
    np.random.shuffle(indices)

    mnist_images = mnist_images[indices]
    mnist_labels = mnist_labels[indices].astype(np.long)

    num_gold = int(len(mnist_labels)*gold_fraction)
    num_silver = len(mnist_labels) - num_gold

    for i in range(num_silver):
        mnist_labels[i] = np.random.choice(num_classes, p=corruption_matrix[mnist_labels[i]])

    dataset = {'x': mnist_images, 'y': mnist_labels}
    gold = {'x': dataset['x'][num_silver:], 'y': dataset['y'][num_silver:]}

    return dataset, gold, num_gold, num_silver 