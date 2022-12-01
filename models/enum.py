import enum

# User is a natural person, admin is a tech person in the rent plataform and he can not operate as owner or renter,
# if he want to operate in the platform he must create a new user with personal references.
class UserType(enum.Enum):
    user = "user"
    admin = "admin"

class UserState(enum.Enum):
    enable = "enable"
    disable = "disable"

# # One person can have the owner or renter role, depending of the operation that this person needs to do
# class RoleType(enum.Enum):
#     owner = "Owner"
#     renter = "Renter"
#     admin = "Admin"

# The period used to indicate the rate of rent
class Period(enum.Enum):
    hour = "Hour"
    day = "Day"
    week = "Week"
    month = "Month"

# State of the requests to rent, is managed by the owner
class BidState(enum.Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"
