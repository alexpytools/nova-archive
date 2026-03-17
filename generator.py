import json
import datetime
import os
import re

title=input("Title: ")
desc=input("Description: ")
tags=input("Tags (comma): ").split(",")

slug=re.sub(r'[^a-z0-9]+','-',title.lower()).strip("-")

date=datetime.date.today().strftime("%d %B %Y")

print("Write post content (finish with CTRL+Z then ENTER):")

content=""
try:
    while True:
        content+=input()+"\n"
except:
    pass

reading_time=str(max(1,len(content.split())//200))+" min read"

html=f"""

<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">
<title>{title}</title>

<link rel="stylesheet" href="../style.css">

</head>

<body>

<div class="post-container">

<h1>{title}</h1>

<div class="post-date">{date}</div>
<div class="reading">{reading_time}</div>

<div class="tags">
{" ".join([f'<span class="tag">#{t.strip()}</span>' for t in tags])}
</div>

<div class="post-content">

{content}

</div>

</div>

</body>

</html>

"""

path=f"posts/{slug}.html"

with open(path,"w",encoding="utf8") as f:
    f.write(html)

with open("data/posts.json","r") as f:
    posts=json.load(f)

posts.append({
"title":title,
"desc":desc,
"date":date,
"tags":[t.strip() for t in tags],
"url":path
})

with open("data/posts.json","w") as f:
    json.dump(posts,f,indent=2)

print("Post created:",path)