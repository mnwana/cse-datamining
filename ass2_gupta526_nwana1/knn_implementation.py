# File to get the K nearest neighbors and 
# classfy on the basis of majority vote
# input file: eculiden diatance iris or euclidean distance income

import csv, sys, os, string, operator
# from read_input import transform_income

# from distance_functions import calculateDist

def getclass(neighbors,p,last_column_num):
	classVotes={}
	i=3
	for neighbor in neighbors:
		for i in range(p,k):
			# get class and then add to class votes
			class_ = neighbor[i]
			if class_ in classVotes:
				classVotes[class_] += 1
			else:
				classVotes[class_] = 1
			i = i+3
	predicted_class = sorted(classVotes.items(), key=operator.itemgetter(1), 
						reverse=True)
	return (predicted_class[0][0])

def getClassSetFromIris():
	iris_test_file = open("dataset/transformed_iris_test_file.csv")
	reader = csv.reader(iris_test_file)
	# test_set={id:class}
	# test_set = {}
	for row in reader:
		test_set = {row[5]: row[4]}
	iris_test_file.close()
	return test_set

def getClassSetFromIncome():
	income_test_file = open("dataset/transformed_inc_test_file.csv")
	reader = csv.reader(income_test_file)
	# test_set={id:class}
	# test_set = {}
	for row in reader:
		test_set = {row[0]: row[14]}
	iris_test_file.close()
	return test_set

def get_knn_iris(k):
	test_set_iris = getClassSetFromIris()
	iris_out_file = open('output/knn_result_iris.csv', 'w')
	header=("Transactuion ID", "Predicted Class", "Actual Class")
	iris_test_file = open("dataset/transformed_iris_test_file.csv")
	reader = csv.reader(iris_test_file)
	writer = csv.writer(iris_out_file)
	# k=5
	writer.writerow(header)
	for row in reader:
		predicted_class = getclass(row,0,k*3)
		actual_class = test_set_iris.get(row[0])
		result_row=(row[0],predicted_class,actual_class)
		writer.writerow(result_row)

	iris_out_file.close()
	iris_test_file.close()

def get_knn_income(k):
	test_set_income = getClassSetFromIncome()
	income_out_file = open('output/knn_result_income.csv', 'w')
	header=("Transactuion ID", "Predicted Class", "Actual Class")
	income_test_file = open("dataset/transformed_inc_test_file.csv")
	reader = csv.reader(income_test_file)
	writer = csv.writer(income_out_file)
	# k=5
	writer.writerow(header)
	for row in reader:
		predicted_class = getclass(row,0,k*3)
		actual_class = test_set_income.get(row[0])
		result_row=(row[0],predicted_class,actual_class)
		writer.writerow(result_row)

	income_out_file.close()
	income_test_file.close()
	pass

def main():
	k=5
	get_knn_iris(k)
	get_knn_income(k)
	
main()