from titanic.entity import Entity
from titanic.service import Service

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import  RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

import pandas as pd
class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    def modeling(self, train, test):
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.crate_train(this)
        return this


    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.entity
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this.id = this.test['PassengerId']
        # print(f'트레인 드랍 전 컬럼 : {this.train.columns}')
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        # print(f'트레인 드랍 후 컬럼 : {this.train.columns}')
        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        this = service.drop_feature(this, 'Name')
        this = service.drop_feature(this, 'PassengerId')
        this = service.age_ordinal(this)
        this = service.sex_nominal(this)
        this = service.fareBand_nominal(this)
        this = service.drop_feature(this, 'Fare')
        print(f'전처리 마감 후 컬럼 : {this.train.columns}')
        print(f'train 널의 수량 : {this.train.isnull().sum()}')
        print(f'test 널의 수량 : {this.test.isnull().sum()}')
        return this

    def learning(self, train, test):
        service = self.service
        this = self.modeling(train, test)
        #label = service.create_label()

        # accuracy = service.accuracy_by_dtree(this)
        #  accuracy = service.accuracy_by_rforest(this)
        #  accuracy = service.accuracy_by_nb(this)
        #  accuracy = service.accuracy_by_knn(this)
        #  accuracy = service.accuracy_by_svm(this)

        print(f'결정트리 활용한 검증 정확도 {service.accuracy_by_dtree(this)}')
        print(f'랜덤포레스트 활용한 검증 정확도 {service.accuracy_by_rforest(this)}')
        print(f'나이브베이즈 활용한 검증 정확도 {service.accuracy_by_nb(this)}')
        print(f'KNN 활용한 검증 정확도 {service.accuracy_by_knn(this)}')
        print(f'SVM 활용한 검증 정확도 {service.accuracy_by_svm(this)}')

    def submit(self, train, test):
        service = self.service
        this = self.modeling(train, test)
        clf = SVC()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        submission=pd.DataFrame(
            {
                'PassengerId' : this.id,
                'Survived' : prediction
            }.to_csv('./data/submission.csv',index_label =False)
        )
