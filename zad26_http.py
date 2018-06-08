
list = [{"url":"www.google.pl", "status": True, "response_time": 12},
        {"url":"www.wp.pl", "status": False},
        {"url":"www.google.pl", "status": False},
        {"url":"www.wp.pl", "status": True, "response_time": 10},
        {"url": "www.wp.pl", "status": False},
        {"url": "www.wp.pl", "status": True, "response_time": 10},
        {"url": "www.google.pl", "status": True, "response_time": 12}]

# Napisac program, który dla kazdego urla wypisze ilosc udanych oraz nieudanych zapytan,
# a takze srednia czasu odpowiedzi zapytan, które sie powiodły.

infoDlaUrli = {}

for element in list:
    url = element["url"]

    if url not in infoDlaUrli:
        infoDlaUrli[url] = { "Sukces": 0, "porazka": 0, "SrCzas": 0}

    if element["status"] == True:
        infoDlaUrli[url]["Sukces"] += 1
        infoDlaUrli[url]["SrCzas"] += element["response_time"]
    else:
        infoDlaUrli[url]["porazka"] += 1

for x in infoDlaUrli:
    infoDlaUrli[x]["SrCzas"] = infoDlaUrli[x]["SrCzas"] / infoDlaUrli[x]["Sukces"]

print(infoDlaUrli)

