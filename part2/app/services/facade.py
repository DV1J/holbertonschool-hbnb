from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
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

    # method to create amenity
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    # method to amenity by id
    def get_amenity(self, amenity_id):
        return self.amenity_repo(amenity_id)

    # method for getting list of all amenities
    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    # method for updating amenity
    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo(amenity_id)
        if not amenity:
            return None
        self.amenity_repo.update(amenity_id, amenity_data)
        return amenity

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
    
    #method to create review
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review.repo.add(review)
        return review
    
    #method for getting the review
    def get_review(self, review_id):
        return self.review_repo.get(review_id)
    
    #method to get all reviews
    def get_all_reviews(self):
        return self.review_repo.get_all()
    
    #method to get all review for specific place
    def get_reviews_by_place(self, place_id):
        return self.review_repo.get_by_attribute(place_id)

    #method to update a review
    def update_review(self, review_id, review_data):
        review = self.review_repo(review_id)
        if not review:
            return None
        self.review_repo.update(review_id, review_data)
        return review

    #method to delete a review
    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            return None
        self.review_repo.delete(review_id)
        return review



