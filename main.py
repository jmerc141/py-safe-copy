import sys, os, safecopy

if __name__ == '__main__':
	src = sys.argv[1]
	dst = sys.argv[2]

	# Assuming if src is a dir then destination should be a dir
	if os.path.isdir(src) and os.path.isdir(dst):
		# is a folder
		try:
			os.makedirs(dst)
		except FileExistsError as e:
			# Already exists, continue
			pass
		srcFiles = dstFiles = []

		for root, dirs, files in os.walk(src):
			for f in files:
				srcFiles.append(os.path.join(root, f))
			for d in dirs:
				srcFiles.append(os.path.join(root, d))

		safecopy.safeCopy(src, srcFiles, dst)
	# Only copying one file
	elif not os.path.isdir(src) and not os.path.isdir(dst):
		safecopy.safeCopyOne(src, dst)
	# If source is a file and dest is a folder
	elif not os.path.isdir(src) and os.path.isdir(dst):
		safecopy.safeCopyOnef(src, dst)
	else:
		print('Source and destination both must be folders or files')
		sys.exit()