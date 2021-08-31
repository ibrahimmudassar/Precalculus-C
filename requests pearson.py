import requests

for i in range(1, 1069 + 1):
    zero_padded_i = "".join(["0" for i in range(4 - int(len(str(i))))]) + str(i)

    url = "https://catalog.mcgraw-hill.com/secure/JKJZZZRM5VN4Z15VGTTY84X830;s=1C05604B89F6DB417D253E5A2092EC07/OPS/images/page" + zero_padded_i + ".svgz"
    r = requests.get(url, allow_redirects=True)

    open('precalc' + zero_padded_i + '.svg', 'wb').write(r.content)