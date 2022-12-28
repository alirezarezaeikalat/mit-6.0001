# Problem Set 4A
# Name: Alirez Rezaei Kalat
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # recursion base case
    if len(sequence) == 1:
        return [sequence]
    else:
        i = 0
        new_permutations = []
        # remove the first char and get the permutatinos
        permutations = get_permutations(sequence[1:])
        # add first char at all positions for each of the permutations
        for permutation in permutations:
            for i in range(0, len(permutation) + 1, 1):
                new_permutations.append(permutation[:i] + sequence[0] + permutation[i:])
        return new_permutations
        

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print('----------------')
    
    example_input_2 = 'dhu'
    print('Input:', example_input)
    print('Expected Output:', ['dhu', 'duh', 'uhd', 'udh', 'hdu', 'hud'])
    print('Actual Output:', get_permutations(example_input_2))   
    print('-------------')
    
    example_input_3 = 'lkj'
    print('Input:', example_input)
    print('Expected Output:', ['lkj', 'ljk', 'jkl', 'jlk', 'klj', 'kjl'])
    print('Actual Output:', get_permutations(example_input_3))   
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)


