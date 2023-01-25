import re
import json
from pprint import pprint
with open("question.txt", "r") as f:
  # lines = f.readlines()
  all = f.read()

array_quest = []
questions = all.split("QUESTION")
for q in questions[1:]:
  dict_quest = {}
  qLines = q.split("\n")
  print(qLines[0])
  dict_quest["number"] = qLines[0]
  if str(qLines[1]) == "SIMULATION":
    dict_quest["question"] = str(qLines[2])
  else: 
    dict_quest["question"] = str(qLines[1])
  
    options = []
    for i in qLines[3:]:
      options.append(i[3:])
    while "" in options:
      options.remove('')
    dict_quest["options"] = options
  dict_quest["answer"] = [""]
  array_quest.append(dict_quest)
  pprint(dict_quest)

# with open("questions1.json", "a") as f:
#   json.dump(dict_quest, f)

with open("question2.json", "w") as f:
  json.dump(array_quest, f, indent=2)