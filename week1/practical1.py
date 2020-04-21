def recursive_or(test_list):
    print(set(test_list).sorted())
recursive_or([False, False, False, False, True, False])
def quick_or(test_list):
    return any(test_list)