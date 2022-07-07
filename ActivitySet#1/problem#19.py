def solve_sudoku(puzzle):
    """
    Solve sudoku puzzle using RRN.
    :param puzzle: an array-like data with shape [9, 9], blank positions are filled with 0
    :return: a [9, 9] shaped numpy array
    """
    puzzle = np.array(puzzle, dtype=np.long).reshape([-1])
    model_path = 'ckpt'
    if not os.path.exists(model_path):
        os.mkdir(model_path)

    model_filename = os.path.join(model_path, 'rrn-sudoku.pkl')
    if not os.path.exists(model_filename):
        print('Downloading model...')
        url = 'https://data.dgl.ai/models/rrn-sudoku.pkl'
        urllib.request.urlretrieve(url, model_filename)

    model = torch.load(model_filename, map_location='cpu')

    g = _basic_sudoku_graph()
    sudoku_indices = np.arange(0, 81)
    rows = sudoku_indices // 9
    cols = sudoku_indices % 9

    g.ndata['row'] = torch.tensor(rows, dtype=torch.long)
    g.ndata['col'] = torch.tensor(cols, dtype=torch.long)
    g.ndata['q'] = torch.tensor(puzzle, dtype=torch.long)
    g.ndata['a'] = torch.tensor(puzzle, dtype=torch.long)

    pred, _ = model(g, False)
    pred = pred.cpu().data.numpy().reshape([9, 9])
    return pred 