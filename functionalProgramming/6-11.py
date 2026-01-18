test_results = [
    {"name":"Peter","result":27},
    {"name":"Anna","result":63},
    {"name":"Robert","result":92},
    {"name":"Paul","result":46},
    {"name":"Barbara","result":52}
]

selected = list(
    filter(lambda s: 50 <= s["result"] <= 70, test_results)
)

for s in selected:
    print(s["name"], s["result"])
