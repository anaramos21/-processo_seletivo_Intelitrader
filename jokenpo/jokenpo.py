
def jokenpo(primeiro_jogador, segundo_jogador):
    Opcao_moviment = ['Pedra', 'Papel', 'Tesoura']
    Opcao_jogadores = [primeiro_jogador, segundo_jogador]
    
       if Opcao_jogadores.count('Pedra') == 1 and Opcao_jogadores.count('Tesoura') == 1:
        return 'Ganhador: Pedra'

    if Opcao_jogadores.count('Tesoura') == 1 and Opcao_jogadores.count('Papel') == 1:
        return 'Ganhador: Tesoura'

    if Opcao_jogadores.count('Papel') == 1 and Opcao_jogadores.count('Pedra') == 1:
        return 'Ganhador: Papel'

     if  Opcao_movimento.count(primeiro_jogador) == 0 or  Opcao_movimento.count(segundo_jogador) == 0:
        return 'Opção inválida!'

    if primeiro_jogador == segundo_jogador:
        return 'Empatou!'