import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
import pandas as pd

# Leitura dos dados
dados = pd.read_csv(r'C:\Users\camil\Downloads\fauna\fauna_ameacada.csv')

def verificar_risco():
    especie_ou_subespecie = line_edit.text().strip()
    if especie_ou_subespecie:  # Verifica se a entrada não está vazia
        if especie_ou_subespecie in dados['especie_ou_subespecie'].values:
            risco = dados.loc[dados['especie_ou_subespecie'] == especie_ou_subespecie, 'lista_2014'].iloc[0]
            if risco == 0:
                label.setText(f"{especie_ou_subespecie} está fora de perigo.")
            elif risco == 1:
                label.setText(f"{especie_ou_subespecie} está em perigo.")
            else:
                label.setText(f"{especie_ou_subespecie} não está definido.")
        else:
            label.setText(f"{especie_ou_subespecie} não foi encontrada.")
    else:
        label.setText("Por favor, digite o nome de uma espécie ou subespécie.")

# Criar uma instância da aplicação
app = QApplication(sys.argv)

# Criar uma janela
window = QWidget()
window.setWindowTitle('Verificar Risco')

# Criar um rótulo para a instrução
label = QLabel(window)
label.setText('Digite o nome da espécie ou subespécie:')
label.move(20, 20)

# Criar uma caixa de texto
line_edit = QLineEdit(window)
line_edit.move(20, 50)

# Criar um botão
button = QPushButton('Verificar', window)
button.clicked.connect(verificar_risco)
button.move(20, 80)

# Ajustar o tamanho da janela
window.resize(300, 150)

# Exibir a janela
window.show()

# Executar a aplicação
sys.exit(app.exec_())
