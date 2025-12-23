from server.models.database_extensions import db
from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    # table name
    __tablename__ = "users"
    
    # table columns and user instance attributes
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    phone = Column(String(13), unique=True, nullable=False)
    id_number = Column(String(14), unique=True, nullable=False)
    _password_hash = Column("password_hash", String(255), nullable=False)  # ← Private attribute
    active = Column(String, nullable=False, default="inactive")

    # db constraints 
    __table_args__ = (
        CheckConstraint(
            "active IN ('active', 'inactive', 'suspended')",
            name="check_user_account_status"
        ),
    )

    # Define Relationships
    member = relationship(
        'Member', 
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )
    
    administrator_profile = relationship(
        "AdministratorProfile", 
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    roles = relationship(
        "Role",
        secondary="user_roles",
        back_populates="users",
    )

    @property
    def password_hash(self):
        """Prevent reading the password hash."""
        raise AttributeError("Password hash is not readable")

    @password_hash.setter
    def password_hash(self, password):
        """
        Automatically hash the password when set.
        
        Args:
            password (str): Plain text password to hash
        """
        if password:
            # Only hash if it's not already hashed
            if not password.startswith(('scrypt:', 'pbkdf2:', 'bcrypt')):
                self._password_hash = generate_password_hash(password)  # ← Assign to _password_hash
            else:
                self._password_hash = password  # ← Assign to _password_hash

    def verify_password(self, password):
        """
        Verify a password against the stored hash.
        
        Args:
            password (str): Plain text password to verify
            
        Returns:
            bool: True if password matches, False otherwise
        """
        return check_password_hash(self._password_hash, password)  # ← Read from _password_hash

    def __str__(self):
        return (
            f"User({{"
            f"'id': {self.id}, "
            f"'first_name': '{self.first_name}', "
            f"'last_name': '{self.last_name}', "
            f"'email': '{self.email}', "
            f"'phone': '{self.phone}', "
            f"'id_number': '{self.id_number}', "
            f"'active': {self.active}"
            f"}})"
        )