speeds = [48, 47, 54, 50, 42, 68, 39, 46]
limit = 50

too_fast = list(filter(lambda s: s > limit, speeds))

print("Recorded values:", speeds)
print("Speed too high:", too_fast)
