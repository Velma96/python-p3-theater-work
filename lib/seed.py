from models import Session, Role, Audition

# Start a session
session = Session()

# Create some roles
role1 = Role(character_name="Hamlet")
role2 = Role(character_name="Macbeth")

session.add_all([role1, role2])
session.commit()

# Create some auditions
audition1 = Audition(actor="John Doe", location="New York", phone=1234567890, role=role1)
audition2 = Audition(actor="Jane Smith", location="Los Angeles", phone=9876543210, role=role1)
audition3 = Audition(actor="Mike Brown", location="Chicago", phone=5556667777, role=role2)

session.add_all([audition1, audition2, audition3])
session.commit()

print("Data successfully added!")
