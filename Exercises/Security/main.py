floor = input().replace('x', '')

if "$T" in floor or "T$" in floor:
	print("ALARM")
elif "$G" in floor or "G$" in floor:
	print("quiet")
