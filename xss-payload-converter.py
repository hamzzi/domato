with open("xss-payload-original.txt") as f:
    lines = f.readlines()

with open("xss-payload-copy.txt", "w") as f2:
    for line in lines:
        if len(line.strip()) > 0:
            line = line.replace("<", "<lt")
            line = line.replace(">", "gt>")
            line = line.replace("<lt", "<lt>")
            line = line.replace("gt>", "<gt>")
            f2.write(f"<xss_payload> = {line}")
