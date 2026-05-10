class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:  
            return []

        word_length = len(words[0])  # Длина одного слова 
        total_length = len(words) * word_length  
        result = [] 
        word_count = {}  

        for word in words:  # Подсчитываем количество вхождений каждого слова в исходном списке
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        for i in range(word_length):  # Перебираем все возможные сдвиги
            left = i  
            sub_count = {} 
            count = 0  

            for j in range(i, len(s) - word_length + 1, word_length):  # Сканируем строку с шагом word_length
                sub_word = s[j:j + word_length]  # Извлекаем текущее слово из строки

                if sub_word in word_count: 
                    if sub_word in sub_count:
                        sub_count[sub_word] += 1
                    else:
                        sub_count[sub_word] = 1
                    count += 1 

                    while sub_count[sub_word] > word_count[sub_word]:  # Если текущее слово встречается чаще, чем нужно, сдвигаем левую границу
                        sub_count[s[left:left + word_length]] -= 1  # Убираем левое слово из окна
                        count -= 1  
                        left += word_length  # Сдвигаем левую границу вправо на длину слова

                    if count == len(words):  # Если количество слов в окне равно общему количеству слов, значит найдена подстрока
                        result.append(left)  # Добавляем индекс левой границы в результат
                else:  # Если встретили слово, которого нет в исходном списке, сбрасываем окно
                    sub_count.clear()  
                    count = 0  
                    left = j + word_length  
        
        return result  