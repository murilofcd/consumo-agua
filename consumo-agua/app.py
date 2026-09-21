# Solicitando o tipo de imóvel e o consumo mensal ao usuário
tipo_imovel = input("Digite o tipo do imóvel (comercial, casa ou apartamento): ").strip().lower()
consumo_m3 = float(input("Digite o consumo mensal de água em m³: "))

print("\n--- Classificação do Perfil de Consumo ---")

# Aplicando as regras de negócio
if tipo_imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif tipo_imovel == "apartamento" and consumo_m3 < 10:
    print("Consumo econômico – excelente controle de água!")
elif tipo_imovel == "apartamento" or (tipo_imovel == "casa" and consumo_m3 <= 25):
    print("Consumo moderado – dentro do padrão residencial.")
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
