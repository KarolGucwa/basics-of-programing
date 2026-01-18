countries = [
    {"country":"Denmark","gold":2,"silver":4,"bronze":6},
    {"country":"Finland","gold":5,"silver":0,"bronze":4},
    {"country":"USA","gold":12,"silver":5,"bronze":11},
    {"country":"Peru","gold":0,"silver":1,"bronze":7}
]

qualified = list(
    filter(lambda c: c["gold"] + c["silver"] + c["bronze"] >= 10, countries)
)

print("COUNTRIES WITH AT LEAST 10 MEDALS")
for c in qualified:
    print(f"{c['country']}: {c['gold']},{c['silver']},{c['bronze']}")
