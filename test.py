# -*- coding: utf-8 -*-

import base64
import email
import email.header

str1 = 'ndEGTLY6gc386hVvzW5JhRvTRPnd0FuglMLxdGKscvNlsw5XD4mH/mJwPPYnLj1LVSeMpi3sTTc6Mbg/Rv4YxKHJiPOPPDAF336ebqegNXBQw2tk+Xmr7hwAHwbXLPXBUqhB1iyvEEXb7rUuChXrA1wWnYXg0C5Y/SxvESqyKdGz4SSyv2c/6Bj8Mk3nFF/GvvLJNh2uYUMqsP2Aj8BzX3zNeu6nDFzbfyCOHEUfYOodUyuAmVFQlfomgHjYZO9A/KZ/lSd2270gllIF76GiegWJx6VPbSlNspJWL58DlgjbB67BzRw/FF1CaVWF7GxQQf5IL5sr81ItlyeWXRhzPqkkjbRDgKPbm0abVYVHTv3Tiqb8caoEfYhaFMLXVXEHiAx1gey0WgGQJN29LncTgJ8357cI4A2DNrh2Rc2tny5sQ38rtbSyyiW3+Wff35HGmdzK4JFxL73e25/qaoTDRKPiz1Jbl3krJkA1xnb7SfP3VSKrft3EXaoq7089GCoITIFIALdnsKb1GugbeO3M855IjyURpA/9B1CmDHjVRD7PcDbGKQkV85JlSOAFiTvhm6MN/xbag7+xnRQZAQhwnZ0X25saqWhLXwcNBiLOzxcqrrst5Jl+sJ/39EeK3sWrUOJ0p8Y0XSKetdvV/UFZ4A=='
str3 = str1.encode(encoding='utf-8', errors='strict')
print(str3),
print('')

str4 = base64.b64encode(str3)

print(str4)
print('')

print(str4.decode())
print('')

str5 = base64.b64encode(str4)
print(str5.decode())


# res = base64.b64decode(res)
# # base64.decodestring(img)
# # res = res.decode('base64','strict')
# print(res)


def decode_mime_words(s):
    return u''.join(
        word.decode(encoding or 'utf8') if isinstance(word, bytes) else word
        for word, encoding in email.header.decode_header(s))


print(decode_mime_words(str1))
