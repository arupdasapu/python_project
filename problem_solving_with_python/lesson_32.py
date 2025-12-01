from google.colab import files
uploaded = files.upload()


import sys
sys.path.append('.')
import our_module
from our_module import find_max

our_module.lower_case('HELLO PYTHON')
our_module.upper_case('hello python')
result = find_max([1, 120, 500, 10])
print(result)
