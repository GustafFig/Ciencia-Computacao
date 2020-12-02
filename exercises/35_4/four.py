from three import verify_email


def verify_emails(emails):
    corrects_emails = []
    for email in emails:
        try:
            verify_email(email)
        except ValueError as err:
            print(email)
            continue
        else:
            corrects_emails.append(email)

    return corrects_emails
