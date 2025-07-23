from anytree import Node, RenderTree
from grammer_rules import get_grammer
from dataclasses import dataclass
from tqdm.auto import tqdm

import psutil
import time
import hashlib
import os
import json
import random

DEBUG = False

@dataclass
class Program:
    script: str
    output: str
    hash: str

    def to_dict(self):
        return {
            'script': self.script,
            'output': self.output,
            'hash': self.hash
        }
    
    def __str__(self):
        return f"Script: {self.script}\nOutput: {self.output}\nHash: {self.hash}"


class CodeGenerator:
    def __init__(self, max_initialized_vars=3):
        self.max_initialized_vars = max_initialized_vars
        self.var_count = 0
        self.grammer = get_grammer()
    
    def generate_code(self, symbol, current_variables, used_variables: set, parent=None):
        node = Node(symbol, parent=parent)
        if symbol in self.grammer:
            if symbol == 'IDENTIFIER_INITIALIZATION':
                if self.var_count < self.max_initialized_vars:
                    self.var_count += 1
                else:
                    symbol = 'INITIALIZATION'

            rule = random.choice(self.grammer[symbol])
            symbols = rule.split()
            
            generated_symbols = [self.generate_code(s, current_variables, used_variables, node) for s in symbols]
                        
            if symbol == 'INITIALIZATION':
                var_name = generated_symbols[0]
                variable_val = generated_symbols[4] # Check grammer rules for a sanity check
                current_variables[var_name] = variable_val
            
            if symbol == 'ASSIGNMENT_SIMPLE' or symbol == 'ASSIGNMENT_COMPLEX':
                if generated_symbols[0]:
                    used_variables.add(generated_symbols[0])
            
            return ''.join(generated_symbols)
        
        if symbol == 'EXPRESSION_IDENTIFIER':
            identifier = random.choice(
                tuple(current_variables.keys()) if current_variables 
                else random.choice(self.grammer['DIGIT'])
            )
            return identifier
    
        elif symbol == 'DISPLAY_IDENTIFIER':
            try:
                return tuple(used_variables)[0]
            except:
                return random.choice(tuple(current_variables.keys()))
        
        else: return symbol;
    
    def memory_usage(self):
        process = psutil.Process(os.getpid())
        mem = process.memory_info().rss / (1024 * 1024)
        return mem
    
    def print_tree(self, root):
        for pre, _, node in RenderTree(root):
            print(f"{pre}{node.name}")
    
    def generate_program(self, level):
        current_variables = {}
        used_variables = set()
        root = Node("PROGRAM")
        
        match level:
            case '1.1':
                self.max_initialized_vars = 2
            case '1.2':
                self.max_initialized_vars = 3
            case _:
                self.max_initialized_vars = 3
        
        if level == 'ALL': level_passed = level
        else: level_passed = f'LEVEL_{level}'
        
        program = self.generate_code(level_passed, current_variables, used_variables, root)
        
        program = program \
            .replace('SPACE', ' ') \
            .replace('NEW_LINE', '\n') \
            .replace('TAB', '\t')
        
        return root, program
    
    def generate_and_write_program(self, num_programs, level, output_file='output/output_raw.json', deduplicate=True):
        output_dict = [] # Hash, script, output
        generated_programs = 0
        hashes = set()
        
        start_time = time.time()
        start_mem = self.memory_usage()
        max_tries = 1000
        num_tries = 0
        
        pbar = tqdm(total=num_programs, desc="Generating Programs", unit="program")
        
        while generated_programs < num_programs:
            try:
                root, script = self.generate_program(level)
                if DEBUG:
                    self.print_tree(root)
                program_hash = hashlib.sha256(script.encode('utf-8')).hexdigest()

                program = Program(script=script, output='', hash=program_hash)
                
                if deduplicate:
                    if program_hash not in hashes:
                        hashes.add(program_hash)
                        output_dict.append(program.to_dict())
                        generated_programs += 1
                        pbar.update(1)
                        num_tries = 0
                    else:
                        num_tries += 1
                        if num_tries >= max_tries:
                            print(f"Max tries reached: {max_tries}. Stopping generation.")
                            break
            except Exception as e:
                continue
        
        with open(output_file, 'w') as f:
            json.dump(output_dict, f, indent=4)
                    
            
def main():
    generator = CodeGenerator()
    num_programs = 1000
    level = 'ALL'
    output_file = 'output/output_raw.json'
    
    if not os.path.exists('output'):
        os.makedirs('output')
    
    generator.generate_and_write_program(num_programs, level, output_file, deduplicate=True)
    print(f"Generated {num_programs} programs at level {level} and saved to {output_file}")
    
if __name__ == "__main__":
    main()