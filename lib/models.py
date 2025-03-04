from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine, MetaData
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)

    # Relationship to Audition (One role has many auditions)
    auditions = relationship("Audition", backref=backref("role", lazy=True))

    def actors(self):
        """Returns a list of actor names for this role."""
        return [audition.actor for audition in self.auditions]

    def locations(self):
        """Returns a list of locations from auditions for this role."""
        return [audition.location for audition in self.auditions]

    def lead(self):
        """Returns the first hired audition or a message if none are hired."""
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        return hired_auditions[0] if hired_auditions else "no actor has been hired for this role"

    def understudy(self):
        """Returns the second hired audition or a message if none are available."""
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        return hired_auditions[1] if len(hired_auditions) > 1 else "no actor has been hired for understudy for this role"

class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    hired = Column(Boolean, default=False)  # Default is not hired

    role_id = Column(Integer, ForeignKey('roles.id'))  # Foreign key to Role

    def call_back(self):
        """Changes hired attribute to True."""
        self.hired = True

# Connect to SQLite database
engine = create_engine('sqlite:///moringa_theater.db')

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()


