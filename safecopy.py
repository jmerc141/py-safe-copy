import hashlib, copyFile, os

def safeCopy(r, s, dst):
	os.system('cls' if os.name == 'nt' else 'clear')
	x=0
	srcHash = dstHash = ''
	for i in s:
		if os.path.isdir(i):
			#print('making', i)
			os.makedirs(i.replace(r, dst))
		else:
			dest = i.replace(r, dst)
			#print('dest:', dest)
			print(s[x], '->', dest)
			srcHash = copyFile.copy_with_progress(s[x], dest, True)
			#print('\nCreating destination hash...')
			dstHash = hashlib.md5(open(dest, 'rb').read()).hexdigest()
			print()
			if not srcHash == dstHash:
				print('Hashes do not match, try again? (y/n)')
				t = input()
				if t == 'y':
					x-=1
				else:
					return
			#print(srcHash, dstHash)
		x+=1


def safeCopyOne(src, dst):
	print(src, '->', dst)
	srcHash = copyFile.copy_with_progress(src, dst, False)

	print('\nCreating destination hash...')
	dstHash = hashlib.md5()
	with open(dst, 'rb') as d:
		while True:
			buf = d.read(65536)
			if not buf:
				break
			dstHash.update(buf)

	print(srcHash, dstHash.hexdigest())
	if not srcHash == dstHash.hexdigest():
		print('Hashes do not match, try again? (y/n)')
		t = input()
		if t == 'y':
			x-=1
		else:
			return

def safeCopyOnef(src, dst):
	print(src, '->', dst)
	dst = os.path.join(dst, os.path.basename(src))
	srcHash = copyFile.copy_with_progress(src, dst, False)

	print('\nCreating destination hash...')
	dstHash = hashlib.md5()
	with open(dst, 'rb') as d:
		while True:
			buf = d.read(65536)
			if not buf:
				break
			dstHash.update(buf)

	if not srcHash == dstHash.hexdigest():
		print('Hashes do not match, try again? (y/n)')
		t = input()
		if t == 'y':
			x-=1
		else:
			return
	else:
		print('Hashes match:', srcHash)
		

		

	