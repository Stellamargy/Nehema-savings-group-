from server.models import db ,SaccoMemberProfile
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
    #name
    # name=db.Column(db.String,nullable=False)
    # Ownership
    owner_type = db.Column(
        db.Enum(LedgerOwnerType),
        nullable=False
    )
    # 
    member_id = db.Column(
        db.Integer,
        db.ForeignKey("sacco_member_profiles.id"),
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
    sacco_member = db.relationship("SaccoMemberProfile", back_populates="ledger_accounts",uselist=False)

    __table_args__ = (
        CheckConstraint(
            "(owner_type = 'MEMBER' AND member_id IS NOT NULL) "
            "OR (owner_type = 'ORG' AND member_id IS NULL)",
            name="ck_ledger_owner"
        ),
    )

   
    def __repr__(self):
        return f"<LedgerAccount {self.id} {self.account_type.value} {self.balance}>"
