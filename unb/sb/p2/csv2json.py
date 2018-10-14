import csv, json

value_or_not = lambda x,y: x if x else y
unpack = lambda x,y: (x[z] for z in y)

def script_main():
	name = 'questoes_p2'
	ifilen = '%s.csv'%(name)
	ofilen = '%s.json'%(name)
	print('(I) Converting %s to Vue readable JSON...'%(ifilen,))

	json_data = []
	with open(ifilen,'r',encoding='utf-8') as fp:
		for idx, item in enumerate(csv.DictReader(fp), start=1):
			question_text = value_or_not(
				*unpack(item, ('questao_html','questao_texto'))
			)
			trivia = item['resposta']
			json_data.append({
				'text':question_text,
				'trivia':int(trivia),
				'idx':idx,
			})

	json.dump(json_data, open(ofilen,'w',encoding='utf-8'), ensure_ascii=False)

	return True
if __name__ == '__main__':
	script_main()