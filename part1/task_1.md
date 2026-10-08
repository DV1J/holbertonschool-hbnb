classDiagram


class User {
    +id
    +first_name
    +last_name
    +email
    +password
    +created_at
    +updated_at
    +create()
    +update()
}


class Place {
    +id
    +title
    +description
    +price
    +location
    +created_at
    +updated_at
    +create()
    +update()
}


class Review {
    +id
    +text
    +rating
    +created_at
    +updated_at
    +create()
    +update()
}


class Amenity {
    +id
    +name
    +description
    +created_at
    +updated_at
    +create()
    +update()
}


    User "1" --> "0..*" Place : owns
    User "1" --> "0..*" Review : writes
    Place "1" --> "0..*" Review : has
    Place "0..*" --> "0..*" Amenity : has
