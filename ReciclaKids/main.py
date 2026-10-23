import pygame
import random

pygame.init()

# Configurações
LARGURA = 900
ALTURA = 600
POSICAO_INICIAL = (LARGURA // 2, 190)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Recicla Kids")

# Cores
BRANCO = (255, 255, 255)
AZUL = (0, 102, 204)
VERMELHO = (255, 0, 0)
VERDE = (0, 180, 0)
AMARELO = (255, 215, 0)
PRETO = (0, 0, 0)

FUNDO = (220, 245, 220)

# Fonte
fonte = pygame.font.SysFont("Arial", 30)
fonte_objeto = pygame.font.SysFont("Segoe UI Emoji", 80)

fonte_vitoria = pygame.font.SysFont(
    "Arial",
    50,
    bold=True
)

instrucao = fonte.render(
    "Arraste o resíduo para a lixeira correta",
    True,
    PRETO
)


# Lixeiras
lixeiras = {
    "papel": pygame.Rect(30, 400, 180, 180),
    "plastico": pygame.Rect(240, 400, 180, 180),
    "vidro": pygame.Rect(450, 400, 180, 180),
    "metal": pygame.Rect(660, 400, 180, 180)
}


# Objetos recicláveis

objetos = [
    ("📰", "papel"),
    ("🥤", "plastico"),
    ("🍾", "vidro"),
    ("🥫", "metal")
]

nomes_objetos = {
    "📰": "Jornal",
    "🥤": "Garrafa PET",
    "🍾": "Garrafa de vidro",
    "🥫": "Lata de alumínio"
}

dicas = {
    "📰": "O papel pode ser reciclado.",
    "🥤": "O plástico leva anos para se decompor.",
    "🍾": "O vidro é 100% reciclável.",
    "🥫": "O metal pode ser reciclado muitas vezes."
}

objeto_atual = random.choice(objetos)



# Caixa do objeto

titulo = fonte.render(
    "RECICLA KIDS",
    True,
    VERDE
)

titulo_rect = titulo.get_rect(
    center=(LARGURA//2, 30)
)

objeto_rect = pygame.Rect(0, 0, 200, 80)
objeto_rect.center = POSICAO_INICIAL

arrastando = False
pontuacao = 0
mensagem = ""

rodando = True

lixeira_papel = pygame.image.load("Plain Text/lixeiraazul.png")
lixeira_papel = pygame.transform.scale(lixeira_papel, (180, 180))

lixeira_plastico = pygame.image.load("Plain Text/lixeiravermelha.png")
lixeira_plastico = pygame.transform.scale(lixeira_plastico, (180, 180))

lixeira_vidro = pygame.image.load("Plain Text/lixeiraverde.png")
lixeira_vidro = pygame.transform.scale(lixeira_vidro, (180, 180))

lixeira_metal = pygame.image.load("Plain Text/lixeiraamarela.png")
lixeira_metal = pygame.transform.scale(lixeira_metal, (180, 180))

clock = pygame.time.Clock()


while rodando:

    clock.tick(60)

    tela.fill(FUNDO)

    tela.blit(titulo, titulo_rect)

    instrucao_rect = instrucao.get_rect(
        center=(LARGURA // 2, 90)
    )

    tela.blit(instrucao, instrucao_rect)

    # Eventos
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN and pontuacao < 100:
            if objeto_rect.collidepoint(evento.pos):
                arrastando = True

        if evento.type == pygame.MOUSEBUTTONUP and arrastando:
            arrastando = False

            categoria = objeto_atual[1]

            if objeto_rect.colliderect(lixeiras[categoria]):

                pontuacao += 10

                mensagens_sucesso = [
                    "Muito bem!",
                    "Excelente!",
                    "Você acertou!",
                    "Parabéns!",
                    "Ótimo trabalho!"
                ]

                mensagem = random.choice(mensagens_sucesso)

                novo_objeto = random.choice(objetos)

                while novo_objeto == objeto_atual:
                    novo_objeto = random.choice(objetos)

                objeto_atual = novo_objeto

                objeto_rect.center = POSICAO_INICIAL
            else:

                mensagem = "Tente novamente!"

                objeto_rect.center = POSICAO_INICIAL

        if evento.type == pygame.MOUSEMOTION and arrastando:
            objeto_rect.center = evento.pos


            objeto_rect.x = max(0, min(objeto_rect.x, LARGURA - objeto_rect.width))
            objeto_rect.y = max(0, min(objeto_rect.y, ALTURA - objeto_rect.height))

    # Desenhar lixeiras
    #pygame.draw.rect(tela, AZUL, lixeiras["papel"])
    #pygame.draw.rect(tela, VERMELHO, lixeiras["plastico"])
    #pygame.draw.rect(tela, VERDE, lixeiras["vidro"])
    #pygame.draw.rect(tela, AMARELO, lixeiras["metal"])

    #tela.blit(fonte.render("Papel", True, PRETO), (90, 485))
    #tela.blit(fonte.render("Plástico", True, PRETO), (290, 485))
    #tela.blit(fonte.render("Vidro", True, PRETO), (520, 485))
    #tela.blit(fonte.render("Metal", True, PRETO), (730, 485))

    # Objeto
    #pygame.draw.rect(tela, (200, 200, 200), objeto_rect)


    if pontuacao < 100:
        sombra_rect = objeto_rect.copy()
        sombra_rect.x += 5
        sombra_rect.y += 5

        pygame.draw.rect(
            tela,
            (180, 180, 180),
            sombra_rect,
            border_radius=10
        )

        pygame.draw.rect(
            tela,
            BRANCO,
            objeto_rect,
            border_radius=10
        )

        pygame.draw.rect(
            tela,
            VERDE,
            objeto_rect,
            3,
            border_radius=10
        )
        texto_objeto = fonte_objeto.render(
            objeto_atual[0],
            True,
            PRETO
        )

        emoji_rect = texto_objeto.get_rect(
            center=objeto_rect.center
        )

        tela.blit(texto_objeto, emoji_rect)

        nome = nomes_objetos[objeto_atual[0]]

        texto_nome = fonte.render(
            nome,
            True,
            PRETO
        )

        nome_rect = texto_nome.get_rect(
            center=(LARGURA // 2, 260)
        )

        tela.blit(texto_nome, nome_rect)

        texto_dica = fonte.render(
            dicas[objeto_atual[0]],
            True,
            PRETO
        )

        dica_rect = texto_dica.get_rect(
            center=(LARGURA // 2, 310)
        )

        tela.blit(texto_dica, dica_rect)



    # Pontuação
    texto_meta = fonte.render(
        f"🎯 Meta: {pontuacao}/100",
        True,
        PRETO
    )

    tela.blit(texto_meta, (700, 20))
    pygame.draw.rect(
        tela,
        PRETO,
        (650, 60, 200, 20),
        2
    )

    pygame.draw.rect(
        tela,
        VERDE,
        (
            650,
            60,
            min(pontuacao * 2, 200),
            20
        )
    )

    texto_pontos = fonte.render(
        f"⭐ Pontos: {pontuacao}",
        True,
        PRETO
    )
    tela.blit(texto_pontos, (20, 20))



    if pontuacao >= 100:
        tela.fill(FUNDO)

        tela.blit(titulo, titulo_rect)


        texto_vitoria = fonte_vitoria.render(
            "VOCÊ VENCEU!",
            True,
            VERDE
        )

        vitoria_rect = texto_vitoria.get_rect(
            center=(LARGURA // 2, 200)
        )

        tela.blit(texto_vitoria, vitoria_rect)
        texto_final = fonte.render(
            "Obrigado por ajudar o planeta!",
            True,
            VERDE
        )

        final_rect = texto_final.get_rect(
            center=(LARGURA // 2, 260)
        )

        tela.blit(texto_final, final_rect)

        texto_final2 = fonte.render(
            "Você é um herói da reciclagem!",
            True,
            VERDE
        )

        final2_rect = texto_final2.get_rect(
            center=(LARGURA // 2, 320)
        )

        tela.blit(texto_final2, final2_rect)

        texto_missao = fonte.render(
            "🏆 Missão concluída!",
            True,
            AMARELO
        )

        missao_rect = texto_missao.get_rect(
            center=(LARGURA // 2, 120)
        )

        tela.blit(texto_missao, missao_rect)

        pygame.display.update()

        pygame.time.wait(5000)

        rodando = False

    # Mensagem
    cor_msg = VERDE



    if pontuacao >= 100:
        cor_msg = AMARELO

    if mensagem == "Tente novamente!":
        cor_msg = VERMELHO

    if pontuacao >= 100:
        mensagem = ""

    texto_msg = fonte.render(
        mensagem,
        True,
        cor_msg
    )

    msg_rect = texto_msg.get_rect(
        center=(LARGURA // 2, 70)
    )


    tela.blit(texto_msg, msg_rect)


    #jornal = pygame.image.load("Plain Text/envelope.png")
    #jornal = pygame.transform.scale(jornal, (120, 120))

    #pet = pygame.image.load("Plain Text/copoplastico.png")
    #pet = pygame.transform.scale(pet, (120, 120))

    #vidro = pygame.image.load("Plain Text/xicaradevidro.png")
    #vidro = pygame.transform.scale(vidro, (120, 120))

    #lata = pygame.image.load("Plain Text/lata.png")
    #lata = pygame.transform.scale(lata, (120, 120))

    if pontuacao < 100:
        tela.blit(lixeira_papel, (30, 400))
        tela.blit(lixeira_plastico, (240, 400))
        tela.blit(lixeira_vidro, (450, 400))
        tela.blit(lixeira_metal, (660, 400))

        tela.blit(fonte.render("📰 Papel", True, PRETO), (70, 485))
        tela.blit(fonte.render("🥤 Plástico", True, PRETO), (260, 485))
        tela.blit(fonte.render("🍾 Vidro", True, PRETO), (500, 485))
        tela.blit(fonte.render("🥫 Metal", True, PRETO), (700, 485))

    pygame.display.update()

pygame.quit()





