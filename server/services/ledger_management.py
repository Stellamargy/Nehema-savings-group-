from server.models import LedgerAccount,LedgerAccountType,LedgerOwnerType,db
class LedgerManagement():
    @classmethod
    def create_primary_acc(cls,member_id_no):
        primary_acc=LedgerAccount(
            # name="primary",
            owner_type=LedgerOwnerType.MEMBER,
            account_type=LedgerAccountType.SAVINGS,
            member_id=member_id_no
            )
        db.session.add(primary_acc)
        return primary_acc