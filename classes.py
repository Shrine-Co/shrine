class User:
    def __init__(self, uid, user_name, pass_key, status="online", each_server_profiles={}, dms={}, bio="", banner="", friends=[], requests=[]):
        self.uid = uid
        self.user_name = user_name
        self.pass_key = pass_key
        self.status = status
        self.each_server_profiles = each_server_profiles
        self.dms = dms
        self.bio = bio
        self.status = status
        self.banner = banner

class Message:
    def __init__(self, id, channel, sender, data, sent_at, reactions={}, server_code="", iframe="", attachments=[], replied_to=None, reply_ping=False, role_mentions=[]):
        self.id = id
        self.channel=channel
        self.sender=sender
        self.data=data
        self.sent_at=sent_at
        self.reactions=reactions
        self.server_code=server_code
        self.iframe=iframe
        self.attachments=attachments
        self.role_mentions=role_mentions

class Channel:
    def __init__(self, id, name, call_id="", messages=[], channel_type="normal", iframe=None, pinned_messages=[], roles_access = {}):
        self.id=id
        self.name=name
        self.call_id=call_id
        self.messages=messages
        self.channel_type=channel_type
        self.iframe=iframe
        self.pinned_messages=pinned_messages
        self.roles_access=roles_access