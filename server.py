import socket
import threading
from time import sleep
from questions import Questions
import json
import random
import operator
import pickle

#Variables for holding information about connections
connections = []
total_connections = 0

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True

scores = {"p0":  0,
          "p1" : 0,
          "p2" : 0}

answered_questions = []
total_questions = 25 * 3 #all fields

class Client(threading.Thread):
    def __init__(self, socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal
        self.score = 0
        self.questions = Questions() 
        self.askedQuestionCtg = ""
        self.askedQuestionNum = ""
        self.askedQuestionCode = ""

    def __str__(self):
        return str(self.id) + " " + str(self.address)
    
    def id(self):
        return self.id
    
    def run(self):
        while self.signal:
            try:
                data = self.socket.recv(2048)
            except:
                print("Client " + str(self.address) + " has disconnected\n")
                self.signal = False
                connections.remove(self)
                break
            # ako stignalo neshto
            if data != "":
                decoded_data = str(data.decode("utf-8"))

                # return scores from all players 
                if decoded_data == "get_scores":
                    data_rsp = json.dumps(scores)
                    #print("server response data= ", data_rsp)
                    connections[self.id].socket.sendall(data_rsp.encode())                
                
                elif decoded_data == "get_answered_questions":
                    data_rsp = json.dumps(answered_questions)
                    connections[self.id].socket.sendall(data_rsp.encode())                

                # answer response (in json format)
                elif is_json(data.decode("utf-8")):
                    json_data  = json.loads(data.decode("utf-8"))
                    
                    print("Received from client\n")
                    print(json_data)
                    print("Q: ",json_data.get("question"))
                    print("A: ",json_data.get("answer"))
                    
                    corr_answer = self.questions.GetCorrectAnswer(self.askedQuestionCtgName, \
                                                                  int(self.askedQuestionNum), \
                                                                  self.askedQuestionCode)

                    print("Corr answer is: ",corr_answer)
                    print("User's answer is: ",json_data.get("answer"))
                    
                    if json_data.get("answer") == corr_answer:
                        print("Correct answer!\n")
                        data_rsp = json.dumps({"a": "correct"})
                        connections[self.id].socket.sendall(data_rsp.encode())
                        # update global scores
                        scores["p"+str(self.id)] += 100
                    else: 
                        print("Incorrect answer!\n")
                        data_rsp = json.dumps({"a": "incorrect"})
                        connections[self.id].socket.sendall(data_rsp.encode())
                        # update global scores
                        scores["p"+str(self.id)] -= 100

                    
                    print("Answered ", self.askedQuestionCode)
                    answered = "cat"+str(self.askedQuestionNum)+"."+ self.askedQuestionCode[-3:]
                    answered_questions.append(answered)           
                            
                    print(scores)
               
                    print("ID " + str(self.id) + ": sent: " + str(data.decode("utf-8")))
               

                # if set data has "q_" prefix then it is question from client!
                elif decoded_data[0:2] == "q_":
                    print("Decoded data: ", decoded_data)
                    cat_num = str(data.decode("utf-8"))[5]
                    print("Asked Question is from category: ", cat_num)
                    
                    category_name = self.questions.GetCategoryName(int(cat_num)-1)
                    print("Question is from category: ", category_name)
                    self.askedQuestionCtgName = category_name
                    
                    questions_cat = self.questions.GetAllQuestionsFromCategory(category_name)
                    print("All questions from this category: ", questions_cat)

                    question_number = decoded_data[-3]
                    print("Question number is ", question_number)
                    self.askedQuestionNum = question_number

                    print("Question content is:")
                    q_str = "q" + question_number + "." + question_number + "00"
                    print(q_str)
                    self.askedQuestionCode = q_str

                    print("QA: ", questions_cat[int(question_number)-1]) 
                    print("--------------------------------------")
                
                    question_content = questions_cat[int(question_number)-1].get(str(q_str)).get("content")
                    print(question_content)

                    print("Possible answers:\n")
                    question_answers = questions_cat[int(question_number)-1].get(str(q_str)).get("possible_answers")
                    print(list(question_answers))
                    
                    # Send question
                    q_data = json.dumps({"q": question_content,
                                         "a": list(question_answers)[0], 
                                         "b": list(question_answers)[1], 
                                         "c": list(question_answers)[2]})
                    print(q_data)
                    connections[self.id].socket.sendall(q_data.encode())
                # elif decoded_data == "get_answered":
                #     data_ = pickle.dumps(answered_questions)
                #     connections[self.id].socket.sendall(data_)                
                else:
                    pass

#Wait for new connections
def newConnections(socket):
    while True:
        sock, address = socket.accept()
        global total_connections
        connections.append(Client(sock, address, total_connections, "", True))
        connections[len(connections) - 1].start()
        print("New connection at ID " + str(connections[len(connections) - 1]))
        
        connections [total_connections].socket.sendall(str.encode("connected"))
        total_connections += 1
        print("Total players (connections) are ", total_connections)             
        if total_connections == 3: 
            for client in connections:
                if(client.id == 1):
                    print("Sending -start_first- to client ", client.id)
                    client.socket.sendall(str.encode("start_first"))
                else:
                    print("Sending -start- to client ", client.id)
                    client.socket.sendall(str.encode("start"))
            print("Entered max number of players. No more room for new players!\n")
            
            # server is not longer accepting new connections
            # while True:
            #     pass
            
            
def chooseWinner(socket):
    while True:
        #print(answered_questions)
        if len(answered_questions) == total_questions:
            print("All questions are answered! End of game!")
            winner = max(scores.items(),key=operator.itemgetter(1))[0]
            score = scores[winner]
            print("Winner is {} with {}".format(winner,score))
            for conn in connections:
                data_to_send = "winner_"+str(winner[-1])
                conn.socket.sendall(data_to_send.encode())
            #socket.close()
        sleep(1)
            

def main():
    #Get host and port
    host = "localhost" #input("Host: ")
    port = 8080 #int(input("Port: "))

    print("Server is up and running\n")
    print("Waiting for players...")
    #Create new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    #Create new thread to wait for connections
    newConnectionsThread = threading.Thread(target = newConnections, args = (sock,))
    newConnectionsThread.start()

    winnerThread = threading.Thread(target=chooseWinner, args=(sock,))
    winnerThread.start()                                  
    
main()
