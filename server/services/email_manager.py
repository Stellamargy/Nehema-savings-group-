from flask_mail import Message

class EmailManager:
    
    @classmethod
    def send_account_setup_email(cls, user_email, first_name, temporary_password):
        """
        Creates and returns a welcome email message for new user account setup.
        
        Args:
            user_email (str): The recipient's email address
            first_name (str): The user's first name
            temporary_password (str): Temporary password for first login
            
        Returns:
            Message: Flask-Mail Message object ready to be sent
        """
        acc_setup_email = Message(
            subject="Welcome to Nehema Savings Group – Your Account Is Ready",
            recipients=[user_email]  # Add recipient here directly
        )
        
        # Set HTML body
        acc_setup_email.html = cls.create_account_setup_email(
            user_email, 
            first_name, 
            temporary_password
        )
        
        return acc_setup_email

    @staticmethod
    def create_account_setup_email(user_email, first_name, temporary_password):
        """
        Generates the HTML content for account setup email.
        
        Args:
            user_email (str): The user's email address
            first_name (str): The user's first name
            temporary_password (str): Temporary password for first login
            
        Returns:
            str: HTML email content
        """
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <body style="font-family: Arial, sans-serif; background-color: #f6f8fb; padding: 20px;">
            <table width="100%" cellspacing="0" cellpadding="0">
                <tr>
                    <td align="center">
                        <table width="600" style="background-color: #ffffff; padding: 30px; border-radius: 8px;">
                            <tr>
                                <td>
                                    <h2 style="color: #2c3e50;">
                                        Welcome to Nehema Savings Group 🎉
                                    </h2>

                                    <p>Hello <strong>{first_name}</strong>,</p>

                                    <p>
                                        We're excited to welcome you to <strong>Nehema Savings Group</strong> —
                                        a community built on trust, discipline, and financial growth.
                                    </p>

                                    <p>
                                        Your savings account has been successfully created.
                                        Use the details below to log in and start saving.
                                    </p>

                                    <ul>
                                        <li><strong>Email:</strong> {user_email}</li>
                                        <li><strong>Temporary Password:</strong> {temporary_password}</li>
                                    </ul>

                                    <p style="text-align: center; margin: 30px 0;">
                                        
                                            href="https://your-app-url.com/login"
                                            style="
                                                background-color: #1e88e5;
                                                color: #ffffff;
                                                padding: 12px 24px;
                                                text-decoration: none;
                                                border-radius: 5px;
                                                display: inline-block;
                                            "
                                        >
                                            Log in to your Account
                                        </a>
                                    </p>

                                    <p style="font-size: 14px; color: #555;">
                                        For security reasons, please change your password immediately after logging in.
                                    </p>

                                    <p>
                                        If you need any assistance, feel free to reach out — we're happy to help.
                                    </p>

                                    <p>
                                        Warm regards,<br />
                                        <strong>Nehema Savings Group</strong><br />
                                        <em>Building a secure financial future together</em>
                                    </p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """
        return html_content