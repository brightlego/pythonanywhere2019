plain_text = ''.join(raw_input("Plain text: ").upper().split())
cipher_text = plain_text[::2]+plain_text[1::2]
print(' '.join(re.findall("\w{5}",cipher_text)))