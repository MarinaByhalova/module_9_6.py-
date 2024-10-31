def all_variants(text):
    for х in range(len(text)):
        for r in range(len(text)-х):
            yield text[r:r+х+1]


a = all_variants("abc")
for i in a:
    print(i)
