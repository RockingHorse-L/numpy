import numpy as np

print(np.char.add(['hello'], [' xyz']))
print(np.char.multiply('hello', 3))
print(np.char.center('abc', 30, fillchar='*'))
print(np.char.capitalize("abcdef"))
print(np.char.title('i like python'))
print(np.char.split('www.ai.com', sep='.'))
print(np.char.join(['*', '='], ['microsoft', 'huawei']))
print(np.char.replace('你是日本人', '日本人', '***'))