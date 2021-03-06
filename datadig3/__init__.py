# -*-encoding=utf-8-*-
import h2o
from h2o.estimators.random_forest import H2ORandomForestEstimator

h2o.init()
# trainData = pd.read_csv("C:\Users\scc\PycharmProjects\untitled1\datadig3\\train.csv")
# testData = pd.read_csv("C:\Users\scc\PycharmProjects\untitled1\datadig3\\test.csv")

trainData = h2o.import_file("C:\Users\scc\PycharmProjects\untitled1\datadig3\\train.csv")
testData = h2o.import_file("C:\Users\scc\PycharmProjects\untitled1\datadig3\\test.csv")
realTrainData = trainData[2:18]  # 不选取第1、2和最后一列

model = H2ORandomForestEstimator(ntrees=18, max_depth=11)
model.train(x=realTrainData.names, y='Catrgory', training_frame=trainData)
pre_tag = H2ORandomForestEstimator.predict(model, testData)
pre_tag.head()
# 合并预测集合与测试集合
pre_and_test = pre_tag.cbind(testData)
# 计算准确率
n = pre_and_test.nrow
target_n = pre_and_test[pre_and_test['predict'] == pre_and_test['Catrgory'], :].nrow
accuracy = float(target_n) / float(n)

print accuracy

h2o.download_csv(pre_and_test, "predict.csv")
