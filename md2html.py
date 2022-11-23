import os
# import re

def good_format(title):
    return " ".join(map(lambda s: s[0].upper() + s[1:] if len(s) != 1 else s, title.split("-")))

if not os.path.isdir("./temp"):
    os.mkdir("temp")

for file in os.listdir("mds"):
    name_no_ext = file.split(".")[0]

    with open("mds/" + file) as F:
        content = F.read()

        # content = re.sub("⚠️", "!!!", content)
        # content = re.sub("✅", "", content)
        # content = re.sub("\\\\lt", "<", content)
        # content = re.sub("\\\\gt", ">", content)

    with open("temp/" + name_no_ext + ".md", "w") as NF:
        NF.write(content)

    print("Processing " + name_no_ext + ".md")

    os.system(f"pandoc --standalone --mathjax --metadata title=\"{good_format(name_no_ext)}\" -f markdown -t html temp/" + name_no_ext + ".md -o html/" + name_no_ext + ".html")

os.system("rm -rf ./temp")
