import re
import sys
import os
import random


def generate_prompt(lines):
    nodes = re.findall(r'node\((\d+)\)\.', lines)
    nodes = [x for x in nodes]
    nodes = ', '.join([x for x in nodes])
    links = re.findall(r'link\((\d+),(\d+)\)', lines)
    links = list(map(lambda x: (int(x[0]), int(x[1])), links))
    links = list(set(map(tuple, map(sorted, links))))
    links = ' '.join([f'Nodes {x[0]} and {x[1]} are linked.'for x in links])
    colour = re.findall(r'colour\((\w+)\)\.', lines)
    colour = [x for x in colour]
    colour = ', '.join([x for x in colour])

    prompt_node = 'The nodes are {}.'.format(nodes)
    prompt_color = 'The colors are {}.'.format(colour)

    prompt_question = 'Please solve a graph coloring problem. The goal is to color the nodes of a graph in such a way that no two adjacent nodes have the same color.'
    prompt_note = 'The output format is (node, color).'
    prompt = prompt_question + ' ' + prompt_color + ' ' + \
        prompt_node + ' ' + links + ' ' + prompt_note
    return prompt


if __name__ == "__main__":
    folder_path = f'/home/yhayamizu/llm_asp_survey/nodes_{sys.argv[1]}/'

    problem_files = os.listdir(folder_path)
    random_problem = random.choice(problem_files)
    problem_path = os.path.join(folder_path, random_problem)
    print('problem path: {}'.format(problem_path))
    with open(problem_path, 'r') as file:
        lines = file.read()

    prompt = generate_prompt(problem_path)
    print('prompt: {}'.format(prompt))
