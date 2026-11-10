from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})
@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        review_data = api.payload
        new_review = facade.create_review(review_data)
        return {'ratings': new_review.ratings, 'texting': new_review.texting, 'place_id': new_review.place_id, 'user_id': new_review.user_id},201
    
    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        review = facade.get_all_review()
        review_list = []
        for review in review:
            review_list.append({'ratings': review.ratings, 'texting': review.texting, 'place_id': review.place_id, 'user_id': review.user_id})
            return review_list, 200
        
        @api.route('/<review_id>')
        class ReviewResource(Resource):
            @api.response(200, 'Review details retrieved successfully')
            @api.response(404, 'Review not found')
            def get(self, review_id):
                """Get review details by ID"""
                review = facade.get_review(review_id)
        if not review:
            return ('review not found'), 404
        return {'ratings': review.ratings, 'texting': review.texting, 'place_id': review.place_id, 'user_id': review.user_id},200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        review_data = api.payload
        review = facade.update_place(review_id, review_data)
        if not review:
            return ('review not found'), 404
        return {'ratings': review.ratings, 'texting': review.texting, 'place_id': review.place_id, 'user_id': review.user_id},400
    
    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        review_data = api.payload
        review = facade.delete_review(review_id, review_data)
        if not review:
            return ('review not found'), 404
        return {'ratings': review.ratings, 'texting': review.texting, 'place_id': review.place_id, 'user_id': review.user_id},400
            
        
        

    
    
    
        


    
    
    

