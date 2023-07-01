from functions import *

if __name__ == '__main__':
    saldar()
    previsao_tempo()
    #menu()

    while True:
        tecla_espaco()
        while True:
            intent = ouvir()
            if intent == None:
                intent
            else:
                break

        if 'abrir o opera' in intent or 'abrir navegador' in intent:
            os.system('start chrome')
        elif 'txt' in intent:
            escrever_txt()
        elif 'previsao do tempo' in intent:
            previsao_tempo()
        elif 'conte uma piada' in intent:
            joke = pyjokes.get_joke('pt-br')
        elif 'abrir camera' in intent:
            abrir_camera()
        elif 'meu ip' in intent:
            meu_ip()
        elif 'pesquise no youtube' in intent:
            video = ouvir()
            youtube(video)
        elif 'pesquisar' in intent :  
            pesquisa = ouvir()
            pesquisar_google(pesquisa)
        elif 'desligar note' in intent:
            desligar_pc()
        elif 'desligar agora' in intent:
            fale('até mais tarde Mestre')
            break
        elif 'pesquisa avançada' in intent:
            chatgpt()

        else:
            fale('não entendi, pode repetir?')

