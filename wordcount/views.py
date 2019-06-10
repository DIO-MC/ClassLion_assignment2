from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split() #문자열 분리 후 리스트로 저장

    word_dictionary = {} #빈 딕셔너리 생성

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1 #단어 존재하면 카운트
        else:
            word_dictionary[word] = 1 #첨 나오는 단어면 key, value 등록
    
    return render(request, 'count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})
