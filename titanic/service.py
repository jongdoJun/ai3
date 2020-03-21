from titanic.entity import Entity
import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import  RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.model_selection import train_test_split#테스트를 위해서 나누어서
from sklearn.model_selection import KFold#k개로 나누고
from sklearn.model_selection import cross_val_score#크로스로 확인한다


"""
PassengerId  고객ID,   # 확률변서들
Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼  # 확률변서들

print(f'결정트리 활용한 검증 정확도 {None}')
print(f'랜덤포레스트 활용한 검증 정확도 {None}')
print(f'나이브베이즈 활용한 검증 정확도 {None}')
print(f'KNN 활용한 검증 정확도 {None}')
print(f'SVM 활용한 검증 정확도 {None}')
        
"""
class Service:
    def __init__(self):
        self.entity = Entity()

    def new_model(self, payload):
        this = self.entity
        this.context = './data/'
        this.fname = 'train.csv'
        return pd.read_csv(this.context+this.fname)

    @staticmethod
    def crate_train(this):
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this):
        return this.train['Survived']


    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis = 1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked': "S"})
        this.test = this.test.fillna({'Embarked': "S"})
        this.train['Embarked'] = this.train['Embarked'].map({"S" : 1, "C" : 2, "Q": 3})
        this.test['Embarked'] = this.test['Embarked'].map({"S": 1, "C": 2, "Q": 3})
        return this

    @staticmethod
    def fare_ordinal(this) ->object:
        this.train['FareBand'] = pd.qcut(this['Fare'], 4, labels={1,2,3,4})
        this.test['FareBand'] = pd.qcut(this['Fare'], 4, labels={1,2,3,4})
        return this

    @staticmethod
    def fareBand_nominal(this) -> object:
        this.train = this.train.fillna({'FareBand': 1})
        this.test = this.test.fillna({'FareBand': 1})
        return this


    @staticmethod
    def title_nominal(this) ->object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer','Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
        # print(this.train[['Title','Survived']].groupby(['Title'], as_index=False).mean())
        title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}# 문자를 숫자로 매핑하는 것
        for dataset in combine:
            dataset['Title'] = dataset['Title'].map(title_mapping)
            dataset['Title'] = dataset['Title'].fillna(0)
        this.train = this.train
        this.test = this.test
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        combine = [this.train, this.test]
        sex_mapping = {'male': 0, 'female': 1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)
        print(this.train[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean())
        this.train = this.train
        this.test = this.test
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown','Baby','Child','Teenager','Student','Young Adult','Adult', 'Senior']
        train['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)
        test['AgeGroup'] = pd.cut(test['Age'], bins, labels=labels)
        age_title_mapping = {
            0: 'Unknown', 1: 'Baby', 2: 'Child', 3: 'Teenager', 4: 'Student',
            5: 'Young Adult', 6: 'Adult', 7: 'Senior'
        }
        for x in range(len(train['AgeGroup'])):
            if train['AgeGroup'][x] == 'Unknown':
                train['AgeGroup'][x] = age_title_mapping[train['Title'][x]]
        for x in range(len(test['AgeGroup'])):
            if test['AgeGroup'][x] == 'Unknown':
                test['AgeGroup'][x] = age_title_mapping[test['Title'][x]]
        age_mapping = {
            'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
            'Young Adult': 5, 'Adult': 6, 'Senior': 7
        }
        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        test['AgeGroup'] = test['AgeGroup'].map(age_mapping)
        this.train = train
        this.test = test
        return this

#머신러닝
        @staticmethod
        def create_k_fold():#self안쓰므로 지워라. 그리고 전역으로 설정
            k_fold = KFold(n_splits=10,shuffle=True, random_state=0)#
            return k_fold

        @staticmethod
        def create_random_variable(train, X_features, Y_features) -> []:#확률변수 : 첫글자는 대문자로 쓴다
            the_X_features =X_features
            the_Y_features = Y_features
            train2, test2 = train_test_split(train, test_size=0.3, random_state=0)#교차로 훈련시키는 코드
            train_X = train2(the_X_features)
            train_Y = train2(the_Y_features)
            test_X = test2(the_X_features)
            test_Y = test2(the_Y_features)
            return (train_X,train_Y,test_X,test_Y)

        def accuracy_by_dtree(self, this):#label은 답이다
            #clf = DecisionTreeClassifier() #분류기 학습시키는것
           # scoring = 'accuracy'
          #  k_ford = self.create_k_fold()
            score = cross_val_score(
                DecisionTreeClassifier(), #분류기
                this.model,
                this.label,
                cv = self.create_k_fold(),
                n_jobs=1,
                scoring='accuracy')# sklearn 의 기능
            return round(np.mean(score)*100,2)

        def accuracy_by_rforest(self, this):
           # clf = RandomForestClassifier() #분류기 학습시키는것
           # scoring = 'accuracy'
           # k_ford = self.create_k_fold()
           #  score = cross_val_score(clf, this.model, this.label,cv = k_ford, n_jobs=1,  scoring=scoring)# sklearn 의 기능
           #  accuracy = round(np.mean(score)*100,2)
           #  return accuracy

            score = cross_val_score(
                RandomForestClassifier(), #분류기
                this.model,
                this.label,
                cv = self.create_k_fold(),
                n_jobs=1,
                scoring='accuracy')# sklearn 의 기능
            return round(np.mean(score)*100,2)

        def accuracy_by_nb(self, this):
            # clf = GaussianNB()
            # scoring = 'accuracy'
            # k_ford = self.create_k_fold()
            # score = cross_val_score(clf, this.model, this.label,cv = k_ford, n_jobs=1,  scoring=scoring)# sklearn 의 기능
            # accuracy = round(np.mean(score)*100,2)
        # return accuracy

            score = cross_val_score(
                GaussianNB(),  # 분류기
                this.model,
                this.label,
                cv=self.create_k_fold(),
                n_jobs=1,
                scoring='accuracy')  # sklearn 의 기능
            return round(np.mean(score) * 100, 2)

        def accuracy_by_knn(self, this):
            # clf = KNeighborsClassifier()
            # scoring = 'accuracy'
            # k_ford = self.create_k_fold()
            # score = cross_val_score(clf, this.model, this.label,cv = k_ford, n_jobs=1,  scoring=scoring)# sklearn 의 기능
            # accuracy = round(np.mean(score)*100,2)
            # return accuracy

            score = cross_val_score(
                KNeighborsClassifier(),  # 분류기
                this.model,
                this.label,
                cv=self.create_k_fold(),
                n_jobs=1,
                scoring='accuracy')  # sklearn 의 기능
            return round(np.mean(score) * 100, 2)
        def accuracy_by_svm(self, this):
            # clf = SVC()
            # scoring = 'accuracy'
            # k_ford = self.create_k_fold()
            # score = cross_val_score(clf, this.model, this.label,cv = k_ford, n_jobs=1,  scoring=scoring)# sklearn 의 기능
            # accuracy = round(np.mean(score)*100,2)
            # return accuracy

            score = cross_val_score(
                SVC(),  # 분류기
                this.model,
                this.label,
                cv=self.create_k_fold(),
                n_jobs=1,
                scoring='accuracy')  # sklearn 의 기능
            return round(np.mean(score) * 100, 2)

       # def submit(self):

        #nb
        #KNN
        #svm



