import wolframalpha

question = input('Question: ')
app_id = 'U5HXGG-79KT69H58Q'
client = wolframalpha.Client(app_id)
res = client.query(question)
answer = next(res.results).text
print(answer)
