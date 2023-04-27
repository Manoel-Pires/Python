algo = input ('digite algo ')
print ( '0 tipo primitivo digitado é: ', type(algo))
print ('o valor digitado (é numero?) {} (é alfanumérico?) {} (é só letra?) {} (está em maiusculo?) {}' . format (algo.isnumeric(), algo.isalnum(), algo.isalpha(), algo.isupper()))




