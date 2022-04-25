def cipher(msg, key):  
  c = [] #ciphered text
  final = ""
  msg = msg.upper() #plaintext in all uppercase
  
  for i in range(0, len(msg)):
   if ord(msg[i])>=65 and ord(msg[i]) <=90:
     char_ord = ((ord(msg[i])+key-65)) % 26 +65    
     char= chr(char_ord)
     c.append(char)
  
  for i in range(0,len(c), 5):  
      if i == 0 :    
        final = c[i:5]
        print(("".join(final)), end = " ") 
       
      elif i % 50 != 0:       
        j = i + 5
        final = c[i:j]
        print(("".join(final)), end = " ")
        
      else: 
        print("")
        j = i + 5
        final = c[i:j]
        print(("".join(final)), end = " ")  
  return ""
      



