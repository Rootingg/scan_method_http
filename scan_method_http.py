import http.client

print("** This program retuns a list of methods if OPTIONS is enabled **\n")

host = input("Insert the host : ")
port = input("Insert the port: ")

if port=="":
    port = 80

try:
    connection = http.client.HTTPConnection(host,port)
    connection.request('OPTIONS','/')
    response = connection.getresponse()
    print("Enabled methods are: ",response.getheader('allow'))
    connection.close()
except:
    print("connecton failed")

  