def solve(a0, a1, a2, b0, b1, b2):
	alice_score = 0
	bob_score = 0

	if a0 > b0:
		alice_score += 1
	elif a0 != b0:
		bob_score += 1

	if a1 > b1:
		alice_score += 1
	elif a1 != b1:
		bob_score += 1

	if a2 > b2:
		alice_score += 1
	elif a2 != b2:
		bob_score += 1

	return alice_score, bob_score
