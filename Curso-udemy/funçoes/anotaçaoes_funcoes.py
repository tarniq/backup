"""
Variaveis dentro de funçoes sao protegidas e so funcionam dentro daquelas funçoes nao alterando as que estao fora delas
y= 50
x= 1 
def sla1():
    x=10
    print(x+y)
    
    def sla2():
        x=70
        y=30
        print(x+y)
    
    sla2()

print(f"{x}|{y}")


sla1()

desse jeito ai (funaçao dentro de funçao é paia) (a funçao q esta dentro de outra so pode ser executada dentro do escopo da primeira se for for n vai)


"""

def somas (x,y):
    print(x+y)
    return x+y

somas(1,2)

soma1 = somas(2,2)

soma2 = somas(80,20)


somas(soma1,soma2)
