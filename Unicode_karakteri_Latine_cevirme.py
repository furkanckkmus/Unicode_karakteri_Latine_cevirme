from typing import ByteString


aa = 'Alb\u00fcm: S\u0131la'
s = bytes(aa, 'unicode-escape')
print (s)
print ((s.decode('unicode-escape')))

