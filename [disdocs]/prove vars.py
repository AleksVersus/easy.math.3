import re
import os

def get_files_list(folder:str, filters:list=None) -> list:
	""" Create list of files in folder and includes folders. """
	if filters is None: filters = [".qsps",'.qsp-txt','.txt-qsp']
	build_files = []
	tree = os.walk(folder)
	for abs_path, _, files in tree:
		for file in files:
			sp = os.path.splitext(file)
			if not filters or (sp[1] in filters):
				build_files.append(os.path.join(abs_path, file))
	if not build_files:
		write_error_log(f'[200] Folder is empty. Prove path «{folder}».')
	return build_files

def main():
	vars_path = os.path.abspath('..\\[source]\\00_sets\\_variables.qsps_')
	files_fold = os.path.abspath('..\\[source]')

	files_labels = []
	for file in get_files_list(files_fold):
		with open(file, 'r', encoding='utf-8') as fp:
			lines = fp.readlines()
		for line in lines:
			match = re.match(r'!@pp:if\((\w+)\):include', line)
			if match is not None:
				files_labels.append(match.group(1))

	vars_labels = []
	with open(vars_path, 'r', encoding='utf-8') as fp:
		lines = fp.readlines()
	for line in lines:
		match = re.match(r'!@pp:var\((\w+)\)', line)
		if match is not None:
			vars_labels.append(match.group(1))

	print(set(files_labels) - set(vars_labels))
	print(set(vars_labels) - set(files_labels))

if __name__ == '__main__':
	main()