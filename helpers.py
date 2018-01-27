"""
Convenience functions for kaggle house prices comp.
"""


def get_info(query):
    """Convenience to print description"""
    f = open('data/data_description.txt', 'r')
    lines = f.readlines()
    for line in lines:
        if line.startswith(query):
            return(line.split(":")[-1])
