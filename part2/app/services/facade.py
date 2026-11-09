from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    # method for getting a user's info
    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    # method for updating a user's info
    def update_user(self, user_id, user_data):
        user = self.user_repo.get(user_id)
        if not user:
            return None
        self.user_repo.update(user_id, user_data)
        return user

    # method for getting a list of all users
    def get_all_users(self):
        return self.user_repo.get_all()

    # method for getting user's info by user's email
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    # method for creating place
    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    # method for getting place info
    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    # method for getting lists of all place
    def get_all_places(self):
        return self.place_repo.get_all()

    # method to update place info
    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        self.place_repo.update(place_id, place_data)
        return place