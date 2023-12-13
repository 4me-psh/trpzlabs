from model.Recommendations import Recommendations


class Recommendations_Not_Registered(Recommendations):
    def recommend(self):
        print(" Not recommended content")
#клас для незареєстрованих користувачів