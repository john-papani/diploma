f = open('./debate.txt', 'r', encoding='utf8')
content = f.read()

split_text = content.split("Αθήνα, σήμερα ")
before_athens = split_text[0]
after_athens = "Αθήνα, σήμερα " + split_text[1]
print(before_athens)

print("----------------")
print(after_athens)
