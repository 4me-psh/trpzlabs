import model.Recommendations_Not_Registered
import model.Recomendations_Registered


class Factory_Recommendations:

    def create_recommendation(self, user_type):
        if user_type == "registered":
            return model.Recomendations_Registered
        elif user_type == "not_registered":
            return model.Recommendations_Not_Registered
#клас для реалізації factory method