traffic_signals = ("red", "yellow", "green", "red")
print(traffic_signals)
print(type(traffic_signals))

print("yellow" in traffic_signals)

travel_docs = ("passport", "visa", "RT-PCR")
print(travel_docs)
print(type(travel_docs))

print(len(travel_docs))

print(travel_docs[2])

print(traffic_signals.count("red"))

print(traffic_signals.index("red"))


for value in traffic_signals:
    print(value)


##FACT ABOUT LIST. 1) IMMUTABLE(Values NOT UPDATABLE) 2) CAN HAVE DUPLICATE VALUES