

# Abre o arquivo nomedoarquivo.fasta para escrita:
with open("todos.fasta", "w") as file:

    # Percorre a lista de arquivos a serem lidos:
    for temp in ["Aethiopicajuntos.fas", "Arabicajuntos.fas", "Braziliensisjuntos.fas", "Donovanijuntos.fas", "Enriettiijuntos.fas", "Infantumjuntos.fas", "Majorjuntos.fas", "Mexicanajuntos.fas", "Panamensisjuntos.fas", "Peruvianiajuntos.fas"]:

        # Abre cada arquivo para leitura:
        with open(temp, "r") as t:

            # Escreve no arquivo o conteúdo:
            file.writelines(t)
            file.writelines('\n')
