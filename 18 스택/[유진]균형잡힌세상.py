import sys, re
input = sys.stdin.readline

while True:
	s = input()
	if s == ".\n":
		break
	s = re.sub("[a-zA-Z. ]", "", s)
	while ("()" in s) or ("[]" in s):
		s = s.replace("()", "")
		s = s.replace("[]", "")
	if len(s.strip()) ==0:
		print("yes")
	else: print("no")

# 33032KB, 176ms