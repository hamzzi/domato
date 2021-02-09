with open("xss-payload.txt", "a") as f2:
    for i in range(5):
        with open(f"xss-payload-list{i}.txt", encoding='utf-8',
                 errors='ignore') as f:
            lines = f.readlines()

        for line in lines:
            if line[0] == "#":
                continue
            if len(line.strip()) > 0:
                line = line.replace("<", "<lt")
                line = line.replace(">", "gt>")
                line = line.replace("<lt", "<lt>")
                line = line.replace("gt>", "<gt>")
                f2.write(f"<xss_payload> = {line}")
