import re

conv = input("> ")

conv = re.sub(r'(\d) sin', r'\1*sin', conv)
conv = re.sub(r'(\d) t', r'\1*t', conv)
conv = re.sub(r'θ', r'step', conv)
conv = re.sub(r'\) step', r')*step', conv)
conv = re.sub(r'(\d) π', r'\1*math.pi', conv)
conv = re.sub(r'π', r'math.pi', conv)

print(conv)