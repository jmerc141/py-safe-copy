import sys, os, safecopy

if __name__ == '__main__':
	src = sys.argv[1]
	dst = sys.argv[2]

	# Assuming if src is a dir then destination should be a dir
	if os.path.isdir(src):
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
	elif not os.path.isdir(src):
		safecopy.safeCopyOne(src, dst)
	else:
		print('Source and destination must be folders')
		sys.exit()