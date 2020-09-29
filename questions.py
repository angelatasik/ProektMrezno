# list of dicts
Q = [{"Општи знаења" : [{'q1.100': {'content': "Која е единица мерка за јачина на електрична струја?", 'possible_answers': {'Волт','Ампер','Ват'}, 'correct_answer': 'Ампер'}},
                        {'q2.200': {'content': "Колку дециметри има во 0.2 км?", 'possible_answers': {'20000 dm','2000 dm','200 dm'}, 'correct_answer': '2000'}},
                        {'q3.300': {'content': "На кој хем. елемент се однесува Ag?", 'possible_answers': {'Сребро','Злато','Аргон'}, 'correct_answer': 'Сребро'}},
                        {'q4.400': {'content': "Зелениот пигмент во листот се нарекува:", 'possible_answers': {'Хлоропласт','Хлорофил','Хлорофилин'}, 'correct_answer': 'Хлорофил'}},
                        {'q5.500': {'content': "Најдолгата река во светот е:", 'possible_answers': {'Нил','Амазон','Јангцекјанг'}, 'correct_answer': 'Амазон'}}]}, 
    
    {"Главни градови" : [{'q1.100': {'content': "Кој е главен град на Германија?", 'possible_answers': {'Минхен','Берлин','Келн'}, 'correct_answer': 'Берлин'}},
                         {'q2.200': {'content': "Кој е главен град на Франција?", 'possible_answers': {'Анкара','Париз','Рим'}, 'correct_answer': 'Париз'}},
                         {'q3.300': {'content': "Кој е главен град на Италија?", 'possible_answers': {'Рим','Милано','Фиренца'}, 'correct_answer': 'Рим'}},
                         {'q4.400': {'content': "Кој е главен град на Полска?", 'possible_answers': {'Минск','Варшава','Прага'}, 'correct_answer': 'Варшава'}},
                         {'q5.500': {'content': "Кој е главен град на Норвешка?", 'possible_answers': {'Осло','Стокхолм','Берген'}, 'correct_answer': 'Осло'}}]},
    
    {"Биологија" :     [{'q1.100': {'content': "Колку коски има во човековото тело?", 'possible_answers': {'210','300','206'}, 'correct_answer': '206'}},
                        {'q2.200': {'content': "ДНК е позната и како:", 'possible_answers': {'РНК','Х-хромозом','Двојна спирала'}, 'correct_answer': 'Двојна спирала'}},
                        {'q3.300': {'content': "Кој дел од човековото око ја детектира светлината", 'possible_answers': {'Рожница','Мрежница','Белка'}, 'correct_answer': 'Мрежница'}},
                        {'q4.400': {'content': "Црниот дроб произведува", 'possible_answers': {'Плунка','Жлочен сок','Крв'}, 'correct_answer': 'Жлочен сок'}},
                        {'q5.500': {'content': "Која е основната структурна единица на сите живи организми?", 'possible_answers': {'Клетка','Крв','Кожа'}, 'correct_answer': 'Клетка'}}]},

    {"Математика" :    [{'q1.100': {'content': "Ако x+4=7, која е вредноста на x?", 'possible_answers': {'11','2','3'}, 'correct_answer': '3'}},
                        {'q2.200': {'content': "Бројот 36,873 заокружен на најблиската илјадарка е", 'possible_answers': {'36900','37000','40000'}, 'correct_answer': '37000'}},
                        {'q3.300': {'content': "Ако 5y-5=25, која е вредноста на y", 'possible_answers': {'5','4','6'}, 'correct_answer': '6'}},
                        {'q4.400': {'content': "Колку е квадратен корен од 64?", 'possible_answers': {'32','8','16'}, 'correct_answer': '8'}},
                        {'q5.500': {'content': "Кој број ќе го добиете ако ги помножите сите цифри од копчињата со бројки на телефонот?", 'possible_answers': {'0','40320','362880'}, 'correct_answer': '0'}}]},

    {"Географија":      [{'q1.100': {'content': "Која држава не се граничи со Мексико?", 'possible_answers': {'Хондурас','Сад','Тексас'}, 'correct_answer': 'Хондурас'}},
                         {'q2.200': {'content': "Која земја не излегува на Средоземно Море?", 'possible_answers': {'Шпанија','Русија','БиХ'}, 'correct_answer': 'Русија'}},
                         {'q3.300': {'content': "Која река тече низ Рим?", 'possible_answers': {'Сена','Рина','Тибер'}, 'correct_answer': 'Тибер'}},
                         {'q4.400': {'content': "Во која држава се наоѓа пустината Атакама?", 'possible_answers': {'Перу','Чиле','Аргентина'}, 'correct_answer': 'Чиле'}},
                         {'q5.500': {'content': "Која земја се наоѓа северно од Бугарија", 'possible_answers': {'Србија','Романија','Унгарија'}, 'correct_answer': 'Романија'}}]}]
   

class Questions:
    # Returns list of questions
    def GetAllQuestions(self):
        return Q
    
    # Returns list of questions from specific category
    def GetAllQuestionsFromCategory(self, category):
         for cat in self.GetAllQuestions(): 
            for key in cat:
                 if(key == category):
                     return cat.get(category)

    def GetQuestionAnswers(self, category, question):
        return self.GetAllQuestionsFromCategory(category).get(question)

    def GetCategoryName(self, category_number):
        return str(list(self.GetAllQuestions()[category_number])[0])
    
    def GetCorrectAnswer(self, category_name, question_number, question_code):
        ctg_qs = self.GetAllQuestionsFromCategory(category_name)
        a =  ctg_qs[question_number-1].get(question_code).get("correct_answer")
        return a

#q = Questions()
# print(q.GetCategoryName(0))
#q_cat1 = q.GetAllQuestionsFromCategory(q.GetCategoryName(0))
# # all questions from category
# print(q_cat1)

# print("\n")
# # 1st question
# print(q_cat1[0])
# print("\n")

# # just question text
# print(q_cat1[0].get("q1.100").get("content")) 

# print(q_cat1[0].get("q1.100").get("possible_answers")) # all_answers
# print(list(q_cat1[0].get("q1.100").get("possible_answers"))[0]) # a)
# print(list(q_cat1[0].get("q1.100").get("possible_answers"))[1]) # b)
# print(list(q_cat1[0].get("q1.100").get("possible_answers"))[2]) # c)


#print(q_cat1[0].get
##print(q.GetCategoryName(1))

#print(q.GetCorrectAnswer("Главни градови", 1, "q1.100"))