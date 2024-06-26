import boto3
def send_email(emailAddress):
    
    # Set up the email parameters
    # Set up the email parameters
    sender = 'info@elogicals.com'
    recipient = emailAddress
    subject = 'Test Email'
    body_text = 'This is a test email.'
    body_html = '<html><body><h1>Test Email</h1><p>This is a test email.</p></body></html>'

    # Send the email
    try:
        response = ses_client.send_email(
            Source=sender,
            Destination={'ToAddresses': [recipient]},
            Message={
                'Subject': {'Data': subject},
                'Body': {
                    'Text': {'Data': body_text},
                    'Html': {'Data': body_html}
                }
            }
        )
        print("Email sent! Message ID:", response['MessageId'])
    except Exception as e:
        print("Error:", e)

# if __name__ == "__main__":
#     send_email()
