from bs4 import BeautifulSoup

with open("cheat-sheet") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
arr = soup.find_all("code")

with open("cheat_sheet.txt", "w") as f2:
    for item in arr:
        print(item.text)
        if len(item.text) > 0:
            line = item.text
            line = line.replace("\n", "")
            line = line.replace("\r", "")
            line = line.replace("<", "<lt")
            line = line.replace(">", "gt>")
            line = line.replace("<lt", "<lt>")
            line = line.replace("gt>", "<gt>")
            f2.write(f"<xss_payload> = {line}\n")
