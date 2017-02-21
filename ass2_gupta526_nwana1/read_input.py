import csv, sys, os, string

file_name = input("Please Enter a file name: ")
input_file = open("dataset/"+file_name, 'r')
out_file = open('dataset/transformed_file.csv', 'w')
reader = (csv.reader(input_file))
writer = csv.writer(out_file)
workclass = {"workclass":" workclass",
			' Never-worked':'0',
			" Without-pay":"1",
			" Self-emp-not-inc":"2",
			" Self-emp-inc":"3",
			" Private":"4",
			" Local-gov":"5",
			" Federal-gov":"6",
			" State-gov":"7"," ?": "?"}
relationship = {"marital_status":"marital_status",
				" Married-civ-spouse":"0",
				" Divorced":"1",
				" Never-married":"2",
				" Widowed":"3",
				" Married-spouse-absent":"4",
				" Married-AF-spouse":"5",
				" Separated":"6"," ?": "?"}
occupation = {"occupation":" occupation",
			" Tech-support":"0",
			" Craft-repair":"1",
			" Other-service":"2",
			" Sales":"3",
			" Exec-managerial":"4",
			" Prof-specialty":"5",
			" Handlers-cleaners":"6",
			" Machine-op-inspct":"7",
			" Adm-clerical":"8",
			" Farming-fishing":"9",
			" Transport-moving":"10",
			" Priv-house-serv":"11",
			" Protective-serv":"12",
			" Armed-forces":"13"," ?": "?"}
dependent = {"relationship": " relationship",
			 " Wife":"0",
			 " Own-child":"1",
			 " Husband":"2",
			 " Not-in-family":"3",
			 " Other-relative":"4",
			 " Unmarried":"5"," ?": "?"}
race = {"race": " race",
		" White":"0",
		" Asian-Pac-Islander":"1",
		" Amer-Indian-Eskimo":"2",
		" Black":"3",
		" Other":"4"," ?": "?"}
gender = {'gender': "gender",
		  ' Male':'0',
		  ' Female':'1'," ?": "?"}
country = {	"native_country": "native_country",
			" United-States":"0",
			" Canada":"1",
			" England":"2",
			" Cambodia": "3",
			" Puerto-Rico":"4",
			" Germany":"5",
			" Outlying-us":"6",
			" India":"7",
			" Japan":"8",
			" Greece":"9",
			" South":"10",
			" China":"11",
			" Cuba":"12",
			" Iran":"13",
			" Honduras":"14",
			" Philippines":"15",
			" Italy":"16",
			" Poland":"17",
			" Jamaica": "18",
			" Vietnam":"19",
			" Mexico":"20",
			" Portugal":"21",
			" Ireland":"22",
			" France":"23",
			" Dominican-Republic":"24",
			" Laos":"25",
			" Ecuador":"26",
			" Taiwan":"27",
			" Haiti":"28",
			" Columbia":"29",
			" Hungary":"30",
			" Guatemala":"31",
			" Nicaragua":"32",
			" Scotland":"33",
			" Thailand":"34",
			" Yugoslavia":"35",
			" El-salvador":"36",
			" Trinadad&Tobago":"37",
			" Hong":"39",
			" Holand-netherlands":"40",
			" ?": "?"}
for row in reader:
	
	row[2] = workclass.get(row[2])
	row[3]=""
	row[6] = relationship.get(row[6])
	row[7] = occupation.get(row[7])
	row[8] = dependent.get(row[8])
	row[9] = race.get(row[9])
	row[10] = gender.get(row[10])
	if row[13].isdigit():
		if int(row[13])>70:
			row[13] = "40"
	row[14] = country.get(row[14])
	j=3
	while(j<15):
		row[j]=row[j+1]
		j=j+1
	row[15]=""
	writer.writerow(row)


out_file.close()
input_file.close()