6# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
from tqdm import tqdm


def evaluate_places(filepath, predicted_places):
    """ Computes percent of correctly predicted birth places.

    Arguments:
      filepath: path to a file with our name, birth place data.
      predicted_places: a list of strings representing the
          predicted birth place of each person.

    Returns:
      (total, correct), floats
    """
    with open(filepath) as fin:
        lines = [x.strip().split('\t') for x in fin]
        if len(lines[0]) == 1:
            print('No gold birth places provided; returning (0,0)')
            return (0, 0)
        true_places = [x[1] for x in lines]
        total = len(true_places)
        assert total == len(predicted_places)
        correct = len(list(filter(lambda x: x[0] == x[1],
                                  zip(true_places, predicted_places))))
        return (float(total), float(correct))


argp = argparse.ArgumentParser()
argp.add_argument('--eval_corpus_path',
    help="Path of the corpus to evaluate on", default=None)
args = argp.parse_args()


predictions = []
for line in tqdm(open(args.eval_corpus_path)):
    predictions.append('London')

total, correct = evaluate_places(args.eval_corpus_path, predictions)
print('Correct: {} out of {}: {}%'.format(correct, total, correct / total * 100))