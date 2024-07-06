from django.shortcuts import render
from .models import userChatWithAI
# Create your views here.
from .utils import results, leetcode



def home(request):
    if request.method == 'POST':
        import ast
        query = request.POST['query'] #get the username
        stats = leetcode(query)
        # username = request.POST['username']
        username = 'anonymous'
        output = results(stats)
        tosend = output
        print()
        print()
        print(output)
        print()
        print()
        output = output.split('\n')
        output = [x for x in output if x != 2]
        data = userChatWithAI.objects.create(user=username, query=query, response=output)
        data.save()
        all_data = userChatWithAI.objects.filter(user=username)
        all_data = all_data[::-1]
        str_list = all_data[0].response
        list_data = ast.literal_eval(str_list)
        data_output = []
        for i in all_data:
            data_output.append([i.query,ast.literal_eval(i.response)])
        # print(data_output[0])
        import spacy
        nlp = spacy.load('en_core_web_sm')
        # data_output[0][1] = nlp(data_output[0][1])
        newResponse = []
        for sent in data_output[0][1]:
            data = []
            for t in nlp(sent).sents:
                data.append(t.text)
            if data != []:
                newResponse.append(' '.join(data))
            print("Printing data: ", data)
        print(newResponse)
        data_output[0][1] = newResponse
        return render(request, 'assistant/home.html', {'all_data': data_output[0],'response':tosend, 'username':query})
    return render(request, 'assistant/home.html')


