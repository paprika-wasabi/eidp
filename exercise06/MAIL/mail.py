# mi84, pw221, ms2149
from dataclasses import dataclass


@dataclass
class MailAddress:
    name: str
    domain: str


@dataclass
class Mail:
    sender: MailAddress
    receiver: MailAddress
    subject: str
    body: str


@dataclass
class MailAccount():
    name: str
    inbox: list[Mail]
    outbox: list[Mail]


@dataclass
class MailServer():
    domain: str
    accounts: list[MailAccount]


def show_mail_address(email: MailAddress) -> str:
    email = email.name + "@" + email.domain
    return email


def show_mail(mail: Mail) -> str:
    mail = "From: " + show_mail_address(mail.sender) + "\nTo: " + show_mail_address(mail.receiver) + "\nSubject: " + mail.subject + "\n\n" + mail.body
    return mail


def show_email_account(account: MailAccount) -> str:
    inbox_str = str()
    for inm in account.inbox:
        inbox_str = inbox_str + "\n" + show_mail(inm)
    outbox_str = str()
    for outm in account.outbox:
        outbox_str = inbox_str + "\n" + show_mail(outm)
    account = account.name + inbox_str + outbox_str
    return account


def show_mail_server(mail_server: MailServer) -> str:
    result = ''
    acc = ''
    for x in acc:
        acc += '\n' + show_email_account(x)
    result += 'Server: ' + mail_server.domain + '\nAccounts' + acc
    return result


def find_server(domain: str, email_Server: list[MailServer]) -> str:
    for x in email_Server:
        if x.domain == domain:
            return domain
        else:
            return None


def find_account(name: str, accounts: list[MailServer]) -> str:
    for x in accounts:
        for i in range(len(accounts)):
            if x.accounts[i].name == name:
                return name
            else:
                None


def deliver_mail(email: str, email_server: list[MailServer]) -> bool:
    for x in email_server:
        if x.accounts == email:
            return True
        else:
            return False


def deliver_all_mail(servers: list[MailServer]):
    i = 0
    for x in servers:
        if x.domain == find_server(x.domain, servers):
            m = len(servers)
            m = m - 1
            for i in range(m):
                if x.accounts[i].name == find_account(x.accounts[i].name, servers):
                    deliver_mail(email=servers[1].accounts[0].name, server=servers[1].domain)
                    x.accounts[i].outbox = []