classDiagram


class PresentationLayer {
  <<interface>>
    +API
    +Services
}


class BusinessLogicLayer {
    +user
    +place
    +review
    +Amenity
}


class PersistenceLayer {
    +Repository
    +Database
}
PresentationLayer --> BusinessLogicLayer : Facade PatternBusinessLogicLayer --> PersistenceLayer : Database Operations
