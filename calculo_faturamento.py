# CRIAÇÃO DAS FUNÇÕES

# Função para calcular o faturamento líquido (erro de lógica: o correto seria subtrair os custos operacionais, não somar)
def calcular_faturamento_liquido(vendas_brutas, taxa_imposto, custos_operacionais):

    # Calcula o imposto sobre as vendas
    valor_imposto = vendas_brutas * taxa_imposto
    # Calcula o faturamento líquido deduzindo impostos e custos
    faturamento_liquido = vendas_brutas - valor_imposto - custos_operacionais

    # Retorna o faturamento líquido calculado
    return faturamento_liquido


# Função para verificar se o faturamento atingiu a meta estipulada
def verificar_bonus(faturamento, meta):
    # Verifica se o faturamento atingiu a meta para liberar o bônus
    if faturamento >= meta:
        print("Meta atingida! Bônus liberado.")
    else:
        print("Meta não atingida.")

# PROGRAMA PRINCIPAL
vendas_loja = 50000
imposto = 0.15          # 15%
custos = 12000
meta_ano = 40000      # Meta estipulada (está como string, o correto seria um número para fazer isso é tirar as aspas)
print("Iniciando análise financeira...") # Primeira mensagem de saída para indicar o início do processo

faturamento_final = calcular_faturamento_liquido(vendas_loja, imposto, custos) # Calcula o faturamento líquido usando a função definida anteriormente
print(f"Faturamento Líquido Calculado: R$ {faturamento_final}") # Exibe o faturamento líquido calculado

verificar_bonus(faturamento_final, meta_ano) # Verifica se o faturamento atingiu a meta estipulada usando a função definida anteriormente

