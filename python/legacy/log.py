import os
import re

path = r'path'
pattern = re.compile(r'.*Bumps\.dat$')
total_size = 0
for dirpath, dirnames, filenames in os.walk(path):
	for fn in filenames:
		full_path = os.path.join(dirpath, fn)
		if re.search(pattern, full_path):
			file_size = os.path.getsize(full_path)
			with open('file.log', 'a') as f:
				text = '%s: %d MB' %(full_path, file_size / (1024 * 1024)) #MB	
				print text
				f.write(text + '\n')
			total_size += file_size

print total_size / (1024 * 1024 * 1024) # GB
