import sys
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtCore import QTimer
import socket
import random
from time import sleep
# CO IDZIE DO SERVERA
# + -> +1 punkt dla gracza
# - -> -1 szansa
# w -> wygranie rundy +10 dla gracza

# CO IDZIE DO GRACZA
# ok -> gracz przyjenty do gry
# no -> gracz nieprzyjety do gry - pokoj pelny lub inny problem
# s -> zaczela sie nowa gra

# n -> nowa runda (ktos wygral runde)
# e -> koniec gry 

sys.path.append('/StartDialogUI.py')
from StartDialogUI import Ui_StartDialog

sys.path.append('/HangmanGameScreen.py')
from HangmanGameScreen import Ui_GameScreen

BUFFER_SIZE = 1024

class GameWindow(QWidget, Ui_GameScreen):
    def __init__(self, connection_thread):
        super(GameWindow, self).__init__()
        self.setupUi(self)
        self.word_to_guess = ""
        self.current_word_state = ""
        self.attempts_left_per_game = 6 
        self.used_letters = set()
        self.round = 0
        self.total_score = 0
        self.connection_thread = connection_thread
     

    def connect_signals(self, connection_thread):
            connection_thread.signal_round_start.connect(self.start_new_round)
            print("Connected signal_round_start to start_new_round")
            connection_thread.signal_game_start.connect(self.handle_game_start)
            print("Connected signal_game_start to handle_game_start")
            connection_thread.signal_game_end.connect(self.handle_game_over)


    def keyPressEvent(self, event):
        key = event.text().upper()
        if key.isalpha() and key not in self.used_letters:
            self.used_letters.add(key)

            if key in self.word_to_guess:
                new_word_state = ""
                for word_letter, current_state_letter in zip(self.word_to_guess, self.current_word_state):
                    if word_letter == key:
                        new_word_state += key
                    else:
                        new_word_state += current_state_letter

                self.current_word_state = new_word_state
                self.update_word_label()

                if "_" not in self.current_word_state:
                    self.handle_round_over("Congratulations! You won this round!")
                    # Wygral info do servera
            else:
                self.attempts_left_per_game -= 1
                self.update_attempts_label()

    
                if self.attempts_left_per_game == 0:
                    self.handle_game_over("Game over! You ran out of attempts for the entire game")

        self.update_used_letters_label()

    def handle_game_start(self):
        print("init game..")
    
    def start_new_round(self, secret_word):
        print(f"Received signal_round_start with secret_word: {secret_word}")
        if self.round < 5:
            # Initialize or reset round variables
            self.word_to_guess = secret_word.upper()
            self.current_word_state = "_" * len(self.word_to_guess)
            self.used_letters = set()

            # Update UI elements
            self.update_word_label()
            self.update_attempts_label()
            self.update_used_letters_label()

            # Increment round number
            self.round += 1
        else:
            # End of the game, display final score
            self.handle_game_over(f"Game over! Your final score is {self.total_score}")


    def update_word_label(self):
        self.wordLabel.setText(" ".join(self.current_word_state))

    def update_attempts_label(self):
        self.attemptsLabel.setText(f"Attempts left: {self.attempts_left_per_game}")

    def update_used_letters_label(self):
        used_letters_text = "Used Letters: " + ", ".join(sorted(self.used_letters))
        self.usedLettersLabel.setText(used_letters_text)

    def handle_round_over(self, message):
        QMessageBox.information(self, "Round Over", message, QMessageBox.Ok)

        round_score = self.attempts_left_per_game

        self.total_score += round_score

        self.start_new_round() # ??????

    def handle_game_over(self, message):
        QMessageBox.information(self, "Game Over", message, QMessageBox.Ok)

 
        reply = QMessageBox.question(self, "Play Again?", "Do you want to play again?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.round = 0
            self.total_score = 0
            self.attempts_left_per_game = 6
            self.start_new_game()
        else:
            self.close()
            startDialog.show()

class ConnectionThread(QThread):
    signal_game_start = pyqtSignal()
    # sygnal co wysyla slowo
    signal_round_start = pyqtSignal(str)
    signal_game_end = pyqtSignal()
    

    def __init__(self, nick_name, game_id):
        super(ConnectionThread, self).__init__()
        self.nick_name = nick_name
        self.game_id = game_id
        self.client_socket = None

    def run(self):
        try:
            server_address = ('localhost', 2000)
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(server_address)

            message = f"{self.nick_name} {self.game_id}"
            self.client_socket.sendall(message.encode('utf-8'))

            response = self.recv_serv_msg()

            if response == "ok":
                print("Joined game.")
                self.handle_server_updates() 

            elif response == "no":
                print("Full room.")
                

            else:
                print("Unexpected message from the server:", response)


        except Exception as e:
            print("Error connecting to server:", e)

    def recv_serv_msg(self):
        msg =""
        while True:
            chunk = self.client_socket.recv(BUFFER_SIZE).decode('utf-8')
            msg+= chunk

            if '\n' in msg:
                msg = msg.strip('\n')
                break
        return msg

    
            
    def handle_server_updates(self):
        while(1):
            mess = self.recv_serv_msg()
            if mess == "s":
                self.signal_game_start.emit()
            elif mess == "n":
                secret_word = self.recv_serv_msg()
                print(secret_word)
                self.signal_round_start.emit(secret_word)
        
            elif mess == "e":
                self.signal_game_end.emit()
            # cos z updatem UI ale nwm czy to w tym wątku czy innym
            else:
                print("Unexpected message from the server:", mess, " ", len(mess))     




class StartDialog(QDialog, Ui_StartDialog):
    def __init__(self):
        super(StartDialog, self).__init__()
        self.setupUi(self)
        self.joinGameButton.clicked.connect(self.onJoinGameButtonClicked)
        self.client_socket = None 
        self.connection_thread = None

    def connect_signals(self, connection_thread):
        connection_thread.signal_game_start.connect(self.start_new_game)

    def onJoinGameButtonClicked(self):
        game_id = self.gameIdEdit.text()
        nick_name = self.nickNameEdit.text()
        print("Clicked Join Game Button. Game ID:", game_id, "Nick Name:", nick_name)

        try:
            self.connection_thread = ConnectionThread(nick_name, game_id)
            self.connection_thread.start()

            # Connect signals after the thread has started
            self.connect_signals(self.connection_thread)

        except Exception as e:
            QMessageBox.warning(self, "Connection Error", f"Error connecting to server: {e}", QMessageBox.Ok)

    def start_new_game(self):
        self.hide()
        self.game_window = GameWindow(self.connection_thread)
        # Connect signals after the GameWindow is created
        self.game_window.connect_signals(self.connection_thread)  
        self.game_window.activateWindow()
        self.game_window.raise_()
        self.game_window.show()

    
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    startDialog = StartDialog()
    startDialog.show()

    sys.exit(app.exec_())