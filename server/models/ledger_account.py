from server.models import db 
from sqlalchemy import CheckConstraint
import enum
class LedgerOwnerType(enum.Enum):
    MEMBER="MEMBER"
    ORG="ORG"
    
class LedgerAccountType(enum.Enum):
    SAVINGS="SAVINGS"
    #I can add other types later

class LedgerAccount (db.Model):
    __tablename__ = "ledger_accounts"

    id = db.Column(db.Integer, primary_key=True)
    # Ownership
    owner_type = db.Column(
        db.Enum(LedgerOwnerType),
        nullable=False
    )
    # 
    member_id = db.Column(
        db.Integer,
        db.ForeignKey("members.id"),
        nullable=True
    )

    # Account classification
    account_type = db.Column(
        db.Enum(LedgerAccountType),
        nullable=False
    )

    # Financial state
    balance = db.Column(
        db.Numeric(14, 2),
        nullable=False,
        default=0
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="ACTIVE"
    )

    
    # Relationships
    member = db.relationship("Member", back_populates="ledger_accounts",uselist=False)

    __table_args__ = (
        CheckConstraint(
            "(owner_type = 'MEMBER' AND member_id IS NOT NULL) "
            "OR (owner_type = 'ORG' AND member_id IS NULL)",
            name="ck_ledger_owner"
        ),
        CheckConstraint(
            "status IN ('ACTIVE', 'INACTIVE', 'SUSPENDED')",
            name="ck_ledger_account_status"
        ),
    
    )

   
    def __repr__(self):
        return f"<LedgerAccount {self.id} {self.account_type.value} {self.balance}>"
