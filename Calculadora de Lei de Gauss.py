import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0, pi
from matplotlib.ticker import MultipleLocator  

#Função para evitar entradas inválidas, para evitar haver entradas não numéricas
def numero_valido(mensagem): 
    while True:
        entrada = input(mensagem).strip().replace(',', '.')
        try:
            return float(entrada) #vai ver o que escrevi e ver se pode ser usado
        except ValueError:
            print("por favor digite apenas números") #se não tiver só números vai dar problema

#função para lei de gauss fora da esfera não condutora, irá retornar o campo elétrico num ponto específico
def lei_de_gauss_ex():
        q = numero_valido("seu valor de carga é:") #importa as variáveis de carga
        r = numero_valido("sua distância até o centro é:") #importa o raio do campo até o centro
        if r <= 0: #não há raio negativo
            print("não há raio negativo, há algo errado com seu dado")
            return None
        else: #faz o calculo e mostra as variáveis
            print(f"sua carga é de {q} (em Coulomb) a uma distância de {r} (em Metros)")
            campo_eletrico = (1/(4*pi*epsilon_0))*(q/r**2) #equação de campo elétrico para carga pontual 
            print(f"seu campo elétrico resultante é de {campo_eletrico:.2e} (N/C)") #mostra o campo elétrico com arredonadamento
            return campo_eletrico

#lei de gauss para dentro da esfera não condutora, irá retornar a carga num ponto dentro do volume da esfera
def lei_de_gauss_in(): 
    q = numero_valido("seu valor de carga é:") #verifica as variáveis de carga
    r = numero_valido("sua distância até o centro é:") #verifica a distância até o ponto desejado
    R = numero_valido("sua esféra tem raio:") #verifica o tamanho da esfera que emite cargas
    if r <= 0 or R <= 0: #procura inconsistências
        print("não há raio negativo, há algo errado com seu dado") 
        return None #retorna a pergunta por que não há significado físico em raios negativos
    elif r > R: #Campos internos não podem ter superfície gaussiana maior que o raio interno 
        print("Entrada inválida para esse tipo de campo, por favor utilize a equação para campos externos")
        return None 
    else: #segue o protocolo padrão igual antes
        print(f"para uma esfera de Raio {R} (em Metro), com carga {q} (em Coulomb) e que possui superfície gaussiana em {r} (em Metro)")
        campo_eletrico = (1/(4*pi*epsilon_0)) * (q/R**3)*(r)
        print(f"seu campos elétrico resultante no ponto {r} será de: {campo_eletrico:.2e} (N/C)") #campo dentro de um volume (superfície gaussiana dentro de um volume)
        return campo_eletrico

#Continuação dos calculos para evitar ficar entrando e saindo do programa
def continuar():
    resposta = input("você deseja calcular novamente? S/N").upper()
    return resposta == "N" #quer saber se vai querer repetir o calculo

#Geração do gráfico de um campo de uma partícula dentro de um esfera indo desde o centro da partícula até a casca
def grafico_in():
    q = numero_valido("Seu valor de carga é:")#verifica a carga
    r = numero_valido("Seu ponto será em:")#ponto da esfera gaussiana
    R = numero_valido("O raio da sua esfera será:")#tamanho da esfera 
    if r <= 0 or R <= 0 or r > R:
        print("As condições de distâncias não podem ser executadas, por favor utilize valores válidos para raios e superfície gaussiana interna")
        return None
    distancia = np.linspace(0.01*R, R, 500) #distância do gráfico
    k = 1/(4*pi*epsilon_0)
    campo = (k*q*distancia)/(R**3)
    campo_usuario = (k*q*r)/(R**3)
    #plot do campo
    plt.plot(distancia, campo, 'b-')     # Curva principal
    plt.plot([r], [campo_usuario], 'ro') # Ponto do usuário
    #Configurações mínimas
    plt.xlabel('Distância (m)') #o que é o eixo x
    plt.ylabel('Campo (N/C)') #o que é o eixo y
    plt.title(f'Carga: {q:.1e} C | Raio: {R} m') #titulo do gráfico 
    plt.axvline(x=R, color='gray', linestyle='--', alpha=0.7)  # Linha do raio
    plt.annotate(f'Raio R={R}m', xy=(R, max(campo)/2), rotation=90)
    plt.tight_layout()  # Melhor ajuste
    plt.grid(True) #presença de um grid
    
    plt.show()

#geração de grafico do campo fora de uma esfera, porém em escala logaritma já que há o decaimento muito rápido e não seria visível a longas distâncias
def grafico_ex():
    q = numero_valido("Seu valor de carga é:")
    r = numero_valido("Sua distância é de:")
    distancia = np.logspace(np.log10(0.001*r), np.log10(r), 500)
    if r <= 0: #não há raio negativo
            print("não há raio negativo, há algo errado com seu dado")
            return None
    k = 1/(4*pi*epsilon_0)
    campo = (k*q)/(distancia**2)
    campo_usuario = (k*q)/(r**2)
    #Plot do campo
    plt.plot(distancia, campo, '-b')
    plt.plot([r], [campo_usuario], 'ro')
 #Configurações mínimas (quase tudo igual ao anterior)
    plt.axvline(x=r, color='gray', linestyle='--', alpha=0.7)  # Linha do raio
    plt.annotate(f'Distância ={r}m', xy=(r, max(campo)/2), rotation=90)
    plt.tight_layout() 
    plt.xlabel('Distância em log (m)') 
    plt.ylabel('Campo (N/C)')
    plt.title(f'Carga: {q:.1e} C | Raio: {r} m')
    plt.grid(True)
    plt.yscale('log') #escala logaritima em x
    plt.xscale('log') #escala logaritima em y
    plt.gca().xaxis.set_major_formatter(plt.ScalarFormatter())
    plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.1e'))
    
    plt.show()


#Codigo principal
def sistema(): 

    while True: #menu principal do sistema 
        print("\n"+"="*50) # deixa mais bonito e esepara as partes
        print(f"{'Bem vindo a calculadora de campos':^50}")
        print(f"{'(Lei de Gauss para esferas não condutoras)':^50}")
        print(f"{'Versão 1.0':^50}")
        print("="*50)
        print("\n Campo dentro de uma esfera não condutora (1):\n Campo fora de uma esfera não condutora (2):\n Gráfico de um campo a partir do centro da esfera (3):\n Gráfico de um campo fora da esfera (em escala de log) (4):\n Sair (5):")
        print("Atenção aos navegantes, ao utilizar a função gerar gráficos lembresse que para cargas pequenas o efeito é pequeno a longa distância")
        print("="*50)
        escolha = input("qual ferramenta deseja utilizar:").strip() 
        
       
        if escolha not in ["1", "2", "3", "4", "5"]: #indica as opções válidas
            print("por favor escolha uma opção válida para proseguirmos:")
            continue
       
        while True: #opções válidas e seus pontos 
            if escolha == "1":
                lei_de_gauss_in()
            elif escolha == "2":
                lei_de_gauss_ex()
            elif escolha == "3": 
                grafico_in()
            elif escolha == "4":
                grafico_ex()
            elif escolha == "5":
                print("encerrando...")
                exit()
            if continuar(): #se não quiser mais continuar.
                print("voltando as equações:")
                break
sistema()