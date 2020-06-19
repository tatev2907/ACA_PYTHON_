import json
with open('storage.json') as f:
  data = json.load(f)
  for d in data:
    parts = ['<?xml version="1.0" encoding="UTF-8" ?>']
    parts .append( ['<{}>'.format(d)])
    for key, val in d.items():
      parts.append('<{0}>{1}</{0}>'.format(key, val))
      parts.append('</{}>'.format(data))
    print(''.join(parts))
