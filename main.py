def ler_nota(numero):
    while True:
        try:
            nota = float(input(f"Digite a {numero}ª nota entre 0 e 10: "))

            if 0 <= nota <= 10:
                return nota

            print("❌ A nota precisa estar entre 0 e 10.")

        except ValueError:
            print("⚠️ Digite apenas números. Exemplo: 8.5")


def calcular_situacao(media):
    if media >= 7:
        return "✅ APROVADO"
    elif media >= 5:
        return "🟡 RECUPERAÇÃO"
    return "❌ REPROVADO"


def mostrar_boletim(nome, notas):
    media = sum(notas) / len(notas)
    maior = max(notas)
    menor = min(notas)
    situacao = calcular_situacao(media)

    print("\n" + "=" * 45)
    print("📘 BOLETIM DO ALUNO".center(45))
    print("=" * 45)
    print(f"👤 Aluno: {nome}")
    print(f"📝 Notas: {notas}")
    print(f"📌 Quantidade de notas: {len(notas)}")
    print(f"⬆️ Maior nota: {maior:.2f}")
    print(f"⬇️ Menor nota: {menor:.2f}")
    print(f"📊 Média final: {media:.2f}")
    print(f"🎯 Situação: {situacao}")
    print("=" * 45)


while True:
    print("\n" + "=" * 45)
    print("🎓 SISTEMA DE MÉDIA ESCOLAR".center(45))
    print("=" * 45)

    nome = input("Digite o nome do aluno: ").strip().title()

    while not nome:
        nome = input("Nome vazio! Digite o nome do aluno: ").strip().title()

    while True:
        try:
            quantidade = int(input("Quantas notas deseja cadastrar? "))

            if quantidade > 0:
                break

            print("❌ Digite uma quantidade maior que zero.")

        except ValueError:
            print("⚠️ Digite um número inteiro. Exemplo: 4")

    notas = []

    for i in range(1, quantidade + 1):
        nota = ler_nota(i)
        notas.append(nota)

    mostrar_boletim(nome, notas)

    repetir = input("\nDeseja calcular outro aluno? (s/n): ").strip().lower()

    if repetir != "s":
        print("\n👋 Programa finalizado. Bons estudos!")
        break