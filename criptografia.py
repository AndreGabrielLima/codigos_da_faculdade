'''quantidade_de_linhas = int(input())


for i in range(quantidade_de_linhas):
   string = input()
   string = list(string)
   
   for j in range(0, len(string)):
        if (string[j].isalpha()):
            string[j] = chr(ord(string[j])+3) 
      
   new_str = string[::-1]
      
   tamanho = len(new_str)//2
      
   for k in range(tamanho, len(new_str)):
        if new_str[k] == " ":
            continue
        new_str[k] = chr(ord(new_str[k])-1)
          
        
print("".join(new_str))'''
n = int(input())


for i in range(n):
   string = input()
   string = list(string)
   
   for j in range(0, len(string)):
      if (string[j].isalpha()):
         string[j] = chr(ord(string[j])+3) 
      
   new_str = string[::-1]
      
   tamanho = len(new_str)//2
      
   for k in range(tamanho, len(new_str)):
      if new_str[k] == " ":
        continue
      new_str[k] = chr(ord(new_str[k])-1)
          
        
   print("".join(new_str))